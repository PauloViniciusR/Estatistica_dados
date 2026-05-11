# 03 - Distribuicao de probabilidade

Notebook base: `03_distribuicao_de_probabilidade.ipynb`

## Variavel aleatoria discreta

Assume valores contaveis, como `0`, `1`, `2`, `3`.

Uma distribuicao discreta precisa satisfazer:

```text
P(X = x_i) >= 0
soma P(X = x_i) = 1
```

## Valor esperado

Media teorica da variavel aleatoria.

```text
E(X) = soma x_i * P(X = x_i)
```

Exemplo:

```text
X        0     1     2
P(X)   0,2   0,5   0,3

E(X) = 0*0,2 + 1*0,5 + 2*0,3
E(X) = 1,1
```

## Variancia

Mede a dispersao teorica.

```text
Var(X) = soma (x_i - E(X))^2 * P(X = x_i)
```

Usando o exemplo anterior:

```text
Var(X) = (0 - 1,1)^2*0,2 + (1 - 1,1)^2*0,5 + (2 - 1,1)^2*0,3
Var(X) = 1,21*0,2 + 0,01*0,5 + 0,81*0,3
Var(X) = 0,242 + 0,005 + 0,243 = 0,49
```

## Desvio padrao

```text
DP(X) = raiz(Var(X))
DP(X) = raiz(0,49) = 0,7
```

## Exercicios

1. Para `X = {1, 2, 3}` com probabilidades `{0,2, 0,5, 0,3}`, calcule `E(X)`.
2. Usando o item anterior, calcule `Var(X)`.
3. Verifique se `{0,15, 0,35, 0,40}` pode ser uma distribuicao de probabilidade.
4. Explique a diferenca entre frequencia observada e probabilidade teorica.

