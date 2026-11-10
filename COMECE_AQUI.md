# Destrava AI — publicar e testar (passo a passo)

## 1. GitHub
1. Abra https://github.com/new e crie um repositório chamado `destrava-ai` (público, para portfólio).
2. Descompacte o arquivo `destrava_ai_pronto_para_publicar.zip`.
3. No repositório: **Add file → Upload files**. Envie **o conteúdo descompactado**, mantendo `app.py`, `design.py`, `utils.py`, `requirements.txt` e a pasta `data/` diretamente na raiz do repositório.
4. Salve com **Commit changes**.
5. Importante: não publique `secrets.toml` nem sua chave de API.

## 2. Chave do Gemini
1. Acesse https://aistudio.google.com/apikey com sua conta Google.
2. Crie uma chave para a API Gemini.
3. Guarde-a em local privado; não a envie por chat, não a coloque no GitHub e não a inclua em prints.

## 3. Publicar Streamlit
1. Abra https://share.streamlit.io/ e entre usando o GitHub.
2. Selecione **Create app → Yup, I have an app**.
3. Informe repositório `seu_usuario/destrava-ai`, branch `main`, arquivo `app.py`.
4. Em **Advanced settings → Secrets**, insira:

```toml
GEMINI_API_KEY = "SUA_CHAVE_PRIVADA_AQUI"
```

5. Salve e clique em **Deploy**.

## 4. Validar antes de incluir no Notion
- [ ] A página inicial carrega corretamente no celular e computador.
- [ ] Em **Documentos**, abra `DOC-03`, clique em **Classificar e resumir com IA** e confira categoria, resumo e etiquetas.
- [ ] Exporte o catálogo CSV.
- [ ] Em **Onboarding**, pergunte "Como solicito acesso às ferramentas?". Resposta deve mencionar a fonte `[DOC-03]`.
- [ ] Pergunte "Qual é o endereço da empresa?". Não deve inventar endereço.
- [ ] Gere o roteiro do primeiro dia e confira as referências.
- [ ] Grave uma demonstração curta das duas áreas.

**O que o projeto demonstra:** uso real da API de IA, organização documental, assistência ao onboarding, publicação web e testes. Usa cinco documentos fictícios curtos como contexto; não há RAG vetorial nem banco corporativo.

**Aviso sobre chave/custos:** a configuração de modelo e cota depende da sua conta. Consulte o painel do Google AI Studio para limites e cobranças. Em um aplicativo público, visitantes podem consumir sua cota de API, portanto monitore o uso ou restrinja o acesso conforme necessário.
