import pytest

from libpythonpro2.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['luiz.fernando_1990@homail.com', 'renzo@pythonpro.br']
)
def test_remetente(destinatario):
    enviador = Enviador()

    resultado = enviador.enviar(
        destinatario,
        'luiz.fernando_1990@hotmail.com',        #destinatário
        'Curso Python Pro',                      #assunto do email
        'Primeira turma',                        #corpo do email
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'renzo']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'luiz.fernando_1990@hotmail.com',        #destinatário
            'Curso Python Pro',                      #assunto do email
            'Primeira turma',                        #corpo do email
    )

