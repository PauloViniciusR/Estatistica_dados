# Estatistica com Python

Repositorio de estudos e projetos aplicados de estatistica para ciencia de dados. A trilha esta organizada em notebooks Jupyter, com progressao dos fundamentos ate testes estatisticos e um projeto aplicado com dados de diabetes.

## Objetivo

Consolidar conceitos estatisticos com implementacao em Python, priorizando:

- analise exploratoria antes de qualquer modelagem;
- interpretacao estatistica dos resultados;
- uso de `pandas`, `numpy`, `scipy`, `scikit-learn` e bibliotecas de visualizacao;
- organizacao de estudos por assunto, com notebooks versionados por ordem de leitura.

## Estrutura do repositorio

| Pasta | Conteudo | README local |
|---|---|---|
| [`Conceitos fundamentais`](Conceitos%20fundamentais/) | tipos de estatistica, variaveis qualitativas e quantitativas, exercicios iniciais | [`README.md`](Conceitos%20fundamentais/README.md) |
| [`Estatistica_Descritiva`](Estatistica_Descritiva/) | analise univariada, frequencias, medidas resumo, outliers, associacao e regressao linear | [`README.md`](Estatistica_Descritiva/README.md) |
| [`Estatistica_Probabilistica`](Estatistica_Probabilistica/) | probabilidade, variaveis aleatorias e distribuicoes discretas e continuas | [`README.md`](Estatistica_Probabilistica/README.md) |
| [`Estatistica_Inferencial`](Estatistica_Inferencial/) | testes de hipoteses, normalidade, homogeneidade, testes parametricos e nao parametricos | [`README.md`](Estatistica_Inferencial/README.md) |
| [`Proj_Statistic`](Proj_Statistic/) | projeto aplicado de analise e modelagem para diabetes | [`README.md`](Proj_Statistic/README.md) |
| [`dados`](dados/) | bases usadas nos notebooks e exercicios | - |

## Ordem recomendada de estudo

1. [`Conceitos fundamentais`](Conceitos%20fundamentais/)
2. [`Estatistica_Descritiva`](Estatistica_Descritiva/)
3. [`Estatistica_Probabilistica`](Estatistica_Probabilistica/)
4. [`Estatistica_Inferencial`](Estatistica_Inferencial/)
5. [`Proj_Statistic`](Proj_Statistic/)

Essa ordem evita usar testes ou modelos antes de entender variaveis, distribuicoes, medidas resumo e pressupostos estatisticos.

## Padrao dos notebooks

Os notebooks devem manter uma estrutura analitica consistente:

1. definir o problema ou conceito estatistico;
2. carregar e inspecionar dados quando houver dataset;
3. tratar dados ausentes, tipos e inconsistencias;
4. aplicar calculos, visualizacoes ou testes;
5. interpretar resultados em linguagem estatistica;
6. registrar limitacoes, pressupostos e proximos passos.

## Datasets

A pasta [`dados`](dados/) concentra bases de apoio para aulas e exercicios. O projeto de diabetes possui seus dados em [`Proj_Statistic/diabetes`](Proj_Statistic/diabetes/), incluindo uma versao original em CSV e uma versao tratada em Parquet.

## Como executar

Abra os notebooks com Jupyter Notebook, JupyterLab ou VS Code:

```bash
jupyter lab
```

Instale as dependencias conforme a necessidade de cada notebook. As bibliotecas mais recorrentes sao:

```bash
pip install pandas numpy scipy scikit-learn matplotlib seaborn plotly pyarrow
```

## Boas praticas do repositorio

- manter nomes de notebooks numerados para preservar a ordem pedagogica;
- separar estudos teoricos, exercicios e projetos aplicados;
- documentar decisoes estatisticas importantes dentro dos notebooks;
- versionar datasets tratados sem sobrescrever a base bruta;
- evitar modelagem antes de EDA, validacao de pressupostos e escolha adequada de metricas.
