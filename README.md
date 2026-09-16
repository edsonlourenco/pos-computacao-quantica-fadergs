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
| | Conceitos de Computação Quântica | 40 horas | Bases e teorias matemáticas da computação quântica. |
| | [Física para Computação Quântica e Qubit](#️-física-para-computação-quântica-e-qubit-ca-concluído) | 40 horas | Comportamento físico de qubits e sistemas quânticos. |
| | Programação para Computação Quântica | 40 horas | Lógica e desenvolvimento de circuitos quânticos iniciais. |
| | Aplicações com Python Qiskit | 40 horas | Uso da biblioteca Qiskit (IBM) para simular algoritmos quânticos. |
| | Aplicações Inovadoras em Computação Quântica | 40 horas | Casos de uso reais e inovações do mercado. |
| | [Criptografia Aplicada & Comunicações Seguras](#-criptografia-aplicada--comunicações-seguras-ca-concluído) | 40 horas | Segurança de dados na era quântica. |
| | Segurança Aplicada à Computação Quântica | 40 horas | Protocolos de segurança de redes e computadores quânticos. |
| **Eixo Personalizável** | Componente Optativo à Escolha | 40 horas | Customização da formação conforme interesses profissionais. |

---

## 🧠 Aprendizado de Máquina (CA Concluído)

Este foi o primeiro módulo concluído no curso. Abaixo, você encontra os tópicos estudados, explicados de forma simples, com links para os **Mapas Mentais** (resumos teóricos em texto) e os **Códigos Práticos** (arquivos `.py` interativos em Python).

### 1. Ensinando um Sistema a Aprender
*   **O que significa?** Como usar dados históricos para treinar um modelo para fazer previsões e como medir se ele está indo bem. Também abordamos o cuidado para o computador não "decorar" as respostas do passado em vez de aprender de verdade (um problema chamado de *overfitting*).
*   🧠 **Resumo Teórico:** [1-ensinando-um-sistema-aprender.md](docs/mapas-mentais/01-aprendizado-de-maquina-overview/1-ensinando-um-sistema-aprender.md)
*   📓 **Código Prático:** [1-classificadores.py](src/fundamentos/1-classificadores.py)

### 2. Clusterização de Dados
*   **O que significa?** É a técnica de agrupar coisas parecidas quando não temos respostas prontas. Por exemplo, agrupar clientes de um e-commerce em "grupos de interesses parecidos" para enviar promoções personalizadas. Também estudamos como criar sistemas de recomendação (como os da Netflix).
*   🧠 **Resumo Teórico:** [2-clusterização-de-dados.md](docs/mapas-mentais/01-aprendizado-de-maquina-overview/2-clusterização-de-dados.md)
*   📓 **Código Prático:** [2-clusterização-de-dados.py](src/fundamentos/2-clusterização-de-dados.py)

### 3. Regressão e Séries Temporais
*   **O que significa?** Usado para prever números exatos (como o preço de uma ação amanhã, o faturamento de uma empresa no próximo mês ou a temperatura). Estudamos como identificar tendências que mudam ao longo do tempo.
*   🧠 **Resumo Teórico:** [3-regressão-e-séries-temporais.md](docs/mapas-mentais/01-aprendizado-de-maquina-overview/3-regressão-e-séries-temporais.md)
*   📓 **Código Prático:** [3-regressão-e-séries-temporais.py](src/fundamentos/3-regressão-e-séries-temporais.py)

### 4. Aprendizado por Reforço, Redes Neurais e Comitês
*   **O que significa?** 
    *   *Aprendizado por Reforço:* Ensinar a máquina através de "tentativa e erro", dando recompensas quando ela acerta e punições quando erra (como ensinar um robô a andar ou jogar videogame).
    *   *Redes Neurais:* Sistemas inspirados no cérebro humano criados para aprender padrões muito complexos (como reconhecer fotos de gatos).
    *   *Comitês:* Juntar várias inteligências artificiais simples para trabalharem juntas, melhorando o resultado final (a união faz a força!).
*   🧠 **Resumo Teórico:** [4-aprendizado-por-reforco-redes-neurais-e-comites.md](docs/mapas-mentais/01-aprendizado-de-maquina-overview/4-aprendizado-por-reforco-redes-neurais-e-comites.md)
*   📓 **Códigos Práticos:**
    *   [4-rl-q-learning.py](src/fundamentos/4-rl-q-learning.py) (Aprendizado por Reforço na prática)
    *   [4b-redes-neurais-comites.py](src/fundamentos/4b-redes-neurais-comites.py) (Redes neurais e combinação de modelos)
    *   [4-aprendizado-por-reforco-redes-neurais-e-comites.py](src/fundamentos/4-aprendizado-por-reforco-redes-neurais-e-comites.py) (Integração de todos os temas do módulo)

---

## ⚛️ Física para Computação Quântica e Qubit (CA Concluído)

Este módulo aprofunda a física por trás da computação quântica: como a informação é codificada e transmitida usando qubits, os fenômenos de superposição e emaranhamento, os diferentes jeitos de construir um qubit fisicamente e como um computador quântico completo (hardware + algoritmos) funciona na prática.

> A unidade introdutória do módulo (fundamentos de física quântica: dualidade onda-partícula, princípio da incerteza etc.) ainda não tem um resumo dedicado aqui; os mesmos conceitos já estão cobertos em [2-fundamentos-da-mecanica-quantica.md](docs/mapas-mentais/02-conceitos-computacao-quantica/2-fundamentos-da-mecanica-quantica.md), do módulo de Conceitos de Computação Quântica.

### 2. Teoria da Informação Quântica
*   **O que significa?** Como a computação quântica também é uma teoria da informação: a diferença entre bit e qubit, os teoremas de Shannon sobre compressão e transmissão de dados, o que é entropia da informação e por que não é possível "copiar e colar" um qubit desconhecido (teorema da não clonagem).
*   🧠 **Resumo Teórico:** [2-teoria-da-informacao-quantica.md](docs/mapas-mentais/03-fisica-para-computacao-quantica-qubit/2-teoria-da-informacao-quantica.md)

### 3. Superposição e Emaranhamento Quântico
*   **O que significa?** Superposição é a capacidade de um qubit estar em mais de um estado ao mesmo tempo; emaranhamento é a correlação profunda entre dois ou mais qubits, que faz com que se comportem como uma única entidade, não importa a distância entre eles.
*   🧠 **Resumo Teórico:** [3-superposicao-e-emaranhamento-quantico.md](docs/mapas-mentais/03-fisica-para-computacao-quantica-qubit/3-superposicao-e-emaranhamento-quantico.md)
*   📓 **Código Prático:** [superposicao-e-emaranhamento.py](src/quantum/superposicao-e-emaranhamento.py) (superposição de 1 qubit e estado de Bell)

### 4. Qubits
*   **O que significa?** O que é, na prática, um qubit físico (spin de elétron, polarização de fóton), as vantagens de memória e velocidade da computação quântica, as portas lógicas quânticas, a esfera de Bloch e as principais formas de implementar um qubit (armadilha de íons, spin de elétrons, supercondutores).
*   🧠 **Resumo Teórico:** [4-qubits.md](docs/mapas-mentais/03-fisica-para-computacao-quantica-qubit/4-qubits.md)

### 5. Computadores Quânticos e Algoritmos Quânticos
*   **O que significa?** Como um computador quântico completo é estruturado (do qubit físico até o algoritmo de alto nível), o que são redes quânticas, e como funciona um algoritmo quântico de verdade — usando o algoritmo de Deutsch como exemplo de como a superposição e o emaranhamento permitem responder uma pergunta com uma única medição.
*   🧠 **Resumo Teórico:** [5-computadores-quanticos-e-algoritmos-quanticos.md](docs/mapas-mentais/03-fisica-para-computacao-quantica-qubit/5-computadores-quanticos-e-algoritmos-quanticos.md)
*   📓 **Código Prático:** [algoritmo-deutsch-jozsa.py](src/quantum/algoritmo-deutsch-jozsa.py) (algoritmo de Deutsch para funções constantes e balanceadas)

---

## 🔐 Criptografia Aplicada & Comunicações Seguras (CA Concluído)

Este módulo cobre a segurança da informação de ponta a ponta: os princípios que orientam qualquer sistema de segurança (confidencialidade, integridade, disponibilidade), os algoritmos de criptografia usados na prática, os protocolos que protegem dados em trânsito, a gestão de riscos e conformidade, e as boas práticas tecnológicas e operacionais para proteger uma organização.

### 1. Princípios da Segurança da Informação
*   **O que significa?** Os três pilares que orientam qualquer decisão de segurança (confidencialidade, integridade e disponibilidade), o que é criptografia e chaves, a diferença entre criptografia simétrica e assimétrica, funções hash, assinatura digital e certificado digital.
*   🧠 **Resumo Teórico:** [1-principios-da-seguranca-da-informacao.md](docs/mapas-mentais/04-criptografia-aplicada-comunicacoes-seguras/1-principios-da-seguranca-da-informacao.md)
*   📓 **Código Prático:** [algoritmos-criptografia.py](src/criptografia/algoritmos-criptografia.py) (hash SHA-256, criptografia simétrica AES e assimétrica RSA)

### 2. Principais Algoritmos de Criptografia
*   **O que significa?** Como funcionam, na prática, os cifradores de fluxo e de bloco, o algoritmo simétrico AES (padrão atual de mercado) e o algoritmo assimétrico RSA (baseado na dificuldade de fatorar números primos gigantes).
*   🧠 **Resumo Teórico:** [2-principais-algoritmos-de-criptografia.md](docs/mapas-mentais/04-criptografia-aplicada-comunicacoes-seguras/2-principais-algoritmos-de-criptografia.md)

### 3. Sistemas Criptográficos
*   **O que significa?** Criptografia de curvas elípticas (mais eficiente que o RSA), os protocolos que protegem dados em trânsito (IPSec, SSL/TLS, PGP, VPN) e uma introdução à criptografia quântica (Distribuição Quântica de Chaves) como ameaça e solução para a criptografia do futuro.
*   🧠 **Resumo Teórico:** [3-sistemas-criptograficos.md](docs/mapas-mentais/04-criptografia-aplicada-comunicacoes-seguras/3-sistemas-criptograficos.md)

### 4. Gestão em Segurança da Informação
*   **O que significa?** Como fazer análise e tratamento de riscos, a Política Nacional de Segurança das Informações e a ICP-Brasil, a LGPD e outras legislações relevantes, auditoria de sistemas (norma ISO/IEC 27002) e os mecanismos de autenticação e controle de acesso (senhas, token, biometria, autenticação de dois fatores).
*   🧠 **Resumo Teórico:** [4-gestao-em-seguranca-da-informacao.md](docs/mapas-mentais/04-criptografia-aplicada-comunicacoes-seguras/4-gestao-em-seguranca-da-informacao.md)

### 5. Boas Práticas em Segurança da Informação
*   **O que significa?** As principais tecnologias de defesa de uma rede (firewall, IPS, DLP, firewall de nova geração), como construir um plano de continuidade de negócios, segurança física e de sistemas operacionais, defesa contra malwares e os principais tipos de ataque a redes.
*   🧠 **Resumo Teórico:** [5-boas-praticas-em-seguranca-da-informacao.md](docs/mapas-mentais/04-criptografia-aplicada-comunicacoes-seguras/5-boas-praticas-em-seguranca-da-informacao.md)

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
  2. Abra um dos arquivos `.py` dentro da pasta `src/fundamentos/`.
  3. Clique na opção **"Run Cell"** (Executar Célula) que aparece em cima de cada bloco para rodar o código de forma interativa.

* **Diretamente pelo terminal:**
  Caso queira rodar o arquivo por inteiro como um script convencional do Python:
  ```bash
  uv run python src/fundamentos/1-classificadores.py
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
