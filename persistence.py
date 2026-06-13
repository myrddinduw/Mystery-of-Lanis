import streamlit as st
from content import get_sala, get_total_salas, TOTAL_SETORES

# Formato do código: 4 caracteres — ex.: "1B2C"
#   [0] versão: "1"
#   [1] setor:  "A"–"D"  (setor 0–3)
#   [2] sala:   hex "0"–"F" (sala_idx 0–15)
#   [3] caderno: "C" (confirmado) | "N" (não)


def _reconstruir_logs(setor_atual: int, sala_idx: int, fase: str) -> list[str]:
    logs = []
    for s in range(TOTAL_SETORES):
        total = get_total_salas(s)
        for i in range(total):
            if fase == "fim":
                sala = get_sala(s, i)
                if sala.log_narrativo:
                    logs.append(sala.log_narrativo)
            elif s < setor_atual or (s == setor_atual and i < sala_idx):
                sala = get_sala(s, i)
                if sala.log_narrativo:
                    logs.append(sala.log_narrativo)
    return logs


def gerar_codigo() -> str:
    setor = st.session_state.setor_atual
    idx = st.session_state.sala_idx
    cc = st.session_state.caderno_confirmado
    return f"1{chr(ord('A') + setor)}{format(idx, 'X')}{'C' if cc else 'N'}"


def aplicar_codigo(codigo: str) -> bool:
    try:
        codigo = codigo.strip().upper()
        if len(codigo) != 4 or codigo[0] != "1":
            return False

        setor = ord(codigo[1]) - ord("A")
        idx = int(codigo[2], 16)
        cc = codigo[3] == "C"

        if not (0 <= setor < TOTAL_SETORES):
            return False
        total = get_total_salas(setor)
        if total == 0 or not (0 <= idx < total):
            return False

        fase = "jogando" if cc else "boot"

        st.session_state.setor_atual = setor
        st.session_state.sala_idx = idx
        st.session_state.setor_anterior = setor if idx == 0 and setor > 0 else None
        st.session_state.caderno_confirmado = cc
        st.session_state.fase = fase
        st.session_state.tentativas = {}
        st.session_state.historico = []
        st.session_state.ultimo_diagnostico = None
        st.session_state.log_acerto_pendente = None
        st.session_state.logs_descobertos = _reconstruir_logs(setor, idx, fase)
        return True
    except Exception:
        return False


def salvar_em_url() -> None:
    if st.session_state.get("fase") not in ("boot", "caderno"):
        st.query_params["s"] = gerar_codigo()


def retomar_se_possivel() -> None:
    if st.session_state.get("_retomada_tentada"):
        return
    st.session_state["_retomada_tentada"] = True
    codigo = st.query_params.get("s", "")
    if codigo:
        aplicar_codigo(codigo)
