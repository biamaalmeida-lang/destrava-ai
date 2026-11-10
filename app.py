"""Destrava AI — gestão de documentos e onboarding com IA generativa.

Interface redesenhada com linguagem editorial minimalista: tons naturais, cartões,
hero de marca e navegação objetiva. As funções do projeto original permanecem.
"""
import csv
import io
import os
from pathlib import Path

import streamlit as st

from design import STYLE, document_title, doc_row, footer, hero, masthead, pagehead, safe
from utils import classification_prompt, first_day_prompt, load_documents, onboarding_prompt, parse_classification

st.set_page_config(page_title="Destrava AI | Lume", page_icon="↗", layout="wide", initial_sidebar_state="collapsed")


def get_api_key():
    """Credenciais em variável de ambiente ou Secrets; nunca no repositório."""
    key = os.environ.get("GEMINI_API_KEY", "")
    if key:
        return key
    try:
        return st.secrets.get("GEMINI_API_KEY", "")
    except (FileNotFoundError, KeyError):
        return ""
    except Exception:
        return ""


def run_ai(prompt, key):
    """Execução real do Gemini via SDK oficial (sem saída simulada)."""
    from google import genai
    model = os.environ.get("GEMINI_MODEL", "gemini-3.5-flash-lite")
    client = genai.Client(api_key=key)
    result = client.models.generate_content(model=model, contents=prompt)
    answer = getattr(result, "text", None)
    if not answer or not answer.strip():
        raise RuntimeError("A IA não retornou texto. Verifique o modelo e a chave da API.")
    return answer.strip()


def csv_catalog(documents):
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["id", "arquivo", "categoria", "resumo", "etiquetas", "origem"])
    for d in documents:
        writer.writerow([d["id"], d["nome"], d["categoria"], d["resumo"], ", ".join(d["etiquetas"]), d["origem"]])
    return buf.getvalue().encode("utf-8-sig")


def change_page(page):
    """Callback Streamlit: chamado antes da execução dos widgets."""
    st.session_state.navigation = page


def respond(question, key):
    """Mostra falhas de maneira transparente, sem inventar respostas."""
    if not key or not question.strip():
        return
    st.session_state.chat.append({"role": "user", "content": question.strip()})
    try:
        with st.spinner("Consultando a biblioteca da Lume..."):
            answer = run_ai(onboarding_prompt(question.strip(), st.session_state.docs), key)
        st.session_state.chat.append({"role": "assistant", "content": answer})
    except Exception as exc:
        st.session_state.chat.append({"role": "assistant", "content": "Não consegui responder agora. Confira a conexão com a API e tente novamente."})
        st.session_state.last_error = str(exc)
    st.rerun()


def add_uploaded(files):
    if not files:
        return
    added = 0
    known = {(d["nome"], d["texto"]) for d in st.session_state.docs}
    for uploaded in files:
        if uploaded.size > 20_000:
            st.error(f"{uploaded.name}: limite de 20 KB por documento.")
            continue
        try:
            content = uploaded.getvalue().decode("utf-8").strip()
        except UnicodeDecodeError:
            st.error(f"{uploaded.name}: utilize codificação UTF-8.")
            continue
        if not content or (uploaded.name, content) in known:
            continue
        new_id = f"DOC-{len(st.session_state.docs)+1:02d}"
        st.session_state.docs.append({
            "id": new_id, "nome": Path(uploaded.name).name,
            "texto": content, "categoria": "Ainda não classificado pela IA",
            "resumo": "", "etiquetas": [], "origem": "Upload nesta sessão",
        })
        known.add((uploaded.name, content))
        added += 1
    if added:
        st.success(f"{added} novo(s) documento(s) adicionado(s) à biblioteca nesta sessão.")
    else:
        st.info("Nenhum novo documento foi adicionado.")


# Estado da sessão (não há armazenamento persistente / banco externo).
if "docs" not in st.session_state:
    st.session_state.docs = load_documents()
if "chat" not in st.session_state:
    st.session_state.chat = []
if "navigation" not in st.session_state:
    st.session_state.navigation = "Visão geral"

api_key = get_api_key()
docs = st.session_state.docs
classified = sum(bool(d["resumo"]) for d in docs)

st.markdown(STYLE, unsafe_allow_html=True)
st.markdown(masthead(), unsafe_allow_html=True)

st.radio("Navegação principal", ["Visão geral", "Documentos", "Onboarding"],
         key="navigation", horizontal=True, label_visibility="collapsed")

