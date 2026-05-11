# 09 - Distribuicao t de Student

Notebook base: `09_t_student.ipynb`

## Quando usar

A distribuicao t e usada principalmente quando:

- a amostra e pequena;
- o desvio padrao populacional e desconhecido;
- queremos inferir sobre a media.

## Estatistica t

```text
t = (media_amostral - media_hipotese) / (s / raiz(n))
```

Onde:

```text
s = desvio padrao amostral
n = tamanho da amostra
gl = n - 1
```

## Exemplo calculado

Uma amostra tem:

```text
n = 16
media_amostral = 52
s = 8
media_hipotese = 50
```

```text
erro_padrao = s / raiz(n) = 8 / 4 = 2
t = (52 - 50) / 2 = 1
gl = 16 - 1 = 15
```

## Intervalo de confianca para media

```text
IC = media_amostral +- t_critico * (s / raiz(n))
```

Exemplo com `t_critico = 2,131`:

```text
IC = 52 +- 2,131 * 2
IC = 52 +- 4,262
IC = [47,738; 56,262]
```

## Pontos importantes

- Quanto maior `n`, mais a t se aproxima da normal.
- A t tem caudas mais pesadas que a normal.
- O grau de liberdade mais comum para uma media e `n - 1`.

## Exercicios

1. Calcule `t` para `n = 25`, media amostral `103`, media hipotetica `100` e `s = 10`.
2. Calcule os graus de liberdade do item anterior.
3. Explique por que usamos `s / raiz(n)` no denominador.
4. Monte um intervalo de confianca usando `t_critico = 2,064`.

