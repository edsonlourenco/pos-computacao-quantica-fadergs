# %% [markdown]
# ## Circuito GHZ com 3 qubits (Qiskit)
#
# Este notebook cria um estado GHZ (Greenberger-Horne-Zeilinger) de 3 qubits, um exemplo clássico de emaranhamento múltiplo. O circuito é simulado localmente com o `BasicSimulator`, sem depender de um provedor em nuvem.
#
# - `H` no qubit 0 cria superposição.
# - `CX(0,1)` e `CX(1,2)` propagam o emaranhamento para os demais qubits.
# - A medição projeta o estado em `000` ou `111`, com probabilidade aproximada de 50% cada.


# %% [markdown]
# ## Importando as bibliotecas


# %%
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit.providers.basic_provider import BasicSimulator


# %% [markdown]
# ## Criando o circuito GHZ de 3 qubits


# %%
circuit = QuantumCircuit(3, 3)
circuit.name = 'Qiskit Sample - 3-qubit GHZ circuit'
circuit.h(0)
circuit.cx(0, 1)
circuit.cx(1, 2)
circuit.measure([0, 1, 2], [0, 1, 2])


# %% [markdown]
# ## Visualizando o circuito


# %%
circuit.draw('mpl')


# %% [markdown]
# ## Executando no simulador local


# %%
backend = BasicSimulator()
job = backend.run(circuit)
result = job.result()
counts = result.get_counts()

print('Counts:', counts)


# %% [markdown]
# ## Histograma dos resultados


# %%
plot_histogram(counts)
