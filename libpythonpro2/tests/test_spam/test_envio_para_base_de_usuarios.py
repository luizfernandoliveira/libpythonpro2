import pytest

from libpythonpro2.spam.enviador_de_email import Enviador
from libpythonpro2.spam.main import EnviadorDeSpam
from libpythonpro2.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome= 'Fernando', email='luiz.fernando@stine.com.br'),
            Usuario(nome= 'Renzo', email='renzo@python.pro.br')
        ],
        [
            Usuario(nome='Renzo', email='renzo@python.pro.br')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luiz.fernando_1990@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados