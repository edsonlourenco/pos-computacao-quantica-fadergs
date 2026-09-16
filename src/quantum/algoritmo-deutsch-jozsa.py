# %% [markdown]
# ## Algoritmo de Deutsch
#
# Este notebook implementa a versão original (de 1 qubit) do algoritmo de Deutsch, discutido no mapa mental
# "Computadores Quânticos e Algoritmos Quânticos": dada uma função `f(x)` de 1 bit, implementada como uma caixa
# preta (oráculo quântico), o algoritmo descobre com uma única execução se `f` é **constante**
# (`f(0) = f(1)`) ou **balanceada** (`f(0) ≠ f(1)`) — algo que um computador clássico só consegue garantir
# testando as duas entradas separadamente.
#
# - Mapa mental relacionado: [5-computadores-quanticos-e-algoritmos-quanticos.md](../../../../docs/mapas-mentais/03-fisica-para-computacao-quantica-qubit/5-computadores-quanticos-e-algoritmos-quanticos.md)


# %% [markdown]
# ## Importando as bibliotecas


# %%
from qiskit import QuantumCircuit
from qiskit.providers.basic_provider import BasicSimulator

backend = BasicSimulator()


# %% [markdown]
# ## Os 4 oráculos possíveis para uma função de 1 bit
#
# - `f(x) = 0`: constante
# - `f(x) = 1`: constante
# - `f(x) = x`: balanceada
# - `f(x) = NOT x`: balanceada
#
# Cada oráculo é um circuito de 2 qubits (`q0` = entrada `x`, `q1` = ancilla) que aplica `f(x)` como uma
# inversão de fase sobre a ancilla, sem nunca revelar `x` diretamente.


# %%
def oraculo_constante_0():
    return QuantumCircuit(2, name='f(x)=0')


def oraculo_constante_1():
    qc = QuantumCircuit(2, name='f(x)=1')
    qc.x(1)
    return qc


def oraculo_balanceado_identidade():
    qc = QuantumCircuit(2, name='f(x)=x')
    qc.cx(0, 1)
    return qc


def oraculo_balanceado_negacao():
    qc = QuantumCircuit(2, name='f(x)=NOT x')
    qc.cx(0, 1)
    qc.x(1)
    return qc


oraculos = [
    oraculo_constante_0(),
    oraculo_constante_1(),
    oraculo_balanceado_identidade(),
    oraculo_balanceado_negacao(),
]


# %% [markdown]
# ## Montando o algoritmo de Deutsch
#
# 1. A ancilla (`q1`) começa em `|1⟩` e ambos os qubits recebem uma porta Hadamard, colocando a entrada em
#    superposição de `0` e `1` ao mesmo tempo.
# 2. O oráculo é aplicado, imprimindo `f(x)` como uma fase sobre a entrada (interferência).
# 3. Uma nova Hadamard na entrada transforma essa fase em um resultado mensurável.
# 4. Medir `q0`: `0` indica função constante, `1` indica função balanceada.


# %%
def circuito_deutsch(oraculo):
    qc = QuantumCircuit(2, 1)
    qc.x(1)
    qc.h(0)
    qc.h(1)
    qc.compose(oraculo, inplace=True)
    qc.h(0)
    qc.measure(0, 0)
    return qc


circuito_deutsch(oraculos[2]).draw('mpl')


# %% [markdown]
# ## Executando os 4 casos
#
# Cada oráculo é testado com uma única execução (`shots=1`), como o algoritmo propõe: uma única medição já
# basta para classificar a função.


# %%
for oraculo in oraculos:
    qc = circuito_deutsch(oraculo)
    job = backend.run(qc, shots=1)
    resultado = list(job.result().get_counts().keys())[0]
    classificacao = 'balanceada' if resultado == '1' else 'constante'
    print(f'{oraculo.name:12s} -> medição = {resultado} -> {classificacao}')

# %%
