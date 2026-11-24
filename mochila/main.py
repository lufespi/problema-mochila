import argparse
from pathlib import Path
from time import perf_counter

from mochila.algoritmo import resolver_mochila
from mochila.busca_tabu import resolver_mochila_tabu
from mochila.genetico import resolver_mochila_genetico
from mochila.leitor import ler_itens


CAPACIDADE = 1270
ARQUIVO = Path(__file__).resolve().parent.parent / "dados" / "Dados.xlsx"


def main():
    parser = argparse.ArgumentParser(description="Problema da Mochila 0/1")
    parser.add_argument("metodo", nargs="?", default="genetico",
                        choices=["genetico", "tabu", "dinamica", "todos"])
    args = parser.parse_args()
    itens = ler_itens(ARQUIVO)
    metodos = {
        "genetico": ("Algoritmo Genético", resolver_mochila_genetico),
        "tabu": ("Busca Tabu", resolver_mochila_tabu),
        "dinamica": ("Programação Dinâmica", resolver_mochila),
    }
    resultados = {}
    for chave in metodos if args.metodo == "todos" else [args.metodo]:
        nome, resolver = metodos[chave]
        inicio = perf_counter()
        valor, selecionados = resolver(itens, CAPACIDADE)
        tempo = perf_counter() - inicio
        peso = sum(item["peso"] for item in selecionados)
        resultados[chave] = (valor, peso, tempo)

        print(f"\nPROBLEMA DA MOCHILA (0/1) - {nome}")
        print(f"Itens disponíveis: {len(itens)}")
        print(f"Capacidade: {CAPACIDADE} kg")
        print(f"{'Valor ótimo' if chave == 'dinamica' else 'Melhor valor encontrado'}: $ {valor}")
        print(f"Peso utilizado: {peso} kg")
        print(f"Itens selecionados: {len(selecionados)}")
        print(f"Tempo de execução: {tempo:.4f} s\n")
        print(f"{'ID':>3}  {'Item':<12}  {'Peso (kg)':>9}  {'Valor ($)':>9}")
        for item in selecionados:
            print(f"{item['id']:>3}  {item['nome']:<12}  "
                  f"{item['peso']:>9}  {item['valor']:>9}")

    if args.metodo == "todos":
        otimo = resultados["dinamica"][0]
        print("\nCOMPARAÇÃO COM O ÓTIMO EXATO")
        for chave, (valor, peso, tempo) in resultados.items():
            gap = 100 * (otimo - valor) / otimo if otimo else 0
            print(f"{metodos[chave][0]}: $ {valor} | {peso} kg | "
                  f"gap: {gap:.4f}% | {tempo:.4f} s")


if __name__ == "__main__":
    main()
