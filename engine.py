from content.schema import Sala


def avaliar(sala: Sala, escolha: list[str]) -> tuple[bool, str | None]:
    if set(escolha) == set(sala.correto):
        return True, None

    pergunta = sala.diagnostico_padrao
    for opcao in escolha:
        if opcao in sala.diagnosticos:
            pergunta = sala.diagnosticos[opcao]
            break

    return False, pergunta
