def calc(d):
    prioridades = {
        1: "Urgente - 1 dia",
        2: "Medio - 3 dias",
        3: "Baixo - 5 dias"
    }
    # Retorna o valor correspondente ou um padrão caso a chave não exista
    return prioridades.get(d.get('p'), "Baixo - 5 dias")
