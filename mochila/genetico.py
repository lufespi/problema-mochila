from random import Random


def resolver_mochila_genetico(itens, capacidade, populacao=100,
                             geracoes=300, semente=42):
    if capacidade < 0 or populacao < 3 or geracoes < 0:
        raise ValueError("Parâmetros inválidos.")
    if any(item["peso"] <= 0 for item in itens):
        raise ValueError("Os pesos devem ser positivos.")
    n = len(itens)
    if not n:
        return 0, []

    rng = Random(semente)
    pesos = [item["peso"] for item in itens]
    valores = [item["valor"] for item in itens]
    ordem = sorted(range(n), key=lambda i: valores[i] / pesos[i])

    def fitness(cromossomo):
        return sum(v for v, gene in zip(valores, cromossomo) if gene)

    def reparar(cromossomo):
        # Remove os itens menos eficientes enquanto houver excesso de peso.
        peso = sum(p for p, gene in zip(pesos, cromossomo) if gene)
        for i in ordem:
            if peso <= capacidade:
                break
            if cromossomo[i]:
                cromossomo[i] = 0
                peso -= pesos[i]
        return cromossomo

    # Cada indivíduo é um vetor binário de itens selecionados.
    individuos = [reparar([rng.randint(0, 1) for _ in range(n)])
                  for _ in range(populacao)]

    for _ in range(geracoes):
        ranking = sorted(individuos, key=fitness, reverse=True)
        # Elitismo: preserva os dois melhores indivíduos.
        nova = [ranking[0].copy(), ranking[1].copy()]

        def selecionar():
            return max(rng.sample(ranking, 3), key=fitness)

        while len(nova) < populacao:
            pai, mae = selecionar(), selecionar()
            # Cruzamento de um ponto, com probabilidade de 85%.
            if n > 1 and rng.random() < 0.85:
                corte = rng.randrange(1, n)
                filho = pai[:corte] + mae[corte:]
            else:
                filho = pai.copy()

            # Mutação bit-flip: em média, um gene por descendente.
            for i in range(n):
                if rng.random() < 1 / n:
                    filho[i] = 1 - filho[i]
            nova.append(reparar(filho))
        individuos = nova

    melhor = max(individuos, key=fitness)
    return fitness(melhor), [item for item, gene in zip(itens, melhor) if gene]
