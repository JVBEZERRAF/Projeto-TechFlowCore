# utils.py - Funções auxiliares para o TechFlow Core

def limpar_terminal():
    # Simula um espaçamento limpo para o menu
    print("\n" * 2)

def validar_cep(cep):
    """Verifica se o CEP tem 8 dígitos (excluindo hífen opcional)."""
    cep_limpo = cep.replace("-", "").strip()
    return cep_limpo.isdigit() and len(cep_limpo) == 8