if st.session_state.navigation == "Visão geral":
    st.markdown(hero(), unsafe_allow_html=True)
    st.markdown('<div class="ds-topline">SEU ESPAÇO DE TRABALHO</div><div class="ds-section-title">Tudo o que importa, em um só lugar.</div><p class="ds-section-text">Uma experiência simples para organizar o conhecimento da Lume e facilitar a chegada de novas pessoas.</p>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="ds-numbers"><div class="ds-number"><strong>{len(docs):02d}</strong><span>Documentos na biblioteca</span></div>'
        f'<div class="ds-number"><strong>{classified:02d}</strong><span>Documentos analisados com IA</span></div>'
        '<div class="ds-number"><strong>02</strong><span>Ferramentas disponíveis</span></div></div>',
        unsafe_allow_html=True,
    )
    left, right = st.columns(2, gap="large")
    with left:
        st.markdown('<div class="ds-feature"><div class="ds-icon">▤</div><h3>Biblioteca inteligente</h3><p>Reúna documentos, organize por assunto e crie resumos e etiquetas com apoio da IA.</p></div>', unsafe_allow_html=True)
        st.button("Explorar documentos  ↗", key="hero-doc-btn", type="primary", use_container_width=True,
                  on_click=change_page, args=("Documentos",))
    with right:
        st.markdown('<div class="ds-feature green"><div class="ds-icon">✧</div><h3>Boas-vindas mais simples</h3><p>Encontre respostas sobre a empresa e crie um roteiro para começar com tranquilidade.</p></div>', unsafe_allow_html=True)
        st.button("Conhecer onboarding  ↗", key="hero-onboard-btn", use_container_width=True,
                  on_click=change_page, args=("Onboarding",))

    st.write("")
    col1, col2 = st.columns([1.45, 1], gap="large")
    with col1:
        st.markdown('<div class="ds-small-label">NA SUA BIBLIOTECA</div><div class="ds-section-title" style="font-size:1.28rem">Pronto para consultar.</div>', unsafe_allow_html=True)
        listing = ''.join(doc_row(d) for d in docs[:4])
        st.markdown(f'<div class="ds-card-callout">{listing}</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="ds-small-label">PARA QUEM ESTÁ CHEGANDO</div><div class="ds-section-title" style="font-size:1.28rem">Um começo leve.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ds-onboard-tip"><h3>Seu primeiro dia, sem adivinhações.</h3><p>Descubra como pedir acesso às ferramentas, entender sua rotina e encontrar orientações dentro da Lume.</p></div>', unsafe_allow_html=True)
        st.markdown('<p class="ds-section-text">As respostas usam os documentos fictícios disponíveis e devem citar as fontes de informação.</p>', unsafe_allow_html=True)
    if not api_key:
        st.info("A biblioteca já está disponível. Para ativar classificação e respostas com IA, configure GEMINI_API_KEY nos Secrets do Streamlit.")

elif st.session_state.navigation == "Documentos":
    st.markdown(pagehead("01 / CENTRAL DE DOCUMENTOS", "Conhecimento bem", "organizado.",
                             "Uma biblioteca enxuta para encontrar informações e organizar documentos com ajuda de inteligência artificial."), unsafe_allow_html=True)
    st.markdown(f'<div class="ds-inline-stats"><span><b>{len(docs):02d}</b> documentos</span><span><b>{classified:02d}</b> classificados pela IA</span><span><b>{len(docs)-classified:02d}</b> aguardando análise</span></div>', unsafe_allow_html=True)
    main, side = st.columns([1.12, .88], gap="large")
    with main:
        st.markdown('<div class="ds-small-label">ACERVO DA LUME</div><div class="ds-section-title" style="font-size:1.33rem">Sua biblioteca.</div>', unsafe_allow_html=True)
        filter_text = st.text_input("Buscar documentos", placeholder="Busque pelo nome, código ou categoria...", key="doc_filter")
        query = filter_text.lower().strip()
        matching = [d for d in docs if query in f'{d["id"]} {document_title(d)} {d["categoria"]} {d["resumo"]}'.lower()]
        if matching:
            st.markdown('<div class="ds-card-callout">' + ''.join(doc_row(d) for d in matching) + '</div>', unsafe_allow_html=True)
        else:
            st.info("Nenhum documento corresponde à busca.")
        st.write("")
        st.markdown('<div class="ds-small-label">ADICIONAR À BIBLIOTECA</div>', unsafe_allow_html=True)
        uploaded_files = st.file_uploader("Enviar arquivos de texto", type=["txt", "md"], accept_multiple_files=True,
                                          help="Aceitamos TXT e Markdown em UTF-8, até 20 KB por arquivo.", key="upload_docs")
        if st.button("Adicionar documentos  +", disabled=not bool(uploaded_files), key="add-docs"):
            add_uploaded(uploaded_files)
        st.caption("Arquivos adicionados permanecem somente nesta sessão. Não envie informações sigilosas.")
    with side:
        st.markdown('<div class="ds-small-label">ASSISTENTE DE ORGANIZAÇÃO</div><div class="ds-section-title" style="font-size:1.33rem">Classificar com IA.</div><p class="ds-section-text">Escolha um documento para obter categoria, resumo e etiquetas.</p>', unsafe_allow_html=True)
        labels = {f'{d["id"]} · {document_title(d)}': d["id"] for d in docs}
        selected = st.selectbox("Documento selecionado", options=list(labels), key="selected_doc")
        doc = next(d for d in docs if d["id"] == labels[selected])
        st.text_area("Conteúdo do documento", value=doc["texto"], height=200, disabled=True)
        if st.button("Classificar e resumir com IA  ✦", type="primary", use_container_width=True,
                     disabled=not bool(api_key), key="classify-doc"):
            with st.spinner("A IA está lendo e organizando o documento..."):
                try:
                    result = parse_classification(run_ai(classification_prompt(doc), api_key))
                    doc.update(result)
                    st.success("Documento analisado e catálogo atualizado!")
                except Exception as exc:
                    st.error("Não foi possível classificar. Confira o acesso à API.")
                    with st.expander("Detalhes do erro"):
                        st.code(str(exc))
        if doc.get("resumo"):
            st.markdown('<div class="ds-small-label">RESULTADO DA IA</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="ds-card-callout"><div class="ds-pic-name">{safe(doc["categoria"])}</div><p class="ds-section-text" style="margin-top:.6rem">{safe(doc["resumo"])}</p><div class="ds-inline-stats">' + ''.join(f'<span class="ds-pill">{safe(tag)}</span>' for tag in doc["etiquetas"]) + '</div></div>', unsafe_allow_html=True)
        st.write("")
        st.download_button("Exportar catálogo CSV  ↓", data=csv_catalog(docs), file_name="destrava_catalogo.csv",
                           mime="text/csv", use_container_width=True)
        if not api_key:
            st.caption("Configure GEMINI_API_KEY nos Secrets para habilitar a classificação.")

