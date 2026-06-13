from content import setor_0_treino, setor_1_diario, setor_2_relatorio, setor_3_debate
from content.schema import Sala

_SETORES: list[list[Sala]] = [
    setor_0_treino.SALAS,
    setor_1_diario.SALAS,
    setor_2_relatorio.SALAS,
    setor_3_debate.SALAS,
]

TOTAL_SETORES = len(_SETORES)

NOMES_SETORES = {
    0: "SETOR 0 — CALIBRAÇÃO",
    1: "SETOR 1 — DIÁRIO DE CAMPO",
    2: "SETOR 2 — RELATÓRIO TÉCNICO",
    3: "SETOR 3 — DEBATE ACADÊMICO",
}


def get_sala(setor: int, idx: int) -> Sala:
    return _SETORES[setor][idx]


def get_total_salas(setor: int) -> int:
    return len(_SETORES[setor])


def proximo_setor_disponivel(setor_atual: int) -> int | None:
    for s in range(setor_atual + 1, TOTAL_SETORES):
        if _SETORES[s]:
            return s
    return None
