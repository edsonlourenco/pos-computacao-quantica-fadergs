# %% [markdown]
# # Aplicação prática: Aprendizado por Reforço, Redes Neurais e Comitês
# Este notebook resume e integra os conceitos do material em exemplos práticos de Python para estudos.
# Ele inclui: Q-learning tabular, redes neurais com MLP e comitê de classificadores.
# - Mapa mental do tema: [4-aprendizado-por-reforco-redes-neurais-e-comites.md](../../../docs/mapas-mentais/01-aprendizado-de-maquina-overview/4-aprendizado-por-reforco-redes-neurais-e-comites.md)
# 


# %%
# Dependências principais
# !pip install --quiet numpy matplotlib scikit-learn


# %%
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

np.random.seed(42)


# %% [markdown]
# ## Seção 1: Aprendizado por Reforço com Q-learning
# Aqui construímos um ambiente MDP simples e treinamos um agente com Q-learning.


# %%
class GridWorld:
    def __init__(self, size=4):
        self.size = size
        self.n_states = size*size
        self.start = 0
        self.terminal = {self.n_states - 1}
        self.n_actions = 4

    def step(self, state, action):
        row, col = divmod(state, self.size)
        if action == 0 and row > 0: row -= 1
        if action == 1 and col < self.size - 1: col += 1
        if action == 2 and row < self.size - 1: row += 1
        if action == 3 and col > 0: col -= 1
        next_state = row * self.size + col
        reward = 1.0 if next_state in self.terminal else 0.0
        done = next_state in self.terminal
        return next_state, reward, done

env = GridWorld(4)
print("GridWorld com", env.n_states, "estados e", env.n_actions, "ações")


# %%
def epsilon_greedy(Q, state, epsilon):
    if np.random.rand() < epsilon:
        return np.random.randint(Q.shape[1])
    return np.argmax(Q[state])

def q_learning(env, episodes=1000, alpha=0.4, gamma=0.95, epsilon=0.25):
    Q = np.zeros((env.n_states, env.n_actions))
    rewards = []
    for ep in range(episodes):
        state = env.start
        total = 0
        while True:
            action = epsilon_greedy(Q, state, epsilon)
            next_state, reward, done = env.step(state, action)
            Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
            state = next_state
            total += reward
            if done:
                break
        rewards.append(total)
        epsilon = max(0.01, epsilon * 0.99)
    return Q, rewards

Q, rewards = q_learning(env, episodes=1000)
print("Q-learning concluído")


# %%
plt.figure(figsize=(9,4))
plt.plot(np.convolve(rewards, np.ones(20)/20, mode="valid"))
plt.title("Aprendizado por Reforço: recompensa por episódio")
plt.xlabel("Episódio")
plt.ylabel("Recompensa")
plt.grid(True)
plt.show()


# %%
policy = np.argmax(Q, axis=1)
directions = ["↑","→","↓","←"]
for r in range(env.size):
    print(" ".join("T" if r*env.size + c in env.terminal else directions[policy[r*env.size + c]] for c in range(env.size)))


# %% [markdown]
# ## Seção 2: Redes Neurais e Comitês
# Nesta seção usamos o dataset Iris para treinar um `MLPClassifier` e depois combinar modelos via `VotingClassifier`.


# %%
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

mlp = MLPClassifier(hidden_layer_sizes=(50,), max_iter=500, random_state=42)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
svm = SVC(probability=True, kernel="rbf", random_state=42)

mlp.fit(X_train, y_train)
rf.fit(X_train, y_train)
svm.fit(X_train, y_train)

for name, model in [("MLP", mlp), ("RF", rf), ("SVM", svm)]:
    preds = model.predict(X_test)
    print(f"{name} accuracy = {accuracy_score(y_test, preds):.4f}")


# %%
committee = VotingClassifier([("mlp", mlp), ("rf", rf), ("svm", svm)], voting="soft")
committee.fit(X_train, y_train)
committee_preds = committee.predict(X_test)
print(f"VotingClassifier accuracy = {accuracy_score(y_test, committee_preds):.4f}")


# %%
print("\nClassification report (VotingClassifier):")
print(classification_report(y_test, committee_preds, target_names=iris.target_names))
cm = confusion_matrix(y_test, committee_preds)
plt.figure(figsize=(5,4))
plt.imshow(cm, cmap="Blues")
plt.colorbar()
plt.xticks(range(3), iris.target_names, rotation=45)
plt.yticks(range(3), iris.target_names)
plt.title("Matriz de confusão")
plt.xlabel("Predito")
plt.ylabel("Verdadeiro")
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, cm[i,j], ha="center", va="center", color="black")
plt.tight_layout()
plt.show()


# %% [markdown]
# ## Resumo das aplicações
# - **Aprendizado por Reforço**: Q-learning em um ambiente discreto.
# - **Redes Neurais**: `MLPClassifier` como exemplo de classificador não linear.
# - **Comitês**: `VotingClassifier` combina múltiplos modelos para melhorar robustez.
# 
# Esses exemplos cobrem conceitos importantes do material e do mapa mental: exploração vs. exploração, Bellman, redes neurais, e ensembles.


