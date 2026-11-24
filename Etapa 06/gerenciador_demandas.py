# Lista global para armazenar as demandas em memória (cada demanda é um dicionário)
demandas = []

def cadastrar_demanda():
    print("\n--- CADASTRAR DEMANDA ---")
    id_demanda = input("Digite o ID único: ").strip()
    
    # Validação: verificar se o ID está vazio
    if not id_demanda:
        print("Erro: O ID não pode estar vazio.")
        return
        
    # Validação: verificar se já existe uma demanda com este ID (evitar duplicados)
    for d in demandas:
        if d["id"] == id_demanda:
            print(f"Erro: Já existe uma demanda com o ID {id_demanda}.")
            return

    titulo = input("Título da demanda: ").strip()
    solicitante = input("Nome do solicitante: ").strip()
    prioridade_str = input("Prioridade (1-Urgente, 2-Médio, 3-Baixo): ").strip()
    cep = input("CEP: ").strip()
    cidade = input("Cidade: ").strip()
    
    # Validação: bloquear campos obrigatórios vazios
    if not titulo or not solicitante or not cep or not cidade:
        print("Erro: Todos os campos devem ser preenchidos.")
        return

    try:
        prioridade = int(prioridade_str)
    except ValueError:
        prioridade = 3 # Valor padrão caso o utilizador digite algo inválido

    # Criação do dicionário da nova demanda
    nova_demanda = {
        "id": id_demanda,
        "titulo": titulo,
        "solicitante": solicitante,
        "prioridade": prioridade,
        "cep": cep,
        "cidade": cidade,
        "status": "Pendente"
    }
    
    demandas.append(nova_demanda)
    print("Sucesso: Demanda cadastrada com sucesso!")

def listar_demandas():
    print("\n--- LISTA DE DEMANDAS ---")
    if not demandas:
        print("Nenhuma demanda registada.")
        return
    for d in demandas:
        print(f"ID: {d['id']} | Título: {d['titulo']} | Solicitante: {d['solicitante']} | Status: {d['status']}")

def buscar_demanda():
    print("\n--- BUSCAR DEMANDA ---")
    termo = input("Digite o ID ou título para procurar: ").strip().lower()
    encontradas = [d for d in demandas if termo in d['id'].lower() or termo in d['titulo'].lower()]
    
    if not encontradas:
        print("Nenhuma demanda encontrada com esse termo.")
        return
        
    for d in encontradas:
        print(f"Encontrada -> ID: {d['id']}, Título: {d['titulo']}, Solicitante: {d['solicitante']}, Status: {d['status']}")

def atualizar_status():
    print("\n--- ATUALIZAR STATUS ---")
    id_demanda = input("Digite o ID da demanda que deseja atualizar: ").strip()
    for d in demandas:
        if d['id'] == id_demanda:
            novo_status = input("Novo status (ex: Em Andamento, Concluído): ").strip()
            if novo_status:
                d['status'] = novo_status
                print("Status atualizado com sucesso!")
            else:
                print("Erro: O status não pode estar vazio.")
            return
    print("Erro: Demanda não encontrada.")

def excluir_demanda():
    print("\n--- EXCLUIR DEMANDA ---")
    id_demanda = input("Digite o ID da demanda que deseja excluir: ").strip()
    global demandas
    tamanho_inicial = len(demandas)
    
    # Mantém na lista apenas as demandas cujo ID seja diferente do informado
    demandas = [d for d in demandas if d['id'] != id_demanda]
    
    if len(demandas) < tamanho_inicial:
        print("Demanda excluída com sucesso!")
    else:
        print("Erro: Demanda não encontrada.")
