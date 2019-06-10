import falcon


def test_get(client):
    rv = client.get('/api/v1/applications')
    assert rv.status == falcon.HTTP_OK


def test_post(client):
    rv = client.post(
        '/api/v1/applications',
        {},
        headers=""
    )
    assert rv.status == falcon.HTTP_OK
    assert rv.json['myparam'] == 'myvalue'
