import pytest
import logging
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurare Logging profesional pentru 2026
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class EnterpriseDashboardPage:
    """Clasă de tip Page Object Model pentru abstractizarea interfeței"""
    def __init__(self, driver):
        self.driver = driver
        self.url = os.getenv("APP_URL", "http://localhost:3000")
        self.data_grid_id = "data-grid-main"

    def navigate(self):
        logger.info(f"Navigare către: {self.url}")
        self.driver.get(self.url)

    def is_data_grid_visible(self):
        try:
            wait = WebDriverWait(self.driver, 15)
            element = wait.until(EC.visibility_of_element_located((By.ID, self.data_grid_id)))
            return element.is_displayed()
        except Exception as e:
            logger.error(f"Elementul {self.data_grid_id} nu a fost găsit: {e}")
            return False

@pytest.fixture
def driver():
    """Configurare Driver optimizată pentru medii Linux/Docker CI/CD"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_dashboard_load_performance(driver):
    """
    Validare nivel Enterprise: Verifică integritatea interfeței și 
    performanța încărcării grid-ului de date.
    """
    dashboard = EnterpriseDashboardPage(driver)
    dashboard.navigate()
    
    # 1. Validare titlu (Business Identity)
    assert "Enterprise" in driver.title, f"Titlul așteptat 'Enterprise' nu a fost găsit. Titlu curent: {driver.title}"
    
    # 2. Validare prezență date (Data Integrity)
    assert dashboard.is_data_grid_visible(), "Grid-ul principal de date nu a fost încărcat în timpul util."
    
    logger.info("QA Status: Dashboard performance and integrity check PASSED.")

if __name__ == "__main__":
    pytest.main([__name__])


