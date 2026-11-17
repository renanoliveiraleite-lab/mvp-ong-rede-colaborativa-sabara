from backend.main import validar_cpf, registrar_entrega

def test_validacao_cpf_valido():
    assert validar_cpf("123.456.789-01") is True

def test_validacao_cpf_invalido():
    assert validar_cpf("111.111.111-11") is False
    assert validar_cpf("12345") is False

def test_integracao_registro_entrega_sucesso():
    banco_ficticio = []
    resultado = registrar_entrega("123.456.789-01", "2026/04", banco_ficticio)
    assert resultado["status"] == "sucesso"

def test_integracao_bloqueio_duplicidade_ciclo():
    banco_ficticio = ["123.456.789-01-2026/04"]
    resultado = registrar_entrega("123.456.789-01", "2026/04", banco_ficticio)
    assert resultado["status"] == "bloqueado"
