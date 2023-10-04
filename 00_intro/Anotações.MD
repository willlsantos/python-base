## Shebang
Em ambientes Linux é muito importante definir o comentário especial Shebang, nele especificamos qual interpretador será usado para executar o programa

```
#!/usr/bin/env python

print("Hello, World!")
```

A primeira linha informa o terminal que aquele programa roda com o Python3 da env em execução, esta forma é possivel omitir o interpretador e executar o script diretamente pelo seu nome.

## Expressão / Expression

É uma instrução onde um valor de retorno é esperado, ex:

1 + 1 -> 2 --  Expressão literal

8 > 10 -> Falso -- Expressão booleana

8 < 10 -> Verdadeiro -- Expressão booleana

## Declaração / Statement

Intrução que prepara o interpretador para uma determinada tarefa, mas não retorna valor.
ex:

if, else
def
for
while
pass

## Atribuição / Assignment

Instrução que pega o retorno de uma expressão e processa o seu valor com intuito de armazenar


ex:

```python
soma = 40 + 2 # O python sempre resolve da esquerda pra direita
soma += 3
soma -= 3
```

No primeiro exemplo, o python primeiro resolve a expressão que retorna um valor, que é 40 + 2.

Em seguida resolve o sinal de igual, que é o simbolo de atribuição que pega o valor para armazenar ou processar

Enfim a variavel (soma) onde o valor é armazenado
## Protocolo
É o que o objeto é capaz de fazer

## Tipo de dados Primários

Os tipos primários, são utilizados para armazenar uma única unidade de informação como por exemplo, um número ou um texto.
Tipos de dados primitivos: int, float, bool e NoneType
ex: 65

