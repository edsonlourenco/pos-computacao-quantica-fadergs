# %% [markdown]
# ## Superposição e emaranhamento quântico
#
# Este notebook demonstra na prática os dois conceitos centrais da unidade "Superposição e Emaranhamento Quântico":
#
# - `porta Hadamard`: coloca um único qubit em superposição de `|0⟩` e `|1⟩`, com 50% de chance de cada resultado.
# - `porta CNOT` aplicada após a Hadamard: cria um estado de Bell, o exemplo canônico de emaranhamento entre 2 qubits.
#
# - Mapa mental relacionado: [3-superposicao-e-emaranhamento-quantico.md](../../../../docs/mapas-mentais/03-fisica-para-computacao-quantica-qubit/3-superposicao-e-emaranhamento-quantico.md)


# %% [markdown]
# ## Importando as bibliotecas


# %%
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit.providers.basic_provider import BasicSimulator

backend = BasicSimulator()


# %% [markdown]
# ## Superposição de um único qubit
#
# Um qubit inicia sempre em `|0⟩`. Aplicar a porta Hadamard (`h`) o coloca em superposição: `(|0⟩ + |1⟩) / √2`.
# Medindo muitas vezes, espera-se aproximadamente 50% de `0` e 50% de `1`.


# %%
superposicao = QuantumCircuit(1, 1)
superposicao.h(0)
superposicao.measure(0, 0)
superposicao.draw('mpl')


# %%
job = backend.run(superposicao, shots=1000)
counts_superposicao = job.result().get_counts()
print('Counts (superposição):', counts_superposicao)
plot_histogram(counts_superposicao)


# %% [markdown]
# ## Emaranhamento: estado de Bell
#
# Aplicando uma porta `CNOT` (qubit 0 como controle, qubit 1 como alvo) depois da Hadamard, os dois qubits deixam
# de ser independentes: o estado resultante é `(|00⟩ + |11⟩) / √2`, o estado de Bell.
#
# Assim como no exemplo das moedas emaranhadas do mapa mental, só é possível medir `00` ou `11`: nunca `01` ou `10`.


# %%
bell = QuantumCircuit(2, 2)
bell.h(0)
bell.cx(0, 1)
bell.measure([0, 1], [0, 1])
bell.draw('mpl')


# %%
job = backend.run(bell, shots=1000)
counts_bell = job.result().get_counts()
print('Counts (estado de Bell):', counts_bell)
plot_histogram(counts_bell)

# %%
