## Implementação do Algoritmo de Karatsuba em Python

Este repositório contém uma implementação em Python do algoritmo de Karatsuba para multiplicação eficiente de inteiros grandes. O método reduz o número de multiplicações necessárias ao dividir os operandos em partes e combinar resultados recursivamente, alcançando complexidade subquadrática em relação à multiplicação escolar.

### Lógica da implementação (linha a linha de `main.py`)

1. `from typing import Tuple`: importa anotações de tipo opcionais usadas no arquivo.
2. Definição de `karatsuba(x: int, y: int) -> int`: função que retorna o produto de `x` e `y` usando Karatsuba.
3. Caso base imediato: se algum operando é zero, retorna `0`.
4. Segundo caso base: se algum operando tem módulo menor que `10`, realiza multiplicação direta `x * y`.
5. Cálculo do tamanho `n` em dígitos do maior operando (em valor absoluto) e definição de `m = n // 2` para o ponto de divisão.
6. Cálculo da base `10**m` para separar alto e baixo: `base = 10 ** m`.
7. Decomposição de `x` e `y` em alto/baixo com `divmod(abs(operando), base)`: `ax, bx` e `ay, by`.
8. Chamadas recursivas: `ac = karatsuba(ax, ay)` e `bd = karatsuba(bx, by)`.
9. Cálculo do termo cruzado via identidade de Karatsuba: `ad_bc = karatsuba(ax + bx, ay + by) - ac - bd`.
10. Combinação dos termos: `result = ac * 10**(2*m) + ad_bc * base + bd`.
11. Ajuste de sinal com XOR lógico sobre negatividade: `sign = -1 if ((x < 0) ^ (y < 0)) else 1`.
12. Retorno do produto assinado: `return sign * result`.
13. Bloco de teste em `if __name__ == "__main__":` que define dois inteiros grandes `a` e `b` e imprime `karatsuba(a, b)`.

## Como executar o projeto

- Pré-requisito: Python 3.8+ instalado.
- Passos:
  1. Clonar o repositório e entrar na pasta do trabalho:
     ```bash
     git clone <url-do-seu-repositorio>
     cd "Trabalho 1"
     ```
  2. Executar o programa:
     ```bash
     python main.py
     ```
  3. A saída será o produto de `a` por `b` calculado por Karatsuba.

## Relatório técnico

### Complexidade Ciclomática

- Fluxo de controle da função `karatsuba`:
  - Há decisões condicionais para os casos base e a recursão segue três chamadas por nível (para `ac`, `bd` e o termo combinado). Ao final, há um ajuste de sinal e retorno.

- Grafo de fluxo textual (nós e arestas):
  - Nós (N):
    1. Início da função
    2. Teste `x == 0 or y == 0`
    3. Retorno 0
    4. Teste `abs(x) < 10 or abs(y) < 10`
    5. Retorno `x * y`
    6. Cálculos de `n`, `m`, `base`, particionamento `ax,bx, ay,by`
    7. Chamada recursiva `ac = karatsuba(ax, ay)`
    8. Chamada recursiva `bd = karatsuba(bx, by)`
    9. Chamada recursiva para soma: `karatsuba(ax + bx, ay + by)` e cálculo de `ad_bc`
    10. Combinação `result`
    11. Cálculo do `sign`
    12. Retorno final
  - Arestas (E):
    - 1→2, 2→3 (verdadeiro), 2→4 (falso)
    - 4→5 (verdadeiro), 4→6 (falso)
    - 6→7, 7→8, 8→9, 9→10, 10→11, 11→12

  Considerando 12 nós e 12 arestas ao incluir transições de saída, temos `E = 12`, `N = 12`. Para um único componente conectado, `P = 1`.

- Cálculo da complexidade ciclomática:
  - Fórmula: `M = E − N + 2P`
  - `M = 12 − 12 + 2*1 = 2`.
  - Interpretação: dois pontos de decisão independentes (os dois casos base), demais passos são sequenciais.

### Complexidade Assintótica

- Complexidade temporal:
  - Melhor caso: `O(1)`.
  - Caso médio e pior caso: `O(n^{log_2 3}) ≈ O(n^{1.585})`, com três multiplicações de tamanho `n/2` e trabalho linear adicional por nível.

- Complexidade espacial:
  - `O(n)`, devido à profundidade da recursão e estruturas intermediárias proporcionais ao tamanho dos operandos.
