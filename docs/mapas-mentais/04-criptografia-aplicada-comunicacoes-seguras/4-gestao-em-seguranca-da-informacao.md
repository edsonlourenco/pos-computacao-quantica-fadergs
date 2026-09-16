# Gestão em Segurança da Informação

- Introdução
  - "Não se gerencia o que não se mede, não se mede o que não se define, não se define o que não se entende e não há sucesso no que não se gerência" (William Edwards Deming)
  - Implementar controles e tecnologias que aumentam a segurança de um ambiente de TI é fundamental, mas não suficiente: é indispensável avaliar esses controles para comprovar sua efetividade
  - Kevin Mitnick, hacker mundialmente conhecido, afirmava que nunca estaremos 100% protegidos; o que se pode fazer é se proteger o tanto quanto possível e mitigar riscos até um grau aceitável — o risco é presença constante

- Análise de riscos
  - Risco: combinação da possibilidade de um determinado evento ocorrer e de suas consequências na organização
  - Evento: relacionamento que ocorre entre ameaças, vulnerabilidades e consequências
  - As consequências dos riscos impactam a tríade CID (Confidencialidade, Integridade e Disponibilidade) dos ativos
  - NBR ISO/IEC 27005 (ABNT, 2019): norma específica para gestão de riscos de segurança da informação
    - Processo de avaliação de riscos: estabelecimento do contexto → identificação de riscos → análise de riscos → avaliação de riscos → tratamento de riscos, com atividades contínuas de comunicação e consulta, e de monitoramento e análise crítica
    - Objetivos que não podem ficar de fora de uma análise de riscos: identificar a informação e seu valor; determinar as vulnerabilidades e ameaças; determinar quais ameaças podem se tornar um risco; determinar o custo/benefício do tratamento de um risco
    - O custo das medidas de segurança para tratar riscos deve ser comparado com as perdas potenciais causadas pela efetivação do risco
    - Formas de tratamento de risco: mitigar, transferir, aceitar ou evitar
  - Outros frameworks e normas que também apoiam a gestão de riscos de segurança da informação: COBIT, ISO/IEC 27002, ISO 31000, PMBOK, RISK IT
  - Matriz de Risco: ferramenta visual para apresentar o resultado de uma análise de riscos, permitindo identificar quais riscos devem receber mais atenção
    - As linhas representam a probabilidade de o risco ocorrer; as colunas representam os impactos do risco (prejuízos ou danos causados)
    - Recomenda-se medir tanto a probabilidade quanto o impacto em níveis: muito baixo, baixo, moderado, alto e muito alto
    - Um risco pode ter duas faces: ameaça (algo ruim, gera prejuízo caso aconteça) e oportunidade (um "risco bom", possibilidade de a empresa melhorar seus resultados)

- Política Nacional de Segurança das Informações
  - Instituída pelo Decreto nº 3.505, editado pelo Presidente da República em 13 de junho de 2000
  - Reconhece que a administração pública processa informações sensíveis que requerem proteção contra intrusão e modificações desautorizadas
  - Suas diretrizes mencionam o uso e desenvolvimento de equipamentos dotados de recursos criptográficos (art. 4º, inciso VII: padrões, níveis e tipos de métodos criptográficos para garantir confidencialidade e integridade) e estabelecem como meta a implementação de uma infraestrutura de chaves públicas para uso por todos os órgãos públicos (inciso XIV)

- Instituto Nacional de Tecnologia da Informação (ITI)
  - Autarquia federal vinculada à Casa Civil da Presidência da República
  - É a Autoridade Certificadora Raiz (AC Raiz) da Infraestrutura de Chaves Públicas Brasileira (ICP-Brasil), ocupando a posição de primeira autoridade da cadeia de certificação
  - Principais competências: coordenar o funcionamento da ICP-Brasil; estabelecer política, critérios e normas técnicas para credenciamento de ACs, ARs e demais prestadores de serviço; estabelecer a política de certificação e regras operacionais da AC-Raiz; homologar, auditar e fiscalizar a AC-Raiz e seus prestadores de serviço; aprovar políticas de certificados e credenciar ACs e ARs; negociar acordos de certificação bilateral e cooperação internacional; atualizar e revisar os procedimentos da ICP-Brasil
  - ICP-Brasil: criada pela Medida Provisória nº 2.200-2, de 24 de agosto de 2001; possui 25 ACs de 1º Nível, 123 ACs de 2º Nível e 2.030 ARs (Autoridades de Registro)

