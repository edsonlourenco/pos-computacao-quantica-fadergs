# Boas Práticas em Segurança da Informação

- Introdução
  - Os ataques a postos de trabalho ou servidores cresceram fortemente com a expansão do home office: segundo estudo da Kaspersky, passaram de uma média diária de 402 mil em fevereiro para mais de 1,7 milhão em abril, crescimento de 333% em apenas dois meses
  - Esse crescimento exige que os profissionais de segurança tenham uma visão global de toda a infraestrutura de tecnologia da informação, e não apenas de criptografia

- Aspectos tecnológicos da segurança da informação
  - Os objetivos da segurança da informação (confidencialidade, integridade e disponibilidade) podem ser apoiados por diversas tecnologias, que variam conforme objetivo, tipo de dispositivo, camada de rede e perímetro de rede
  - Exemplo: um Gateway Antivírus e um Antivírus Endpoint se diferenciam pela posição na rede — o Endpoint fica instalado nos dispositivos finais dos usuários (notebooks, desktops, smartphones), enquanto o Gateway Antivírus fica na borda do perímetro, analisando o tráfego entre redes (normalmente entre a rede local e a internet)

- Firewall
  - Um dos dispositivos de segurança mais importantes de uma rede; atua como barreira de proteção entre a rede local e a internet, bloqueando ataques e contribuindo para confidencialidade, integridade e disponibilidade
  - Pode e deve ser usado tanto em redes de grandes e pequenas empresas quanto por usuários domésticos
  - Pode ser implementado em hardware ou em software (nesse caso, inclusive como uma máquina virtual)
  - Analisa o tráfego da rede e determina se as ações de envio e recebimento de dados são legítimas, definindo o que pode entrar, sair ou passar pela rede
  - Fica localizado entre os perímetros da rede, normalmente entre a rede local e a internet
  - Pode atuar na camada 3 e/ou na camada 7 do Modelo OSI

- Filtro de conteúdo web
  - Parte considerável dos ataques que uma organização sofre tem origem na navegação em sites não confiáveis
  - A melhor forma de prevenção é impedir que os usuários naveguem nesses tipos de sites; o filtro de conteúdo web realiza esse bloqueio
  - Assim como o firewall, fica localizado entre a rede local e a internet

- Intrusion Prevention System (IPS)
  - Ferramenta ativa capaz de detectar uma tentativa de intrusão no ambiente, analisar a relevância do evento e bloqueá-lo
  - Pode ser entendida como a junção de duas outras ferramentas: o Intrusion Detection System (IDS), que apenas detecta intrusões, e o firewall, que consegue bloqueá-las
  - Atua monitorando o tráfego de rede de servidores e demais equipamentos; ao identificar comportamento suspeito ou qualquer sinal de risco à integridade ou confidencialidade das informações, entra em ação
  - Não deve ser visto como substituto do firewall, mas como um complemento à segurança fornecida por ele
  - Fica localizado entre os perímetros da rede, tipicamente entre o firewall e o roteador que dá acesso à internet (todo o tráfego passa pelo IPS)

- Data Loss Prevention (DLP)
  - Ferramenta focada na prevenção de perda de dados, garantindo que dados confidenciais não sejam acessados por pessoas não autorizadas
  - Monitora a forma como os dados são acessados em uma rede: uma tentativa de acesso, cópia ou remoção gera um alerta
  - Provê mecanismos de proteção relacionados diretamente à confidencialidade das informações, apoiando também o alcance dos objetivos previstos na LGPD

- Pentest (teste de penetração)
  - Simulação de um ataque aos sistemas de uma organização, a fim de identificar vulnerabilidades
  - Permite avaliar a eficiência dos controles implementados, decidindo se são suficientes ou precisam evoluir
  - Exploit Database (exploit-db.com): projeto sem fins lucrativos da Offensive Security, que disponibiliza uma coleção de exploits para uso por testadores de penetração e pesquisadores de vulnerabilidade

- Firewall de Nova Geração (NGFW)
  - "Não se trata de uma nova tecnologia, mas sim do aprimoramento do firewall tradicional: um Firewall de Nova Geração realiza todas as tarefas de um firewall tradicional, mais uma série de novos recursos que o equipamento padrão não executa" (Moraes, 2015)
  - Serviços de segurança normalmente reunidos em um NGFW: firewall camada 3; firewall camada 7 (ou controle de aplicações); filtro de conteúdo web; filtro de Domain Name System (DNS); IPS; Gateway Antivírus; antispam
  - Vantagem: administrar diversas ferramentas de segurança em uma só interface, com integração perfeita entre elas
  - Principais fabricantes: Fortinet, Sonicwall, Palo Alto, Sophos

