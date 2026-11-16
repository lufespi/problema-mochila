# Problema da Mochila

Programa em Python para resolver o problema da mochila 0/1 usando os 100 itens da planilha `dados/Dados.xlsx`.

## Algoritmo

Foi utilizada **Programação Dinâmica** para encontrar a combinação de itens de maior valor, sem ultrapassar a capacidade de 1.270 kg. Cada item pode ser escolhido uma única vez.

## Requisitos

- Python 3.10 ou superior
- Biblioteca `openpyxl`

Instale a dependência com:

```bash
pip install -r requirements.txt
```

## Execução

Na pasta principal do projeto, execute:

```bash
python -m mochila.main
```

O programa mostra o valor máximo, o peso utilizado e a lista de itens selecionados.
