# História da Computação Quântica

- Introdução
  - Computação quântica é uma das grandes tecnologias do século 21
  - Ainda não está completamente desenvolvida, mas já tem resultados promissores
  - Grandes empresas investem quantias significativas em projetos de desenvolvimento e parcerias
  - História curta: começa aproximadamente em 1994 e se desdobra até os dias de hoje
  - A supremacia quântica é o ponto culminante desse desenvolvimento

- Objetivos da unidade
  - Ter uma visão histórica do desenvolvimento da computação quântica
  - Entender e avaliar os diferentes caminhos trilhados pelo desenvolvimento dessa área

- Origens teóricas (1979-1985)
  - 1979: Paul Benioff submete um trabalho demonstrando as bases físicas para o computador quântico
  - 1981: Richard Feynman dá a palestra "Simulating Physics with Computers"
    - Defende que um sistema clássico nunca poderia representar adequadamente um sistema quântico
    - Define um conjunto de funcionalidades que um computador quântico deveria possuir para ser funcional
    - Na época, ninguém acreditava ser capaz de construir uma máquina desse tipo
  - 1982: Feynman propõe formalmente um computador quântico capaz de tirar vantagem dos princípios atômicos de superposição, interferência e emaranhamento
  - 1985: David Deutsch, físico de Oxford, descreve em detalhe como um computador quântico funcionaria
    - Antecipa que um dia seria possível construir computadores quânticos
    - Desenvolve um algoritmo que seria executado mais rapidamente em um computador quântico
    - Generaliza esse algoritmo posteriormente com Richard Jozsa (algoritmo de Deutsch-Jozsa)

- Primeiros algoritmos quânticos (1993-1994)
  - Ordem do algoritmo: notação usada para avaliar a eficiência de um algoritmo (quantos passos são necessários para executá-lo)
  - 1993: Bernstein e Vaziran (BV) publicam um trabalho descrevendo um algoritmo quântico
    - Mostra separação entre execução quântica e clássica mesmo quando pequenos erros são permitidos
    - Demonstra vantagem quântica não determinística
    - Descreve uma versão quântica da transformada de Fourier, usada mais tarde por Peter Shor
  - Algoritmo de Jozsa demonstra uma vantagem quântica determinística
  - 1994: Seth Lloyd publica um trabalho descrevendo um método prático para construir uma computação quântica
    - Propõe um dispositivo capaz de processar informação usando apenas fenômenos quânticos
    - Os bits podem ser colocados em superposição de estados 0 e 1 por meio de pulsos e frequências de ressonância adequadas
    - Considerada a primeira abordagem prática de um computador quântico

- O algoritmo de Shor e a criptografia (1994-2001)
  - 1994: Peter Shor, pesquisador na Bell Labs, elabora um algoritmo para fatorar grandes números em dois fatores primos
    - A fatoração de grandes números é um problema intratável em um computador clássico
    - É a base da criptografia de chave pública (algoritmo RSA), usada em segurança bancária e comunicações na internet
    - Shor resolve um problema equivalente à fatoração usando o algoritmo da transformada de Fourier quântica
  - 2001: Isaac Chuang realiza a primeira implementação do algoritmo de Shor
    - Usa um sistema de ressonância magnética nuclear para fatorar o número 15 como demonstração

- O algoritmo de busca de Grover
  - Lov Grover demonstra o uso de computadores quânticos em um algoritmo de busca
  - Um problema de busca não estruturada leva N passos em um computador clássico
  - O mesmo objetivo pode ser alcançado em aproximadamente √N passos em um computador quântico (ganho quadrático)

- Implementações físicas pioneiras (1995-2001)
  - 1995: Cirac e Zoller propõem uma armadilha de íons que usa lasers para ionizar átomos presos em potenciais elétricos
  - 2001: Yasunobu Nakamura constrói e demonstra a funcionalidade de um qubit supercondutor controlável
    - Usa junções de Josephson para criar um sistema de dois níveis manipulável entre os dois estados

- Critérios de DiVincenzo
  - David DiVincenzo formaliza os critérios que um sistema físico precisa cumprir para ser um computador quântico
  - 1. Sistema físico escalável, com qubits distintos entre si e possibilidade de contar exatamente quantos qubits existem no sistema
  - 2. Capacidade de inicializar o estado de qualquer qubit para um estado definido na base computacional
  - 3. Os qubits devem manter seu estado por tempo suficiente (isolamento do ambiente), evitando perda de coerência que descontrola o processamento
  - 4. O sistema deve ser capaz de aplicar uma sequência de operações unitárias aos estados dos qubits, incluindo operações unitárias em pares de qubits
  - 5. O sistema deve ser capaz de realizar uma medição forte: uma técnica que mede o estado do qubit para a propriedade escolhida sem alterar esse estado

