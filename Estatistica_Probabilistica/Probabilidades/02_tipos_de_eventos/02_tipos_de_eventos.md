# 02 - Tipos de eventos

Notebook base: `02_tipos_de_eventos.ipynb`

## Eventos mutuamente exclusivos

Dois eventos sao mutuamente exclusivos quando nao podem ocorrer ao mesmo tempo.

```text
P(A e B) = 0
P(A ou B) = P(A) + P(B)
```

Exemplo: em um unico lancamento de dado, sair `2` e sair `5` ao mesmo tempo e impossivel.

```text
P(2 ou 5) = 1/6 + 1/6 = 2/6 = 1/3
```

## Eventos nao mutuamente exclusivos

Podem ocorrer juntos.

```text
P(A ou B) = P(A) + P(B) - P(A e B)
```

Exemplo: uma pessoa pode estudar Python e SQL.

```text
P(Python) = 0,45
P(SQL) = 0,35
P(Python e SQL) = 0,20
P(Python ou SQL) = 0,45 + 0,35 - 0,20 = 0,60
```

## Eventos independentes

A ocorrencia de um evento nao altera a probabilidade do outro.

```text
P(A e B) = P(A) * P(B)
```

Exemplo: lancar uma moeda e um dado.

```text
P(cara e numero 6) = 1/2 * 1/6 = 1/12
```

## Eventos dependentes

A ocorrencia de um evento altera a probabilidade do outro.

Exemplo: retirar duas cartas sem reposicao.

```text
P(2 ases sem reposicao) = 4/52 * 3/51
```

## Erros comuns

- Usar soma para eventos independentes que deveriam ser multiplicados.
- Esquecer de subtrair a intersecao em eventos nao exclusivos.
- Tratar retiradas sem reposicao como eventos independentes.

## Exercicios

1. Um dado e uma moeda sao lancados. Calcule `P(numero par e cara)`.
2. Em uma amostra, `P(A) = 0,30`, `P(B) = 0,25` e `P(A e B) = 0`. Calcule `P(A ou B)`.
3. Em uma pesquisa, `P(A) = 0,50`, `P(B) = 0,40` e `P(A e B) = 0,22`. Calcule `P(A ou B)`.
4. Uma caixa tem 10 pecas, 3 defeituosas. Calcule a probabilidade de retirar duas defeituosas sem reposicao.

