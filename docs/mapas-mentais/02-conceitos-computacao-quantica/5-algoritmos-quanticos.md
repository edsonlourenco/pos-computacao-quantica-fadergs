# Algoritmos Quânticos

- Introdução
  - Algoritmos quânticos exploram superposição, interferência e emaranhamento para resolver certos problemas mais rapidamente que algoritmos clássicos
  - Nem todo problema se beneficia da computação quântica; a vantagem quântica é específica de certas classes de problemas
  - O ganho de desempenho é medido comparando a ordem de complexidade do melhor algoritmo clássico com a do algoritmo quântico equivalente

- Objetivos da unidade
  - Compreender os princípios que dão vantagem computacional aos algoritmos quânticos
  - Conhecer os algoritmos quânticos mais relevantes historicamente e seus objetivos
  - Entender a diferença entre ganho exponencial e ganho quadrático
  - Conhecer algoritmos híbridos usados na era atual de hardware limitado (NISQ)

- Paralelismo quântico e interferência
  - Paralelismo quântico
    - Uma superposição de N qubits permite avaliar uma função sobre 2^N entradas simultaneamente em uma única execução
    - A dificuldade está em extrair essa informação, já que a medição retorna apenas um resultado
  - Interferência quântica
    - Amplitudes de probabilidade podem se somar (interferência construtiva) ou se cancelar (interferência destrutiva)
    - Algoritmos quânticos são projetados para amplificar a amplitude da resposta correta e cancelar as respostas erradas antes da medição

- Algoritmo de Deutsch e Deutsch-Jozsa
  - Problema de Deutsch: determinar se uma função de um bit é constante ou balanceada
  - Um algoritmo clássico precisa avaliar a função duas vezes na pior hipótese; o algoritmo quântico resolve com uma única avaliação
  - Generalização de Deutsch-Jozsa (Deutsch e Richard Jozsa)
    - Estende o problema para funções de N bits
    - Um algoritmo clássico determinístico pode precisar de até 2^(N-1) + 1 avaliações; o algoritmo quântico resolve com uma única avaliação
    - Um dos primeiros exemplos de vantagem exponencial garantida da computação quântica

- Algoritmo de Bernstein-Vazirani
  - Objetivo: descobrir uma string binária escondida usada em uma função linear
  - Um algoritmo clássico precisa de N consultas (uma por bit) para descobrir a string
  - O algoritmo quântico descobre a string com uma única consulta à função, usando superposição e a transformada de Hadamard

- Algoritmo de Simon
  - Objetivo: encontrar um período escondido em uma função que mapeia 2 entradas distintas para a mesma saída
  - Demonstra separação exponencial entre computação clássica e quântica
  - Historicamente importante por inspirar diretamente a estrutura do algoritmo de Shor

- Transformada Quântica de Fourier (QFT)
  - Versão quântica da transformada discreta de Fourier, implementada com portas Hadamard e portas de fase controladas
  - Permite extrair periodicidades escondidas em uma superposição de estados
  - Componente central de vários algoritmos quânticos importantes, especialmente o algoritmo de Shor

- Algoritmo de Shor
  - Objetivo: fatorar um número inteiro grande em seus fatores primos
  - Reduz o problema de fatoração a um problema de busca de período, resolvido eficientemente usando a QFT
  - Um algoritmo clássico conhecido leva tempo sub-exponencial (mas ainda impraticável para números muito grandes); o algoritmo de Shor resolve em tempo polinomial
  - Ameaça direta à criptografia de chave pública (RSA), que depende da dificuldade de fatorar números grandes
  - Motivou o desenvolvimento da criptografia pós-quântica, resistente a computadores quânticos

- Algoritmo de Grover
  - Objetivo: buscar um item específico em uma lista não estruturada de N itens
  - Um algoritmo clássico precisa, em média, de N/2 consultas; o algoritmo de Grover encontra o item em aproximadamente √N consultas
  - Ganho quadrático (não exponencial), mas aplicável a uma classe muito ampla de problemas de busca e otimização
  - Funciona por meio de "amplificação de amplitude": inverte a fase do estado alvo e reflete em torno da média, aumentando gradualmente sua probabilidade de medição

- Algoritmos variacionais (era NISQ)
  - Motivação: hardware quântico atual tem poucos qubits e alta taxa de erro, tornando algoritmos como Shor impraticáveis em escala útil
  - Abordagem híbrida: um circuito quântico parametrizado é executado repetidamente, e um otimizador clássico ajusta os parâmetros com base no resultado
  - VQE (Variational Quantum Eigensolver)
    - Estima o menor autovalor de energia de um sistema (ex.: energia do estado fundamental de uma molécula)
    - Aplicação principal: simulação de química quântica e ciência de materiais
  - QAOA (Quantum Approximate Optimization Algorithm)
    - Busca soluções aproximadas para problemas de otimização combinatória
    - Alterna entre operadores que codificam o problema e operadores que exploram o espaço de soluções

- Computação quântica adiabática e annealing quântico
  - Baseia-se no teorema adiabático: um sistema quântico que evolui lentamente o suficiente permanece em seu estado de menor energia
  - Annealing quântico (usado por empresas como D-Wave) é uma implementação especializada, focada em problemas de otimização
  - Não é um modelo de computação quântica universal; resolve apenas classes específicas de problemas

- Classes de complexidade quântica
  - BQP (Bounded-error Quantum Polynomial time): classe de problemas resolvidos eficientemente por um computador quântico com erro limitado
  - Relação com classes clássicas: acredita-se que BQP seja maior que P, mas não se sabe se resolve problemas NP-completos em tempo polinomial
  - Grover e Shor são exemplos de algoritmos que colocam seus respectivos problemas dentro de BQP com vantagem sobre os melhores algoritmos clássicos conhecidos

- Aplicações e limitações práticas
  - Aplicações promissoras: simulação de moléculas e materiais, otimização combinatória, criptografia e quebra de criptografia, aprendizado de máquina quântico
  - Limitações atuais: poucos qubits estáveis, alta taxa de erro, necessidade de correção de erros com grande sobrecarga de qubits físicos
  - A maioria das vantagens comprovadas hoje é teórica ou demonstrada apenas em problemas pequenos; a vantagem prática em larga escala ainda depende de avanços de hardware

- Siglas e termos explicados
  - QFT: Quantum Fourier Transform (Transformada Quântica de Fourier)
  - VQE: Variational Quantum Eigensolver
  - QAOA: Quantum Approximate Optimization Algorithm
  - NISQ: Noisy Intermediate-Scale Quantum
  - BQP: Bounded-error Quantum Polynomial time
  - RSA: algoritmo de criptografia de chave pública baseado na dificuldade de fatoração

- Referências para ampliar a pesquisa
  - Nielsen, M. & Chuang, I. "Quantum Computation and Quantum Information"
  - Shor, P. "Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer" (1997)
  - Grover, L. "A fast quantum mechanical algorithm for database search" (1996)
  - IBM Quantum Learning: https://learning.quantum.ibm.com
