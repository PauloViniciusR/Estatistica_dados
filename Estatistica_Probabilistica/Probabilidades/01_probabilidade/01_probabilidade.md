# 01 - Probabilidade

Notebook base: `01_probabilidade.ipynb`

## Calculos principais

### Probabilidade classica

Quando todos os resultados sao igualmente provaveis:

```text
P(A) = numero de casos favoraveis / numero de casos possiveis
```

Exemplo: probabilidade de sair numero par em um dado comum.

```text
Espaco amostral = {1, 2, 3, 4, 5, 6}
A = {2, 4, 6}
P(A) = 3 / 6 = 0,5
```

### Complemento

```text
P(A^c) = 1 - P(A)
```

Exemplo: se `P(chover) = 0,30`, entao:

```text
P(nao chover) = 1 - 0,30 = 0,70
```

### Uniao de eventos

Para evitar contar a intersecao duas vezes:

```text
P(A ou B) = P(A) + P(B) - P(A e B)
```

Exemplo:

```text
P(A) = 0,40
P(B) = 0,50
P(A e B) = 0,20
P(A ou B) = 0,40 + 0,50 - 0,20 = 0,70
```

### Probabilidade condicional

```text
P(A | B) = P(A e B) / P(B)
```

Interpretacao: probabilidade de `A` acontecer sabendo que `B` ja aconteceu.

Exemplo:

```text
P(A e B) = 0,18
P(B) = 0,30
P(A | B) = 0,18 / 0,30 = 0,60
```

## Pontos que exigem atencao

- Em `P(A | B)`, o universo deixa de ser o espaco amostral completo e passa a ser apenas `B`.
- Na uniao, subtraia a intersecao quando os eventos puderem acontecer juntos.
- Probabilidades sempre ficam entre `0` e `1`.

## Exercicios

1. Em uma turma de 40 alunos, 18 gostam de Python, 14 gostam de SQL e 8 gostam dos dois. Calcule a probabilidade de um aluno gostar de Python ou SQL.
2. Em uma caixa ha 5 bolas vermelhas e 3 azuis. Calcule a probabilidade de retirar uma bola vermelha.
3. Se `P(A) = 0,65`, calcule `P(A^c)`.
4. Se `P(A e B) = 0,12` e `P(B) = 0,40`, calcule `P(A | B)`.