- Legislações com maior impacto na atuação do profissional de segurança da informação
  - Código de Defesa do Consumidor (CDC)
  - Marco Civil da Internet
  - Lei Geral de Proteção de Dados (LGPD): traz transformações relevantes para todos os brasileiros; muitas empresas ainda coletam dados sem utilizar técnicas adequadas de segurança da informação

- Outras normas e boas práticas de segurança da informação
  - PCI (Payment Card Industry): padrão para o manuseio de dados de pagamentos relacionados a cartões de crédito
  - SOX (Sarbanes-Oxley): lei criada após problemas nas contabilidades de empresas norte-americanas
  - Basel III Accord: fornece orientação e visa tornar mais eficientes os esforços de gerenciamento de riscos
  - ITIL (Information Technology Infrastructure Library): modelo de referência para gerenciamento de serviços de TI, com itens específicos sobre segurança da informação
  - COBIT (Control Objectives for Information and Related Technologies): framework para governança de TI

- Auditoria de sistemas
  - "A auditoria do ambiente de tecnologia da informação tem por objetivo revisar e avaliar os recursos comuns utilizados no processamento dos diversos sistemas de informação da empresa" (Gil, 2018)
  - Em auditorias de TI, os controles internos mais observados relacionam-se à segurança da informação e ao desempenho
  - Apoiada pela NBR ISO/IEC 27002 (código de prática para a gestão da segurança da informação), que estabelece diretrizes e princípios para iniciar, implementar, manter e melhorar a gestão de segurança da informação; contém 14 seções, 35 objetivos de controle e 114 controles
    - As 14 seções: 1) Políticas de segurança da informação; 2) Organização da segurança da informação; 3) Segurança em recursos humanos; 4) Gestão de ativos; 5) Controle de acesso; 6) Criptografia; 7) Segurança física e do ambiente; 8) Segurança nas operações; 9) Segurança nas comunicações; 10) Aquisição, desenvolvimento e manutenção de sistemas; 11) Relacionamento na cadeia de suprimento; 12) Gestão de incidentes de segurança da informação; 13) Aspectos da segurança da informação na gestão da continuidade do negócio; 14) Conformidade
  - É a única norma de gestão de segurança da informação que possui certificação para profissionais (prova EXIN ISO 27002)
  - Etapas recomendadas para execução de uma auditoria (Gil, 2018): planejamento do projeto de auditoria do ambiente de TI; levantamento e caracterização do ambiente; inventário, eleição e seleção dos pontos de controle para auditoria; revisão e avaliação dos pontos de controle eleitos; elaboração do relatório de avaliação de controle interno e de auditoria

- Autenticação e controle de acesso
  - A criação de regras de acesso a redes, sistemas e bancos de dados é fundamental para garantir os princípios da segurança da informação
  - "Como controle de acesso entende-se o gerenciamento da visualização de informações e da utilização dos recursos digitais de uma rede de computadores, considerando as propriedades da segurança da informação: confidencialidade, integridade e disponibilidade" (Machado, 2014)
  - Um correto controle de acesso evita visualização não autorizada (protege confidencialidade), impede modificações não autorizadas (protege integridade) e garante que os dados estejam sempre aptos para uso por usuários autorizados (garante disponibilidade)
  - Três fases do controle de acesso, que se complementam: identificação, autenticação e autorização
    - Identificação: identificar o usuário (pode ser uma credencial como nome de usuário, uma assinatura digital ou um atributo anatômico como impressão digital)
    - Autenticação: verificar a autenticidade do usuário, fornecendo uma segunda peça de informação (algo que ele saiba, possua ou seja) que é comparada com o que está armazenado no sistema
    - Autorização: o sistema verifica se o usuário possui direitos e privilégios para realizar as ações requeridas
  - É fundamental usar identificação única por usuário (nunca compartilhar contas de acesso), para permitir rastrear quem realizou cada ação
  - Controles de acesso lógicos: softwares utilizados para identificar, autenticar, autorizar e registrar as atividades dos usuários

