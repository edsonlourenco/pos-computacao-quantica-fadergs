# Pós-Graduação em Computação Quântica - FADERGS 🎓✨

Bem-vindo ao repositório de estudos e práticas da pós-graduação em **Computação Quântica** pela FADERGS. O grande objetivo deste espaço é reunir e organizar todo o conhecimento, anotações, mapas mentais e códigos desenvolvidos ao longo do curso.

Este repositório foi construído com foco no meu desenvolvimento profissional em **Computação Quântica aplicada à Inteligência Artificial (IA)**, mas também foi planejado para servir de consulta e apoio para qualquer pessoa interessada em aprender sobre esses temas incríveis.

---

## 🧐 O que é Computação Quântica e Aprendizado de Máquina? (Explicado de um jeito simples!)

Se você não é da área de tecnologia, não se preocupe! Aqui está uma explicação bem simples sobre o que estudamos neste curso:

*   **Computação Quântica 🌌:** Os computadores normais (como o seu celular ou notebook) guardam e processam informações usando bits, que são como lâmpadas que só podem estar apagadas (0) ou acesas (1). Já o computador quântico usa as regras da física quântica (o comportamento de partículas minúsculas, como átomos e elétrons). Isso permite que ele use "qubits" (bits quânticos), que podem estar apagados, acesos ou *nos dois estados ao mesmo tempo*! Isso dá a ele um poder gigantesco para resolver problemas super complexos muito mais rápido.
*   **Aprendizado de Máquina (Machine Learning) 🤖:** É uma técnica onde ensinamos os computadores a aprenderem sozinhos a partir de exemplos (dados), sem que a gente precise programar regras rígidas. É o que faz o YouTube te recomendar vídeos parecidos com o que você já assistiu ou o que ajuda os bancos a detectarem se uma compra no cartão de crédito é fraude.

---

## 🏛️ Estrutura da Pós-Graduação

O curso é muito completo e estruturado para cobrir desde a física básica necessária até as aplicações práticas de programação quântica em negócios. A matriz curricular é composta pelos seguintes componentes:

