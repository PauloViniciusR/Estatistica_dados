# 04 - Distribuicao uniforme discreta

Notebook base: `04_discretas_uniforme.ipynb`

## Ideia central

Na uniforme discreta, todos os valores possiveis tem a mesma probabilidade.

Se existem `n` valores possiveis:

```text
P(X = x) = 1 / n
```

## Media

Para valores inteiros de `a` ate `b`:

```text
E(X) = (a + b) / 2
```

Exemplo: dado comum, `a = 1`, `b = 6`.

```text
E(X) = (1 + 6) / 2 = 3,5
```

## Variancia

Para inteiros consecutivos de `a` ate `b`, com `n = b - a + 1`:

```text
Var(X) = (n^2 - 1) / 12
```

Exemplo: dado comum.

```text
n = 6
Var(X) = (6^2 - 1) / 12 = 35 / 12 = 2,9167
```

## Probabilidade acumulada

```text
P(X <= k) = quantidade de valores <= k / n
```

Exemplo:

```text
P(X <= 4) em um dado = 4 / 6 = 0,6667
```

## Exercicios

1. Uma variavel uniforme discreta assume valores de `1` a `10`. Calcule `P(X = 7)`.
2. Calcule `E(X)` para valores de `1` a `10`.
3. Calcule `Var(X)` para valores de `1` a `10`.
4. Calcule `P(X <= 6)` para valores de `1` a `10`.

