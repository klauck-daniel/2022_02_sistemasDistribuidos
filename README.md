#Repositório para trabalho do curso de  Sistemas Distribuídos e de Tempo Real  do GA - UNISINOS. 2022/02

Trabalho 2 - Entrega da lista 3 (pode ser em duplas ou em trios)

Data da entrega: 26/09 (apresentação individual para a prof, sem slides)

Postar somente o arquivo .c no Moodle

Construa um programa com três threads, TS1, TS2 e TA. TS1 e TS2 devem gerar valores
aleatórios e preencher dois vetores, VS1 e VS2, com 5 posições cada, com estes valores (isso
simula as últimas leituras de dois sensores – você deve dizer qual é a aplicação que está
simulando e o significado das grandezas que está “medindo”)(contextualizar). TA deve analisar se os valores
lidos são aceitáveis ou não (você determina o que é aceitável de acordo com a sua aplicação).
Os valores não aceitáveis devem ser gravados nos arquivos log_S1.txt e log_S2.txt juntamente
com a data e a hora e a descrição de cada evento. Ex.: “valor muito alto (ou muito baixo),
possível [descrição do que pode ter acontecido]”. As threads irão executar ao mesmo tempo e
o acesso aos vetores deve ser protegido por mutex.
Obs.:
• Veja o exemplo de uso de arquivos no Moodle.
• Na aula 2 há um link sobre data e hora em C.
• Para gerar valores aleatórios, use a função rand.
• Considere que os arquivos serão criados na mesma pasta que o executável. É possível
fazer isso no online gdb.
• Use um mutex para cada vetor.
• Entregas: um PDF (1 página é suficiente) contendo uma breve descrição da aplicação
que você está simulando (grandezas que você está “medindo” e significados dos
eventos – valores muito baixos ou muito altos) e o código em linguagem C. Não poste
arquivos .zip etc. O Moodle está configurado para aceitar arquivos separados.