else:  # Onboarding
    st.markdown(pagehead("02 / INTEGRAÇÃO DE PESSOAS", "Chegar bem faz", "diferença.",
                             "Um guia para quem acabou de entrar. Pergunte com liberdade e encontre orientações com fontes documentais."), unsafe_allow_html=True)
    chat_col, aside = st.columns([1.33, .87], gap="large")
    with chat_col:
        st.markdown('<div class="ds-small-label">CONVERSE COM A LUME</div><div class="ds-section-title" style="font-size:1.33rem">Como podemos ajudar?</div>', unsafe_allow_html=True)
        if not st.session_state.chat:
            st.markdown('<div class="ds-hello"><strong>Olá, que bom ter você por aqui! ✳</strong><span>Sou o Destrava AI. Posso explicar o primeiro dia, as ferramentas de trabalho e os procedimentos da Lume. Minhas respostas indicam os documentos consultados.</span></div>', unsafe_allow_html=True)
        for message in st.session_state.chat:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        with st.form("ask_form", clear_on_submit=True):
            question = st.text_input("Sua dúvida", placeholder="Ex.: Como consigo acesso às ferramentas?", disabled=not bool(api_key))
            sent = st.form_submit_button("Enviar pergunta  ↗", disabled=not bool(api_key), type="primary")
        if sent and question.strip():
            respond(question, api_key)
        if st.session_state.get("last_error"):
            with st.expander("Detalhes da última falha da API"):
                st.code(st.session_state.pop("last_error"))
        st.caption("As respostas são geradas com base em documentos fictícios e podem conter erros.")
    with aside:
        st.markdown('<div class="ds-onboard-tip"><h3>Primeiro dia, passo a passo.</h3><p>Gere um roteiro de integração com ações práticas, com referência aos documentos internos.</p></div>', unsafe_allow_html=True)
        if st.button("Criar roteiro com IA  ✦", key="create-day", disabled=not bool(api_key), use_container_width=True):
            with st.spinner("Preparando seu primeiro dia..."):
                try:
                    st.session_state.roteiro = run_ai(first_day_prompt(docs), api_key)
                except Exception as exc:
                    st.error("Não foi possível gerar o roteiro.")
                    with st.expander("Detalhes técnicos"):
                        st.code(str(exc))
        if st.session_state.get("roteiro"):
            st.markdown('<div class="ds-small-label">SEU ROTEIRO PERSONALIZADO</div>', unsafe_allow_html=True)
            st.markdown(st.session_state.roteiro)
        st.write("")
        st.markdown('<div class="ds-small-label">PERGUNTAS FREQUENTES</div>', unsafe_allow_html=True)
        for i, prompt in enumerate([
            "Como solicito acesso às ferramentas?",
            "O que preciso fazer no meu primeiro dia?",
            "Como funciona o reembolso de despesas?",
        ]):
            if st.button(prompt + "  ↗", key=f"quick_{i}", disabled=not bool(api_key), use_container_width=True):
                respond(prompt, api_key)
        if not api_key:
            st.info("A demonstração de IA precisa de uma chave Gemini configurada em Secrets.")

st.markdown(footer(), unsafe_allow_html=True)
