import re


def nome_válido(nome):
    return nome.isalpha()
        
def cpf_valido(numero_cpf):
    return len(numero_cpf )== 11
        
def rg_valido(numero_rg):
    return len(numero_rg )== 9

def celular_valido(n_celular):
    '''Verifica se o número de celular é válido (XX) 9 XXXX-XXXX'''

    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, n_celular)

    return resposta