- Hardware, transistores e o limite da miniaturização
  - Computadores quânticos são, em certo sentido, similares aos computadores clássicos dos anos 1950, com algoritmos implementados diretamente no hardware
  - A velocidade de processamento de um computador clássico depende do número de transistores na CPU
  - Lei de Moore (Gordon Moore, cofundador da Intel): o poder de processamento dobraria a cada dois anos
    - A previsão funcionou bem entre 1965 e 2013 (capacidade dobrando a cada 18 meses)
    - Após 2013, o processo passou a sofrer desaceleração
  - Reduzir o transistor até o tamanho de um átomo levou a problemas de tunelamento quântico (o transistor passa a conduzir elétrons mesmo desligado)
  - O conceito de computação quântica surge, em parte, como forma de lidar com esse limite físico da miniaturização clássica

- Supremacia quântica
  - Termo criado por John Preskill para descrever o ponto em que um computador quântico resolve problemas que um computador clássico não consegue resolver
  - Exige prova de um ganho de velocidade super-polinomial em relação às melhores máquinas clássicas disponíveis

- Linha do tempo da supremacia quântica
  - 1982 - Richard Feynman: propõe um computador quântico capaz de tirar vantagem dos princípios atômicos de superposição, interferência e emaranhamento
  - 1994 - Peter Shor: cria o algoritmo de fatoração quântica; não é implementado nem demonstrado experimentalmente na época, mas gera grande expectativa sobre o potencial dos algoritmos quânticos
  - 2012 - John Preskill: cunha formalmente o termo "supremacia quântica"
  - 2016 - Google: decide encarar o desafio da supremacia quântica e constrói um chip de 9 qubits capaz de gerar distribuições amostrais inacessíveis a qualquer computador clássico em tempo razoável
  - 2017 - Pesquisadores da IBM simulam circuitos de 49 e 56 qubits em um supercomputador clássico (Blue Gene/Q)
    - Aumenta o número de qubits necessário para se alegar supremacia quântica
    - O ceticismo cresce, pois as estimativas de erro dos computadores quânticos chegam a 3% da entrada em cada ciclo
    - O maior desafio passa a ser a correção de erros causados pela perda de coerência dos qubits

- O caso Sycamore (Google, 2019)
  - Sycamore, processador quântico de 53 qubits criado pela Google, completa uma tarefa em 200 segundos
  - A empresa alega que a mesma tarefa levaria 10.000 anos em supercomputadores clássicos, reivindicando a supremacia quântica
  - A Google usa o supercomputador Summit (o mais rápido do mundo à época) para estimar o tempo clássico equivalente
  - A IBM contra-argumenta, afirmando que a tarefa levaria apenas 2,5 dias em um computador clássico como o Summit
  - O maior desafio do sistema da Google é manter os 54 qubits estáveis
    - Temperatura ambiente e vibrações sujeitam o sistema a erros
    - O processador é mantido a 15 mili-Kelvins, cerca de 200 vezes menor que a temperatura ambiente

- Outras abordagens e o caso D-Wave
  - A empresa canadense D-Wave Systems vende computadores quânticos de até 2.000 qubits
  - Utilizam annealing quântico, uma abordagem controversa e capaz de resolver apenas tipos específicos de problemas de otimização
  - A D-Wave não detém a supremacia quântica: seus resultados são discutíveis porque aplicam princípios de processamento quântico a casos bem específicos, não a um computador quântico universal

- Modelos e arquiteturas de computação quântica
  - Modelos teóricos principais: Máquina de Turing Quântica, computação quântica adiabática, circuitos quânticos
  - Muitos computadores quânticos atuais se baseiam no modelo de máquina de Turing e usam loops supercondutores compostos por micro-ondas, capacitores e indutores
  - A corrente elétrica flui nesses loops supercondutores de forma mais rápida do que em circuitos semicondutores clássicos
  - Abordagens físicas distintas convivem no mercado
    - Íons presos (ion trap), explorados pela empresa IonQ, onde o elétron do átomo é usado para transferir dados
    - Pontos quânticos (quantum dots) feitos de silício, desenvolvidos pela Intel
  - Linguagens e plataformas de programação quântica: Ocean (D-Wave), Q# (Microsoft), Cirq (Google), Qiskit (IBM)
  - Um circuito quântico é projetado usando qubits (dados), operações (portas quânticas) e resultados associados (medição)

- Aplicações e investimentos do mercado
  - Empresas que investem fortemente em pesquisa: Google, IBM, Amazon, DARPA, Honeywell, entre outras
  - Aplicações em vários campos: predição, inteligência artificial e segurança digital
  - Exemplo de aplicação recente: parceria entre Mercedes-Benz e IBM para desenvolver baterias de íons de lítio em estado sólido usando computação quântica, visando veículos com emissão zero de carbono

- Siglas e termos explicados
  - BV: algoritmo de Bernstein-Vazirani
  - RSA: algoritmo de criptografia de chave pública baseado na dificuldade de fatorar números grandes
  - NMR: ressonância magnética nuclear (Nuclear Magnetic Resonance), técnica usada na primeira implementação do algoritmo de Shor

- Referências para ampliar a pesquisa
  - Nussenzveig, H. M. "Curso de Física Básica", Editora Blucher
  - Falbriard, C.; Brosso, I. "Computação Quântica", Editora Alta Books
  - Nielsen, M. & Chuang, I. "Quantum Computation and Quantum Information" (contexto histórico dos principais algoritmos)