- Plano de continuidade do negócio
  - A segurança da informação possui três pilares (confidencialidade, integridade e disponibilidade); confidencialidade e integridade são fortemente apoiadas pela criptografia, enquanto a disponibilidade é a que mais se relaciona com o plano de continuidade de negócio
  - Medição da disponibilidade
    - A disponibilidade das informações está diretamente relacionada à disponibilidade dos componentes de hardware e software que provêm aquele serviço
    - A análise de riscos que compõe o plano de continuidade de negócios deve considerar a taxa de falhas dos componentes e o tempo médio de conserto
    - Tempo Médio entre Falhas (MTBF): tempo médio disponível para um sistema ou componente executar suas operações normais entre falhas
    - Tempo Médio de Conserto (MTTR): tempo médio necessário para consertar um componente com falha, incluindo detectar o problema, mobilizar a equipe de manutenção, diagnosticar, obter recursos, consertar, testar e retomar as operações normais
    - Disponibilidade da informação = tempo ativo do sistema / (tempo ativo do sistema + tempo inativo do sistema), ou, em termos de MTBF e MTTR: Disponibilidade = MTBF / (MTBF + MTTR)
  - Análise de impacto no negócio
    - Processo que produz um relatório detalhando os incidentes e seus impactos sobre as funções do negócio (em termos de tempo ou dinheiro), permitindo realimentar o plano de continuidade e implementar medidas preventivas
    - Passos recomendados: identificar os processos-chave críticos à operação; determinar os atributos do processo (aplicativos, bancos de dados, requisitos de hardware e software); avaliar os custos da falha para cada processo; calcular a máxima interrupção tolerável e definir o Tempo de Recuperação (RTO) e o Ponto de Recuperação (RPO) para cada processo; estabelecer os recursos mínimos requeridos; estabelecer as estratégias de recuperação e seu custo; otimizar a estratégia de backup e recuperação com base nas prioridades comerciais; analisar o estado atual de prontidão da Business Continuity (BC) e otimizar planejamentos futuros
  - Ponto único de falha
    - Analisar o datacenter em busca de sistemas suscetíveis a um ponto único de falha (que pode comprometer a disponibilidade do sistema ou serviço de TI inteiro) e implementar redundância ou outros mecanismos de tolerância a falhas
    - Um serviço com componentes redundantes só falha se todos os componentes da redundância falharem simultaneamente, o que é bem menos provável
    - Exemplos: configuração de RAID (Conjunto Redundante de Discos Independentes) contra falhas de disco; armazenamento (storage) em localidade remota; agregação de portas em switch para caminhos alternativos; implementação de clusters de servidores
  - Replicação de dados
    - Solução para recuperação de falhas: manter diversas cópias dos dados originais apoia o restabelecimento das operações quando os dados originais são perdidos
    - Formas de implementação: backup e recuperação de dados; replicação na mesma localidade; replicação em localidade remota; replicação baseada no host (servidor)
  - Ciclo de vida do plano de continuidade de negócios
    - Um plano de continuidade não deve ser estático: precisa de mecanismos de revisão, pois requisitos de negócio, de clientes e de disponibilidade mudam ao longo do tempo
    - Recomenda-se que possua cinco estágios: 1) estabelecer objetivos; 2) analisar; 3) projetar e desenvolver; 4) implementar; 5) treinar, testar, avaliar e realizar manutenção

- Boas práticas em segurança da informação
  - Basear-se em boas práticas é um ótimo ponto de partida para escolher quais controles implementar; aproveitar experiências positivas de outras organizações economiza tempo e evita incidentes
  - As normas ISO 27001 e ISO 27002 estão entre as melhores boas práticas disponíveis em segurança da informação
  - Não é viável definir um projeto de segurança da informação que atenda a todos os tipos de organizações ao mesmo tempo, pois cada uma tem particularidades (tipo de negócio, clientes, país de atuação) que definem quais boas práticas são aderentes a ela — ainda assim, alguns controles se aplicam à maioria das organizações

- Segurança física
  - "Vivemos em um mundo físico [...] Nossa tendência natural é considerar a segurança de computadores estritamente em um contexto digital [...] e nunca são acessados diretamente ou com ferramentas físicas, como um martelo, uma chave de fenda ou um frasco de nitrogênio líquido" (Goodrich, 2013)
  - Por causa dessa visão, a segurança física dos equipamentos é frequentemente negligenciada, o que impacta a segurança das informações armazenadas
  - Aspectos a observar: proteção de localização; detecção de intrusão física; ataques ao hardware; intromissão; ataques físicos a interfaces

