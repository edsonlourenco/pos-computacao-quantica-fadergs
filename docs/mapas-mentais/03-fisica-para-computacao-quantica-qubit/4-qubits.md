# Qubits

- Objetivos da unidade
  - Compreender o conceito de qubit
  - Analisar a aplicação desse conceito em portas lógicas quânticas
  - Entender os princípios de funcionamento de um algoritmo quântico

- Do bit clássico ao qubit físico
  - Um computador clássico precisa de um conjunto de cerca de 10.000 elétrons para formar um único bit binário confiável
    - As propriedades quânticas de cada elétron individual se perdem em uma média estatística, e o conjunto se comporta como um bit clássico
  - Um computador quântico usa um único objeto quântico (um elétron isolado, um fóton) para criar um qubit, preservando suas propriedades quânticas
  - Na prática, o qubit é um sistema quântico de dois níveis, como o spin de um elétron ou a polarização de um fóton
    - Convenção: |↑⟩ associado ao número binário 0, |↓⟩ associado ao número binário 1

- Vantagens da computação quântica
  - Primeira vantagem: ganho de memória
    - Um registrador clássico de N bits armazena um único número binário de N dígitos por vez
    - Um registrador de N qubits, pelo princípio da superposição, armazena os números binários simultaneamente
    - Exemplo: 32 qubits podem armazenar mais informação que os 16 bilhões de bits clássicos de 2 GB de memória
  - Segunda vantagem: ganho de velocidade computacional
    - Um computador clássico executa cálculos sequencialmente, passo a passo
    - Um computador quântico usa superposição para somar e processar múltiplos resultados ao mesmo tempo (computação massivamente paralela)
    - O resultado, porém, só pode ser lido por meio de uma medição, que colapsa a superposição para um único valor aleatório
  - O emaranhamento resolve o problema da leitura: adiciona uma "identificação" que correlaciona entrada e saída de cada passo do cálculo, permitindo saber a qual etapa pertence o resultado obtido

- Portas lógicas quânticas
  - Estrutura física que recebe um conjunto de qubits de entrada e os combina em uma saída
  - Diferença fundamental em relação às portas lógicas clássicas: reversibilidade
    - Preservam superposição e emaranhamento, de forma que a entrada pode ser reconstruída a partir da saída
    - Não perdem informação ao longo da computação
  - Principais portas lógicas quânticas: porta Hadamard (cria estados de superposição usando laser ou pulsos de micro-ondas), porta controlled-NOT (CNOT) e porta Toffoli

- Esfera de Bloch
  - Representação visual do estado de um único qubit
  - Polo superior representa |0⟩, polo inferior representa |1⟩
  - Uma flecha a partir do centro indica o estado atual do qubit; no equador, o qubit tem 50% de chance de colapsar em |0⟩ e 50% em |1⟩
  - Mudanças de estado correspondem a rotações da flecha na esfera
  - Representa apenas um único qubit; não pode ser usada para sistemas de dois ou mais qubits

- Computação massivamente paralela
  - Um registrador de 300 qubits poderia, em princípio, armazenar e combinar mais estados do que o número estimado de partículas no Universo

- Decoerência
  - Processo pelo qual a informação armazenada nos qubits se degrada em ruído aleatório, devido à interação com o ambiente
  - Principal desafio prático da computação quântica
  - Não é possível corrigir erros copiando qubits como se faz com bits clássicos, por causa do teorema da não clonagem (medir um estado desconhecido para copiá-lo destrói a superposição)
  - Dois mecanismos principais de decoerência
    1. Spin-flip: mudança aleatória do estado de spin de um qubit; o "tempo de coerência" mede quanto tempo um qubit sobrevive antes de sofrer esse efeito (tipicamente microssegundos)
    2. Princípio da incerteza de Heisenberg: a troca de energia com o ambiente (flutuação quântica) distorce os estados dos qubits
  - Estratégias de mitigação
    - Refrigeradores de diluição: mantêm o processador próximo do zero absoluto, reduzindo a decoerência
    - Computação quântica tolerante a falhas: agrupa vários qubits físicos frágeis em um único qubit lógico mais estável (mínimo teórico de 5 qubits físicos por qubit lógico com correção de erro)

- Tipos de qubits (implementações físicas)
  - Armadilha de íons
    - Confina uma cadeia de átomos carregados isolados em um tubo a vácuo, usando um campo magnético de rádio frequência gerado por hastes cilíndricas
    - |0⟩ é o estado fundamental (energia mais baixa) do íon; |1⟩ é obtido excitando o íon com um feixe de laser intenso
    - Operações de múltiplos qubits (superposição, emaranhamento) usam os "modos normais de quantização": oscilações mecânicas coletivas dos íons, acoplados por repulsão elétrica
    - Maiores tempos de coerência já medidos entre as diferentes implementações
    - Armadilhas de Penning combinam campo magnético e elétrico para melhorar ainda mais o tempo de coerência
  - Qubits de spin de elétrons
    - Ligados ao desenvolvimento da tecnologia de semicondutores, especialmente o silício
    - Modelo de Kane (Bruce Kane, 1998): rede de átomos de fósforo (impureza do silício) imersos em substrato de silício puro; o qubit é codificado no spin nuclear do fósforo
    - Pontos quânticos (quantum dots), propostos por David Loss e David DiVincenzo: confinam elétrons isolados em substratos de silício usando uma rede de eletrodos metálicos, controlando seu movimento por diferença de potencial
  - Qubits supercondutores
    - Implementação mais usada atualmente nos principais computadores quânticos
    - Baseados na supercondutividade, descoberta em 1911 por Heike Kamerligh Onnes (resistência elétrica desaparece abaixo de uma temperatura crítica)
    - Explicados pela teoria BCS (Bardeen, Cooper, Schrieffer): pares de elétrons (pares de Cooper) se movem pela rede cristalina sem perda de energia
    - Arquitetura-chave: junção de Josephson, dois supercondutores separados por uma barreira isolante fina, permitindo efeito túnel de pares de Cooper
    - Três tipos principais de qubits supercondutores: qubit de carga (presença/ausência de um par de Cooper), qubit de fluxo ou de corrente persistente (corrente circulando em sentido horário ou anti-horário em um anel supercondutor), e o SQUID (dispositivo supercondutor de interferência quântica, que mede a direção do fluxo)

- Referências para ampliar a pesquisa
  - Mahon, José Roberto P. "Mecânica Quântica - Desenvolvimento Contemporâneo com Aplicações". Grupo GEN, 2011
  - Artigo sobre armadilhas de íons na computação quântica (arxiv.org/abs/1904.04178)
  - "Kane quantum computer" (en.wikipedia.org)
  - "Superconducting quantum computing" (en.wikipedia.org)
