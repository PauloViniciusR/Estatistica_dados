# 05 - Bernoulli e Binomial

Notebook base: `05_discretas_binomial.ipynb`

## Bernoulli

Experimento com dois resultados: sucesso ou fracasso.

```text
X ~ Bernoulli(p)
P(X = 1) = p
P(X = 0) = 1 - p
E(X) = p
Var(X) = p(1 - p)
```

## Binomial

Conta o numero de sucessos em `n` tentativas independentes, com probabilidade de sucesso `p`.

```text
X ~ Binomial(n, p)
P(X = k) = C(n, k) * p^k * (1 - p)^(n - k)
```

Onde:

```text
C(n, k) = n! / (k! * (n-k)!)
```

## Exemplo calculado

Probabilidade de sair exatamente 3 caras em 5 lancamentos de uma moeda justa.

```text
n = 5
k = 3
p = 0,5

C(5,3) = 5! / (3! * 2!) = 10
P(X = 3) = 10 * 0,5^3 * 0,5^2
P(X = 3) = 10 * 0,03125 = 0,3125
```

## Media e variancia

```text
E(X) = n*p
Var(X) = n*p*(1-p)
DP(X) = raiz(n*p*(1-p))
```

Exemplo:

```text
n = 10
p = 0,5
E(X) = 10 * 0,5 = 5
Var(X) = 10 * 0,5 * 0,5 = 2,5
```

## Probabilidade acumulada

Para `P(X <= k)`, some as probabilidades de `0` ate `k`.

```text
P(X <= 2) = P(0) + P(1) + P(2)
```

Em Python, isso corresponde a `binom.cdf(k, n, p)`.

## Exercicios

1. Calcule `P(X = 4)` para `X ~ Binomial(10, 0,5)`.
2. Calcule `P(X <= 2)` para `X ~ Binomial(6, 0,3)`.
3. Calcule media e variancia para `X ~ Binomial(20, 0,2)`.
4. Explique por que a binomial exige independencia entre tentativas.

