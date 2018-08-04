import dotrc

def test_load():
    config = dotrc.load('dot')
    print(config)

    assert config is not None
    assert config['id'] == 17
    assert config['name'] == 'John Doe'
    assert config['status'] == 'Active'