- Mecanismos de autenticação
  - Senhas
    - Mecanismo de autenticação mais comum; sequência de caracteres protegida
    - As 20 senhas mais "hackeadas" do mundo em 2019 (Forbes) incluíam "123456" (23,2 milhões de ocorrências), "123456789", "qwerty" e "password", evidenciando o quanto usuários negligenciam a força de suas senhas
    - Boa prática: implementar requisitos de complexidade (número mínimo de caracteres, exigência de números, maiúsculas, minúsculas e caracteres especiais — ex.: recurso nativo do Microsoft Active Directory) e usar geradores de senha, sem anotá-las
    - A troca periódica obrigatória de senhas, prática antes considerada efetiva, foi contestada pela própria Microsoft, que a classifica como uma prática obsoleta
  - Token: dispositivo de hardware gerador de senhas, separado do computador do usuário; apresenta em intervalos de tempo uma lista de caracteres diferente, que deve ser inserida na aplicação (ex.: RSA SecurID)
  - Hash: usado para comparar a integridade de dados; dados do usuário (nome, matrícula, departamento) podem ser criptografados em uma função hash, criando uma assinatura digital
  - Biometria: verifica um atributo pessoal único do usuário; considerado um método de verificação muito efetivo, pois, ao contrário de senhas, não pode ser perdido, observado ou copiado com a mesma facilidade
    - Scanner de dedo: extrai características específicas da impressão digital, ocupando pouco espaço em disco e permitindo pesquisas rápidas
    - Scanner de retina: projeta um feixe de luz dentro do olho e compara o padrão de vasos sanguíneos da retina a um arquivo de referência
    - Scanner de íris: analisa o padrão único da íris (fendas, cores, anel, coroas, sulcos)
    - Outras tecnologias: geometria da mão, impressão de voz, escaneamento facial, topologia da mão

- Autenticação de dois fatores
  - Recurso que acrescenta uma camada adicional de segurança ao login de contas, exigindo duas formas de autenticação (em geral, a senha mais um segundo fator, como SMS ou código de e-mail)
  - Teoria geral: para efetuar login, o indivíduo deve saber e possuir algo a mais (Donohue, 2014)
  - Excelente barreira contra acessos não autorizados: mesmo que a senha seja descoberta, o atacante precisaria também descobrir e acessar o segundo fator, geralmente exigindo acesso físico ao dispositivo que o recebe
  - Benefício adicional: alerta o usuário quando alguém tenta acessar sua conta com a senha correta, já que ele recebe um código de autenticação que não solicitou

- Autenticação centralizada
  - Implementar controle de acesso individualmente em cada sistema gera dificuldade de gerenciamento das credenciais, tanto para a equipe de TI quanto para o usuário
  - Solução: autenticação centralizada, em que a organização armazena em um único servidor todas as credenciais de acesso, e os demais sistemas consultam esse servidor para autorizar os usuários
  - Cria um ponto único de gestão de usuários e uma credencial de acesso única para diversos sistemas diferentes
  - Pode ser implementada por meio de um serviço de diretório, como o Microsoft Active Directory

- Outras boas práticas de controle de acesso
  - Limite de tentativas de login: tentativas sucessivas de login podem ser evidência de um ataque de força bruta; bloquear a conta do usuário ao atingir o limite evita um incidente de segurança
  - Monitoramento de controle de acesso: método fundamental para controlar quem tenta acessar recursos em uma rede; funciona como mecanismo de detecção e prevenção, evidenciando, por exemplo, acesso a sistemas sem autorização ou acessos fora do horário de trabalho do usuário

- Referências para ampliar a pesquisa
  - ABNT. NBR ISO/IEC 27005:2019 — Tecnologia da informação — Técnicas de segurança — Gestão de riscos de segurança da informação
  - ABNT. NBR ISO/IEC 27002:2013 — Código de prática para a gestão da segurança da informação
  - Gil, Antônio de Loureiro. "Auditoria do negócio com TI: gestão e operação". 1. ed. São Paulo: Saraiva Educação, 2018
  - Machado, Felipe Nery R. "Segurança da informação: princípios e controle de ameaças". Rio de Janeiro: Érica, 2014
  - Gomes, Heloisa dos S. "Lei Geral de Proteção de Dados (LGPD): uma análise dos impactos da lei na cultura e tratamento de dados no Brasil". Trabalho de Estudo de Caso, Universidade do Sul de Santa Catarina, 2019
  - O'Flaherty (Forbes): lista das 20 senhas mais hackeadas em 2019
  - Site institucional do ITI (gov.br/iti) e da estrutura da ICP-Brasil (estrutura.iti.gov.br)
