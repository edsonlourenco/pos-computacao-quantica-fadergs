# Computadores Quânticos e Algoritmos Quânticos

- Objetivos da unidade
  - Compreender a estrutura de um computador quântico
  - Compreender os princípios de funcionamento de um algoritmo quântico
  - Entender os resultados de um processamento quântico

- Exemplo de arquitetura: D-Wave
  - Abordagem diferente da computação quântica baseada em portas lógicas
  - Processador supercondutor com qubits de fluxo: loops micrométricos de metal supercondutor com junções de Josephson
    - D-Wave One (2011): primeiro processador comercial, com 128 qubits
  - Usa anelamento quântico (quantum annealing)
    - Processo de busca do mínimo global de uma função a partir de um conjunto de soluções candidatas
    - Parte de uma superposição quântica de todos os estados candidatos e evolui no tempo em direção a uma solução de baixa energia
    - Útil para problemas de otimização (minimização de energia) e para amostragem probabilística (ex.: aplicações de aprendizado de máquina)
  - Qubit central: o SQUID (dispositivo supercondutor de interferência quântica), equivalente ao transistor no computador clássico
    - Existem dois tipos: de corrente direta (DC) e de rádio frequência (RF)
    - O material do loop, geralmente nióbio, torna-se supercondutor quando resfriado e passa a exibir efeitos quânticos
  - Acopladores (loops supercondutores) conectam os SQUIDs entre si, permitindo formar um processador de múltiplos qubits

- Estrutura geral de um computador quântico (camadas)
  - Plano quântico de dados: onde os qubits físicos estão fisicamente localizados, incluindo hardware e circuitos de suporte às portas lógicas
  - Plano de medição: hardware responsável por controlar os sinais enviados aos qubits e por processar a saída das medições (às vezes chamado de plano de controle e medição)
  - Plano de controle do processador: identifica e dispara as operações das portas lógicas específicas, executando o código fornecido por um processador clássico (host)
  - Camadas adicionais: interface quântico-clássica, ambiente de programação quântica (linguagem assembly quântica, simuladores, compositor de circuitos, APIs em linguagens de alto nível) e aplicações de negócio construídas sobre elas
  - Infraestrutura física de suporte: um refrigerador de diluição leva o processador a temperaturas extremamente baixas (da ordem de 15 milikelvin, mais frio que o espaço profundo), com amplificadores quânticos, isoladores criogênicos e blindagem contra radiação eletromagnética para preservar a qualidade dos qubits

- Redes quânticas (internet quântica)
  - Relação com computadores quânticos análoga à relação entre computadores clássicos e redes de computadores tradicionais
  - Os nós de uma rede quântica são processadores quânticos de um ou mais qubits; a linha de comunicação mais usada é a fibra ótica
  - Exemplo: rede de distribuição de chaves quânticas de Tóquio, com arquitetura de três camadas
    - Camada quântica: links quânticos ponto a ponto que geram chaves seguras
    - Camada intermediária: responsável pela gestão das chaves geradas
    - Camada de comunicação: estabelece a comunicação segura para troca de arquivos, usando a criptografia quântica

- Algoritmos quânticos
  - Um algoritmo quântico é a sequência de operações (portas lógicas) que faz o computador quântico executar uma tarefa desejada
  - Algoritmo de Grover: busca em uma base de dados de forma mais rápida que qualquer algoritmo de busca clássico, usando estados emaranhados
    - Eficácia comprovada matematicamente, mas limitada na prática pela decoerência dos qubits
  - Paralelismo quântico: maior vantagem dos computadores quânticos sobre os clássicos, pois qubits em superposição permitem realizar uma operação sobre todos os estados possíveis simultaneamente

- Vantagem de memória (aprofundamento)
  - Em um computador clássico, armazenar M números diferentes requer uma quantidade de bits proporcional (linear) a M
  - Em um computador quântico, o número de qubits necessários para representar os mesmos estados cresce de forma logarítmica em relação à quantidade de números desejada
  - Na prática, porém, o maior supercomputador clássico atual só consegue simular um computador quântico de até aproximadamente 46 qubits, pois cada qubit adicional dobra a memória clássica necessária para simulá-lo

- Limite fundamental do paralelismo quântico
  - Medir a saída de um computador quântico colapsa a superposição de estados para um único resultado
  - Não é possível extrair todos os resultados calculados em paralelo de uma só vez (analogia do "caderno secreto": a natureza mostra apenas uma página por vez e destrói o restante)
  - Por isso, os computadores quânticos têm utilidade prática apenas para certos tipos de problemas, não para qualquer cálculo em geral

- Algoritmo de Deutsch-Jozsa
  - Problema: dada uma "caixa preta" (função) que recebe uma entrada e produz uma saída, determinar se essa função é constante ou balanceada
  - Um computador clássico precisaria testar múltiplas entradas para responder com certeza, um processo exponencialmente mais lento
  - O algoritmo de Deutsch-Jozsa resolve o problema com uma única medição, mostrando se o resultado (|0⟩ ou |1⟩) indica função constante ou balanceada, para funções de qualquer número de entradas
  - Não tem aplicação comercial direta, mas ilustra conceitos usados em algoritmos quânticos mais complexos, como o algoritmo de fatoração de Shor

- Como um algoritmo quântico é escrito, na prática
  - Os qubits passam por uma série de portas lógicas quânticas até gerar os qubits de saída
  - Como todos os valores possíveis de entrada existem simultaneamente em superposição, medir a saída faz o sistema colapsar para um único valor aleatório, sem controle direto sobre qual entrada esse valor representa
  - Estratégia de projeto: manipular (rotacionar) o vetor de estado do sistema para que a resposta correta seja a mais provável de ser observada na medição
  - Execução repetida: como cada execução dá um resultado, os computadores quânticos reais rodam o mesmo algoritmo muitas vezes e constroem um histograma dos resultados (ex.: o IBMQ executa o algoritmo 1024 vezes) para identificar a resposta mais frequente, que é a resposta correta
  - O emaranhamento é essencial nesse processo: qubits emaranhados formam um único vetor de estado, o que permite correlacionar entradas e saídas ao longo do algoritmo

- Referências para ampliar a pesquisa
  - Falbriard, Claude; Brosso, Ines. "Computação Quântica". Rio de Janeiro: Alta Books, 2020
  - Mahon, José Roberto P. "Mecânica Quântica - Desenvolvimento Contemporâneo com Aplicações". Grupo GEN, 2011
  - Nussenzveig, Herch M. "Curso de Física Básica". São Paulo: Editora Blucher, 2014
  - "Deutsch–Jozsa algorithm" (en.wikipedia.org)
  - Artigo sobre o algoritmo de Grover (sol.sbc.org.br)
