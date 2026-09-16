# %% [markdown]
# # Redes Neurais e Comitês — Exemplo prático
# Este notebook mostra como treinar uma rede neural simples (`MLPClassifier`) e como montar um comitê de modelos usando `VotingClassifier` sobre o dataset Iris.
# 
# - Mapa mental do tema: [4-aprendizado-por-reforco-redes-neurais-e-comites.md](../../../docs/mapas-mentais/01-aprendizado-de-maquina-overview/4-aprendizado-por-reforco-redes-neurais-e-comites.md)
# 
# Vamos comparar modelos individuais e um ensemble para ver como comitês podem melhorar a robustez.


# %%
# Execute se necessário:
# !pip install --quiet scikit-learn matplotlib numpy


# %%
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
print("Treino:", X_train.shape, "Teste:", X_test.shape)


# %% [markdown]
# ## 1. Treinamento de modelos individuais
# - `MLPClassifier`: rede neural feedforward com uma camada oculta.
# - `RandomForestClassifier`: comitê de árvores de decisão.
# - `SVC`: máquina de vetores de suporte com kernel RBF.


# %%
mlp = MLPClassifier(hidden_layer_sizes=(50,), max_iter=500, random_state=42)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
svm = SVC(probability=True, kernel="rbf", random_state=42)

mlp.fit(X_train, y_train)
rf.fit(X_train, y_train)
svm.fit(X_train, y_train)

predictions = {}
for name, model in [("MLP", mlp), ("RF", rf), ("SVM", svm)]:
    preds = model.predict(X_test)
    predictions[name] = accuracy_score(y_test, preds)
    print(f"{name} accuracy = {accuracy_score(y_test, preds):.4f}")


# %% [markdown]
# ## 2. Comitê de modelos
# O `VotingClassifier` combina previsões de múltiplos modelos. Usamos `voting="soft"` para somar probabilidades, o que melhora o desempenho quando os classificadores são bem calibrados.


# %%
voting = VotingClassifier([("mlp", mlp), ("rf", rf), ("svm", svm)], voting="soft")
voting.fit(X_train, y_train)
voting_preds = voting.predict(X_test)
print(f"VotingClassifier accuracy = {accuracy_score(y_test, voting_preds):.4f}")


# %%
print("\nClassification report (VotingClassifier):")
print(classification_report(y_test, voting_preds, target_names=iris.target_names))
cm = confusion_matrix(y_test, voting_preds)
plt.figure(figsize=(5,4))
plt.imshow(cm, cmap="Blues")
plt.colorbar()
plt.xticks(range(len(iris.target_names)), iris.target_names, rotation=45)
plt.yticks(range(len(iris.target_names)), iris.target_names)
plt.xlabel("Predito")
plt.ylabel("Verdadeiro")
plt.title("Matriz de confusão do VotingClassifier")
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, cm[i,j], ha="center", va="center", color="black")
plt.tight_layout()
plt.show()


# %% [markdown]
# ## 3. Conclusões e relacionamento com o mapa mental
# - Comitês reduzem variância e podem superar modelos individuais.
# - `MLP` é um exemplo de rede neural simples com camadas densas.
# - `RandomForest` e `SVM` são modelos clássicos de aprendizado de máquina usados em comitês.
# - A combinação de aprendizagem profunda e comitês é útil em aplicações reais, como detecção de padrões e classificação.


