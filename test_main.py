import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def setup_items():
    client.post("/items/1", json={"name": "item1"})
    client.post("/items/2", json={"name": "item2"})
    client.post("/items/4", json={"name": "item4"})
    yield
    client.delete("/items/1")
    client.delete("/items/2")
    client.delete("/items/4")

def test_read_all_items():
    response = client.get("/items")
    print(f"All items: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {}

def test_create_item():
    response = client.post("/items/1", json={"name": "item1"})
    print(f"Create 1 response: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"message": "Item criado com sucesso"}

    response = client.post("/items/1", json={"name": "item1"})
    print(f"Create 1 twice response: {response.json()}")
    assert response.status_code == 400
    assert response.json() == {"detail": "Item já existe"}

def test_read_item(setup_items):
    response = client.get("/items/2")
    print(f"Read item 2 response: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"name": "item2"}

    response = client.get("/items/3")
    print(f"Read item 3 response: {response.json()}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item não encontrado"}

def test_update_item(setup_items):
    response = client.put("/items/4", json={"name": "updated_item4"})
    assert response.status_code == 200
    print(f"Update item 4 response: {response.json()}")
    assert response.json() == {"message": "Item atualizado com sucesso"}

    response = client.put("/items/5", json={"name": "item5"})
    print(f"Update item 5 response: {response.json()}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item não encontrado"}

def test_delete_item(setup_items):
    client.post("/items/6", json={"name": "item6"})
    response = client.delete("/items/6")
    print(f"Delete item 6 response: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"message": "Item removido com sucesso"}

    response = client.delete("/items/7")
    print(f"Delete item 7 response: {response.json()}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item não encontrado"}

def test_read_all_items_with_data(setup_items):
    response = client.get("/items")
    print(f"All items with data: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {'1': {'name': 'item1'}, '2': {'name': 'item2'}, '4': {'name': 'updated_item4'}}
    print(f"Read item 2 response: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"name": "item2"}

    response = client.get("/items/3")
    print(f"Read item 3 response: {response.json()}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item não encontrado"}

def test_update_item():
    client.post("/items/4", json={"name": "item4"})
    response = client.put("/items/4", json={"name": "updated_item4"})
    assert response.status_code == 200
    print(f"Update item 4 response: {response.json()}")
    assert response.json() == {"message": "Item atualizado com sucesso"}

    response = client.put("/items/5", json={"name": "item5"})
    print(f"Update item 5 response: {response.json()}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item não encontrado"}

def test_delete_item():
    client.post("/items/6", json={"name": "item6"})
    response = client.delete("/items/6")
    print(f"Delete item 6 response: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"message": "Item removido com sucesso"}

    response = client.delete("/items/7")
    print(f"Delete item 7 response: {response.json()}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item não encontrado"}

def test_read_all_items_with_data():
    response = client.get("/items")
    print(f"All items with data: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {'4': {'name': 'updated_item4'}}