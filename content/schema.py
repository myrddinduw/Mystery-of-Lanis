from dataclasses import dataclass, field


@dataclass
class Documento:
    titulo: str
    corpo: str
    tipo: str = "diario"
    autor: str = ""
    data_campo: str = ""
    registro: str = ""


@dataclass
class Sala:
    id: str
    setor: int
    habilidade: str
    tutorial: bool
    ambiente: str
    documentos: list[Documento]
    desafio: str
    tipo_input: str
    opcoes: list[str]
    correto: list[str]
    diagnosticos: dict[str, str]
    diagnostico_padrao: str
    texto_sucesso: str
    log_narrativo: str = ""
