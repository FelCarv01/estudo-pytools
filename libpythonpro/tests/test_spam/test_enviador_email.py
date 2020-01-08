import pytest

from libpythonpro.spam.enviador_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['feliped3carvalho@gmail.com', 'foo@bar.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'pilacontra@gmail.com',
        'alguma coisa',
        'nada fejaozada'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'foobar.com']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'pilacontra@gmail.com',
            'alguma coisa',
            'nada fejaozada'
        )
