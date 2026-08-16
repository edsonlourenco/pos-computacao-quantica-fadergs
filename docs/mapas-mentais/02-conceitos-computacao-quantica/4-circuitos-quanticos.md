# Circuitos Quânticos

- Introdução
  - Circuito quântico: modelo mais usado para descrever e programar algoritmos quânticos
  - Analogia com circuitos clássicos: qubits substituem bits, portas quânticas substituem portas lógicas
  - Diferença central: portas quânticas são operações unitárias reversíveis, portas clássicas (AND, OR) geralmente não são

- Objetivos da unidade
  - Compreender a estrutura e a leitura de um circuito quântico
  - Conhecer as principais portas quânticas de um e múltiplos qubits
  - Entender como circuitos criam superposição e emaranhamento
  - Relacionar propriedades matemáticas (unitariedade, reversibilidade) com o comportamento físico do circuito
  - Conhecer ferramentas usadas para simular e executar circuitos quânticos

- Estrutura de um circuito quântico
  - Representação gráfica
    - Cada linha horizontal representa um qubit (ou um registrador quântico)
    - Caixas sobre as linhas representam portas quânticas aplicadas ao(s) qubit(s)
    - O tempo flui da esquerda para a direita
    - Símbolo de medidor no final da linha representa a medição do qubit
  - Registrador quântico
    - Conjunto de qubits tratado como uma unidade
    - Estado inicial padrão: todos os qubits em |0⟩
  - Qubits ancilla
    - Qubits auxiliares usados para cálculos intermediários ou correção de erros
    - Geralmente não fazem parte do resultado final do algoritmo

- Portas quânticas de um qubit
  - Porta Pauli-X
    - Equivalente quântico da porta NOT clássica
    - Inverte |0⟩ em |1⟩ e |1⟩ em |0⟩
  - Porta Pauli-Y e Pauli-Z
    - Rotações de 180° em torno dos eixos Y e Z da esfera de Bloch
    - Pauli-Z inverte a fase do estado |1⟩, mantendo |0⟩ inalterado
  - Porta Hadamard (H)
    - Cria superposição a partir de um estado definido
    - Aplicada a |0⟩, produz uma superposição igual de |0⟩ e |1⟩ (50%/50% de chance na medição)
    - Peça fundamental na maioria dos algoritmos quânticos
  - Porta de fase (S) e porta T
    - Aplicam uma rotação de fase ao estado |1⟩, sem alterar as probabilidades de medição isoladas
    - Fundamentais para alcançar um conjunto universal de portas junto com H e CNOT
  - Portas de rotação (Rx, Ry, Rz)
    - Rotacionam o estado do qubit por um ângulo arbitrário em torno de um dos eixos da esfera de Bloch
    - Permitem preparar qualquer estado de superposição possível para um único qubit

- Portas quânticas de múltiplos qubits
  - CNOT (Controlled-NOT)
    - Porta de dois qubits: um qubit de controle e um qubit alvo
    - Se o qubit de controle estiver em |1⟩, aplica um X (inversão) no qubit alvo; caso contrário, não faz nada
    - Peça central para criar emaranhamento entre qubits
  - CZ (Controlled-Z)
    - Aplica uma inversão de fase no qubit alvo apenas quando o qubit de controle está em |1⟩
  - SWAP
    - Troca o estado entre dois qubits
  - Toffoli (CCNOT)
    - Porta de três qubits: dois qubits de controle e um qubit alvo
    - Inverte o qubit alvo apenas quando ambos os qubits de controle estão em |1⟩
    - Reversível e capaz de implementar qualquer função lógica clássica (AND, OR, NOT) dentro do modelo quântico

- Propriedades fundamentais dos circuitos quânticos
  - Unitariedade
    - Toda porta quântica é descrita por uma matriz unitária
    - Preserva a norma do vetor de estado (a soma das probabilidades continua sendo 1)
  - Reversibilidade
    - Toda porta quântica tem uma porta inversa que desfaz sua operação
    - Diferente de portas clássicas irreversíveis, que podem perder informação (ex.: AND apaga informação sobre as entradas)
  - Conjunto universal de portas
    - Um pequeno conjunto de portas (ex.: Hadamard, porta T e CNOT) é suficiente para aproximar qualquer operação unitária possível
    - Permite construir qualquer algoritmo quântico combinando apenas essas portas básicas
  - Não-clonagem
    - Não existe uma porta quântica capaz de copiar um estado desconhecido e arbitrário de um qubit
    - Consequência direta do teorema da não clonagem, herdado da mecânica quântica

- Criação de emaranhamento em um circuito
  - Par de Bell (exemplo clássico de circuito)
    - Aplicar uma porta Hadamard no primeiro qubit, colocando-o em superposição
    - Aplicar uma porta CNOT usando o primeiro qubit como controle e o segundo como alvo
    - Resultado: os dois qubits ficam emaranhados, e medir um deles determina instantaneamente o resultado do outro
  - Generalização: circuitos com várias portas Hadamard e CNOT podem gerar estados de Greenberger-Horne-Zeilinger (GHZ), emaranhando múltiplos qubits simultaneamente

- Medição em circuitos quânticos
  - A medição é a única operação não reversível de um circuito quântico
  - Colapsa a superposição do qubit medido para um dos estados possíveis (0 ou 1), com probabilidade dada pela amplitude do estado
  - A base de medição pode ser escolhida (ex.: base computacional Z, ou bases X e Y), alterando o resultado possível da medição
  - Geralmente realizada ao final do circuito, mas medições intermediárias também são usadas em técnicas de correção de erros

- Complexidade de um circuito quântico
  - Profundidade (depth): número de "camadas" de portas em sequência, relacionado ao tempo de execução
  - Largura (width): número de qubits usados no circuito
  - Contagem de portas: número total de portas aplicadas, relevante para estimar ruído acumulado
  - Circuitos mais profundos acumulam mais erro devido à decoerência, um fator crítico em hardware atual (era NISQ)

- Ferramentas para construir e simular circuitos
  - Qiskit (IBM): framework em Python para criar, simular e executar circuitos em hardware real da IBM
  - Cirq (Google): framework em Python voltado a circuitos NISQ
  - Q# (Microsoft): linguagem de programação quântica dedicada, integrada ao Azure Quantum
  - Simuladores locais permitem testar circuitos pequenos em computadores clássicos antes de rodar em hardware quântico real

- Siglas e termos explicados
  - CNOT: Controlled-NOT (porta NOT controlada)
  - CZ: Controlled-Z (porta Z controlada)
  - CCNOT / Toffoli: Controlled-Controlled-NOT
  - GHZ: estado de Greenberger-Horne-Zeilinger, um estado emaranhado de três ou mais qubits
  - NISQ: Noisy Intermediate-Scale Quantum, era atual de computadores quânticos com poucos qubits e ruído significativo

- Referências para ampliar a pesquisa
  - Nielsen, M. & Chuang, I. "Quantum Computation and Quantum Information"
  - IBM Quantum, documentação do Qiskit: https://docs.quantum.ibm.com
  - Google Quantum AI, documentação do Cirq: https://quantumai.google/cirq
  - Microsoft, documentação do Q# e Azure Quantum: https://learn.microsoft.com/azure/quantum
