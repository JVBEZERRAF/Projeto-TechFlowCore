# utils.py - Funções auxiliares para o TechFlow Core

def limpar_terminal():
    # Simula um espaçamento limpo para o menu
    print("\n" * 2)

def validar_cep(cep):
    """Verifica se o CEP tem 8 dígitos (excluindo hífen opcional)."""
    cep_limpo = cep.replace("-", "").strip()
    return cep_limpo.isdigit() and len(cep_limpo) == 8
    
import urllib.request
import json

def consultar_cep_api(cep):
    """Consulta a API pública do ViaCEP para obter a cidade correspondente."""
    # Limpa o CEP para garantir apenas números
    cep_limpo = cep.replace("-", "").strip()
    
    if len(cep_limpo) != 8:
        return None
        
    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    
    try:
        # Faz o pedido HTTP à API do ViaCEP
        with urllib.request.urlopen(url) as resposta:
            dados = json.loads(resposta.read().decode('utf-8'))
            
            # Se a API retornar um erro "erro": true, o CEP não existe
            if "erro" in dados:
                return None
                
            # Retorna o nome da cidade encontrada
            return dados.get("localidade")
    except Exception:
        # Caso haja problemas de conexão à internet no laboratório
        return None