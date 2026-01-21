import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_dashboard_load_performance():
    """
    Test demonstrativ pentru verificarea încărcării interfeței 
    și a elementelor de tip Enterprise.
    """
    # Configurare Chrome pentru rulare în CI/CD (Headless)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    
    try:
        # Link către frontend-ul aplicației (simulat)
        driver.get("http://localhost:3000") 
        
        # Verificăm dacă titlul paginii conține cuvintele cheie
        assert "Enterprise" in driver.title
        
        # Verificăm prezența unui element de date (Specific pentru React/Angular/SAPUI5)
        data_table = driver.find_element(By.ID, "data-grid-main")
        assert data_table.is_displayed()
        
        print("QA Check: Dashboard elements loaded successfully.")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    pytest.main([__file__])
  