| Eixo Curricular | Componente de Aprendizagem (CA) | Duração Estimada | Foco do Componente |
| :--- | :--- | :---: | :--- |
| **Eixo de Desenvolvimento Integral** | Felicidade no Trabalho e Performance Sustentável | 40 horas | Desenvolvimento de competências profissionais, bem-estar e carreira. |
| **Eixo Específico (Obrigatórios)** | [Aprendizado de Máquina](#-aprendizado-de-máquina-ca-concluído) | 40 horas | Fundamentos de IA e algoritmos clássicos de aprendizado. |
| | [Conceitos de Computação Quântica](#-conceitos-de-computação-quântica-ca-concluído) | 40 horas | Bases e teorias matemáticas da computação quântica. |
| | Física para Computação Quântica e Qubit | 40 horas | Comportamento físico de qubits e sistemas quânticos. |
| | Programação para Computação Quântica | 40 horas | Lógica e desenvolvimento de circuitos quânticos iniciais. |
| | Aplicações com Python Qiskit | 40 horas | Uso da biblioteca Qiskit (IBM) para simular algoritmos quânticos. |
| | Aplicações Inovadoras em Computação Quântica | 40 horas | Casos de uso reais e inovações do mercado. |
| | Criptografia Aplicada & Comunicações Seguras | 40 horas | Segurança de dados na era quântica. |
| | Segurança Aplicada à Computação Quântica | 40 horas | Protocolos de segurança de redes e computadores quânticos. |
| **Eixo Personalizável** | Componente Optativo à Escolha | 40 horas | Customização da formação conforme interesses profissionais. |

---

## 🧠 Aprendizado de Máquina (CA Concluído)

Este foi o primeiro módulo concluído no curso. Abaixo, você encontra os tópicos estudados, explicados de forma simples, com links para os **Mapas Mentais** (resumos teóricos em texto) e os **Notebooks** (códigos práticos em Python).

### 1. Ensinando um Sistema a Aprender
*   **O que significa?** Como usar dados históricos para treinar um modelo para fazer previsões e como medir se ele está indo bem. Também abordamos o cuidado para o computador não "decorar" as respostas do passado em vez de aprender de verdade (um problema chamado de *overfitting*).
*   🧠 **Resumo Teórico:** [1-ensinando-um-sistema-aprender.md](docs/mapas-mentais/01-aprendizado-de-maquina-overview/1-ensinando-um-sistema-aprender.md)
*   📓 **Código Prático:** [1-classificadores.py](src/01-aprendizado-de-maquina-overview/notebooks/1-classificadores.py)

### 2. Clusterização de Dados
*   **O que significa?** É a técnica de agrupar coisas parecidas quando não temos respostas prontas. Por exemplo, agrupar clientes de um e-commerce em "grupos de interesses parecidos" para enviar promoções personalizadas. Também estudamos como criar sistemas de recomendação (como os da Netflix).
*   🧠 **Resumo Teórico:** [2-clusterização-de-dados.md](docs/mapas-mentais/01-aprendizado-de-maquina-overview/2-clusterização-de-dados.md)
*   📓 **Código Prático:** [2-clusterização-de-dados.py](src/01-aprendizado-de-maquina-overview/notebooks/2-clusterização-de-dados.py)

### 3. Regressão e Séries Temporais
*   **O que significa?** Usado para prever números exatos (como o preço de uma ação amanhã, o faturamento de uma empresa no próximo mês ou a temperatura). Estudamos como identificar tendências que mudam ao longo do tempo.
*   🧠 **Resumo Teórico:** [3-regressão-e-séries-temporais.md](docs/mapas-mentais/01-aprendizado-de-maquina-overview/3-regressão-e-séries-temporais.md)
*   📓 **Código Prático:** [3-regressão-e-séries-temporais.py](src/01-aprendizado-de-maquina-overview/notebooks/3-regressão-e-séries-temporais.py)

### 4. Aprendizado por Reforço, Redes Neurais e Comitês
*   **O que significa?** 
    *   *Aprendizado por Reforço:* Ensinar a máquina através de "tentativa e erro", dando recompensas quando ela acerta e punições quando erra (como ensinar um robô a andar ou jogar videogame).
    *   *Redes Neurais:* Sistemas inspirados no cérebro humano criados para aprender padrões muito complexos (como reconhecer fotos de gatos).
    *   *Comitês:* Juntar várias inteligências artificiais simples para trabalharem juntas, melhorando o resultado final (a união faz a força!).
*   🧠 **Resumo Teórico:** [4-aprendizado-por-reforco-redes-neurais-e-comites.md](docs/mapas-mentais/01-aprendizado-de-maquina-overview/4-aprendizado-por-reforco-redes-neurais-e-comites.md)
*   📓 **Códigos Práticos:**
    *   [4-rl-q-learning.py](src/01-aprendizado-de-maquina-overview/notebooks/4-rl-q-learning.py) (Aprendizado por Reforço na prática)
    *   [4b-redes-neurais-comites.py](src/01-aprendizado-de-maquina-overview/notebooks/4b-redes-neurais-comites.py) (Redes neurais e combinação de modelos)
    *   [4-aprendizado-por-reforco-redes-neurais-e-comites.py](src/01-aprendizado-de-maquina-overview/notebooks/4-aprendizado-por-reforco-redes-neurais-e-comites.py) (Integração de todos os temas do módulo)

---

## 🧬 Conceitos de Computação Quântica (CA Concluído)

Este módulo cobre os fundamentos teóricos da computação quântica: da história da área até os algoritmos que hoje motivam o interesse do mercado. Como é um módulo mais teórico, os tópicos abaixo têm apenas **Mapas Mentais** (resumos teóricos em texto), sem notebooks de código.

### 1. História da Computação Quântica
*   **O que significa?** A trajetória da computação quântica desde as primeiras propostas teóricas (Feynman, Deutsch, Shor) até a corrida atual entre Google, IBM e outras empresas pela chamada "supremacia quântica" — o momento em que um computador quântico resolve algo que nenhum computador clássico consegue resolver em tempo viável.
*   🧠 **Resumo Teórico:** [1-historia-da-computacao-quantica.md](docs/mapas-mentais/02-conceitos-computacao-quantica/1-historia-da-computacao-quantica.md)

### 2. Fundamentos da Mecânica Quântica
*   **O que significa?** A base de física necessária para entender computação quântica: por que a física clássica não explica certos fenômenos, o que é superposição, incerteza, emaranhamento e como esses conceitos são representados matematicamente.
*   🧠 **Resumo Teórico:** [2-fundamentos-da-mecanica-quantica.md](docs/mapas-mentais/02-conceitos-computacao-quantica/2-fundamentos-da-mecanica-quantica.md)

### 3. Tipos de Qubits
*   **O que significa?** O qubit é a unidade básica de informação de um computador quântico, equivalente ao bit clássico, mas capaz de estar em superposição. Estudamos como ele é representado (esfera de Bloch), seus desafios (decoerência) e como diferentes empresas o constroem fisicamente (íons presos, spin de elétrons, supercondutores).
*   🧠 **Resumo Teórico:** [3-tipos-de-qubits.md](docs/mapas-mentais/02-conceitos-computacao-quantica/3-tipos-de-qubits.md)

### 4. Circuitos Quânticos
*   **O que significa?** Assim como um circuito clássico combina portas lógicas para processar bits, um circuito quântico combina portas quânticas (Hadamard, CNOT, entre outras) para manipular qubits, criar superposição e emaranhamento.
*   🧠 **Resumo Teórico:** [4-circuitos-quanticos.md](docs/mapas-mentais/02-conceitos-computacao-quantica/4-circuitos-quanticos.md)

### 5. Algoritmos Quânticos
*   **O que significa?** Os algoritmos que realmente mostram a vantagem de um computador quântico sobre um clássico, como o algoritmo de Shor (que ameaça a criptografia atual) e o algoritmo de Grover (busca mais rápida em listas não organizadas).
*   🧠 **Resumo Teórico:** [5-algoritmos-quanticos.md](docs/mapas-mentais/02-conceitos-computacao-quantica/5-algoritmos-quanticos.md)

---

## 🚀 Como Rodar o Projeto Localmente

Para executar os códigos e estudar em seu computador, siga os passos abaixo. Utilizaremos o **uv**, que é uma ferramenta moderna e extremamente rápida para gerenciar projetos em Python.

### 1. Clonar o repositório
Abra o seu terminal e rode o comando abaixo para baixar o código:
```bash
git clone https://github.com/edsonlourenco/pos-computacao-quantica-fadergs.git
cd pos-computacao-quantica-fadergs
```

### 2. Instalar o `uv`
Se você ainda não tem o `uv` instalado, pode instalá-lo facilmente:
* **macOS / Linux:**
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
* **Windows:**
  ```powershell
  powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

### 3. Criar o ambiente e instalar dependências
Para preparar o ambiente virtual local (que evita misturar os pacotes deste projeto com outros do seu computador) e instalar todos os pacotes necessários descritos no arquivo [pyproject.toml](pyproject.toml), rode:
```bash
# Cria o ambiente virtual (.venv) e instala tudo automaticamente
uv sync
```

### 4. Executar os códigos (.py interativos)
Como convertemos os notebooks para arquivos `.py` interativos com linhas mágicas (`# %%`), você tem duas formas principais de executá-los:

* **Pelo VS Code (Recomendado):**
  1. Abra a pasta do projeto no VS Code.
  2. Abra um dos arquivos `.py` dentro da pasta `src/01-aprendizado-de-maquina-overview/notebooks/`.
  3. Clique na opção **"Run Cell"** (Executar Célula) que aparece em cima de cada bloco para rodar o código de forma interativa.

* **Diretamente pelo terminal:**
  Caso queira rodar o arquivo por inteiro como um script convencional do Python:
  ```bash
  uv run python src/01-aprendizado-de-maquina-overview/notebooks/1-classificadores.py
  ```

---

## 👥 Contribuições e Modificações

Este repositório é público para incentivar o compartilhamento de conhecimento. Contudo, como o foco principal é meu desenvolvimento pessoal durante as disciplinas da pós-graduação, **qualquer alteração, sugestão ou conteúdo adicional deve passar estritamente pela minha avaliação e aprovação prévia**.

Se tiver alguma sugestão de melhoria, sinta-se à vontade para abrir uma *Issue* ou enviar um *Pull Request* para que eu possa analisar!

---

## 🔗 Referências

Toda a organização e ementa do curso foram baseadas nos canais oficiais da instituição de ensino:

1.  **Página Oficial do Curso:** [Pós-Graduação em Computação Quântica - FADERGS](https://pos.fadergs.edu.br/curso/computacao-quantica)
2.  **Matriz Curricular Oficial (PDF):** [Visualizar Matriz Completa do Curso](https://uploads-pos-graduacao.s3.us-east-1.amazonaws.com//COMPUTACAO_QUANTICA_matriz_site_EAD_e_LIVE_77a7a85d3d.pdf)
