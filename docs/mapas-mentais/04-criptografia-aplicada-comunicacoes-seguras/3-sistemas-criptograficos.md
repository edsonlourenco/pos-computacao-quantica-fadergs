# Sistemas Criptográficos

- Introdução
  - Unidade dedicada a um criptossistema de chaves assimétricas mais performático (curvas elípticas), aos protocolos usados para garantir a confidencialidade de informações em trânsito e a uma perspectiva de futuro com a criptografia quântica

- Criptossistema de curvas elípticas (ECC)
  - Utiliza a matemática das curvas elípticas para promover criptografia de chave pública
  - Essas funções matemáticas são simples de calcular, mas muito difíceis de reverter — princípio que fundamenta a segurança dos criptossistemas assimétricos: dificuldade de resolver problemas matemáticos
  - Na década de 1980, Neal Koblitz e Victor Miller concluíram que a rica estrutura matemática das curvas elípticas poderia ser usada como base para criptossistemas assimétricos
  - A segurança decorre da inviabilidade de calcular o logaritmo discreto de um elemento de curva elíptica aleatório em relação a um ponto de base — o problema do logaritmo discreto de curva elíptica (ECDLP)
  - ECDSA (Elliptic Curve Digital Signature Algorithm): algoritmo de assinatura digital de curva elíptica, amplamente usado para criptografia de chave pública
    - Vantagem sobre o RSA: oferece força criptográfica equivalente com tamanhos de chave muito menores (ex.: 256 bits do ECDSA equivalem a 3072 bits do RSA)
    - Algoritmos baseados em curvas elípticas oferecem desempenho semelhante ao de algoritmos de criptografia simétrica, conhecidamente mais rápidos
    - Menor esforço computacional: criptografia mais forte com menos capacidade de computação e largura de banda — vantagem relevante para dispositivos móveis e Internet das Coisas (IoT)
    - Recomendado atualmente pelo Instituto Nacional de Padrões e Tecnologia dos EUA (NIST) e aprovado pela Agência de Segurança Nacional dos EUA (NSA)

- Esquemas de estabelecimento de chaves
  - A chave de um sistema criptográfico é fundamental para a proteção dos dados
  - Em criptografia de curvas elípticas, a segurança é garantida pelo problema do logaritmo discreto para curvas elípticas — DLP (Discrete Logarithm Problem)
  - Esse problema matemático é considerado impossível de resolver computacionalmente, o que é ideal para garantir a segurança dos dados criptografados, já que a chave não pode ser quebrada
  - Definição matemática do DLP: dados os elementos R e Q pertencentes a um grupo, e um primo P, encontrar um número k tal que R = Qᵏ mod P; k é chamado de logaritmo discreto de R na base Q

- Protocolos seguros de comunicação e protocolos criptográficos
  - O uso de determinados protocolos garante autenticação de mensagens e privacidade nas camadas de rede, transporte e aplicação
  - Uma arquitetura de segurança aplicada a múltiplas camadas fortalece a proteção contra ataques maliciosos

- IPSec (IP Security)
  - Desenvolvido pelo IETF (Internet Engineering Task Force); atua na camada de rede e oferece recursos de segurança a um pacote
  - Pode atuar em dois modos
    - Modo de transporte: protege as informações entregues da camada de transporte para a camada de rede, mas não protege o cabeçalho IP; geralmente usado em comunicações host a host — o host emissor autentica e/ou criptografa o payload, e o host receptor verifica a autenticação e/ou descriptografa
    - Modo túnel: protege todo o pacote, inclusive o cabeçalho IP original; gera um novo cabeçalho IP; geralmente usado entre dois roteadores, como em uma VPN Site-to-Site; o pacote original trafega inteiro dentro de um túnel protegido
  - Protocolos de segurança do IPSec: AH e ESP
    - AH (Authentication Header — cabeçalho de autenticação)
      - Autentica o host de origem e garante a integridade do payload transportado no pacote IP
      - Utiliza uma função hash e uma chave simétrica para criar um resumo de mensagem, inserido no cabeçalho de autenticação
      - O valor original do campo de protocolo do cabeçalho IP é substituído por 51 para identificar que o datagrama transporta um cabeçalho de autenticação
      - Fornece autenticação de fonte e integridade de dados, mas não privacidade (confidencialidade)
    - ESP (Encapsulating Security Payload — payload de segurança de encapsulamento)
      - Definido posteriormente ao AH, pois este não fornece privacidade; oferece autenticação de fonte, integridade e confidencialidade
      - Adiciona um cabeçalho e um trailer ao payload, criptografa o payload e o trailer, e modifica o campo de protocolo do cabeçalho IP para 50
  - Quadro comparativo de serviços do IPSec: controle de acesso, autenticação de mensagens e de entidades, e proteção contra ataque de reprodução são oferecidos tanto por AH quanto por ESP; confidencialidade é oferecida apenas pelo ESP
  - IPSec é totalmente transparente para o usuário final, pois é estabelecido entre equipamentos que conectam toda a rede (firewall, roteador), sem necessidade de configuração nos dispositivos finais
  - Suportado tanto por IPv4 quanto por IPv6

