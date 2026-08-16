# Fundamentos da Mecânica Quântica

- Introdução
  - Mecânica quântica: teoria física que descreve o comportamento da matéria e da energia em escalas atômica e subatômica
  - A física clássica (Newton, Maxwell) falha ao descrever fenômenos em escala muito pequena
  - Base teórica necessária para entender qubits, superposição, emaranhamento e algoritmos quânticos

- Objetivos da unidade
  - Compreender os experimentos que motivaram a criação da mecânica quântica
  - Entender os postulados fundamentais da mecânica quântica
  - Conhecer a notação de Dirac (bra-ket) usada em computação quântica
  - Compreender superposição, medição, incerteza e emaranhamento em nível de física
  - Relacionar os conceitos físicos com a futura definição de qubit

- Da física clássica à física quântica
  - Radiação de corpo negro
    - Problema: física clássica previa emissão de energia infinita em altas frequências (catástrofe do ultravioleta)
    - Solução de Max Planck (1900): energia é emitida em pacotes discretos, os quanta
    - Quantum de energia: E = h·f (h = constante de Planck, f = frequência)
  - Efeito fotoelétrico
    - Luz incidindo sobre um metal ejeta elétrons
    - Física clássica não explica por que a energia dos elétrons depende da frequência da luz, não da intensidade
    - Einstein (1905): luz se comporta como pacotes de energia (fótons), cada um com energia E = h·f
    - Comprovou a natureza quantizada e corpuscular da luz
  - Modelo atômico de Bohr
    - Elétrons orbitam o núcleo apenas em níveis de energia discretos (quantizados)
    - Emissão/absorção de luz ocorre quando o elétron salta entre níveis
    - Primeira evidência de quantização da energia em sistemas atômicos
  - Hipótese de de Broglie
    - Toda partícula tem um comprimento de onda associado: λ = h / p
    - Introduz a dualidade onda-partícula para matéria, não só para luz
  - Experimento da dupla fenda
    - Elétrons (ou fótons) disparados um a um contra duas fendas formam um padrão de interferência
    - Comportamento ondulatório mesmo quando partículas passam individualmente
    - Observar por qual fenda a partícula passou destrói o padrão de interferência (efeito da medição sobre o sistema)
    - Evidência central da dualidade onda-partícula e do papel da observação na física quântica

- Postulados da mecânica quântica
  - Estado quântico
    - O estado de um sistema é representado por um vetor em um espaço vetorial complexo (espaço de Hilbert)
    - Notação de Dirac (bra-ket)
      - Ket |ψ⟩: representa o vetor de estado do sistema
      - Bra ⟨ψ|: representa o vetor dual (conjugado transposto)
      - Produto interno ⟨φ|ψ⟩: mede a sobreposição entre dois estados
  - Superposição
    - Um sistema quântico pode existir em uma combinação linear de estados possíveis simultaneamente
    - Exemplo: |ψ⟩ = a|0⟩ + b|1⟩, onde a e b são amplitudes de probabilidade (números complexos)
    - Normalização: a soma dos módulos ao quadrado das amplitudes deve ser igual a 1 (|a|² + |b|² = 1)
  - Evolução temporal
    - A evolução de um sistema quântico isolado é governada pela equação de Schrödinger
    - Descreve como o vetor de estado muda continuamente no tempo
    - É uma evolução determinística e reversível (antes de qualquer medição)
  - Medição (postulado de Born)
    - Medir um observável produz um dos autovalores possíveis do operador associado
    - A probabilidade de obter cada resultado é dada pelo quadrado da amplitude correspondente
    - Após a medição, o estado "colapsa" para o autoestado associado ao resultado obtido
    - A medição é o único processo não determinístico e irreversível da teoria

- Operadores e observáveis
  - Observáveis físicos (posição, momento, energia, spin) são representados por operadores lineares hermitianos
  - Autovalores do operador correspondem aos possíveis resultados de uma medição
  - Autovetores (autoestados) são os estados nos quais o resultado da medição é certo (100% de probabilidade)
  - Comutadores
    - Medem se dois observáveis podem ser conhecidos simultaneamente com precisão
    - Se dois operadores não comutam, existe um limite fundamental de precisão conjunta (base da incerteza)

- Princípio da incerteza de Heisenberg
  - Não é possível conhecer simultaneamente, com precisão arbitrária, certos pares de grandezas (ex.: posição e momento)
  - Δx · Δp ≥ ħ/2
  - Não é uma limitação de instrumentos de medição, é uma propriedade fundamental da natureza
  - Consequência direta da natureza ondulatória da matéria

- Spin quântico
  - Grau de liberdade intrínseco das partículas, sem análogo clássico direto (não é uma "rotação" literal)
  - Pode assumir valores discretos (ex.: elétron tem spin 1/2, com projeções +1/2 e -1/2)
  - Um dos sistemas físicos de dois níveis mais usados para implementar qubits
  - Medido experimentalmente por meio de campos magnéticos (ex.: experimento de Stern-Gerlach)

- Emaranhamento quântico
  - Fenômeno em que dois ou mais sistemas quânticos interagem de forma que seus estados não podem mais ser descritos independentemente
  - O estado conjunto não pode ser escrito como produto dos estados individuais dos subsistemas
  - Medir um dos sistemas determina instantaneamente o resultado da medição do outro, mesmo à distância
  - Não permite transmitir informação mais rápido que a luz (sem sinalização superluminal, apenas correlação)
  - Correlações violam desigualdades de Bell, o que não tem explicação em teorias clássicas locais
  - Fenômeno central para o poder computacional de sistemas com múltiplos qubits

- Decoerência (visão geral)
  - Processo pelo qual um sistema quântico perde suas propriedades quânticas por interação com o ambiente
  - Causada por ruído: vibrações mecânicas, flutuações térmicas, campos eletromagnéticos externos
  - Principal obstáculo prático para manter superposição e emaranhamento por tempo suficiente
  - Detalhado com mais profundidade na unidade sobre tipos de qubits

- Da física quântica para a computação quântica
  - Bit clássico: representado por um estado definido (0 ou 1)
  - Qubit: sistema quântico de dois níveis que pode estar em superposição de |0⟩ e |1⟩
  - Superposição e emaranhamento são os recursos físicos que dão à computação quântica seu potencial de processamento paralelo
  - A medição de um qubit, assim como em qualquer sistema quântico, colapsa a superposição e retorna um resultado clássico (0 ou 1)

- Siglas e termos explicados
  - ħ (h-bar): constante de Planck reduzida (h dividido por 2π)
  - E = h·f: energia de um quantum de radiação
  - λ = h / p: comprimento de onda de de Broglie
  - Ket / Bra: notação de Dirac para vetores de estado e seus duais
  - Autovalor / Autovetor: resultado possível de uma medição e o estado associado a esse resultado

- Referências para ampliar a pesquisa
  - Nussenzveig, H. M. "Curso de Física Básica" (volume de física moderna/quântica), Editora Blucher
  - Griffiths, D. J. "Introduction to Quantum Mechanics"
  - Feynman, R. "The Feynman Lectures on Physics, Vol. III"
  - Nielsen, M. & Chuang, I. "Quantum Computation and Quantum Information" (capítulos introdutórios de mecânica quântica)
