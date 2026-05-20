# Estatistica inferencial

Trilha de testes de hipoteses e inferencia estatistica. Os notebooks cobrem validacao de pressupostos, testes parametricos, testes nao parametricos e interpretacao de resultados.

## Roteiro dos notebooks

### Fundamentos e pressupostos

| Ordem | Notebook | Quando usar | O que observar |
|---:|---|---|---|
| 1 | [`01_testes_hipoteses.ipynb`](01_testes_hipoteses.ipynb) | para entender a logica geral de um teste estatistico | `H0`, `H1`, nivel de significancia, p-valor, erro tipo I e erro tipo II |
| 2 | [`02_testes_normalidade_ks.ipynb`](02_testes_normalidade_ks.ipynb) | para avaliar aderencia a uma distribuicao teorica, especialmente em amostras maiores | o teste K-S exige cuidado quando media e desvio padrao sao estimados pela propria amostra |
| 3 | [`03_testes_shapiro_wilk.ipynb`](03_testes_shapiro_wilk.ipynb) | para verificar normalidade em uma amostra, comum antes de testes parametricos | recomendado para amostras pequenas e medias; combine com histogramas e QQ plot |
| 4 | [`04_testes_homogeneidade_variancias.ipynb`](04_testes_homogeneidade_variancias.ipynb) | para comparar se grupos possuem variancias semelhantes | pressuposto importante em teste t, ANOVA e comparacoes entre grupos |

### Testes parametricos

Testes parametricos trabalham com parametros populacionais, como media, variancia ou proporcao. Em geral, exigem dados quantitativos, independencia das observacoes e algum controle sobre normalidade e homogeneidade de variancias.

| Ordem | Notebook | Pergunta estatistica | Uso principal |
|---:|---|---|---|
| 5 | [`05_testes_parametricos_teste_z.ipynb`](05_testes_parametricos_teste_z.ipynb) | a media ou proporcao observada difere de um valor de referencia? | teste Z, usado quando a variancia populacional e conhecida ou quando a aproximacao normal e adequada |
| 6 | [`06_testes_parametricos_teste_t_student.ipynb`](06_testes_parametricos_teste_t_student.ipynb) | a media de uma amostra difere de um valor esperado? | teste t para uma amostra, com variancia populacional desconhecida |
| 7 | [`07_teste_t_student_duas_amostras_independentes.ipynb`](07_teste_t_student_duas_amostras_independentes.ipynb) | duas medias de grupos independentes sao diferentes? | comparacao entre dois grupos distintos, com atencao a normalidade e variancias |
| 8 | [`08_testes_t_student_duas_amostras_pareadas.ipynb`](08_testes_t_student_duas_amostras_pareadas.ipynb) | houve mudanca media entre duas medicoes relacionadas? | antes/depois, pares correspondentes ou medidas repetidas no mesmo individuo |
| 9 | [`09_testes_hipoteses_parametricos_anova_one_way.ipynb`](09_testes_hipoteses_parametricos_anova_one_way.ipynb) | pelo menos uma media difere entre tres ou mais grupos? | ANOVA one-way para comparar medias de varios grupos independentes |

### Testes nao parametricos

Testes nao parametricos sao alternativas quando os pressupostos dos testes parametricos nao sao atendidos ou quando os dados sao ordinais/nominais. Eles tendem a comparar distribuicoes, postos, frequencias ou medianas, em vez de depender diretamente de medias e variancias.

| Ordem | Notebook | Pergunta estatistica | Uso principal |
|---:|---|---|---|
| 10 | [`10_testes_hipoteses_nao_parametricos_qui_quadrado_uma_amostra.ipynb`](10_testes_hipoteses_nao_parametricos_qui_quadrado_uma_amostra.ipynb) | as frequencias observadas seguem uma distribuicao esperada? | teste de aderencia para uma variavel categorica |
| 11 | [`11_testes_hipoteses_nao_parametricos_wilcoxon.ipynb`](11_testes_hipoteses_nao_parametricos_wilcoxon.ipynb) | duas medicoes pareadas apresentam diferenca sistematica? | alternativa nao parametrica ao teste t pareado |
| 12 | [`12_testes_hipoteses_nao_parametricos_qui_quadrado_duas_amostras.ipynb`](12_testes_hipoteses_nao_parametricos_qui_quadrado_duas_amostras.ipynb) | duas variaveis categoricas estao associadas? | teste qui-quadrado de independencia em tabelas de contingencia |
| 13 | [`13_testes_hipoteses_nao_parametricos_mann_whitney.ipynb`](13_testes_hipoteses_nao_parametricos_mann_whitney.ipynb) | dois grupos independentes diferem em localizacao/distribuicao? | alternativa nao parametrica ao teste t para duas amostras independentes |
| 14 | [`14_testes_hipoteses_nao_parametricos_friedman.ipynb`](14_testes_hipoteses_nao_parametricos_friedman.ipynb) | tres ou mais medicoes relacionadas diferem entre si? | alternativa nao parametrica para ANOVA de medidas repetidas |
| 15 | [`15_testes_hipoteses_nao_parametricos_kruskal_wallis.ipynb`](15_testes_hipoteses_nao_parametricos_kruskal_wallis.ipynb) | tres ou mais grupos independentes diferem entre si? | alternativa nao parametrica para ANOVA one-way |

## Como escolher o teste

| Situacao | Teste recomendado |
|---|---|
| uma media contra valor de referencia, dados quantitativos e pressupostos atendidos | teste t para uma amostra ou teste Z |
| duas medias independentes, dados quantitativos e pressupostos atendidos | teste t para duas amostras independentes |
| duas medicoes relacionadas, dados quantitativos e pressupostos atendidos | teste t pareado |
| tres ou mais medias independentes, dados quantitativos e pressupostos atendidos | ANOVA one-way |
| frequencias de uma variavel categorica contra valores esperados | qui-quadrado de aderencia |
| associacao entre duas variaveis categoricas | qui-quadrado de independencia |
| duas amostras pareadas sem normalidade | Wilcoxon |
| duas amostras independentes sem normalidade | Mann-Whitney |
| tres ou mais amostras pareadas sem normalidade | Friedman |
| tres ou mais amostras independentes sem normalidade | Kruskal-Wallis |

## Exercicios

- [`Ex/01_exercicios.ipynb`](Ex/01_exercicios.ipynb): exercicios de testes inferenciais.

## Arquivos auxiliares

- [`auxiliares.py`](auxiliares.py): funcoes de apoio para os notebooks;
- [`graficos.py`](graficos.py): funcoes de visualizacao estatistica.

## Boas praticas de inferencia

- formular `H0` e `H1` antes de calcular o teste;
- escolher o nivel de significancia antes de observar o p-valor;
- validar pressupostos de normalidade, independencia e homogeneidade quando o teste exigir;
- reportar estatistica do teste, p-valor, decisao e interpretacao pratica;
- evitar concluir causalidade quando o desenho dos dados nao sustenta essa inferencia.
