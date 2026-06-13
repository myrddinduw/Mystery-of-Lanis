from content.schema import Sala, Documento

SALAS: list[Sala] = [
    Sala(
        id="2.1",
        setor=2,
        habilidade="separar hipótese descartada de dado operacional",
        tutorial=False,
        ambiente=(
            "> SETOR 2 — RELATÓRIO TÉCNICO\n"
            "> carregando Rel. Cont. Nº 002 — CLASSIFICADO...\n"
            "> aviso: documento contém múltiplas hipóteses testadas.\n"
            "> nem toda variável testada é uma variável que importa."
        ),
        documentos=[
            Documento(
                titulo="Relatório de Contenção — Espécime Ω (Ômega)",
                corpo=(
                    "DELINEAMENTO E CALIBRAÇÃO\n"
                    "Quarenta e oito canteiros de controle (n=48, ±0,3°C, solo pH 6,8±0,1) foram "
                    "utilizados para isolar os fatores determinantes do efeito de alteração da Ômega "
                    "sobre espécimes vizinhos. Todos os sensores foram recalibrados no Ciclo 46 para "
                    "garantir consistência inter-ciclo.\n\n"
                    "HIPÓTESE 1 — LUMINOSIDADE (descartada)\n"
                    "Testamos a hipótese de que intensidade luminosa (alta vs. baixa) modula o efeito "
                    "de alteração. Após 72h de exposição em 16 canteiros pareados, nenhuma diferença "
                    "significativa foi observada entre condições (p=0,41). A hipótese de efeito por "
                    "luminosidade foi descartada.\n\n"
                    "HIPÓTESE 2 — TEMPERATURA E CONTATO DE RAÍZES (confirmada)\n"
                    "Temperatura e contato radicular foram testados em conjunto e separadamente:\n"
                    "— Temperatura ≥ 15°C + contato direto de raízes: efeito de alteração ativo "
                    "em 100% dos espécimes vizinhos (n=12/12).\n"
                    "— Temperatura < 15°C + contato direto de raízes: zero alterações (n=0/12).\n"
                    "— Temperatura ≥ 15°C + barreira radicular (tela de separação, malha 2mm): "
                    "zero alterações (n=0/12).\n"
                    "Conclusão operacional: o efeito só se manifesta quando as duas condições "
                    "ocorrem simultaneamente. A anulação de qualquer uma das duas é suficiente "
                    "para tornar a Ômega inerte em relação às plantas vizinhas.\n\n"
                    "CONSIDERAÇÕES ADICIONAIS\n"
                    "Volume amostral (n=48) foi considerado adequado para os propósitos operacionais. "
                    "Futuros estudos poderão expandir para n=96 para maior robustez estatística. "
                    "Variáveis de umidade do solo não mostraram correlação com o efeito "
                    "nas condições testadas."
                ),
                tipo="artigo",
                autor="Dra. R. Vello; Dr. C. Andrade (coord.)",
                data_campo="Estação Épsilon — Ciclo 47, Dias 12–16",
                registro="Rel. Cont. Nº 002 — CLASSIFICADO",
            )
        ],
        desafio=(
            "Lanis precisa atravessar o canteiro 12 para recuperar o último log de Vello. "
            "O efeito de alteração da Ômega pode estar ativo. "
            "Com base no relatório, qual medida garante que o efeito não se dispara?"
        ),
        tipo_input="single",
        opcoes=[
            "Instalar barreiras de luminosidade antes de entrar",
            "Manter a temperatura do canteiro abaixo de 15°C antes de atravessar",
            "Irrigar o solo com excesso de água para neutralizar o efeito",
            "Coletar nova amostragem ampliada (n=96) antes de qualquer intervenção",
        ],
        correto=["Manter a temperatura do canteiro abaixo de 15°C antes de atravessar"],
        diagnosticos={
            "Instalar barreiras de luminosidade antes de entrar": (
                "Essa hipótese foi testada no relatório — com que resultado? "
                "O que o valor p=0,41 indica sobre a relação entre luminosidade e o efeito de alteração?"
            ),
            "Irrigar o solo com excesso de água para neutralizar o efeito": (
                "O relatório testa a umidade do solo como variável que afeta o efeito? "
                "O que a seção de considerações adicionais diz sobre ela?"
            ),
            "Coletar nova amostragem ampliada (n=96) antes de qualquer intervenção": (
                "O relatório menciona n=96 como dado operacional já disponível, "
                "ou como sugestão metodológica para estudos futuros? "
                "Qual a diferença entre o que ainda precisa ser estudado e o que já foi concluído?"
            ),
        },
        diagnostico_padrao=(
            "O relatório apresenta duas hipóteses: uma descartada e uma confirmada. "
            "Quais são as condições que, segundo a hipótese confirmada, devem ocorrer "
            "simultaneamente para o efeito se manifestar? "
            "O que acontece se Lanis anular uma delas antes de entrar?"
        ),
        texto_sucesso=(
            "Dedução correta. O efeito exige temperatura ≥ 15°C E contato de raízes simultaneamente. "
            "Manter o canteiro abaixo de 15°C anula a primeira condição — a Ômega fica inerte. "
            "Arquivo validado."
        ),
        log_narrativo=(
            "NOTA INTERNA — Dr. C. Andrade (adicionada ao Rel. Cont. Nº 002 em Ciclo 47, Dia 18):\n"
            "\"Acabei de confirmar o pH do canteiro 12: 8,1 — solo alcalino. "
            "Se os resultados de pH do Art. Téc. Nº 003 se aplicarem aqui, "
            "o frio sozinho pode não ser suficiente para uma contenção definitiva. "
            "Preciso falar com Vello urgentemente.\""
        ),
    ),

    Sala(
        id="2.2",
        setor=2,
        habilidade="identificar fatores com efeito a partir de hipóteses nulas rejeitadas",
        tutorial=False,
        ambiente=(
            "> carregando Art. Téc. Nº 003 — análise de fatores de ativação...\n"
            "> aviso: documento usa linguagem de teste de hipóteses.\n"
            "> rejeitar H0 significa que há evidência de efeito. não rejeitar: ausência de evidência."
        ),
        documentos=[
            Documento(
                titulo="Análise de Fatores de Ativação da Dormência — Espécime Ω",
                corpo=(
                    "DELINEAMENTO\n"
                    "Para identificar os fatores determinantes da saída de dormência da Ômega, "
                    "foram testadas três hipóteses nulas independentes em amostras de n=24 por fator, "
                    "com análise post-hoc de Bonferroni para controle de erros tipo I. "
                    "Critério de significância: α=0,05.\n\n"
                    "HIPÓTESE NULA 1 — TEMPERATURA\n"
                    "H0: variações de temperatura não influenciam a saída de dormência da Ômega.\n"
                    "Resultado: H0 rejeitada (p<0,01). Temperaturas acima de 15°C estão associadas "
                    "à retomada de atividade em 100% dos espécimes testados.\n\n"
                    "HIPÓTESE NULA 2 — pH DO SOLO\n"
                    "H0: o pH do solo não influencia a saída de dormência da Ômega.\n"
                    "Resultado: H0 rejeitada (p=0,02). pH alcalino (>7,5) está associado à retomada "
                    "de atividade mesmo sob temperaturas marginalmente abaixo de 15°C "
                    "em 58% dos espécimes testados.\n\n"
                    "HIPÓTESE NULA 3 — LUMINOSIDADE\n"
                    "H0: intensidade luminosa não influencia a saída de dormência da Ômega.\n"
                    "Resultado: H0 não rejeitada (p=0,63). Não há evidência de efeito da luminosidade "
                    "sobre a saída de dormência nas condições testadas.\n\n"
                    "NOTA FINAL\n"
                    "O tamanho amostral (n=24/fator) foi suficiente para o poder estatístico "
                    "planejado (80%). Os resultados de pH merecem atenção especial: "
                    "se o solo de Delta for alcalino, a contenção exclusivamente por frio "
                    "pode não ser definitiva."
                ),
                tipo="artigo",
                autor="Dr. C. Andrade",
                data_campo="Estação Épsilon — Ciclo 47, Dia 15",
                registro="Art. Téc. Nº 003",
            )
        ],
        desafio=(
            "Quais fatores influenciam de forma estatisticamente significativa "
            "a saída da Ômega da dormência, segundo o artigo de Andrade?"
        ),
        tipo_input="multi",
        opcoes=["Temperatura", "pH do solo", "Luminosidade", "Tamanho da amostra (n=24)"],
        correto=["Temperatura", "pH do solo"],
        diagnosticos={
            "Luminosidade": (
                "O artigo rejeita ou não rejeita a hipótese nula para luminosidade? "
                "O que significa não rejeitar H0 — o fator tem efeito confirmado, "
                "ou não há evidência suficiente de efeito?"
            ),
            "Tamanho da amostra (n=24)": (
                "O tamanho da amostra é um dos fatores testados quanto à saída de dormência, "
                "ou é um parâmetro do próprio delineamento do estudo? "
                "O artigo formula uma hipótese nula sobre n=24?"
            ),
        },
        diagnostico_padrao=(
            "Para cada hipótese nula, localize no artigo se ela foi 'rejeitada' ou 'não rejeitada'. "
            "Rejeitar H0 = há evidência de efeito. Não rejeitar = sem evidência de efeito. "
            "Com base nisso, quais hipóteses foram rejeitadas?"
        ),
        texto_sucesso=(
            "Dedução correta. Temperatura (p<0,01) e pH do solo (p=0,02) têm H0 rejeitadas — "
            "há evidência de que ambos influenciam a saída de dormência. "
            "Luminosidade (p=0,63) e tamanho amostral não são fatores de efeito. "
            "Arquivo validado."
        ),
        log_narrativo=(
            "LOG RECUPERADO — Dra. R. Vello, Ciclo 47, Dia 19 (anotação no próprio artigo):\n"
            "\"Carlos — lemos o mesmo dado. pH 8,1 no canteiro 12. "
            "Se H0 de pH foi rejeitada com p=0,02, não posso ignorar os 58%. "
            "O sistema de refrigeração precisa ser autônomo e permanente — "
            "não pode depender da rede principal. Estou verificando as baterias de reserva.\""
        ),
    ),
]
