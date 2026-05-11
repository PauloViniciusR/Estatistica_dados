# 07 - Distribuicao normal

Notebook base: `07_distribuicoes_variaveis_continuas_normal_inicio.ipynb`

## Ideia central

A distribuicao normal e definida por media `mu` e desvio padrao `sigma`.

```text
X ~ Normal(mu, sigma)
```

Para calcular probabilidades, padronizamos para a normal padrao:

```text
Z = (X - mu) / sigma
```

## Exemplo de padronizacao

Se `X ~ Normal(100, 15)`, calcule `P(X <= 130)`.

```text
Z = (130 - 100) / 15 = 2
P(X <= 130) = P(Z <= 2)
```

Pela tabela normal ou pelo Python:

```text
P(Z <= 2) aproximadamente 0,9772
```

## Intervalos

Para `P(a <= X <= b)`:

```text
Z_a = (a - mu) / sigma
Z_b = (b - mu) / sigma
P(a <= X <= b) = P(Z <= Z_b) - P(Z <= Z_a)
```

Exemplo: `X ~ Normal(100, 15)`, calcule `P(85 <= X <= 115)`.

```text
Z_85 = (85 - 100) / 15 = -1
Z_115 = (115 - 100) / 15 = 1
P(85 <= X <= 115) = P(Z <= 1) - P(Z <= -1)
P = 0,8413 - 0,1587 = 0,6826
```

## Regra empirica

```text
mu +- 1 sigma: cerca de 68%
mu +- 2 sigma: cerca de 95%
mu +- 3 sigma: cerca de 99,7%
```

## Exercicios

1. Para `X ~ Normal(70, 10)`, calcule o escore-z de `X = 85`.
2. Para `X ~ Normal(70, 10)`, calcule `P(X <= 85)`.
3. Para `X ~ Normal(70, 10)`, calcule `P(60 <= X <= 80)`.
4. Explique quando faz sentido usar aproximacao normal para dados reais.

