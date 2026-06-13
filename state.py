import streamlit as st
from content import get_total_salas, proximo_setor_disponivel


def init_state() -> None:
    defaults = {
        "fase": "boot",
        "setor_atual": 0,
        "setor_anterior": None,
        "sala_idx": 0,
        "tentativas": {},
        "historico": [],
        "caderno_confirmado": False,
        "logs_descobertos": [],
        "ultimo_diagnostico": None,
        "escolha_pendente": None,
        "log_acerto_pendente": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

    from persistence import retomar_se_possivel
    retomar_se_possivel()


def confirmar_caderno() -> None:
    st.session_state.caderno_confirmado = True
    st.session_state.fase = "jogando"
    st.rerun()


def registrar_acerto(sala_id: str, log: str, texto_sucesso: str) -> None:
    st.session_state.historico.append({"sala": sala_id, "acertou": True})
    if log:
        st.session_state.logs_descobertos.append(log)
    st.session_state.ultimo_diagnostico = None
    st.session_state.log_acerto_pendente = (texto_sucesso, log)
    st.session_state.fase = "acerto"
    st.rerun()


def registrar_erro(sala_id: str, diagnostico: str) -> None:
    st.session_state.tentativas[sala_id] = (
        st.session_state.tentativas.get(sala_id, 0) + 1
    )
    st.session_state.ultimo_diagnostico = diagnostico
    st.session_state.fase = "feedback"
    st.rerun()


def avancar_sala() -> None:
    setor = st.session_state.setor_atual
    idx = st.session_state.sala_idx + 1

    if idx < get_total_salas(setor):
        st.session_state.sala_idx = idx
        st.session_state.fase = "jogando"
    else:
        proximo = proximo_setor_disponivel(setor)
        if proximo is not None:
            st.session_state.setor_anterior = setor
            st.session_state.setor_atual = proximo
            st.session_state.sala_idx = 0
            st.session_state.fase = "transicao_setor"
        else:
            st.session_state.fase = "fim"

    st.rerun()
