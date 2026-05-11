# 11 - Graus de liberdade

Notebook base: `11_graus_de_liberdade.ipynb`

## Ideia central

Graus de liberdade representam quantas informacoes podem variar livremente depois que uma restricao foi imposta.

## Media amostral

Quando a media amostral e fixada, apenas `n - 1` valores podem variar livremente.

```text
gl = n - 1
```

Exemplo: tres valores tem media 10.

```text
x1 + x2 + x3 = 30
```

Se escolhermos:

```text
x1 = 8
x2 = 12
```

O terceiro fica determinado:

```text
x3 = 30 - 8 - 12 = 10
```

Logo, apenas 2 valores variam livremente.

## Qui-quadrado de aderencia

```text
gl = numero de categorias - 1 - parametros_estimados
```

Se nao houver parametros estimados:

```text
gl = k - 1
```

## Tabela de contingencia

Para teste qui-quadrado de independencia:

```text
gl = (linhas - 1) * (colunas - 1)
```

Exemplo: tabela `3 x 4`.

```text
gl = (3 - 1) * (4 - 1) = 2 * 3 = 6
```

## Teste t

Para uma media:

```text
gl = n - 1
```

Para duas amostras independentes com variancias assumidas iguais:

```text
gl = n1 + n2 - 2
```

## ANOVA

```text
gl_entre = k - 1
gl_dentro = N - k
gl_total = N - 1
```

## Exercicios

1. Uma amostra tem `n = 12`. Calcule os graus de liberdade para estimar a variancia.
2. Uma tabela de contingencia tem 2 linhas e 5 colunas. Calcule os graus de liberdade.
3. Uma ANOVA tem 3 grupos e 27 observacoes. Calcule `gl_entre`, `gl_dentro` e `gl_total`.
4. Um teste qui-quadrado de aderencia tem 6 categorias e 1 parametro estimado. Calcule os graus de liberdade.

