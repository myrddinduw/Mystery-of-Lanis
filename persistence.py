import json
import base64
import streamlit as st
from content import get_sala, get_total_salas, TOTAL_SETORES


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
    data = {
        "v": 1,
        "fa": st.session_state.fase,
        "sa": st.session_state.setor_atual,
        "si": st.session_state.sala_idx,
        "sn": st.session_state.setor_anterior,
        "cc": st.session_state.caderno_confirmado,
        "t": st.session_state.tentativas,
    }
    payload = json.dumps(data, separators=(",", ":")).encode()
    return base64.urlsafe_b64encode(payload).decode().rstrip("=")


def aplicar_codigo(codigo: str) -> bool:
    try:
        padding = (4 - len(codigo) % 4) % 4
        raw = base64.urlsafe_b64decode(codigo + "=" * padding)
        data = json.loads(raw.decode())

        if data.get("v") != 1:
            return False

        setor = int(data.get("sa", 0))
        idx = int(data.get("si", 0))
        setor = max(0, min(setor, TOTAL_SETORES - 1))
        total = get_total_salas(setor)
        if total == 0:
            setor = 0
            idx = 0
            total = get_total_salas(0)
        idx = max(0, min(idx, total - 1))

        fase = str(data.get("fa", "jogando"))
        caderno = bool(data.get("cc", False))
        if fase in ("feedback", "acerto"):
            fase = "jogando"
        if caderno and fase == "boot":
            fase = "jogando"

        st.session_state.setor_atual = setor
        st.session_state.sala_idx = idx
        st.session_state.setor_anterior = data.get("sn")
        st.session_state.caderno_confirmado = caderno
        st.session_state.fase = fase
        st.session_state.tentativas = {
            str(k): int(v) for k, v in data.get("t", {}).items()
        }
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
