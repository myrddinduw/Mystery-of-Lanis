import streamlit as st

st.set_page_config(
    page_title="Estação Épsilon",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed",
)

from state import (
    init_state,
    confirmar_caderno,
    registrar_acerto,
    registrar_erro,
    avancar_sala,
)
from ui import (
    inject_css,
    render_cabecalho,
    render_ambiente,
    render_documento,
    render_desafio,
    render_feedback,
    render_acerto,
    render_boot,
    render_caderno_gate,
    render_transicao,
    render_fim,
)
from engine import avaliar
from content import get_sala, get_total_salas
from content.narrativa import BOOT, CADERNO_GATE, TRANSICOES, FINAL
from persistence import salvar_em_url, aplicar_codigo, gerar_codigo

inject_css()
init_state()
salvar_em_url()

fase = st.session_state.fase

if fase == "boot":
    render_boot(BOOT)

    st.markdown(
        '<div class="sistema">> se possui um código de retomada, insira abaixo:</div>',
        unsafe_allow_html=True,
    )
    codigo_input = st.text_input(
        "código",
        key="input_codigo_boot",
        placeholder="código do caderno...",
        label_visibility="collapsed",
    )
    if st.button("RETOMAR COM CÓDIGO", key="btn_retomar"):
        if codigo_input and aplicar_codigo(codigo_input.strip()):
            st.rerun()
        else:
            st.markdown(
                '<div class="sistema">> código inválido ou não reconhecido.</div>',
                unsafe_allow_html=True,
            )

    st.markdown("<hr>", unsafe_allow_html=True)
    if st.button("INICIALIZAR SISTEMA", key="btn_boot"):
        st.session_state.fase = "caderno"
        st.rerun()

elif fase == "caderno":
    render_caderno_gate(CADERNO_GATE)
    if st.button("CONFIRMAR — CADERNO E CANETA PRONTOS", key="btn_caderno"):
        confirmar_caderno()

elif fase in ("jogando", "feedback"):
    setor = st.session_state.setor_atual
    idx = st.session_state.sala_idx
    sala = get_sala(setor, idx)

    render_cabecalho(setor)

    with st.expander("CÓDIGO DE ACESSO — anote no caderno para retomar depois"):
        st.code(gerar_codigo(), language=None)

    render_ambiente(sala.ambiente)

    for doc in sala.documentos:
        render_documento(doc)

    if fase == "feedback":
        render_feedback(st.session_state.ultimo_diagnostico)

    escolha_raw = render_desafio(sala)

    tentativas = st.session_state.tentativas.get(sala.id, 0)
    btn_label = "SUBMETER NOVA DEDUÇÃO" if fase == "feedback" else "SUBMETER DEDUÇÃO"
    btn_key = f"btn_submit_{sala.id}_{tentativas}"

    if st.button(btn_label, key=btn_key):
        if escolha_raw is None or escolha_raw == []:
            st.markdown(
                '<div class="sistema">> selecione uma opção antes de submeter.</div>',
                unsafe_allow_html=True,
            )
        else:
            escolha = (
                escolha_raw if isinstance(escolha_raw, list) else [escolha_raw]
            )
            acertou, diagnostico = avaliar(sala, escolha)
            if acertou:
                registrar_acerto(sala.id, sala.log_narrativo, sala.texto_sucesso)
            else:
                registrar_erro(sala.id, diagnostico)

elif fase == "acerto":
    setor = st.session_state.setor_atual
    idx = st.session_state.sala_idx
    sala = get_sala(setor, idx)

    render_cabecalho(setor)

    with st.expander("CÓDIGO DE ACESSO — anote no caderno para retomar depois"):
        st.code(gerar_codigo(), language=None)

    if st.session_state.log_acerto_pendente:
        texto_sucesso, log = st.session_state.log_acerto_pendente
        render_acerto(texto_sucesso, log)

    if st.button("CONTINUAR", key=f"btn_continuar_{sala.id}"):
        st.session_state.log_acerto_pendente = None
        avancar_sala()

elif fase == "transicao_setor":
    setor_anterior = st.session_state.setor_anterior
    setor_atual = st.session_state.setor_atual

    render_cabecalho(setor_anterior)

    with st.expander("CÓDIGO DE ACESSO — anote no caderno para retomar depois"):
        st.code(gerar_codigo(), language=None)

    render_transicao(TRANSICOES.get(setor_anterior, "> próximo setor..."))

    if st.button("CONTINUAR", key=f"btn_transicao_{setor_anterior}_{setor_atual}"):
        st.session_state.fase = "jogando"
        st.rerun()

elif fase == "fim":
    render_fim(FINAL, st.session_state.logs_descobertos)
