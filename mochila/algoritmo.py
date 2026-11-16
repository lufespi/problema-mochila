def resolver_mochila(itens, capacidade):
    quantidade = len(itens)
    tabela = [[0] * (capacidade + 1) for _ in range(quantidade + 1)]

    # Calcula o melhor valor para cada quantidade de itens e capacidade.
    for i in range(1, quantidade + 1):
        peso = itens[i - 1]["peso"]
        valor = itens[i - 1]["valor"]

        for limite in range(capacidade + 1):
            sem_item = tabela[i - 1][limite]

            if peso <= limite:
                com_item = valor + tabela[i - 1][limite - peso]
                tabela[i][limite] = max(sem_item, com_item)
            else:
                tabela[i][limite] = sem_item

    # Percorre a tabela de trás para frente para descobrir os itens escolhidos.
    escolhidos = []
    limite = capacidade

    for i in range(quantidade, 0, -1):
        if tabela[i][limite] != tabela[i - 1][limite]:
            item = itens[i - 1]
            escolhidos.append(item)
            limite -= item["peso"]

    escolhidos.reverse()
    return tabela[quantidade][capacidade], escolhidos
