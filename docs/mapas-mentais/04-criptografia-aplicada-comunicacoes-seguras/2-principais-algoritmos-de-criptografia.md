# Principais Algoritmos de Criptografia

- Introdução
  - Alan Turing, considerado o pai da computação, foi matemático e criptógrafo, conhecido por decifrar o código da máquina Enigma usada pelos alemães na Segunda Guerra Mundial
  - A criptografia evoluiu muito desde então; existe mais de um tipo de algoritmo de criptografia
  - Para garantir a confidencialidade das informações, usam-se algoritmos de chave simétrica ou de chave assimétrica, e dentro de cada tipo há diversas implementações
    - Chave simétrica: AES, DES, Idea, RC4, RC5, RC6, Blowfish
    - Chave assimétrica: RSA, Diffie-Hellman, DSS, El Gamal
  - A escolha do algoritmo depende do cenário de aplicação: tamanho dos arquivos, quantidade de usuários envolvidos, tipo de aplicação relacionada aos dados

- Cifradores de fluxo e de bloco
  - Ambos pertencem à família de algoritmos de chave simétrica (mesma chave para criptografar e descriptografar)
  - Cifradores de fluxo
    - Processam cada bit da mensagem separadamente (processamento bit a bit)
    - Também chamados de cifras de estado, pois a criptografia de cada dígito depende do estado atual do mecanismo de codificação
    - A partir de uma chave inicial, geram uma sequência de bits chamada keystream (chave contínua)
    - A encriptação ocorre pela combinação do texto plano com a keystream por meio de operações XOR (Ou-Exclusivo)
    - Geralmente mais rápidos que cifradores de bloco, por operarem unidades menores de dados
    - Recomendados quando o volume de dados é variável, como em uma conexão wi-fi
  - Cifradores de bloco
    - Operam em grupos de bits (blocos) de comprimento fixo, normalmente 64 ou 128 bits
    - Um texto sem formatação de N bits, junto com a chave secreta, gera um bloco de texto cifrado correspondente de N bits; a descriptografia ocorre da mesma forma, no sentido inverso
    - Mensagens mais longas que o tamanho do bloco são divididas em vários blocos, cada um cifrado com a mesma chave
    - Se a mensagem não for múltipla do tamanho do bloco, é inserido um enchimento chamado padding no último bloco; cabeçalhos no arquivo cifrado informam o algoritmo usado, o tamanho do bloco e o tamanho real do arquivo, para que o padding seja descartado na decriptação
    - Mais indicados para criptografar dados estáticos, cujo tamanho já é conhecido de antemão
    - Problema de segurança: como a mesma chave é usada, uma sequência repetida no texto original gera a mesma sequência repetida no texto cifrado, criando um padrão
    - Solução: uso de feedback modes, como Electronic Code Book (ECB), Cipher Block Chaining (CBC), Cipher Feedback Block (CFB) ou Output Feedback Block (OFB)
  - Duas das cifras de bloco mais populares: DES (Data Encryption Standard) e AES (Advanced Encryption Standard)
    - O uso do DES com chaves de 40 bits o torna bastante vulnerável à quebra; se escolhido, é preciso usar chaves mais longas

- O AES (Advanced Encryption Standard)
  - Criado a partir de uma competição lançada pelo NIST (National Institute of Standards and Technologies) em 1997, para suceder o DES
  - Pré-requisitos definidos pelo NIST: algoritmo publicamente definido; ser uma cifra simétrica de bloco; projetado para que o tamanho da chave possa aumentar; implementável tanto em hardware quanto em software; disponibilizado livremente ou de acordo com termos ANSI
  - Em 2001, o algoritmo vencedor foi definido: criado por Vincent Rijmen e Joan Daemen
  - Trabalha com um bloco fixo de 128 bits e chave de tamanho variável (128, 192 ou 256 bits), recebendo os nomes AES-128, AES-192 e AES-256
  - Em 2010, o AES-256 foi considerado a melhor opção para criptografia simétrica de propósito geral; suportado pelos principais sistemas operacionais (Windows, macOS, Linux)

- O criptossistema RSA
  - Sistema de criptografia que utiliza chaves assimétricas (uma pública e uma privada); o destinatário não precisa ter relacionamento prévio com o remetente para compartilhar chaves
  - RSA = Rivest, Shamir and Adleman, nome de seus criadores: Ron Rivest, Adi Shamir e Len Adleman, nos laboratórios do MIT, em 1977
  - Um dos algoritmos de chave assimétrica mais utilizados; foi patenteado nos EUA, mas pode ser usado sem licença em outros países
  - As chaves pública e privada são geradas a partir da multiplicação de dois números primos muito grandes (de 100 a 200 dígitos ou mais)
  - Encriptação e decriptação são feitas usando potenciação modular; a corretude dos algoritmos é baseada no Teorema de Euler e em propriedades de aritmética modular
  - A segurança do RSA está fortemente vinculada à dificuldade de fatorar o resultado dessa multiplicação; em 2010, foi recomendado o uso de chave de 2.048 bits
  - RSA garante confidencialidade e autenticidade, mas, devido à sua complexidade, é mais lento que algoritmos simétricos como o DES e não é recomendado para criptografar grandes blocos de dados
  - Uso comum: servidores web, onde o administrador cria uma chave privada (key) mantida em segredo no servidor e um arquivo CSR (Certificate Signing Request) enviado à Autoridade de Registro para emissão do certificado

- Siglas e termos explicados
  - XOR (Ou-Exclusivo): operação lógica usada para combinar o texto plano com a keystream nos cifradores de fluxo
  - Padding: enchimento adicionado a um bloco incompleto, para que a mensagem seja múltipla do tamanho do bloco do cifrador
  - ECB / CBC / CFB / OFB: diferentes feedback modes usados em cifradores de bloco para evitar padrões repetidos no texto cifrado
  - CSR (Certificate Signing Request): arquivo enviado por um servidor à Autoridade de Registro para solicitar um certificado digital baseado em RSA

- Referências para ampliar a pesquisa
  - Pinheiro, José Maurício S. "Criptografia com Chaves Simétricas", 2010 (on-line)
  - Medeiros, Higor. "Utilizando Criptografia Simétrica em Java" (devmedia.com.br)
  - Documentação da Microsoft: "Walkthrough: Creating a Cryptographic Application" (.NET)
