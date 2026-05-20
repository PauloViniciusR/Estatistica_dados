# Projeto estatistico: diabetes

Projeto aplicado de analise exploratoria, tratamento de dados e modelagem estatistica/machine learning usando dados de diabetes.

## Notebook

| Notebook | Tema |
|---|---|
| [`projeto_diabetes_.ipynb`](projeto_diabetes_.ipynb) | EDA, tratamento, preparacao de dados e modelagem para diabetes |

## Dados

| Arquivo | Descricao |
|---|---|
| [`diabetes/diabetes.csv`](diabetes/diabetes.csv) | base original em CSV |
| [`diabetes/diabetes_tratado.parquet`](diabetes/diabetes_tratado.parquet) | base tratada/versionada em Parquet |

## Estrutura esperada do projeto

1. carregar e auditar a base original;
2. analisar tipos, ausencias, duplicidades e distribuicoes;
3. tratar inconsistencias e salvar dataset tratado;
4. separar variaveis explicativas e alvo;
5. criar baseline de modelagem;
6. avaliar com metricas adequadas ao problema;
7. registrar conclusoes, limitacoes e proximas melhorias.

## Boas praticas

- preservar o CSV original sem sobrescrita;
- usar o Parquet tratado como versao limpa para reprodutibilidade;
- evitar overfitting com separacao treino/teste e validacao adequada;
- comparar modelos com metricas coerentes para classificacao, como acuracia, recall, precision, F1 e ROC-AUC quando aplicavel.
