# Problema da Mochila

Programa em Python para resolver o problema da mochila 0/1 com os 100 itens de `dados/Dados.xlsx` e capacidade de 1.270 kg. Cada item pode ser escolhido uma única vez.

## Algoritmos

- **Algoritmo Genético:** população de 100 cromossomos binários, 300 gerações, seleção por torneio (3 indivíduos), cruzamento de um ponto (85%), mutação bit-flip (1/n por gene), elitismo (2 indivíduos) e reparo de peso. Semente 42 para reproduzir a execução.
- **Busca Tabu:** solução inicial gulosa, movimentos de inserção, remoção e troca, lista tabu de 7 iterações, aspiração e limite de 500 iterações. Mantém as soluções viáveis.
- **Programação Dinâmica:** método exato, usado como referência para comparar as metaheurísticas.

## Requisitos

- Python 3.10 ou superior
- Biblioteca `openpyxl`

```bash
pip install -r requirements.txt
```

## Execução

Na pasta principal do projeto:

```bash
python -m mochila.main genetico
python -m mochila.main tabu
python -m mochila.main dinamica
python -m mochila.main todos
```

Sem argumento, `python -m mochila.main` executa o Algoritmo Genético. O modo `todos` compara os três métodos com o ótimo exato, mostrando valor, peso, tempo de processamento (sem leitura da planilha) e diferença percentual para o ótimo.

As metaheurísticas retornam a melhor solução encontrada, sem garantia de otimalidade.
