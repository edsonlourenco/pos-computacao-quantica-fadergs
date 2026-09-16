# %% [markdown]
# # Q-Learning: GridWorld (exemplo prático)
# Este notebook demonstra o algoritmo tabular de **Q-learning** em um ambiente simples de GridWorld 4x4.
# 
# - Mapa mental do tema: [4-aprendizado-por-reforco-redes-neurais-e-comites.md](../../../docs/mapas-mentais/01-aprendizado-de-maquina-overview/4-aprendizado-por-reforco-redes-neurais-e-comites.md)
# 
# Com este exemplo você verá: 
# - definição do ambiente como um MDP
# - política epsilon-greedy
# - atualização de valor via equação de Bellman
# - análise de convergência e política aprendida


# %%
# Execute se precisar instalar dependências
# !pip install --quiet numpy matplotlib


# %%
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass

np.random.seed(42)


# %% [markdown]
# ## 1. Ambiente GridWorld
# O ambiente é um tabuleiro 4x4 onde o agente começa no canto superior esquerdo e o objetivo está no canto inferior direito.
# Cada estado é representado por um número inteiro, e as ações são: **cima**, **direita**, **baixo** e **esquerda**.
# A recompensa é `1.0` apenas ao alcançar o estado terminal, caso contrário `0.0`.


# %%
class GridWorld:
    def __init__(self, size=4):
        self.size = size
        self.n_states = size * size
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

env = GridWorld(size=4)
print("Estados:", env.n_states, "Ações:", env.n_actions)


# %% [markdown]
# ## 2. Implementação do Q-learning
# O Q-learning atualiza os valores de Q usando a fórmula:
# 
# \(Q(s,a) \leftarrow Q(s,a) + lpha [r + \gamma \max_{a'} Q(s', a') - Q(s,a)]\)
# 
# onde `lpha` é a taxa de aprendizagem e `\gamma` é o fator de desconto.


# %%
def epsilon_greedy(Q, state, epsilon):
    if np.random.rand() < epsilon:
        return np.random.randint(Q.shape[1])
    return np.argmax(Q[state])

def q_learning(env, episodes=2000, alpha=0.5, gamma=0.99, epsilon=0.3):
    Q = np.zeros((env.n_states, env.n_actions))
    reward_history = []
    for ep in range(episodes):
        state = env.start
        total_reward = 0.0
        while True:
            action = epsilon_greedy(Q, state, epsilon)
            next_state, reward, done = env.step(state, action)
            best_next = np.max(Q[next_state])
            Q[state, action] += alpha * (reward + gamma * best_next - Q[state, action])
            state = next_state
            total_reward += reward
            if done:
                break
        reward_history.append(total_reward)
        epsilon = max(0.01, epsilon * 0.995)
    return Q, reward_history

Q, rewards = q_learning(env, episodes=2000, alpha=0.5, gamma=0.95, epsilon=0.3)
print("Treinamento concluído com", len(rewards), "episódios")


# %%
plt.figure(figsize=(10,4))
plt.plot(np.convolve(rewards, np.ones(50)/50, mode="valid"), lw=1.5)
plt.title("Recompensa total por episódio (média móvel)")
plt.xlabel("Episódio")
plt.ylabel("Recompensa")
plt.grid(True)
plt.show()


# %%
policy = np.argmax(Q, axis=1)
actions = ["↑","→","↓","←"]
for row in range(env.size):
    row_actions = []
    for col in range(env.size):
        state = row * env.size + col
        if state in env.terminal:
            row_actions.append("T")
        else:
            row_actions.append(actions[policy[state]])
    print(" ".join(row_actions))


# %% [markdown]
# ## 3. Análise dos resultados
# - A curva de recompensas mostra a convergência do agente.
# - A tabela Q capturada representa a expectativa de recompensa para cada par estado-ação.
# - A política final indica o melhor movimento em cada célula do GridWorld.
# 
# ### Conexões com o material de estudo
# - O Q-learning é um algoritmo de **Aprendizado por Reforço** sem modelo.
# - Ele utiliza a **Equação de Bellman** para atualizar `Q(s,a)`.
# - A técnica epsilon-greedy equilibra **exploração** e **exploração**.
# - O ambiente segue a estrutura de um **MDP** (Processo de Decisão de Markov).


# %%
print("Tabela Q final (primeiros estados):")
for s in range(env.n_states):
    print(f"s={s}: {Q[s].round(3)}")


