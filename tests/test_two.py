def test_two(client):
    assert client.get('/') == ''
