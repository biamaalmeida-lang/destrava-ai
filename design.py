"""Camada de apresentação do Destrava AI — estilo editorial / software corporativo."""
from html import escape

# Textos arbitrários devem ser escapados antes de entrar em HTML da interface.
def safe(value):
    return escape(str(value), quote=True)


STYLE = r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');
:root { --ink:#202822; --pine:#203a2f; --forest:#14291f; --moss:#6d8c72; --mist:#f5f5f0; --cream:#f8f7f3; --sand:#eae8df; --line:#e5e7df; --muted:#798178; --peach:#f7b79b; }
html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {background:var(--cream); color:var(--ink);font-family:'DM Sans','Segoe UI',sans-serif;}
[data-testid="stHeader"]{background:transparent; height:1.2rem;}
[data-testid="stDecoration"], #MainMenu, footer {display:none!important;}
[data-testid="stMainBlockContainer"], .block-container {max-width:1180px!important; padding:1.1rem 2.7rem 3rem!important;}
h1,h2,h3,h4,button {font-family:'Manrope','Segoe UI',sans-serif!important;letter-spacing:-.03em;}
p, label, [data-testid="stMarkdownContainer"] {font-family:'DM Sans','Segoe UI',sans-serif;}
[data-testid="stVerticalBlock"] {gap:.78rem;}
/* Masthead */
.ds-masthead {display:flex; justify-content:space-between;align-items:center; padding:1rem 0 .95rem;gap:1rem;border-bottom:1px solid var(--line);}
.ds-brand {display:flex;align-items:center;gap:.7rem;font:800 1.39rem/1 'Manrope',sans-serif;letter-spacing:-.065em;color:var(--ink);}
.ds-brand-icon{width:34px;height:34px;border-radius:13px 13px 13px 4px;background:var(--pine);display:inline-flex;align-items:center;justify-content:center; color:#fff;font-size:23px; font-weight:500;line-height:1;}
.ds-brand-ai{color:#789981;}
.ds-mast-meta{display:flex;align-items:center;gap:.55rem;font-size:.73rem;color:#737a70;}
.ds-mast-meta strong{background:#ebede6;padding:.48rem .75rem;border-radius:20px;color:#455147;letter-spacing:.03em;font-weight:700;}
.ds-live{display:inline-block;width:7px;height:7px;border-radius:50%;background:#92b79a;margin-right:6px;}
/* navigation */
[data-testid="stRadio"]{margin-top:-.1rem;margin-bottom:.1rem;}
[data-testid="stRadio"]>div[role="radiogroup"]{display:flex;gap:.48rem;flex-wrap:wrap;align-items:center;}
[data-testid="stRadio"]>div[role="radiogroup"] label{display:flex;justify-content:center;align-items:center;border:1px solid transparent;border-radius:99px;padding:.55rem 1.02rem;background:transparent;color:#737b73;transition:.2s ease;cursor:pointer;}
[data-testid="stRadio"]>div[role="radiogroup"] label:hover{background:#edeee8;}
[data-testid="stRadio"]>div[role="radiogroup"] label:has(input:checked){background:var(--pine);box-shadow:0 3px 8px rgba(26,48,35,.09);}
[data-testid="stRadio"]>div[role="radiogroup"] label:has(input:checked) p{color:#fff!important;}
[data-testid="stRadio"]>div[role="radiogroup"] label p{font-size:.85rem!important;font-weight:700!important;margin:0!important;}
[data-testid="stRadio"]>div[role="radiogroup"] label input, [data-testid="stRadio"]>div[role="radiogroup"] label>div:first-child{display:none;}
/* hero */
.ds-hero{position:relative;min-height:338px;display:grid;grid-template-columns:1.36fr .84fr;align-items:center;overflow:hidden;background:linear-gradient(121deg,#203b2f 0%,#243d32 49%,#406453 100%);color:#fff;border-radius:22px;margin:1.05rem 0 1.65rem;padding:3.2rem 4.1rem 3.4rem;isolation:isolate;}
.ds-hero:before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 81% 30%,rgba(157,185,148,.25),transparent 36%),radial-gradient(ellipse at 10% 100%,rgba(18,27,21,.5),transparent 56%);z-index:-1;}
.ds-hero:after{content:'';position:absolute;right:-7rem;top:-10rem;width:33rem;height:33rem;border:1px solid rgba(225,237,219,.12);border-radius:50%;box-shadow:0 0 0 58px rgba(0,0,0,0), 0 0 0 59px rgba(225,237,219,.1),0 0 0 130px rgba(0,0,0,0),0 0 0 131px rgba(225,237,219,.08);z-index:-1;}
.ds-eyebrow{color:#d4e1d4;letter-spacing:.15em;font-size:.67rem;font-weight:700;display:flex;align-items:center;gap:.6rem;text-transform:uppercase;}
.ds-eyebrow .ds-pulse{height:7px;width:7px;background:#c6d8bc;border-radius:100%;display:inline-block;box-shadow:0 0 0 4px rgba(221,237,208,.1);}
.ds-hero h1{font-family:'Manrope',sans-serif;font-size:clamp(2.2rem,4.5vw,4rem);line-height:1.08;letter-spacing:-.068em;margin:1rem 0 1rem;font-weight:700;}
.ds-hero h1 em{font-family:Georgia,serif;font-style:italic;font-weight:400;letter-spacing:-.06em;color:#d3dfc6;}
.ds-hero p{max-width:450px;line-height:1.68;color:#dce5dc;font-size:.91rem;margin:0;}
.ds-hero-tags{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:1.65rem;}
.ds-hero-tags span{border:1px solid rgba(255,255,255,.27);font-weight:600;color:#e5eae1;font-size:.68rem;border-radius:99px;padding:.44rem .75rem;}
.ds-hero-art{min-height:265px;display:flex;align-items:center;justify-content:center;position:relative;}
.ds-hero-art:before{content:'';width:218px;height:218px;border-radius:49% 49% 49% 14%;background:linear-gradient(145deg,#b8cdb0,#72947b);transform:rotate(-13deg);box-shadow:26px 21px 80px rgba(3,19,11,.26);}
.ds-hero-art:after{content:'';position:absolute;width:135px;height:135px;border:1px solid rgba(247,250,241,.4);border-radius:50%;transform:translate(40px,-15px);}
.ds-art-note{position:absolute;top:26px;left:-3%;min-width:171px;background:#fff;border-radius:14px;padding:14px 15px;box-shadow:0 14px 33px rgba(5,15,7,.22);color:var(--ink);transform:rotate(-5deg);}
.ds-art-note2{top:auto;bottom:19px;left:auto;right:-1%;transform:rotate(5deg);}
.ds-art-label{font-size:.57rem;letter-spacing:.11em;text-transform:uppercase;color:#8b9487;font-weight:800;margin-bottom:6px;}
.ds-art-line{display:flex;align-items:center;gap:.5rem;font-size:.78rem;font-weight:700;white-space:nowrap;}
.ds-art-circle{width:21px;height:21px;display:inline-flex;justify-content:center;align-items:center;background:#e2eee2;border-radius:50%;color:#346a47;font-weight:900;}
.ds-art-sub{font-size:.63rem;color:#879188;margin-top:4px;}
/* headings and section scaffolding */
.ds-topline{font-size:.66rem;font-weight:800;letter-spacing:.15em;text-transform:uppercase;color:#79847a;margin:0 0 .5rem;}
.ds-section-title{font-family:'Manrope',sans-serif;font-weight:800;letter-spacing:-.053em;font-size:1.55rem;line-height:1.18;margin:0 0 .55rem;color:var(--ink);}
.ds-section-text{font-size:.86rem;line-height:1.65;color:#727d72;margin:.2rem 0 .95rem;max-width:700px;}
.ds-pagehead{display:flex;justify-content:space-between;gap:1rem;align-items:end;padding:1.35rem 0 .65rem;}
.ds-pagehead h1{font-size:clamp(2rem,4vw,3.25rem);font-weight:800;letter-spacing:-.065em;line-height:1.09;margin:0;color:var(--ink);}
.ds-pagehead h1 em{font-family:Georgia,serif;color:#6e8c72;font-weight:400;letter-spacing:-.045em;}
.ds-pagehead p{font-size:.85rem;color:#7d857c;max-width:560px;line-height:1.55;margin:.8rem 0 .2rem;}
.ds-numbers{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:13px;margin:.2rem 0 1.7rem;}
.ds-number{padding:1.05rem 1.3rem;border:1px solid var(--line);border-radius:17px;background:#fff;}
.ds-number strong{font:800 1.8rem/1.2 'Manrope',sans-serif;letter-spacing:-.055em;color:#2a3d30;display:block;}
.ds-number span{display:block;color:#879086;font-size:.72rem;font-weight:600;margin-top:4px;}
.ds-feature{min-height:193px;background:#fff;border:1px solid var(--line);border-radius:20px;padding:1.45rem 1.65rem 1.25rem;position:relative;overflow:hidden;transition:box-shadow .2s ease,transform .2s ease;}
.ds-feature:hover{box-shadow:0 12px 26px rgba(24,51,32,.06);transform:translateY(-1px);}
.ds-feature.green{background:#e7ede4;border-color:#e1e7dc;}
.ds-icon{width:43px;height:43px;border:1px solid #e5eae2;border-radius:13px;background:#f4f6f0;display:flex;align-items:center;justify-content:center;color:var(--pine);font-size:1.22rem;margin-bottom:1rem;}
.ds-feature h3{font-weight:800;font-size:1.08rem;letter-spacing:-.045em;margin:0 0 .42rem;color:#233326;}
.ds-feature p{font-size:.82rem;color:#778177;line-height:1.58;margin:0;max-width:380px;}
.ds-feature.green p{color:#667a69;}
.ds-card-callout{border:1px solid var(--line);border-radius:19px;padding:1.2rem 1.45rem;background:#fff;}
.ds-small-label{font-size:.65rem;text-transform:uppercase;letter-spacing:.12em;color:#869084;font-weight:800;margin-bottom:.5rem;}
.ds-pic-row{display:flex;align-items:center;gap:.8rem;padding:.8rem 0;border-bottom:1px solid #e9ede7;}
.ds-pic-row:last-child{border-bottom:0;}
.ds-doc-icon{width:38px;height:44px;display:grid;place-items:center;border-radius:10px;background:#edf1e8;color:#4b6856;font-weight:800;font-family:'Manrope',sans-serif;font-size:.7rem;flex-shrink:0;}
.ds-pic-meta{min-width:0;flex:1;}
.ds-pic-name{font-size:.83rem;font-weight:800;color:#2c372e;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.ds-pic-sub{font-size:.7rem;color:#8a9388;margin-top:4px;}
.ds-pill{border-radius:99px;padding:.35rem .7rem;background:#eff1eb;color:#67806b;font-size:.62rem;font-weight:800;white-space:nowrap;}
.ds-pill.ai{background:#e2efe5;color:#39734e;}
.ds-pill.pending{background:#f4f1eb;color:#9b8e78;}
.ds-inline-stats{display:flex;gap:1rem;flex-wrap:wrap;align-items:center;margin:0 0 .7rem;color:#798578;font-size:.76rem;}
.ds-inline-stats b{font-size:.85rem;color:#2c3e31;}
.ds-onboard-tip{background:#e5ebe1;border-radius:17px;padding:1.2rem 1.4rem;margin:.5rem 0 .7rem;}
.ds-onboard-tip h3{font-size:1rem;margin:0 0 .35rem;color:#304d39;}
.ds-onboard-tip p{font-size:.8rem;color:#617465;line-height:1.6;margin:0;}
.ds-hello{background:linear-gradient(135deg,#eff3eb,#f8faf5);border-radius:18px;border:1px solid #e6ecdf;padding:1.3rem;margin-bottom:1.1rem;}
.ds-hello strong{display:block;font-size:1rem;color:#2c4835;letter-spacing:-.03em;margin-bottom:.4rem;}
.ds-hello span{font-size:.83rem;color:#7a867a;line-height:1.6;}
.ds-captionbar{display:flex;justify-content:space-between;gap:1rem;border-top:1px solid var(--line);margin-top:2.3rem;padding:1.4rem 0;font-size:.7rem;color:#919b8e;}
.ds-captionbar b{color:#5d7764;}
/* buttons and input widgets */
[data-testid="stButton"]>button, [data-testid="stFormSubmitButton"]>button, [data-testid="stDownloadButton"]>button{border-radius:99px!important;min-height:2.6rem!important;border:1px solid #dfe4dc!important;background:#fff!important;color:#314535!important;font-weight:800!important;font-size:.77rem!important;padding:.55rem 1.15rem!important;box-shadow:none!important;}
[data-testid="stButton"]>button:hover,[data-testid="stDownloadButton"]>button:hover{border-color:#8ca793!important;background:#edf3eb!important;color:#253e2f!important;}
[data-testid="stButton"]>button[kind="primary"],[data-testid="stFormSubmitButton"]>button[kind="primary"]{background:var(--pine)!important;color:#fff!important;border-color:var(--pine)!important;}
[data-testid="stButton"]>button[kind="primary"]:hover,[data-testid="stFormSubmitButton"]>button[kind="primary"]:hover{background:#385947!important;}
[data-testid="stButton"]>button:disabled,[data-testid="stFormSubmitButton"]>button:disabled{opacity:.45!important;}
[data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea, [data-testid="stSelectbox"]>div>div, [data-testid="stFileUploader"] section {border:1px solid #e1e6dc!important; border-radius:12px!important;background:#fff!important;}
[data-testid="stTextArea"] textarea{font-size:.8rem;line-height:1.65;}
[data-testid="stWidgetLabel"] label,[data-testid="stWidgetLabel"] p{font-size:.76rem!important;color:#657267!important;font-weight:700!important;}
[data-testid="stFileUploader"] section{border-style:dashed!important;padding:.5rem!important;}
[data-testid="stForm"] {border:0!important;padding:.5rem 0!important;}
[data-testid="stAlert"]{border-radius:12px!important;}
[data-testid="stExpander"] {border:1px solid var(--line)!important;border-radius:13px!important;background:#fff;}
[data-testid="stChatMessage"] {background:#fff!important;border-radius:16px!important;border:1px solid var(--line);padding:1rem!important;margin:0 0 .7rem;}
[data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] p{font-size:.85rem;line-height:1.6;}
[data-testid="stHorizontalBlock"] {gap:1rem;}
.st-key-hero-doc-btn button,.st-key-hero-onboard-btn button{width:100%;}
/* mobile */
@media(max-width:780px){
[data-testid="stMainBlockContainer"],.block-container{padding:.9rem 1.1rem 2rem!important;}
.ds-masthead{padding:.6rem 0;}
.ds-mast-meta .ds-note{display:none;}
.ds-hero{padding:2rem 1.65rem 2.2rem;display:block;min-height:auto;border-radius:19px;}
.ds-hero h1{font-size:2.6rem;}
.ds-hero-art{min-height:168px;margin-top:.3rem;transform:scale(.72);}
.ds-hero-art:before{width:176px;height:176px;}
.ds-art-note{left:0;top:17px;}
.ds-art-note2{right:0;bottom:4px;}
.ds-numbers{grid-template-columns:repeat(3,minmax(0,1fr));gap:7px;}
.ds-number{padding:.76rem .7rem;}
.ds-number strong{font-size:1.4rem;}
.ds-number span{font-size:.6rem;}
.ds-pagehead{padding:.65rem 0 .4rem;}
.ds-pagehead h1{font-size:2.3rem;}
.ds-captionbar{display:block;line-height:1.8;}
[data-testid="stHorizontalBlock"]{gap:.6rem;}
}
</style>
"""

DOCUMENT_TITLES = {
    "DOC-01": "Boas-vindas à Lume",
    "DOC-02": "Seu primeiro dia",
    "DOC-03": "Acessos e ferramentas",
    "DOC-04": "Rotina de trabalho",
    "DOC-05": "Reembolsos e despesas",
}


def document_title(doc):
    return DOCUMENT_TITLES.get(doc["id"], str(doc["nome"]).rsplit(".", 1)[0].replace("_", " "))


def masthead():
    return """<div class="ds-masthead"><div class="ds-brand"><span class="ds-brand-icon">↗</span>destrava<span class="ds-brand-ai">.ai</span></div><div class="ds-mast-meta"><span class="ds-note"><span class="ds-live"></span>Ambiente demonstrativo</span><strong>LUME / WORKSPACE</strong></div></div>"""


def hero():
    return """<section class="ds-hero"><div><div class="ds-eyebrow"><span class="ds-pulse"></span>INTELIGÊNCIA PARA O DIA A DIA</div><h1>Menos dúvidas.<br><em>Mais movimento.</em></h1><p>O conhecimento da sua empresa em um lugar só. Organize documentos, encontre respostas e comece bem cada nova jornada.</p><div class="ds-hero-tags"><span>01 / Documentos</span><span>02 / Onboarding</span><span>IA aplicada ao trabalho</span></div></div><div class="ds-hero-art"><div class="ds-art-note"><div class="ds-art-label">Biblioteca inteligente</div><div class="ds-art-line"><span class="ds-art-circle">✓</span> Informação organizada</div><div class="ds-art-sub">Tudo no lugar certo</div></div><div class="ds-art-note ds-art-note2"><div class="ds-art-label">Nova pessoa na equipe</div><div class="ds-art-line"><span class="ds-art-circle">↗</span> Encontre sua resposta</div><div class="ds-art-sub">Com fontes e contexto</div></div></div></section>"""


def pagehead(eyebrow, before, emphasis, description):
    return (f'<div class="ds-pagehead"><div><div class="ds-topline">{safe(eyebrow)}</div>'
            f'<h1>{safe(before)} <em>{safe(emphasis)}</em></h1><p>{safe(description)}</p></div></div>')


def doc_row(doc):
    raw_title = safe(document_title(doc))
    meta = safe(doc.get("categoria", "Aguardando IA"))
    done = bool(doc.get("resumo"))
    kind = "ai" if done else "pending"
    label = meta if done else "Pendente de IA"
    src = "Enviado nesta sessão" if doc.get("origem") != "Base fictícia" else "Documento de exemplo"
    return (f'<div class="ds-pic-row"><div class="ds-doc-icon">{safe(doc["id"].split("-")[-1])}</div>'
            f'<div class="ds-pic-meta"><div class="ds-pic-name">{raw_title}</div><div class="ds-pic-sub">{safe(doc["id"])} · {safe(src)}</div></div>'
            f'<span class="ds-pill {kind}">{safe(label)}</span></div>')


def footer():
    return """<div class="ds-captionbar"><span><b>destrava.ai</b> · Um projeto de IA aplicada ao trabalho</span><span>Empresa e documentos fictícios · Projeto demonstrativo</span></div>"""
