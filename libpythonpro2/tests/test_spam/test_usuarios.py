from libpythonpro2.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Fernando')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)




def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Fernando'), Usuario(nome='Renzo')]
    for usuario in usuarios:
      sessao.salvar(usuario)
    assert usuarios == sessao.listar()
