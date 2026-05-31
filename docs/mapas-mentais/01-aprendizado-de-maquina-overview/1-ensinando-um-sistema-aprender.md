# Ensinando um sistema a aprender

- Notebook do tema
  - [1-classificadores.ipynb](../../../src/01-aprendizado-de-maquina-overview/notebooks/1-classificadores.ipynb) - Classificadores práticos em Python.

- Introdução
  - Aprendizado de máquina melhora processos invisíveis: previsão de demanda, classificação de busca, recomendações, detecção de fraude, tradução
  - Jeff Bezos (2016): ML aprimora operações principais silenciosa e significativamente
  - Perguntas centrais
    - Como construir programas que aprendem com dados?
    - Quais etapas há na construção e implantação?
    - Como usar métricas de avaliação?

- Objetivos da unidade
  - Compreender o que é aprendizado de máquina e seus conceitos fundamentais
  - Identificar tipos de aprendizado e classes de problemas
  - Entender etapas de construção e implantação de um sistema de ML
  - Conhecer métricas de avaliação de sistemas de aprendizado
  - Identificar problemas e ferramentas disponíveis no mercado

- Exemplo: sistema de diagnóstico de diabetes
  - Problema: avaliar risco de diabetes com base em dados de associados
  - Base de dados: 200 associados, 20 diagnosticados
  - Objetivo do sistema: prever alto risco de diabetes
  - Tarefa do sistema: classificação

- Conceitos básicos
  - Amostras
    - Cada registro de dados é uma amostra
    - Exemplo: dados de um único paciente
  - Atributos
    - Características que descrevem a amostra
    - Qualitativos: informação não numérica (histórico familiar, cor, nome)
    - Quantitativos: informação numérica
      - Discretos: valores enumeráveis, inteiros
      - Contínuos: valores com casas decimais (IMC, colesterol)
  - Classes
    - Categorias de saída do problema
    - Exemplo: tem diabetes / não tem diabetes
  - Amostra rotulada vs não rotulada
    - Rotulada: classe conhecida previamente
    - Não rotulada: classe desconhecida

- Tipos de tarefas e formas de aprendizado
  - Tarefas de aprendizado
    - Classificação
    - Agrupamento
    - Regressão
  - Formas de aprendizado
    - Aprendizado supervisionado
    - Aprendizado não supervisionado
    - Aprendizado por reforço
  - Exemplo prático: sistema de risco de diabetes é uma tarefa de classificação

- Construção do modelo
  - Visualização dos dados no espaço de características
    - Gráfico de IMC x colesterol
    - Distribuição de amostras por classe
  - Modelo como função matemática
  - Superfície de decisão
    - Separação das regiões de classes no espaço de atributos

- Etapas de construção de um sistema de ML
  - Geração ou coleta de dados
  - Preparação dos dados
  - Seleção de algoritmos
  - Treinamento de modelos
  - Avaliação de modelos
  - Ajuste de parâmetros
  - Implantação e monitoramento

- Métricas de avaliação
  - Propósito: avaliar qualidade do sistema de aprendizado
  - Métricas gerais
    - Acurácia: proporção de previsões corretas em relação ao total de casos analisados.
    - Precisão: fração de classificações positivas que realmente são positivas.
    - Sensibilidade: fração de casos positivos reais corretamente identificados pelo modelo.
    - Especificidade: fração de casos negativos reais corretamente identificados pelo modelo.
    - ROC / AUC: curva que mostra o trade-off entre sensibilidade e taxa de falso positivo, e área sob essa curva.
    - F1-Score: média harmônica entre precisão e sensibilidade, útil para classes desbalanceadas.
    - Logarithmic Loss: medida que penaliza previsões de probabilidade incorretas, avaliando confiança e incerteza.
  - Métricas para agrupamento
    - Silhueta: mede a qualidade do agrupamento avaliando a coesão interna e a separação entre clusters.
    - Adjusted mutual information: compara duas particionamentos ajustando por acaso para avaliar similaridade entre clusters.
    - Adjusted rand score: calcula a concordância entre duas segmentações corrigindo coincidências aleatórias.
  - Métricas para reforço
    - CV error: erro de validação cruzada, usado para medir o desempenho médio do modelo em diferentes subconjuntos de dados.
    - CVaR: valor em risco condicional, estima a perda média nos piores cenários para avaliar risco extremo.
    - SRT: tempo de resposta do sistema, avalia a rapidez com que o agente reage às mudanças do ambiente.
    - IOR: razão de retorno de oportunidade, compara o retorno obtido com o retorno potencial ideal em decisões de reforço.
    - LRT: teste de razão de verossimilhança, usado para comparar e validar hipóteses ou modelos de aprendizado por reforço.

- Ferramentas e ambiente de desenvolvimento
  - Python >= 3+
  - Pandas > 1.1
  - NumPy > 1.10
  - scikit-learn > 0.2
  - TensorFlow > 2.0
  - Keras > 2.0
  - Google Colaboratory para desenvolvimento em nuvem ou local com VSCode

- Práticas sugeridas
  - Prática 1: Aprendendo Python
  - Prática 2: Aprendendo Pandas, NumPy e Matplotlib

- Escolha de algoritmos
  - Existem centenas de algoritmos e variações
  - Testar todos não é viável
  - Devem ser considerados fatores importantes ao escolher algoritmos
