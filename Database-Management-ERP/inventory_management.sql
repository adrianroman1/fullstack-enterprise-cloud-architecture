-- Script pentru gestiunea stocurilor și analiză ERP
-- Creat pentru demonstrarea competențelor de administrare baze de date MySQL

CREATE DATABASE IF NOT EXISTS Gestiune_Bijuteria;
USE Gestiune_Bijuteria;

-- Tabel pentru intrări/ieșiri produse (Gestiune Inventar)
CREATE TABLE Stocuri (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cod_produs VARCHAR(50) NOT NULL,
    nume_produs VARCHAR(100),
    cantitate INT DEFAULT 0,
    pret_unitar DECIMAL(10,2),
    ultima_actualizare TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Interogare pentru generarea raportului de stoc critic (Analiză Analitică)
-- Aceasta identifică produsele care necesită reaprovizionare imediată
SELECT cod_produs, nume_produs, cantitate 
FROM Stocuri 
WHERE cantitate < 5;

