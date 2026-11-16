from openpyxl import load_workbook


def ler_itens(caminho):
    planilha = load_workbook(caminho, read_only=True, data_only=True)
    try:
        aba = planilha.active
        itens = []

        # As quatro primeiras colunas possuem ID, nome, peso e valor.
        for identificador, nome, peso, valor in aba.iter_rows(
            min_row=2, max_col=4, values_only=True
        ):
            if identificador is None:
                continue

            itens.append({
                "id": int(identificador),
                "nome": str(nome),
                "peso": int(peso),
                "valor": int(valor),
            })

        return itens
    finally:
        planilha.close()
