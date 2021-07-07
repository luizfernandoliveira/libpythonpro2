from unittest.mock import Mock

import pytest

from libpythonpro2 import github_api


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('luizfernandoliveira')
    assert 'https://avatars.githubusercontent.com/u/68622358?v=4' == url

@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/68622358?v=4'
    resp_mock.json.return_value = {
        'login': 'luizfernandoliveira', 'id': 68622358,
        'avatar_url': url
    }
    github_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = github_original


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('luizfernandoliveira')
    assert 'https://avatars.githubusercontent.com/u/68622358?v=4'