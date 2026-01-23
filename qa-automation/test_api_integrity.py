import requests
import pytest
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_URL = "http://localhost:8080/api/v1/erp"

def test_api_inventory_status_integrity():
    """
    Validare de Producție: Verifică dacă API-ul de gestiune 
    returnează codul 200 și mesajul de integritate corect.
    """
    endpoint = f"{BASE_URL}/inventory-status"
    
    try:
        response = requests.get(endpoint, timeout=5)
        
        # Validare Cod Status
        assert response.status_code == 200, f"Eroare API: Cod {response.status_code}"
        
        # Validare Conținut (Business Logic)
        data = response.text
        assert "Operational" in data
        assert "Database Integrity: 100%" in data
        
        logger.info("API Integrity Check: PASSED")
        
    except requests.exceptions.ConnectionError:
        pytest.fail("Sistemul Backend nu este pornit. Verifică Docker Compose.")

if __name__ == "__main__":
    pytest.main([__file__])
