# 08 - Distribuicao qui-quadrado

Notebook base: `08_continuas_qui_quadrado.ipynb`

## Ideia central

A distribuicao qui-quadrado surge da soma de quadrados de variaveis normais padronizadas independentes.

```text
X ~ Qui-quadrado(gl)
```

Onde `gl` sao os graus de liberdade.

## Teste de aderencia

Compara frequencias observadas e esperadas.

```text
chi2 = soma ((O_i - E_i)^2 / E_i)
```

Onde:

```text
O_i = frequencia observada
E_i = frequencia esperada
```

## Exemplo calculado

Uma moeda foi lancada 100 vezes:

```text
Observado: cara = 60, coroa = 40
Esperado: cara = 50, coroa = 50
```

```text
chi2 = (60 - 50)^2/50 + (40 - 50)^2/50
chi2 = 100/50 + 100/50
chi2 = 4
```

Graus de liberdade:

```text
gl = numero de categorias - 1 = 2 - 1 = 1
```

## Teste de independencia

Usado em tabelas de contingencia.

Valor esperado de uma celula:

```text
E_ij = (total_linha_i * total_coluna_j) / total_geral
```

Depois:

```text
chi2 = soma ((O_ij - E_ij)^2 / E_ij)
```

## Exercicios

1. Calcule o qui-quadrado para observado `{30, 20}` e esperado `{25, 25}`.
2. Em uma tabela `2 x 3`, calcule os graus de liberdade.
3. Explique por que frequencias esperadas muito pequenas podem prejudicar o teste.
4. Monte uma tabela simples e calcule um valor esperado de uma celula.

