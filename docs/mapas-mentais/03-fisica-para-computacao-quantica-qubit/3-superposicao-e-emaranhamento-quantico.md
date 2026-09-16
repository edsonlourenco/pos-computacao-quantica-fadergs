# Superposição e Emaranhamento Quântico

- Objetivos da unidade
  - Compreender o que são estados emaranhados
  - Compreender como superposição e emaranhamento são usados em algoritmos quânticos
  - Aplicar essas propriedades na criação de circuitos quânticos

- Superposição
  - A nível quântico, matéria ou energia podem estar em dois (ou mais) estados diferentes ao mesmo tempo
    - Ex.: um elétron pode estar com spin para cima e spin para baixo simultaneamente
    - Ex.: um fóton pode estar polarizado vertical e horizontalmente ao mesmo tempo
  - Ao medir uma entidade quântica em superposição, observa-se apenas um dos estados; o resultado não pode ser previsto com certeza antes da medição
  - A natureza "decide" o resultado da medição de forma probabilística (como uma moeda tendenciosa), e essa tendência está relacionada a como os estados estão superpostos
  - Toda a probabilidade da mecânica quântica está associada ao processo de medição, não à evolução de um sistema isolado sem perturbação
  - Analogia clássica (limitada): a figura ambígua "jovem ou senhora" ilustra a ideia de múltiplas interpretações que colapsam em uma só ao serem observadas, mas na mecânica quântica a superposição de atributos é a regra, não a exceção
  - Colapso da função de onda
    - Ao observar um sistema em superposição, apenas um autoestado é revelado, "congelando" o sistema nesse estado
    - Observações subsequentes (sem nova preparação do estado) revelam sempre o mesmo autoestado
    - As probabilidades de cada resultado seguem a regra de Born (Max Born, 1926): é o processo de medição que introduz as probabilidades na mecânica quântica

- Emaranhamento quântico
  - Fenômeno em que duas ou mais entidades quânticas estão tão correlacionadas que se comportam como uma única entidade composta, não importa a distância entre elas
  - Medir uma delas colapsa instantaneamente o estado da outra, de forma consistente com as leis da mecânica quântica (Einstein chamava isso de "ação fantasmagórica à distância" — spooky action)
  - Não permite transmitir informação mais rápido que a luz: a correlação é real, mas não há sinalização superluminal
  - Exemplo físico: emaranhamento de dois fótons por meio de um cristal (ex.: BBO), que transforma um fóton de entrada em dois fótons complementares de menor energia
  - Confirmado por centenas de experimentos; correlações violam as desigualdades de Bell, sem explicação possível por teorias clássicas locais
  - Recurso exclusivo do mundo quântico, sem paralelo clássico, e fundamental para o desenho de algoritmos quânticos eficientes

- Lógica quântica x lógica clássica
  - Superposição e emaranhamento são as propriedades que distinguem a lógica quântica da lógica clássica
  - Na lógica quântica, a lei distributiva da lógica proposicional falha
  - Bits clássicos podem estar em 0 ou 1; qubits podem estar em superposição de 0 e 1, e podem estar emaranhados com outros qubits (algo sem análogo para bits clássicos)
  - Essas propriedades formam a base do paralelismo quântico: um computador quântico pode verificar várias soluções potenciais simultaneamente, enquanto um computador clássico as explora sequencialmente

- Estados produto x estados emaranhados
  - Estados não emaranhados são chamados de "estados produto": podem ser escritos como o produto de estados individuais de cada qubit, e suas probabilidades apenas se multiplicam
  - Teste de emaranhamento: verificar se medir um qubit altera a distribuição de probabilidade do outro qubit
  - Exemplo (estado de Bell): |Ψ⟩ = (1/√2)(|00⟩ + |11⟩)
    - Antes de qualquer medição, o qubit 2 tem 50% de chance de ser medido em |0⟩ ou |1⟩
    - Mas, ao medir o qubit 1, o resultado do qubit 2 passa a ser conhecido com 100% de certeza → os qubits estão emaranhados

- Exemplo intuitivo: moedas emaranhadas
  - Classicamente, duas moedas lançadas muitas vezes produzem CC, CCo, CoC e CoCo, cada uma com 25% de probabilidade
  - Emaranhadas (em um estado de Bell), apenas dois resultados são possíveis: ambas cara (50%) ou ambas coroa (50%); nunca resultados diferentes entre si
  - Mesmo separadas por grandes distâncias, medir uma moeda determina instantaneamente o resultado da outra

- Múltiplos qubits
  - Um sistema de 2 qubits é descrito como uma superposição dos 4 estados da base: |ψ⟩ = α₀₀|00⟩ + α₀₁|01⟩ + α₁₀|10⟩ + α₁₁|11⟩
  - Ao medir os dois qubits, o sistema colapsa para um dos quatro estados da base, com probabilidade |αᵢⱼ|²
  - Se os qubits forem independentes (não emaranhados), a probabilidade conjunta é o produto das probabilidades individuais de cada qubit

- Siglas e termos explicados
  - Estado de Bell: estado maximamente emaranhado de dois qubits, usado como exemplo canônico de emaranhamento
  - Estado produto: estado de vários qubits que pode ser fatorado no produto de estados individuais (não emaranhado)
  - Regra de Born: regra probabilística que relaciona a amplitude de um estado quântico à probabilidade de medição de um resultado

- Referências para ampliar a pesquisa
  - Falbriard, Claude; Brosso, Ines. "Computação Quântica". Rio de Janeiro: Alta Books, 2020
  - Mahon, José Roberto P. "Mecânica Quântica - Desenvolvimento Contemporâneo com Aplicações". Grupo GEN, 2011
  - Quanta Magazine: "Entanglement Made Simple" (quantamagazine.org)
  - Documentação da Microsoft sobre computação quântica (docs.microsoft.com/azure/quantum)
