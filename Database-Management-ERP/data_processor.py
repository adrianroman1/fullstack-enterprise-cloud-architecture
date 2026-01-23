import csv
import os
import logging

# Configurare Logging de producție
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def process_erp_data(input_file):
    """
    Procesează datele de inventar pentru integrarea cu sisteme ERP (ex. SAP).
    Include logică de validare și alertare automată.
    """
    logger.info(f"Inițiere procesare date din: {input_file}")
    
    if not os.path.exists(input_file):
        logger.error(f"Fișierul {input_file} nu a fost găsit. Verifică montarea volumului în Docker.")
        return

    try:
        with open(input_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Validare date (Standard de producție)
                cod = row.get('cod_produs', 'N/A')
                try:
                    cantitate = int(row.get('cantitate', 0))
                except ValueError:
                    logger.warning(f"Format cantitate invalid pentru produsul {cod}")
                    continue
                
                # Logică analitică pentru stocuri critice
                if cantitate < 10:
                    logger.warning(f"[STOC CRITIC] Produsul {cod} necesită aprovizionare. Cantitate: {cantitate}")
                else:
                    logger.debug(f"Produs {cod}: Stoc în parametri optimi.")
                    
    except Exception as e:
        logger.critical(f"Eroare sistemică la procesarea datelor ERP: {e}")

if __name__ == "__main__":
    # În producție, calea fișierului poate fi preluată dintr-o variabilă de mediu
    DATA_PATH = os.getenv('ERP_DATA_PATH', 'stocuri_export.csv')
    process_erp_data(DATA_PATH)


