# 06 - Distribuicao uniforme continua

Notebook base: `06_continuas_uniforme.ipynb`

## Ideia central

Na uniforme continua, qualquer valor dentro do intervalo `[a, b]` tem densidade constante.

```text
X ~ Uniforme(a, b)
f(x) = 1 / (b - a), para a <= x <= b
```

Importante: em variaveis continuas, `P(X = valor exato) = 0`. Calculamos probabilidades em intervalos.

## Probabilidade em intervalo

```text
P(c <= X <= d) = (d - c) / (b - a)
```

Exemplo: `X ~ Uniforme(0, 10)`.

```text
P(2 <= X <= 6) = (6 - 2) / (10 - 0) = 4/10 = 0,40
```

## Media e variancia

```text
E(X) = (a + b) / 2
Var(X) = (b - a)^2 / 12
```

Exemplo:

```text
a = 0
b = 10
E(X) = 5
Var(X) = 100 / 12 = 8,3333
```

## Funcao acumulada

```text
F(x) = P(X <= x) = (x - a) / (b - a)
```

Para `X ~ Uniforme(0, 10)`:

```text
F(7) = (7 - 0) / (10 - 0) = 0,70
```

## Exercicios

1. Para `X ~ Uniforme(5, 15)`, calcule `P(8 <= X <= 12)`.
2. Calcule `E(X)` e `Var(X)` para `X ~ Uniforme(5, 15)`.
3. Para `X ~ Uniforme(20, 50)`, calcule `P(X <= 35)`.
4. Explique por que `P(X = 10)` e zero em distribuicoes continuas.

