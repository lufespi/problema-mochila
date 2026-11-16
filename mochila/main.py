from pathlib import Path

from mochila.algoritmo import resolver_mochila
from mochila.leitor import ler_itens


CAPACIDADE = 1270
ARQUIVO = Path(__file__).resolve().parent.parent / "dados" / "Dados.xlsx"


def main():
    itens = ler_itens(ARQUIVO)
    valor_maximo, selecionados = resolver_mochila(itens, CAPACIDADE)
    peso_total = sum(item["peso"] for item in selecionados)

    print("PROBLEMA DA MOCHILA (0/1)")
    print(f"Itens disponíveis: {len(itens)}")
    print(f"Capacidade: {CAPACIDADE} kg")
    print(f"Valor máximo: $ {valor_maximo}")
    print(f"Peso utilizado: {peso_total} kg")
    print(f"Itens selecionados: {len(selecionados)}")
    print()
    print(f"{'ID':>3}  {'Item':<12}  {'Peso (kg)':>9}  {'Valor ($)':>9}")

    for item in selecionados:
        print(
            f"{item['id']:>3}  {item['nome']:<12}  "
            f"{item['peso']:>9}  {item['valor']:>9}"
        )


if __name__ == "__main__":
    main()