- SSL (Secure Sockets Layer)
  - Conexão SSL: elemento de transporte que provê um tipo de serviço adequado; é a relação ponto a ponto entre cada dispositivo se comunicando em uma rede; toda conexão é associada a uma única sessão
  - Sessão SSL: associação entre um cliente e um servidor, onde são definidos os parâmetros criptográficos de segurança que podem ser compartilhados entre várias conexões, evitando renegociar novos parâmetros a cada conexão; as sessões são criadas pelo Protocolo de Apresentação (Handshake Protocol)
  - HTTPS: sigla para HTTP sobre SSL; combinação do protocolo de aplicação HTTP com o SSL, para prover conexão segura entre servidor web e navegador web (o servidor precisa suportar comunicação HTTPS)
  - Quando se utiliza HTTPS, são criptografados: a URL da página solicitada, o conteúdo da página, o conteúdo dos formulários enviados, os cookies trocados entre navegador e servidor, e o conteúdo do cabeçalho HTTP

- PGP (Pretty Good Privacy)
  - Protocolo de segurança usado principalmente para sistemas de e-mail; inventado por Philip Zimmermann para fornecer privacidade, integridade e autenticação em e-mails; utiliza criptografia assimétrica
  - Surgiu como produto gratuito, mas deixou de ser em 2004; o GnuPG (GPG) surgiu como alternativa livre e compatível com o PGP (é possível cifrar, decifrar, assinar e verificar assinaturas entre os dois programas)
  - Teia de confiança (web-of-trust): conceito usado pelo PGP para certificar que uma determinada chave pertence a um usuário, site ou empresa
    - A confiança é estabelecida através de uma rede: se A confia em B e B confia em C, então A confia em C
    - A rede é construída por meio de relações pessoais entre indivíduos, constatação da identidade da chave e assinatura da chave pública de um usuário pelo outro
    - Após a verificação da identidade do par de chaves, a chave é publicada em um servidor de chaves, para que qualquer pessoa possa obtê-la facilmente

- VPN (Virtual Private Network)
  - Tipos de VPN
    - Site-to-Site (ou Gateway-to-Gateway): estabelecida entre dois equipamentos, normalmente roteadores ou firewalls; geralmente utiliza IPSec, criando um túnel seguro para proteger toda a informação trafegada; trata de conexões remotas entre redes inteiras
    - Client-to-Site (ou Remote Access): caracterizada por conexões pontuais de usuários remotos à rede; geralmente utiliza SSL-VPN
  - SSL VPN: permite criar VPN sem utilizar IPSec; geralmente disponibilizada como um portal web, através de um firewall, onde o usuário se autentica; um túnel é criado sobre a conexão SSL e os protocolos da pilha TCP/IP são encapsulados nesse túnel; os recursos remotos são acessados pelo navegador web que estabeleceu a VPN

- Criptografia quântica
  - Os sistemas de criptografia estudados até então baseiam-se em problemas matemáticos difíceis de resolver, mas a computação quântica pode torná-los obsoletos
  - A criptografia quântica engloba apenas a troca segura de chaves; as trocas de mensagens continuam utilizando métodos clássicos — por isso é mais corretamente chamada de Distribuição Quântica de Chaves ou QKD (Quantum Key Distribution)
  - Utiliza fótons para que duas pessoas definam uma chave secreta que não pode ser quebrada por um algoritmo, pois não é gerada matematicamente — mesmo usando um canal público e inseguro para a comunicação
  - Em 1984, Bennett e Brassard propuseram o primeiro protocolo de criptografia quântica, chamado BB84
  - Característica central da teoria quântica: o simples fato de observar um objeto pode mudar seu estado; aplicada à comunicação quântica, permite detectar sempre que um atacante interfere na transmissão
  - Na computação quântica, os bits (qubits) podem assumir os valores 0 e 1 simultaneamente; um registrador de 8 qubits pode guardar todos os números de 0 a 255 ao mesmo tempo, ao contrário de um computador tradicional
  - Dois algoritmos quânticos populares
    - Shor: realiza fatoração de números primos em tempo polinomial
    - Grover: realiza pesquisa em lista não ordenada em tempo Raiz(n)
  - Comparativo de tempo para quebrar uma chave por fatoração: um número de 2048 bits levaria cerca de 100 mil bilhões de anos com um algoritmo clássico, contra cerca de 36 minutos usando o algoritmo de Shor
  - Nos sistemas atuais de criptografia, a segurança é baseada na chave: quanto mais complexa, mais forte a criptografia, mas a chave também se torna o fator crítico, pois deve ser mantida em segredo — se um atacante tiver acesso a ela, os dados podem ser facilmente descriptografados
  - Solução proposta pela criptografia quântica: o protocolo RPS, feito para distribuir chaves e pacotes de dados usando elementos quânticos; é capaz de detectar erros de transmissão (ex.: leitura não autorizada por um atacante), invalidar a chave usada e reiniciar o processo até que uma chave válida seja enviada com segurança

- Referências para ampliar a pesquisa
  - Russell, John. Artigo sobre criptossistemas de curvas elípticas e ECDLP, 2019 (on-line)
  - Naziridis, Nick. "Comparando ECDSA vs RSA" (ssl.com)
  - Forouzan, Behrouz A. "Comunicação de Dados e Redes de Computadores". 4. ed. Porto Alegre: AMGH, 2008
  - Documentação sobre SSL/TLS: Apache ("SSL/TLS Strong Encryption: How-To"), Nginx ("Configuring HTTPS servers"), Microsoft IIS ("How to Set Up SSL on IIS 7")
  - EFF Surveillance Self-Defense: "How to: Use PGP for Windows" (ssd.eff.org)
  - Netgate pfSense: "IPsec Site-to-Site VPN Example with Pre-Shared Keys"
  - Barnabé et al. Comparativo entre algoritmo clássico e algoritmo de Shor, 2005
