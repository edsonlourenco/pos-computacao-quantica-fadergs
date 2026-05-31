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
*   📓 **Código Prático:** [1-classificadores.ipynb](src/01-aprendizado-de-maquina-overview/notebooks/1-classificadores.ipynb)

### 2. Clusterização de Dados
*   **O que significa?** É a técnica de agrupar coisas parecidas quando não temos respostas prontas. Por exemplo, agrupar clientes de um e-commerce em "grupos de interesses parecidos" para enviar promoções personalizadas. Também estudamos como criar sistemas de recomendação (como os da Netflix).
*   🧠 **Resumo Teórico:** [2-clusterização-de-dados.md](docs/mapas-mentais/01-aprendizado-de-maquina-overview/2-clusterização-de-dados.md)
*   📓 **Código Prático:** [2-clusterização-de-dados.ipynb](src/01-aprendizado-de-maquina-overview/notebooks/2-clusterização-de-dados.ipynb)

### 3. Regressão e Séries Temporais
*   **O que significa?** Usado para prever números exatos (como o preço de uma ação amanhã, o faturamento de uma empresa no próximo mês ou a temperatura). Estudamos como identificar tendências que mudam ao longo do tempo.
*   🧠 **Resumo Teórico:** [3-regressão-e-séries-temporais.md](docs/mapas-mentais/01-aprendizado-de-maquina-overview/3-regressão-e-séries-temporais.md)
*   📓 **Código Prático:** [3-regressão-e-séries-temporais.ipynb](src/01-aprendizado-de-maquina-overview/notebooks/3-regressão-e-séries-temporais.ipynb)

### 4. Aprendizado por Reforço, Redes Neurais e Comitês
*   **O que significa?** 
    *   *Aprendizado por Reforço:* Ensinar a máquina através de "tentativa e erro", dando recompensas quando ela acerta e punições quando erra (como ensinar um robô a andar ou jogar videogame).
    *   *Redes Neurais:* Sistemas inspirados no cérebro humano criados para aprender padrões muito complexos (como reconhecer fotos de gatos).
    *   *Comitês:* Juntar várias inteligências artificiais simples para trabalharem juntas, melhorando o resultado final (a união faz a força!).
*   🧠 **Resumo Teórico:** [4-aprendizado-por-reforco-redes-neurais-e-comites.md](docs/mapas-mentais/01-aprendizado-de-maquina-overview/4-aprendizado-por-reforco-redes-neurais-e-comites.md)
*   📓 **Códigos Práticos:**
    *   [4-rl-q-learning.ipynb](src/01-aprendizado-de-maquina-overview/notebooks/4-rl-q-learning.ipynb) (Aprendizado por Reforço na prática)
    *   [4b-redes-neurais-comites.ipynb](src/01-aprendizado-de-maquina-overview/notebooks/4b-redes-neurais-comites.ipynb) (Redes neurais e combinação de modelos)
    *   [4-aprendizado-por-reforco-redes-neurais-e-comites.ipynb](src/01-aprendizado-de-maquina-overview/notebooks/4-aprendizado-por-reforco-redes-neurais-e-comites.ipynb) (Integração de todos os temas do módulo)

---

## 👥 Contribuições e Modificações

Este repositório é público para incentivar o compartilhamento de conhecimento. Contudo, como o foco principal é meu desenvolvimento pessoal durante as disciplinas da pós-graduação, **qualquer alteração, sugestão ou conteúdo adicional deve passar estritamente pela minha avaliação e aprovação prévia**.

Se tiver alguma sugestão de melhoria, sinta-se à vontade para abrir uma *Issue* ou enviar um *Pull Request* para que eu possa analisar!

---

## 🔗 Referências

Toda a organização e ementa do curso foram baseadas nos canais oficiais da instituição de ensino:

1.  **Página Oficial do Curso:** [Pós-Graduação em Computação Quântica - FADERGS](https://pos.fadergs.edu.br/curso/computacao-quantica)
2.  **Matriz Curricular Oficial (PDF):** [Visualizar Matriz Completa do Curso](https://uploads-pos-graduacao.s3.us-east-1.amazonaws.com//COMPUTACAO_QUANTICA_matriz_site_EAD_e_LIVE_77a7a85d3d.pdf)