- Segurança de sistemas operacionais
  - Segurança da memória e do sistema de arquivos: como os dados residem na memória e no sistema de arquivos, é fundamental proteger esses componentes
    - Aspectos a observar: segurança da memória virtual; autenticação baseada em senha; controle de acesso e permissões de arquivos avançadas; descritores de arquivos; elos simbólicos e atalhos
  - Segurança de aplicações
    - Muitos atacantes preferem explorar aplicações inseguras (nas quais não foram observadas questões de segurança durante o desenvolvimento) em vez de atacar diretamente o sistema operacional
    - Investir na qualificação dos desenvolvedores é fundamental, mas ferramentas de software para verificar o código-fonte também são um grande apoio e não devem ser descartadas

- Programas maliciosos (malwares)
  - O sucesso no combate a malwares depende, muitas vezes, de tratar as vulnerabilidades e fragilidades que eles exploram para obter acesso ao ambiente
  - Principais ações de prevenção: tratar vulnerabilidades específicas de sistemas operacionais e aplicativos por meio de atualizações; considerar a segurança da informação durante o desenvolvimento de aplicações; limitar o acesso de usuários a dispositivos móveis como pendrives; evitar que usuários executem programas com mais privilégios do que os necessários
  - Uso de um bom software antivírus é uma medida fundamental; diferenciais de uma solução de antivírus corporativo em relação a um antivírus doméstico:
    1. instalação automática, economizando tempo e garantindo que todos os computadores estejam protegidos
    2. proteção para diversos tipos de dispositivos (desktops, notebooks, smartphones, servidores)
    3. definição de políticas e tarefas de forma centralizada
    4. múltiplas políticas de proteção e tarefas, baseadas no tipo de endpoint
    5. controle de aplicações, liberando ou bloqueando programas por grupo de usuários
    6. economia de banda de internet, com banco de dados local de atualizações
    7. visão gerencial e relatórios
    8. suporte diferenciado

- Segurança de redes
  - Falsificação de Address Resolution Protocol (ARP): ataque de falsificação detalhado por Michael Goodrich (2013), no livro "Introdução à segurança de computadores"; conhecer seu funcionamento é fundamental para saber como se proteger
  - Falsificação de Protocolo de Internet (IP Spoofing): Goodrich mostra que é relativamente simples realizar um ataque de falsificação de IP
  - Espionagem de pacotes (packet sniffing): compromete diretamente a confidencialidade das informações, pois possibilita ao atacante espionar os dados que trafegam em uma rede
  - Sequestro de sessão do Protocolo de Controle de Transmissão (TCP session hijacking): ataque mais complexo que os anteriores
  - Ataques de negação de serviço (DoS): tipo de ataque cada vez mais popular, no qual um site ou serviço é tirado do ar propositalmente por atacantes
  - Ataques internos: muitas vezes as organizações se preocupam apenas com ataques externos e esquecem que eles também podem vir de dentro da própria organização

- Modelos de segurança adicionais (citados como temas complementares)
  - Política, modelos e confiança
  - Modelos de controle de acesso
  - Padrões de segurança e avaliação
  - Avaliação de vulnerabilidade de software
  - Administração e auditoria
  - Kerberos
  - Armazenamento seguro

- Tratamento de incidentes de segurança
  - "A segurança na internet e nas redes é muito importante para as empresas. A maioria delas procura se proteger criando regras e, então, implantando procedimentos, equipamentos e softwares para fazer com que sejam cumpridas. Mas, mesmo assim, algumas vezes ainda há problemas, como acessos não autorizados a sistemas, ou ataques capazes de parar algum serviço importante, e estes devem ser tratados. O trabalho de uma equipe de Tratamento de Incidentes de Segurança é como o trabalho dos brigadistas, que realizam ações preventivas para evitar que incêndios ocorram, mas, mesmo assim, estão sempre prontos para apagá-los" (NIC.br, 2014)
  - Quando incidentes acontecem, é necessário analisá-los, distribuir alertas e dar a devida resposta aos usuários do serviço, considerando os impactos que poderão acontecer e as contramedidas necessárias

- Referências para ampliar a pesquisa
  - Moraes, Alexandre Fernandes de. "Firewalls: Segurança no Controle de Acesso". São Paulo: Érica, 2015
  - Goodrich, Michael T.; Tamassia, Roberto. "Introdução à Segurança de Computadores". Porto Alegre: Bookman, 2013
  - Somasundaram, G.; Shrivastava, A.; EMC Education Services. "Armazenamento e gerenciamento de informações: como armazenar, gerenciar e proteger informações digitais". Porto Alegre: Bookman, 2011
  - ABNT. NBR ISO/IEC 27001 e NBR ISO/IEC 27002
  - NIC.br. "Tratamento de incidentes de segurança na Internet", 2014
  - Exploit Database (exploit-db.com), Cooperati (artigo sobre Cluster de Failover), Blog Locaweb (ferramentas de avaliação de qualidade de código)
