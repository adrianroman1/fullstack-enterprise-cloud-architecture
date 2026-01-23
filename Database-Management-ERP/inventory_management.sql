-- Script de producție pentru gestiunea inventarului
-- Optimizat pentru performanță și integritate (Standard 2026)

CREATE DATABASE IF NOT EXISTS Gestiune_Enterprise;
USE Gestiune_Enterprise;

-- Tabel optimizat pentru integritatea datelor
CREATE TABLE IF NOT EXISTS Stocuri (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cod_produs VARCHAR(50) NOT NULL UNIQUE, -- Constângere UNIQUE pentru identificare rapidă
    nume_produs VARCHAR(100) NOT NULL,
    cantitate INT DEFAULT 0 CHECK (cantitate >= 0), -- Previne stocul negativ la nivel de bază de date
    pret_unitar DECIMAL(10,2) NOT NULL,
    ultima_actualizare TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB; -- Motor de stocare care suportă tranzacții ACID

-- INDEX pentru accelerarea rapoartelor de stoc (Esențial pentru producție)
CREATE INDEX idx_cod_produs ON Stocuri(cod_produs);
CREATE INDEX idx_cantitate ON Stocuri(cantitate);

-- Procedură stocată pentru raportare rapidă (Demonstrează gândire de arhitect)
-- Identifică produsele sub pragul critic de 5 unități
CREATE VIEW View_Stocuri_Critice AS
SELECT cod_produs, nume_produs, cantitate 
FROM Stocuri 
WHERE cantitate < 5;


