# %% [markdown]
# # Regressão e Sérries Temporais: aplicação prática em Python
# Este notebook aplica os conceitos do material e do mapa mental em exemplos práticos de regressão e previsão de séries temporais.
# 
# - Mapa mental do tema: [3-regressão-e-séries-temporais.md](../../../docs/mapas-mentais/01-aprendizado-de-maquina-overview/3-regressão-e-séries-temporais.md)
# 
# - Regressão linear e multivariada
# - Regularização Lasso, Ridge e ElasticNet
# - Modelos não lineares: Decision Tree, Random Forest e SVR
# - Séries temporais com características temporais e previsão de valores futuros
# - Avaliação com MAE, MSE, RMSE e R²


# %% [markdown]
# ## 1. Instalação de dependências
# Execute esta célula se precisar instalar bibliotecas Python no ambiente.


# %%
!pip install --quiet numpy pandas matplotlib seaborn scikit-learn


# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

sns.set(style='whitegrid', palette='muted', font_scale=1.1)
plt.rcParams['figure.figsize'] = (10, 6)


# %% [markdown]
# ## 2. Gerando uma série temporal sintética de preços de ações
# Vamos criar uma série temporal com tendência, sazonalidade e ruído para simular um preço de ação.


# %%
np.random.seed(42)
periods = 120
dates = pd.date_range(start='2023-01-01', periods=periods, freq='W')
trend = np.linspace(50, 90, periods)
seasonal = 5 * np.sin(np.linspace(0, 4 * np.pi, periods))
noise = np.random.normal(scale=2.5, size=periods)
price = trend + seasonal + noise

df = pd.DataFrame({'date': dates, 'price': price})
df['week'] = df['date'].dt.isocalendar().week.astype(int)
df['month'] = df['date'].dt.month.astype(int)
df['quarter'] = df['date'].dt.quarter.astype(int)

df['lag_1'] = df['price'].shift(1)
df['lag_2'] = df['price'].shift(2)
df['rolling_mean_4'] = df['price'].rolling(window=4, min_periods=1).mean()
df['rolling_std_4'] = df['price'].rolling(window=4, min_periods=1).std().fillna(0)

df = df.dropna().reset_index(drop=True)
df.head()


# %%
plt.figure()
plt.plot(df['date'], df['price'], marker='o', linewidth=1)
plt.title('Série temporal sintética de preços de ações')
plt.xlabel('Data')
plt.ylabel('Preço')
plt.show()


# %% [markdown]
# ## 3. Divisão em treino e teste
# Usamos regressão tradicional em dados de séries temporais com recursos de defasagem (lags) e médias móveis.


# %%
features = ['week', 'month', 'quarter', 'lag_1', 'lag_2', 'rolling_mean_4', 'rolling_std_4']
X = df[features]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, shuffle=False)
print('Treino:', X_train.shape, 'Teste:', X_test.shape)


# %% [markdown]
# ## 4. Treinamento e avaliação de modelos de regressão
# Vamos comparar vários modelos e calcular as métricas principais.
# 
# - MAE: Mean Absolute Error
# - MSE: Mean Squared Error
# - RMSE: Root Mean Squared Error
# - R²: coeficiente de determinação


# %%
def evaluate_model(name, model, X_train, y_train, X_test, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    return {
        'model': name,
        'mae': mae,
        'mse': mse,
        'rmse': rmse,
        'r2': r2
    }

models = [
    ('LinearRegression', LinearRegression()),
    ('Ridge(alpha=1.0)', Ridge(alpha=1.0)),
    ('Lasso(alpha=0.1)', Lasso(alpha=0.1)),
    ('ElasticNet(alpha=0.1, l1_ratio=0.5)', ElasticNet(alpha=0.1, l1_ratio=0.5)),
    ('DecisionTree', DecisionTreeRegressor(random_state=42)),
    ('RandomForest', RandomForestRegressor(n_estimators=100, random_state=42)),
    ('SVR', SVR(C=1.0, epsilon=0.2, kernel='rbf'))
]

results = []
for name, model in models:
    results.append(evaluate_model(name, model, X_train, y_train, X_test, y_test))

results_df = pd.DataFrame(results).set_index('model')
results_df


# %%
plt.figure(figsize=(12, 5))
sns.barplot(x=results_df.index, y='rmse', data=results_df.reset_index())
plt.xticks(rotation=45, ha='right')
plt.title('Comparação de RMSE entre modelos')
plt.ylabel('RMSE')
plt.tight_layout()
plt.show()


# %% [markdown]
# ## 5. Previsão e visualização dos resultados
# Mostrar o ajuste de um modelo e a previsão vs valor real.


# %%
best_model_name = results_df['rmse'].idxmin()
best_model = dict(models)[best_model_name]
best_model.fit(X_train, y_train)
y_pred = best_model.predict(X_test)

comparison = pd.DataFrame({
    'date': df.loc[X_test.index, 'date'],
    'actual': y_test.values,
    'predicted': y_pred
}).reset_index(drop=True)

plt.figure(figsize=(12, 5))
plt.plot(comparison['date'], comparison['actual'], marker='o', label='Real')
plt.plot(comparison['date'], comparison['predicted'], marker='x', label='Previsto')
plt.title(f'Previsão com o melhor modelo: {best_model_name}')
plt.xlabel('Data')
plt.ylabel('Preço da ação')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

comparison.head()


# %% [markdown]
# ## 6. Explicando o uso dos conceitos do material
# - Regressão linear e multivariada: usamos `LinearRegression` com múltiplas features
# - Funções de custo: calculamos MAE, MSE, RMSE e R²
# - Regularização: testamos Ridge, Lasso e ElasticNet
# - Modelos não lineares: avaliamos Decision Tree, Random Forest e SVR
# - Séries temporais: usamos defasagens (`lag_1`, `lag_2`) e estatísticas móveis para capturar dependência temporal
# 
# ### Referências rápidas
# - Scikit-learn linear models: https://scikit-learn.org/stable/modules/linear_model.html
# - SVR: https://scikit-learn.org/stable/modules/svm.html
# - Regularização Lasso / Ridge / ElasticNet: https://scikit-learn.org/stable/modules/linear_model.html


