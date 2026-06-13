import streamlit as st
from content.schema import Sala, Documento
from content import NOMES_SETORES

_CSS = """
<style>
/* ── reset & hide chrome padrão ── */
#MainMenu, footer, header { display: none !important; }
.stDeployButton { display: none !important; }
[data-testid="stToolbar"] { display: none !important; }

/* ── layout raiz ── */
.stApp {
    background-color: #080c10;
    color: #b0bec5;
    font-family: 'JetBrains Mono', 'Courier New', monospace;
}
.main .block-container {
    max-width: 640px;
    padding: 1rem 1rem 3rem;
}

/* ── cabeçalho fixo do terminal ── */
.terminal-header {
    border-bottom: 1px solid #1e4d2b;
    padding-bottom: 0.6rem;
    margin-bottom: 1.25rem;
    color: #4dff91;
    font-size: 0.85rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    font-family: 'JetBrains Mono', 'Courier New', monospace;
}
.terminal-header .setor-status {
    color: #2a8a50;
    margin-top: 0.2rem;
    font-size: 0.78rem;
    letter-spacing: 0.1em;
}

/* ── linhas de sistema ── */
.sistema {
    color: #2a7a45;
    font-size: 1rem;
    margin: 0.2rem 0;
    line-height: 1.7;
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    white-space: pre-wrap;
}

/* ── documento recuperado (papel envelhecido) ── */
.documento-wrapper {
    margin: 1.2rem 0;
}
.documento {
    position: relative;
    padding: 1.4rem 1.6rem 1.6rem;
    border: 1px solid #7a6040;
    border-radius: 2px;
    font-family: Georgia, 'Lora', 'Times New Roman', serif;
    color: #3a2f24;
    line-height: 1.8;
    text-align: justify;
    overflow: hidden;
    background:
        linear-gradient(160deg, #f0e7d2 0%, #e8dbbe 40%, #ddd0a8 100%);
    box-shadow:
        inset 0 0 40px rgba(90, 60, 20, 0.18),
        inset 2px 2px 12px rgba(0,0,0,0.08),
        0 3px 12px rgba(0,0,0,0.5);
}
.documento::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
        radial-gradient(ellipse at 8% 12%, rgba(130, 90, 40, 0.12) 0%, transparent 55%),
        radial-gradient(ellipse at 92% 88%, rgba(100, 65, 25, 0.14) 0%, transparent 50%),
        radial-gradient(ellipse at 50% 5%, rgba(80, 50, 20, 0.08) 0%, transparent 35%);
    pointer-events: none;
}
.documento-artigo {
    background:
        linear-gradient(155deg, #ece3cf 0%, #e2d5b5 45%, #d8c99e 100%);
}

/* ── timbre do documento ── */
.doc-timbre {
    font-family: Georgia, serif;
    font-size: 0.75rem;
    letter-spacing: 0.13em;
    text-transform: uppercase;
    color: #5c4025;
    border-bottom: 1px solid #8b7050;
    padding-bottom: 0.55rem;
    margin-bottom: 0.9rem;
    opacity: 0.88;
    position: relative;
}
.doc-titulo {
    font-size: 0.9rem;
    font-weight: bold;
    margin-bottom: 0.15rem;
    color: #3a2a14;
}
.doc-meta {
    font-size: 0.75rem;
    color: #6b5035;
}

/* ── corpo do documento ── */
.doc-corpo {
    font-size: 1.05rem;
    line-height: 1.8;
    position: relative;
}

/* ── caixa de desafio ── */
.desafio-label {
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    font-size: 1rem;
    color: #7ab89a;
    margin: 1.25rem 0 0.5rem;
    line-height: 1.7;
}
.desafio-label::before {
    content: '> ';
    color: #2a8a50;
}

/* ── caixa de feedback ── */
.feedback-box {
    border: 1px solid #3a3010;
    background: #111006;
    padding: 0.9rem 1.1rem;
    margin: 1rem 0;
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    font-size: 1rem;
    color: #c8a96a;
    line-height: 1.75;
    white-space: pre-wrap;
}
.feedback-box::before {
    content: '> TERMINAL // ';
    color: #6a5020;
    display: block;
    margin-bottom: 0.4rem;
    font-size: 0.78rem;
    letter-spacing: 0.1em;
}

/* ── log de fragmento narrativo ── */
.log-fragment {
    border-left: 2px solid #1e4d2b;
    padding: 0.6rem 1rem;
    margin: 1rem 0;
    color: #3a8a55;
    font-size: 0.95rem;
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    white-space: pre-wrap;
    line-height: 1.75;
}

/* ── tela de acerto ── */
.acerto-box {
    border: 1px solid #1e5535;
    background: #071209;
    padding: 0.9rem 1.1rem;
    margin: 1rem 0;
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    font-size: 1rem;
    color: #4dff91;
    line-height: 1.75;
}
.acerto-box::before {
    content: '> DEDUÇÃO VALIDADA // ';
    color: #2a8a50;
    display: block;
    margin-bottom: 0.4rem;
    font-size: 0.78rem;
    letter-spacing: 0.1em;
}

/* ── tela de boot e fim ── */
.boot-text {
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    font-size: 1rem;
    color: #7ab89a;
    white-space: pre-wrap;
    line-height: 1.9;
    margin-bottom: 1.5rem;
}
.fim-text {
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    font-size: 1rem;
    color: #7ab89a;
    white-space: pre-wrap;
    line-height: 1.9;
    margin-bottom: 1rem;
}
.fim-destaque {
    color: #4dff91;
    font-size: 0.85rem;
}

/* ── ajustes de widgets Streamlit ── */
.stButton > button {
    background: transparent;
    border: 1px solid #2a8a50;
    color: #4dff91;
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    font-size: 0.9rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    padding: 0.5rem 1.1rem;
    border-radius: 2px;
    width: 100%;
    margin-top: 0.75rem;
}
.stButton > button:hover {
    background: #0d2015;
    border-color: #4dff91;
}
.stRadio > label {
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    font-size: 0.8rem;
    color: #b0bec5;
}
.stMultiSelect > label {
    font-family: 'JetBrains Mono', 'Courier New', monospace;
    font-size: 0.8rem;
    color: #b0bec5;
}
div[data-testid="stRadio"] label {
    font-family: 'JetBrains Mono', 'Courier New', monospace !important;
    font-size: 0.8rem !important;
}
div[role="radiogroup"] label span {
    color: #b0bec5 !important;
}
hr {
    border-color: #1a2a1a;
    margin: 1.2rem 0;
}
</style>
"""


