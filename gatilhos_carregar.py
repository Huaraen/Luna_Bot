def carregar_gatilhos(filepath):
    gatilhos = {}
    categoria_atual = None
    with open(filepath, 'r', encoding='utf-8') as file:
        for linha in file:
            linha = linha.strip()
            if linha.startswith('#'):
                categoria_atual = linha[1:].strip()
                gatilhos[categoria_atual] = []
            elif linha:
                gatilhos[categoria_atual].append(linha)
    return gatilhos
