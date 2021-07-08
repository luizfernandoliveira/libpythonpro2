from unittest.mock import Mock

import pytest

from libpythonpro2 import github_api


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('luizfernandoliveira')
    assert 'https://avatars.githubusercontent.com/u/68622358?v=4' == url

@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/68622358?v=4'
    resp_mock.json.return_value = {
        'login': 'luizfernandoliveira', 'id': 68622358,
        'avatar_url': url
    }
    get_mock = mocker.patch('libpythonpro2.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('luizfernandoliveira')
    assert 'https://avatars.githubusercontent.com/u/68622358?v=4'