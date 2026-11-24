def resolver_mochila_tabu(itens, capacidade, iteracoes=500, tenure=7):
    if capacidade < 0 or iteracoes < 0 or tenure < 1:
        raise ValueError("Parâmetros inválidos.")

    if any(item["peso"] <= 0 for item in itens):
        raise ValueError("Os pesos dos itens devem ser positivos.")

    # Começa com uma solução gulosa, pela relação valor/peso.
    ordem = sorted(range(len(itens)), key=lambda i: (
        -itens[i]["valor"] / itens[i]["peso"], i
    ))
    atual = set()
    peso = valor = 0
    for i in ordem:
        if peso + itens[i]["peso"] <= capacidade:
            atual.add(i)
            peso += itens[i]["peso"]
            valor += itens[i]["valor"]

    melhor = atual.copy()
    melhor_valor = valor
    lista_tabu = {}

    for iteracao in range(1, iteracoes + 1):
        dentro = sorted(atual)
        fora = [i for i in range(len(itens)) if i not in atual]
        # Movimentos: retirar, inserir ou trocar um item por outro.
        movimentos = [(i, None) for i in dentro]
        movimentos += [(None, j) for j in fora]
        movimentos += [(i, j) for i in dentro for j in fora]

        escolhido = None
        maior_valor = -float("inf")
        for retirar, inserir in movimentos:
            novo_peso, novo_valor = peso, valor
            if retirar is not None:
                novo_peso -= itens[retirar]["peso"]
                novo_valor -= itens[retirar]["valor"]
            if inserir is not None:
                novo_peso += itens[inserir]["peso"]
                novo_valor += itens[inserir]["valor"]
            if novo_peso > capacidade:
                continue

            # Um item alterado fica bloqueado nas próximas tenure iterações.
            tabu = any(lista_tabu.get(i, 0) >= iteracao
                       for i in (retirar, inserir) if i is not None)
            # Aspiração: permite tabu somente se superar o melhor global.
            if tabu and novo_valor <= melhor_valor:
                continue
            if novo_valor > maior_valor:
                escolhido = (retirar, inserir, novo_peso, novo_valor)
                maior_valor = novo_valor

        if escolhido is None:
            break

        # Aceita o melhor vizinho admissível, mesmo se for pior.
        retirar, inserir, peso, valor = escolhido
        if retirar is not None:
            atual.remove(retirar)
            lista_tabu[retirar] = iteracao + tenure
        if inserir is not None:
            atual.add(inserir)
            lista_tabu[inserir] = iteracao + tenure

        if valor > melhor_valor:
            melhor = atual.copy()
            melhor_valor = valor

    return melhor_valor, [itens[i] for i in sorted(melhor)]
