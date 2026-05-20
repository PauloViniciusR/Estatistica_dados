# Estatistica Probabilistica

Este repositorio organiza uma trilha de estudos sobre probabilidade, variaveis aleatorias e distribuicoes de probabilidade usando Python. O foco e construir intuicao estatistica, validar conceitos com simulacoes e interpretar graficos e probabilidades geradas com `numpy`, `pandas`, `matplotlib`, `seaborn` e `scipy.stats`.

## Objetivo da trilha

O objetivo e sair dos fundamentos de probabilidade e chegar nas principais distribuicoes usadas em inferencia estatistica:

- probabilidade, espaco amostral e eventos;
- variaveis aleatorias discretas e continuas;
- distribuicoes discretas: uniforme discreta e binomial;
- distribuicoes continuas: uniforme continua e normal;
- graus de liberdade;
- distribuicoes para inferencia: qui-quadrado, t de Student e F de Snedecor.

## Estrutura atual

Os notebooks ficam diretamente nesta pasta (`Estatistica_Probabilistica/`) para facilitar a navegacao e a execucao em sequencia.

Os materiais teoricos em Markdown continuam organizados dentro de `Probabilidades/`, separados por assunto. Eles trazem formulas, exemplos calculados e exercicios.

Tambem existe o arquivo [`Probabilidades/indice.md`](Probabilidades/indice.md), que resume a ordem de estudo.

## Ordem recomendada

| Ordem | Notebook | Documento teorico |
|---:|---|---|
| 1 | [`01_probabilidade.ipynb`](01_probabilidade.ipynb) | [`01_probabilidade.md`](Probabilidades/01_probabilidade/01_probabilidade.md) |
| 2 | [`02_tipos_de_eventos.ipynb`](02_tipos_de_eventos.ipynb) | [`02_tipos_de_eventos.md`](Probabilidades/02_tipos_de_eventos/02_tipos_de_eventos.md) |
| 3 | [`03_distribuicao_de_probabilidade.ipynb`](03_distribuicao_de_probabilidade.ipynb) | [`03_distribuicao_de_probabilidade.md`](Probabilidades/03_distribuicao_de_probabilidade/03_distribuicao_de_probabilidade.md) |
| 4 | [`04_discretas_uniforme.ipynb`](04_discretas_uniforme.ipynb) | [`04_discretas_uniforme.md`](Probabilidades/04_discretas_uniforme/04_discretas_uniforme.md) |
| 5 | [`05_discretas_binomial.ipynb`](05_discretas_binomial.ipynb) | [`05_discretas_binomial.md`](Probabilidades/05_discretas_binomial/05_discretas_binomial.md) |
| 6 | [`06_continuas_uniforme.ipynb`](06_continuas_uniforme.ipynb) | [`06_continuas_uniforme.md`](Probabilidades/06_continuas_uniforme/06_continuas_uniforme.md) |
| 7 | [`07_distribuicoes_variaveis_continuas_normal_inicio.ipynb`](07_distribuicoes_variaveis_continuas_normal_inicio.ipynb) | [`07_distribuicoes_variaveis_continuas_normal_inicio.md`](Probabilidades/07_distribuicoes_variaveis_continuas_normal_inicio/07_distribuicoes_variaveis_continuas_normal_inicio.md) |
| 8 | [`11_graus_de_liberdade.ipynb`](11_graus_de_liberdade.ipynb) | [`11_graus_de_liberdade.md`](Probabilidades/11_graus_de_liberdade/11_graus_de_liberdade.md) |
| 9 | [`08_continuas_qui_quadrado.ipynb`](08_continuas_qui_quadrado.ipynb) | [`08_continuas_qui_quadrado.md`](Probabilidades/08_continuas_qui_quadrado/08_continuas_qui_quadrado.md) |
| 10 | [`09_t_student.ipynb`](09_t_student.ipynb) | [`09_t_student.md`](Probabilidades/09_t_student/09_t_student.md) |
| 11 | [`10_f_snedecor.ipynb`](10_f_snedecor.ipynb) | [`10_f_snedecor.md`](Probabilidades/10_f_snedecor/10_f_snedecor.md) |

Observacao: pedagogicamente, graus de liberdade deve ser estudado antes de qui-quadrado, t de Student e F de Snedecor. O notebook original esta numerado como `11`, mas a trilha acima recomenda sua leitura antes das distribuicoes de inferencia.

## Estrutura analitica dos notebooks

Cada notebook deve seguir a mesma logica:

1. apresentar o problema estatistico;
2. definir os conceitos e parametros;
3. executar simulacoes ou calculos em Python;
4. visualizar a distribuicao;
5. interpretar probabilidades, densidades, acumuladas e quantis;
6. discutir aplicacoes e limitacoes.

Esse padrao evita que o notebook vire apenas uma sequencia de celulas de codigo. O codigo deve ser sempre acompanhado de interpretacao estatistica.

## Papel do arquivo `graficos.py`

O arquivo `graficos.py` deve funcionar como camada reutilizavel de visualizacao. Sempre que uma distribuicao precisar destacar PMF, PDF, CDF, PPF ou regioes criticas, a regra ideal e centralizar a logica nesse modulo e usar os notebooks apenas para explicar e chamar as funcoes.

## Funcoes estatisticas recorrentes

| Funcao | Tipo | Interpretacao |
|---|---|---|
| `rvs` | simulacao | gera valores aleatorios seguindo uma distribuicao |
| `pmf` | discreta | calcula probabilidade exata de um valor |
| `pdf` | continua | calcula densidade em um ponto |
| `cdf` | ambas | calcula probabilidade acumulada ate um valor |
| `ppf` | ambas | calcula o valor associado a uma probabilidade acumulada |

Em variaveis continuas, `pdf(x)` nao e a probabilidade de `X = x`. E uma densidade. Probabilidades em distribuicoes continuas sao obtidas por intervalos, geralmente via CDF.
