import csv
import os

# Modul tehnic pentru procesarea datelor destinate integrării ERP (ex: SAP)
# Demonstrează culegerea, clasificarea și interpretarea informațiilor de gestiune.

def process_erp_data(input_file):
    print(f"[*] Inițiere procesare date din: {input_file}")
    
    if not os.path.exists(input_file):
        print("[!] Eroare: Fișierul de date nu a fost găsit pentru import.")
        return

    try:
        with open(input_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Logică analitică pentru identificarea stocurilor critice
                # Aceasta fluidizează informația pentru deciziile de aprovizionare
                cod = row.get('cod_produs', 'N/A')
                cantitate = int(row.get('cantitate', 0))
                
                if cantitate < 10:
                    print(f"[ALERTA STOC] Produsul {cod} necesită reaprovizionare (Cantitate: {cantitate})")
                else:
                    print(f"[INFO] Produs {cod}: Stoc optim.")
                    
    except Exception as e:
        print(f"[!] Eroare tehnică la procesarea datelor: {e}")

if __name__ == "__main__":
    # Simulare procesare fișier exportat din baza de date MySQL
    print("--- Sistem Gestiune Adrian Roman - Data Processor v1.0 ---")
    # process_erp_data('stocuri_export.csv') 

