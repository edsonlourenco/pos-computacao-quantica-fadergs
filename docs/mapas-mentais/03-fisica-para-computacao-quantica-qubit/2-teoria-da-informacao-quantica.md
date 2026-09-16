# Teoria da Informação Quântica

- Introdução
  - A computação quântica também é uma teoria da informação: estuda como codificar, transmitir e proteger informação usando as leis da mecânica quântica
  - Motivação central: troca segura de informação, com a criptografia quântica como uma das aplicações mais relevantes

- Objetivos da unidade
  - Compreender a diferença entre bit clássico e qubit do ponto de vista da informação
  - Conhecer os fundamentos da teoria da informação clássica de Shannon
  - Entender o conceito de entropia da informação e sua versão quântica (Von Neumann)
  - Situar historicamente a evolução da computação quântica até a "supremacia quântica"

- Bit clássico x qubit
  - Bit clássico: assume apenas um dos dois valores possíveis, 0 ou 1
  - Qubit: descrito por uma base computacional |0⟩ e |1⟩
    - Pode existir em superposição: a|0⟩ + b|1⟩, com a e b amplitudes de probabilidade (números complexos)
    - Normalização: |a|² + |b|² = 1
  - Diferença entre informação de especificação (toda a informação necessária para descrever o estado) e informação acessível (o que de fato se consegue extrair por medição)

- Claude Shannon e a teoria clássica da informação
  - Considerado o "pai da teoria da informação"
  - Elementos elementares de um sistema de comunicação: Fonte, Transmissor, Canal, Receptor, Destinatário
  - Teorema 1 (codificação sem ruído / compressão sem perdas)
    - A taxa de codificação não pode ser menor que a entropia da fonte sem que haja perda de informação
    - Relevante para a computação quântica pela necessidade de correção de erros
  - Teorema 2 (teorema do canal com ruído)
    - Mesmo na presença de ruído, existe uma taxa máxima de transmissão de informação praticamente livre de erros
    - Base conceitual para os códigos de correção de erros quânticos

- Entropia da informação
  - Mede a quantidade de informação (em bits) necessária para descrever um sistema, ou seja, o grau de incerteza associado a ele
  - Não deve ser confundida com a entropia termodinâmica, apesar do nome e da origem histórica comum
  - Entropia de Shannon (símbolo H): medida da entropia da informação de uma fonte clássica, em bits
  - Ao enviar múltiplas mensagens simultaneamente (como na computação quântica), a entropia conjunta de mensagens independentes relaciona-se com o produto das entropias individuais e a entropia condicional entre elas

- Teorema da não clonagem (no-cloning theorem)
  - Não é possível copiar um qubit em um estado quântico desconhecido, ao contrário do que ocorre com bits clássicos
  - Consequência direta dos postulados da mecânica quântica e uma das razões pelas quais a correção de erros quânticos é mais difícil que a clássica

- Entropia de Von Neumann
  - Versão quântica da entropia de Shannon
  - Calculada a partir da matriz densidade ρ do sistema e do operador traço (tr)
  - Usada para quantificar a entropia de estados emaranhados e a entropia condicional relativa entre sistemas quânticos

- Linha do tempo da "supremacia quântica"
  - 1982: Richard Feynman propõe o uso de sistemas quânticos (explorando superposição, interferência e emaranhamento) para simular a própria natureza
  - 1994: Peter Shor cria o algoritmo quântico de fatoração de números inteiros
  - 2012: John Preskill cunha o termo "supremacia quântica"
  - 2016/2017: Google constrói um chip quântico de 9 qubits
  - 2017: IBM simula circuitos de 49/56 qubits em um supercomputador clássico
  - D-Wave comercializa computadores de anelamento quântico com cerca de 2000 qubits, voltados a problemas específicos de otimização

- Ceticismo em torno da supremacia quântica
  - Taxas de erro da ordem de 3% por ciclo de computação
  - Dificuldade prática de implementar correção de erros em larga escala devido à decoerência dos qubits

- Referências para ampliar a pesquisa
  - Cardonha, C.; Villela, A.; Tadeu, H. "Desmistificando a Computação Quântica". Dom, n. 37, 2019
  - Falbriard, Claude; Brosso, Ines. "Computação Quântica". Rio de Janeiro: Alta Books, 2020
  - Mahon, José Roberto P. "Mecânica Quântica - Desenvolvimento Contemporâneo com Aplicações". Grupo GEN, 2011
  - Rabelo, W. R. M.; Costa, M. L. M. "Uma abordagem pedagógica no ensino da computação quântica com um processador quântico de 5-qbits". Caderno Brasileiro de Ensino de Física, v. 40, n. 4, 2018