def inject_css() -> None:
    st.markdown(_CSS, unsafe_allow_html=True)


def render_cabecalho(setor: int) -> None:
    nome = NOMES_SETORES.get(setor, f"SETOR {setor}")
    st.markdown(
        f"""<div class="terminal-header">
ESTAÇÃO ÉPSILON // TERMINAL DE ACESSO
<div class="setor-status">{nome}</div>
</div>""",
        unsafe_allow_html=True,
    )


def render_ambiente(texto: str) -> None:
    linhas = "\n".join(
        f"> {l}" if not l.startswith(">") else l for l in texto.splitlines()
    )
    st.markdown(
        f'<div class="sistema">{linhas}</div>',
        unsafe_allow_html=True,
    )
    st.markdown("<hr>", unsafe_allow_html=True)


def render_documento(doc: Documento) -> None:
    tipo_class = "documento-artigo" if doc.tipo == "artigo" else ""

    timbre_parts = []
    if doc.titulo:
        timbre_parts.append(f'<div class="doc-titulo">{doc.titulo}</div>')
    meta = " &nbsp;|&nbsp; ".join(
        p for p in [doc.autor, doc.data_campo, doc.registro] if p
    )
    if meta:
        timbre_parts.append(f'<div class="doc-meta">{meta}</div>')

    timbre_html = (
        f'<div class="doc-timbre">{"".join(timbre_parts)}</div>'
        if timbre_parts
        else ""
    )

    corpo_escaped = (
        doc.corpo
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\n\n", '</p><p class="doc-corpo" style="margin-top:0.7rem">')
        .replace("\n", "<br>")
    )

    st.markdown(
        f"""<div class="documento-wrapper">
<div class="documento {tipo_class}">
{timbre_html}
<p class="doc-corpo">{corpo_escaped}</p>
</div>
</div>""",
        unsafe_allow_html=True,
    )


def render_desafio(sala: Sala) -> list[str] | str | None:
    st.markdown(
        f'<div class="desafio-label">{sala.desafio}</div>',
        unsafe_allow_html=True,
    )

    key = f"input_{sala.id}"

    if sala.tipo_input == "multi":
        return st.multiselect(
            "Selecione todas as opções corretas:",
            options=sala.opcoes,
            key=key,
            label_visibility="collapsed",
        )
    else:
        return st.radio(
            "Selecione uma opção:",
            options=sala.opcoes,
            key=key,
            index=None,
            label_visibility="collapsed",
        )


def render_feedback(pergunta: str) -> None:
    st.markdown(
        f'<div class="feedback-box">{pergunta}</div>',
        unsafe_allow_html=True,
    )


def render_acerto(texto_sucesso: str, log: str) -> None:
    st.markdown(
        f'<div class="acerto-box">{texto_sucesso}</div>',
        unsafe_allow_html=True,
    )
    if log:
        render_log(log)


def render_log(fragmento: str) -> None:
    escaped = (
        fragmento
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    st.markdown(
        f'<div class="log-fragment">{escaped}</div>',
        unsafe_allow_html=True,
    )


def render_boot(texto: str) -> None:
    st.markdown(
        f'<div class="boot-text">{texto}</div>',
        unsafe_allow_html=True,
    )


def render_caderno_gate(texto: str) -> None:
    st.markdown(
        f'<div class="boot-text">{texto}</div>',
        unsafe_allow_html=True,
    )
    st.markdown("<hr>", unsafe_allow_html=True)


def render_transicao(texto: str) -> None:
    st.markdown(
        f'<div class="sistema">{texto}</div>',
        unsafe_allow_html=True,
    )


def render_fim(texto_final: str, logs: list[str]) -> None:
    st.markdown('<div class="terminal-header">ESTAÇÃO ÉPSILON // TERMINAL DE ACESSO<div class="setor-status">SESSÃO ENCERRADA</div></div>', unsafe_allow_html=True)

    if logs:
        st.markdown('<div class="sistema">> REGISTROS RECUPERADOS DURANTE A SESSÃO:</div>', unsafe_allow_html=True)
        for log in logs:
            render_log(log)
        st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown(
        f'<div class="fim-text">{texto_final}</div>',
        unsafe_allow_html=True,
    )
