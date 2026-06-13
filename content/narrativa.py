BOOT = """\
ESTAÇÃO DE PESQUISA BOTÂNICA ÉPSILON — TERMINAL DE ACESSO REMOTO
VERSÃO 7.4.1 — PROTOCOLO DE RECUPERAÇÃO DE EMERGÊNCIA

> inicializando sistema...
> verificando integridade dos arquivos de campo...
> 7 SETORES BLOQUEADOS — modo de emergência ativo
> última atividade registrada: CICLO 47, DIA 23
> tempo desde o último acesso humano: 21 dias

Você é Lanis. Especialista em biossistemas matemáticos.

Você chegou à Estação Épsilon três semanas após o silêncio das comunicações.
O terminal de acesso está online. Os documentos estão preservados. A equipe não está.

Para destrancar os setores e recuperar os registros completos, o terminal exige
que você leia os documentos recuperados e insira suas deduções diretamente.

O terminal não aceita suposições.
Apenas deduções sustentadas pelo que está escrito.

Prepare seu caderno.\
"""

CADERNO_GATE = """\
PROTOCOLO DE CALIBRAÇÃO — FASE INICIAL

> aviso do sistema: o terminal registra apenas deduções verificadas pelo operador.

Antes de iniciar, confirme as condições de operação:

— Um caderno ou folha em branco está à sua frente.
— Uma caneta ou lápis está na sua mão.
— Você lerá cada documento com atenção e anotará o que encontrar
  antes de submeter qualquer dedução ao terminal.

O terminal não fornece dicas. Quando detecta uma falha de leitura,
ele devolve uma pergunta. Nada mais.

> aguardando confirmação do operador...\
"""

TRANSICOES = {
    0: """\
CALIBRAÇÃO CONCLUÍDA — ACESSO AO ARQUIVO DE CAMPO LIBERADO

> 5 de 7 setores desbloqueados.
> carregando Diário de Campo da equipe Épsilon...
> aviso: os documentos que se seguem são registros reais da equipe.
> a linguagem é mais densa. as premissas, mais numerosas.
> o terminal continua esperando apenas suas deduções.\
""",
    1: """\
DIÁRIO DE CAMPO — ARQUIVOS ESGOTADOS

> todos os registros acessíveis do Diário de Campo foram verificados.
> acesso ao Relatório Técnico classificado pendente de liberação futura.
> sessão encerrada.\
""",
}

FINAL = """\
TODOS OS SETORES VERIFICADOS — ACESSO TOTAL CONCEDIDO

> recuperando arquivos finais do Setor Delta...
> decodificando última transmissão...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ARQUIVO FINAL — DECODIFICADO
Transmissão de emergência — Dra. Rafaela Vello
Ciclo 47, Dia 23 — 03h41

"Carlos, Marina — saiam agora. O Protocolo Ômega foi ativado.
Tranquei o Setor Delta por dentro. Não é um erro.
A anomalia não pode cruzar os portões.
O bosque lá fora ainda segue os axiomas.
Que continue assim."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

> transmissão encerrada.
> localização de R. Vello: Setor Delta — STATUS DESCONHECIDO.
> o Setor Delta permanece selado.

Lanis fecha o terminal.

Ela sabe o que encontrou.
E sabe que Rafaela Vello tomou a única decisão
que os axiomas do bosque jamais poderiam calcular.\
"""
