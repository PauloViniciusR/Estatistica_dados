# 10 - Distribuicao F de Snedecor

Notebook base: `10_f_snedecor.ipynb`

## Ideia central

A distribuicao F aparece na comparacao de variancias e na ANOVA.

```text
F = variancia_1 / variancia_2
```

Por convencao, em muitos problemas de comparacao de variancias, colocamos a maior variancia no numerador para obter `F >= 1`.

## Graus de liberdade

Cada variancia tem seu proprio grau de liberdade.

```text
gl_1 = n_1 - 1
gl_2 = n_2 - 1
```

## Exemplo calculado

Duas amostras:

```text
A: n = 11, variancia = 25
B: n = 9, variancia = 10
```

```text
F = 25 / 10 = 2,5
gl_1 = 11 - 1 = 10
gl_2 = 9 - 1 = 8
```

## ANOVA de um fator

Na ANOVA, a estatistica F compara variabilidade entre grupos com variabilidade dentro dos grupos.

```text
F = QM_entre / QM_dentro
```

Onde:

```text
QM_entre = SQ_entre / gl_entre
QM_dentro = SQ_dentro / gl_dentro
```

Graus de liberdade:

```text
gl_entre = k - 1
gl_dentro = N - k
```

`k` e o numero de grupos e `N` e o total de observacoes.

## Exercicios

1. Duas amostras tem variancias `36` e `12`. Calcule `F`.
2. Se `n1 = 15` e `n2 = 10`, calcule `gl1` e `gl2`.
3. Em uma ANOVA com `k = 4` grupos e `N = 32`, calcule `gl_entre` e `gl_dentro`.
4. Explique por que a ANOVA usa uma razao de variancias.

