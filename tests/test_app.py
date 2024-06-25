from fastapi.testclient import TestClient  

from challenge.app import app  

client = TestClient(app)