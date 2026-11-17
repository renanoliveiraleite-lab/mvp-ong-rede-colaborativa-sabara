import re

def validar_cpf(cpf: str) -> bool:
    numeros = re.sub(r'\D', '', cpf)
    return len(numeros) == 11 and numeros != numeros[0] * 11

def registrar_entrega(cpf: str, ciclo: str, entregas_realizadas: list) -> dict:
    if not validar_cpf(cpf):
        return {"status": "erro", "mensagem": "CPF invalido"}
    chave = f"{cpf}-{ciclo}"
    if chave in entregas_realizadas:
        return {"status": "bloqueado", "mensagem": "Entrega ja realizada neste ciclo"}
    entregas_realizadas.append(chave)
    return {"status": "sucesso", "mensagem": "Entrega registrada com sucesso"}
