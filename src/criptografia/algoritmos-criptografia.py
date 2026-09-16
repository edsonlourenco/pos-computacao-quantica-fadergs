# %% [markdown]
# ## Algoritmos de criptografia na prática
#
# Este notebook demonstra os três mecanismos centrais discutidos nos mapas mentais do módulo
# "Criptografia Aplicada & Comunicações Seguras":
#
# - `hash` (SHA-256): verificação de integridade, sem chave e sem reversão.
# - Criptografia simétrica (AES): mesma chave para cifrar e decifrar.
# - Criptografia assimétrica (RSA): par de chaves pública/privada.
#
# - Mapas mentais relacionados:
#   [1-principios-da-seguranca-da-informacao.md](../../docs/mapas-mentais/04-criptografia-aplicada-comunicacoes-seguras/1-principios-da-seguranca-da-informacao.md)
#   [2-principais-algoritmos-de-criptografia.md](../../docs/mapas-mentais/04-criptografia-aplicada-comunicacoes-seguras/2-principais-algoritmos-de-criptografia.md)


# %% [markdown]
# ## Importando as bibliotecas


# %%
import hashlib
import os

from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


# %% [markdown]
# ## Hash (SHA-256)
#
# Um hash gera uma "impressão digital" de tamanho fixo para qualquer entrada. A mesma entrada
# sempre produz o mesmo hash, e a menor mudança na entrada muda o hash por completo — por isso é
# usado para verificar integridade (ex.: conferir se um arquivo baixado não foi alterado).


# %%
mensagem_original = b"Aula de Criptografia Aplicada e Comunicacoes Seguras"
mensagem_alterada = b"Aula de Criptografia Aplicada e Comunicacoes Segura!"

print('Hash original:', hashlib.sha256(mensagem_original).hexdigest())
print('Hash alterado:', hashlib.sha256(mensagem_alterada).hexdigest())


# %% [markdown]
# ## Criptografia simétrica (AES)
#
# A mesma chave cifra e decifra a mensagem. É rápida, mas exige um canal seguro para compartilhar
# a chave entre remetente e destinatário.


# %%
chave_simetrica = os.urandom(32)
iv = os.urandom(16)

texto_plano = b"Mensagem confidencial protegida por AES"

padder = padding.PKCS7(algorithms.AES.block_size).padder()
texto_com_padding = padder.update(texto_plano) + padder.finalize()

cifrador = Cipher(algorithms.AES(chave_simetrica), modes.CBC(iv))
encryptor = cifrador.encryptor()
texto_cifrado = encryptor.update(texto_com_padding) + encryptor.finalize()

print('Texto cifrado (AES):', texto_cifrado.hex())


# %%
decryptor = cifrador.decryptor()
texto_decifrado_com_padding = decryptor.update(texto_cifrado) + decryptor.finalize()

unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
texto_decifrado = unpadder.update(texto_decifrado_com_padding) + unpadder.finalize()

print('Texto decifrado (AES):', texto_decifrado.decode())


# %% [markdown]
# ## Criptografia assimétrica (RSA)
#
# Um par de chaves: a chave pública cifra, e somente a chave privada correspondente decifra.
# Não é preciso compartilhar nenhum segredo previamente com o destinatário.


# %%
chave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
chave_publica = chave_privada.public_key()

mensagem_rsa = b"Mensagem assimetrica via RSA"

texto_cifrado_rsa = chave_publica.encrypt(
    mensagem_rsa,
    asym_padding.OAEP(
        mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

print('Texto cifrado (RSA):', texto_cifrado_rsa.hex())


# %%
texto_decifrado_rsa = chave_privada.decrypt(
    texto_cifrado_rsa,
    asym_padding.OAEP(
        mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

print('Texto decifrado (RSA):', texto_decifrado_rsa.decode())
