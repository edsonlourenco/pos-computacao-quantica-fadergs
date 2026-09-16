# Princípios da Segurança da Informação

- Introdução
  - Cada vez mais dados pessoais e corporativos são armazenados em aplicativos e trafegam pela internet, o que multiplica os riscos de incidentes de segurança
  - Esta unidade cobre os conceitos fundamentais de criptografia, segurança da comunicação e da informação, além de assinaturas digitais e autenticação de mensagens

- Segurança da informação: a tríade CID
  - Três elementos considerados os princípios fundamentais da segurança da informação (presentes no Preâmbulo da Convenção de Budapeste sobre Cibercrime e no Comitê Gestor da Internet no Brasil)
  - Confidencialidade
    - Relacionada ao segredo da informação: garantir que somente pessoas autorizadas tenham acesso aos dados
    - Engloba a prevenção da divulgação não autorizada
    - Ameaças: monitoramento de rede, engenharia social, roubo de senhas
    - Medidas de proteção: criptografia de dados, acompanhamento de tráfego de rede, controle de acesso rigoroso, classificação de dados, treinamento de pessoal
  - Integridade
    - Garantir que não ocorram modificações não autorizadas nos dados; somente usuários autorizados podem alterá-los
    - Exige que hardware, software e comunicação trabalhem de forma conjunta para mover e processar dados sem alteração não autorizada ou inesperada
    - Requer também proteger sistemas e rede contra interferências e contaminações externas
  - Disponibilidade
    - Capacidade de executar e disponibilizar os dados de forma adequada às necessidades da empresa; impacta diretamente a produtividade das operações
    - Ameaças: falhas de equipamentos e softwares, problemas ambientais (calor, umidade, eletricidade estática), ataques de negação de serviço (DoS)
    - Medida de proteção: realização de backups periódicos para recuperação rápida de sistemas e dados críticos

- Criptografia
  - Palavra de origem grega que significa "escrita oculta"
  - Método que transforma dados originais e legíveis (texto simples) em dados reversivelmente ilegíveis (texto cifrado)
  - Somente emissor e receptor conseguem compreender e processar o conteúdo correto, após o texto cifrado ser descriptografado
  - Permite transmissões de informações confidenciais por canais inseguros, sem risco de divulgação não autorizada
  - Um dos principais mecanismos de segurança da informação usados para garantir a confidencialidade dos dados
  - Cifra de César: um dos primeiros sistemas de criptografia, usado pelo imperador romano Júlio César por volta de 50 a.C.; substituía cada letra do alfabeto por outra três posições à frente

- Sistema criptográfico e chaves
  - Sistema criptográfico: capaz de criptografar e descriptografar dados; pode ser implementado em hardware ou software
  - Chave: segredo (longa sequência de bits) utilizado por um algoritmo matemático para codificar e decodificar uma informação
  - Keyspace: gama de valores possíveis para construir uma chave; quanto maior o keyspace, mais aleatórias as chaves e mais difícil para um invasor quebrar a criptografia
  - A segurança de um algoritmo criptográfico depende do tamanho da chave

- Criptografia simétrica
  - Emissor e receptor utilizam a mesma chave (senha) tanto para codificar quanto para decodificar a mensagem
  - Vantagem: fácil de usar e rápida, devido à sua simplicidade
  - Desvantagem: exige um canal de comunicação seguro para transmitir a chave; se uma das pontas vazar a chave, a confidencialidade é comprometida; dificuldade de gerenciar grandes quantidades de chaves
  - Algoritmos que utilizam chaves simétricas: 3DES, AES, Blowfish, RC4

- Criptografia assimétrica
  - Também conhecida como criptografia de chave pública
  - Utiliza duas chaves distintas: uma chave pública (pode ser divulgada) e uma chave privada (deve ser mantida em segredo)
  - Regra básica: a chave pública deve ser usada para codificar e a chave privada para decodificar
  - As duas chaves são relacionadas por um algoritmo matemático: uma mensagem cifrada com a chave pública só pode ser decifrada pela chave privada correspondente
  - Fornece um mecanismo de autenticação: se o emissor codificar com a chave privada, somente sua chave pública correspondente decodifica, provando a identidade do emissor — mas isso sozinho não garante confidencialidade, pois a chave pública é amplamente divulgada
  - Para obter autenticidade e confidencialidade ao mesmo tempo: o remetente cifra a mensagem com sua própria chave privada e, em seguida, cifra novamente com a chave pública do destinatário
  - Algoritmos que utilizam chaves assimétricas: RSA, Diffie-Hellman, DSS
  - RSA: algoritmo mais popular de criptografia assimétrica; tamanho de chave entre 512 e 2.048 bits; não é possível descobrir a chave privada a partir da chave pública, nem a partir do texto codificado

- Funções hash
  - Importante mecanismo para confirmar a integridade de dados
  - Método que, aplicado sobre uma informação, gera um resultado único e de tamanho fixo chamado hash (uma string, ex.: 3b6d2c43e10a067b1a98005d6b1c13c1)
  - Usos: verificação de integridade de arquivos armazenados, de backups, de arquivos baixados da internet (comparando o hash informado pelo site com o hash calculado após o download), geração de assinaturas digitais
  - Teoricamente é possível que informações diferentes gerem hashes iguais (colisão), mas a probabilidade é muito baixa
  - Algoritmos de hash são diferentes de algoritmos de criptografia (hash não é reversível)
  - MD5 (Message Digest 5): criado em 1992 por Ron Rivest (também criador do RSA); opera em blocos de 512 bits e gera um hash de 128 bits
  - SHA / SHS (Secure Hash Algorithm / Standard): desenvolvido pelo governo dos EUA; opera em blocos de 512 ou 1024 bits; SHA-1 gera hash de 160 bits, SHA-2 gera hashes de 224, 256, 384 ou 512 bits; o SHA-1 é considerado superior ao MD5

- Assinatura digital
  - Utiliza os métodos de criptografia assimétrica e hash em conjunto para garantir autenticidade e integridade
  - Corresponde, de forma objetiva, a um valor de hash criptografado com a chave privada do autor
  - Processo: calcula-se o hash do arquivo, criptografa-se esse hash com a chave privada do remetente (gerando a assinatura digital) e anexa-se a assinatura ao arquivo
  - Por meio dela, é possível comprovar que uma informação foi realmente gerada por quem diz ter feito isso, pois apenas o dono conhece a chave privada usada para gerar a assinatura
  - Uma mensagem pode: ser criptografada (confidencialidade); possuir um hash (integridade); ser assinada digitalmente (autenticação e integridade); ou ser criptografada e assinada ao mesmo tempo (autenticação, confidencialidade e integridade)

- Certificado digital
  - Resolve uma limitação dos algoritmos assimétricos: não é possível confirmar, por si só, que uma chave pública pertence realmente à pessoa que diz ser dona dela
  - É um certificado de chave pública: documento eletrônico que contém dados sobre a pessoa ou entidade que o utiliza, para comprovação mútua de autenticidade
  - Emitido e garantido por uma organização de confiança chamada Autoridade Certificadora
  - Permite que duas partes confiem uma na outra indiretamente, por meio da confiança que ambas depositam na Autoridade Certificadora

- Referências para ampliar a pesquisa
  - Machado, Felipe Nery R. "Segurança da informação: princípios e controle de ameaças". Rio de Janeiro: Érica, 2014
  - Basta, A.; Basta, N.; Brown, M. "Segurança de Computadores e Teste de Invasão", 2014
  - Artigos do blog da Certsign sobre certificado digital, chaves públicas/privadas e autoridades certificadoras
