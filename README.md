# Destrava AI — O conhecimento da empresa, organizado e acessível

Aplicação de portfólio para **organização de documentos com IA** e **orientação de novos funcionários com respostas fundamentadas em documentos**, construída com Streamlit + Gemini API.

## O que o projeto faz

1. Começa com cinco documentos TXT de uma empresa **totalmente fictícia**, a Lume.
2. Permite adicionar documentos `.txt` e `.md` (até 20 KB cada) durante a sessão.
3. Envia documentos selecionados à API Gemini para classificação por área, resumo e etiquetas.
4. Exporta o catálogo de documentos em CSV.
5. Responde perguntas de onboarding e produz um roteiro do primeiro dia utilizando a base textual, identificando as fontes por código `[DOC-01]` etc.

**IA real:** as ações de classificação, resumo, respostas e roteiro fazem chamadas à API Gemini. Sem chave configurada, essas ações ficam desabilitadas; o app continua mostrando os documentos. Não há respostas de IA pré-fabricadas.

**Simplicidade técnica:** a coleção de cinco documentos é pequena, por isso ela é enviada inteira como contexto ao modelo. **Não há RAG vetorial, banco de dados externo, agente autônomo nem execução automática de processos corporativos.**

## Executar no computador

1. Instale Python 3.10+.
2. Abra o terminal na pasta do projeto.
3. Instale as dependências: `pip install -r requirements.txt`.
4. Crie a pasta `.streamlit` (ela já vem preparada) e copie `secrets.toml.example` para `secrets.toml`.
5. Obtenha uma chave no [Google AI Studio](https://aistudio.google.com/apikey) e substitua `COLE_AQUI_SUA_CHAVE` em `.streamlit/secrets.toml`.
6. Inicie o projeto: `streamlit run app.py`.

**Nunca coloque sua chave no GitHub**, em arquivos públicos nem em prints. Ela é privada. Você também pode usar a variável de ambiente `GEMINI_API_KEY`.

## Publicar no Streamlit Community Cloud

1. Crie um repositório no GitHub com todos os arquivos deste pacote, mantendo `.gitignore`.
2. Em [share.streamlit.io](https://share.streamlit.io/), crie um aplicativo apontando para o repositório e o arquivo `app.py`.
3. Nas configurações de **Secrets**, registre `GEMINI_API_KEY = "sua_chave"`.
4. Teste o endereço público e grave uma demonstração. Confira limites de uso e eventual cobrança da Gemini API. Para publicar um demo público, prefira credenciais com cota restrita.

## Roteiro rápido de demonstração

- Abra **Organizar documentos**: selecione `DOC-03` (Acessos e Ferramentas) e clique em **Classificar e resumir com IA**.
- Veja a categoria, o resumo e as etiquetas. Baixe o CSV do catálogo.
- Abra **Onboarding** e pergunte: *Como solicito acesso às ferramentas?*
- Em seguida pergunte: *Qual o prazo máximo de reembolso?*; a resposta correta deve indicar que o prazo não está definido na base.
- Clique em **Criar roteiro do primeiro dia** e confira se cada passo remete aos documentos.

## Medição de qualidade (sem inventar resultados)

| Caso | Resultado esperado |
|---|---|
| Como pedir acessos? | Explicar aprovação pela liderança, com [DOC-03] |
| Qual ferramenta usamos para tarefas? | Trello, com [DOC-03] ou [DOC-04] |
| Como pedir reembolso? | Autorização prévia e tarefa no Trello, com [DOC-05] |
| Qual o prazo do reembolso? | Informar que não consta prazo na base, com [DOC-05] |
| Qual é o endereço do escritório? | Dizer que não há informação suficiente, sem inventar endereço |

Registre as respostas realmente obtidas, as fontes, acertos, erros e tempo gasto. **Não afirme que os resultados foram validados até concluir os testes com uma chave de API.**

## Limites importantes

- Documentos acrescentados e classificações ficam **na sessão atual do Streamlit**; não existe armazenamento persistente nem compartilhamento entre funcionários. Exportar CSV preserva o catálogo.
- Há apenas documentos curtos `.txt`/`.md`, para reduzir a complexidade. PDFs e DOCX não são suportados nesta versão.
- Respostas são geradas por um modelo e podem conter erros; as referências propostas pelo modelo devem ser verificadas pelo usuário.
- O texto documental é enviado à API Gemini. **Use somente dados inventados ou autorizados, nunca documentos corporativos confidenciais.**
- O sistema é uma demonstração de portfólio, não uma ferramenta corporativa pronta para produção.

## Tecnologias

- Python / Streamlit
- Gemini API via SDK `google-genai` (Interactions API)
- CSV para exportação
- GitHub + Streamlit Community Cloud para publicação

Documentação: [Gemini API](https://ai.google.dev/gemini-api/docs/) e [Streamlit Secrets](https://docs.streamlit.io/develop/concepts/connections/secrets-management).

## Interface atualizada — versão editorial

A interface foi redesenhada com inspiração em referências de sites editoriais e sistemas de design contemporâneos: navegação em pílulas, fundo off-white, verde profundo, tipografia marcante, hero de destaque, cartões arredondados e bastante espaço em branco.

### Navegação

- **Visão geral:** apresenta o produto, os indicadores da sessão e os atalhos para as duas ferramentas.
- **Documentos:** busca visual, upload de TXT/MD, leitura do arquivo, análise com Gemini (categoria, resumo e etiquetas) e exportação de catálogo em CSV.
- **Onboarding:** conversa com respostas fundamentadas no acervo da Lume, perguntas sugeridas e geração de roteiro do primeiro dia.

Os estilos e componentes HTML ficam em `design.py`, separados da lógica da aplicação em `app.py`. O arquivo `utils.py` permanece com os prompts e funções de processamento, para facilitar a manutenção.

A interface usa cores, formas e ilustrações CSS originais, sem reproduzir fotografias, logotipos ou elementos proprietários das referências enviadas.

**Observação técnica:** a chamada ao Gemini utiliza `client.models.generate_content` do SDK `google-genai`, com modelo padrão `gemini-3.5-flash-lite` (alterável com `GEMINI_MODEL`). Verifique no AI Studio se sua conta tem acesso ao modelo e à cota necessários. O comportamento real da API precisa ser testado com sua chave.
