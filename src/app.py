from src.app import hello_world

def test_hello():
    assert hello_world() == "Hello, GitHub Actions!"
