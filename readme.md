# Veziv.ro Tombola

## Descriere

Tombola este o aplicatie web interactiva pentru gestionarea si desfasurarea de tombole online. Proiectul ofera o solutie completa pentru vanzarea biletelor si extragerea castigatorilor intr-un mod simplu si eficient. Utilizatorii pot vizualiza biletele disponibile, le pot achizitiona si pot participa la extragerea castigatorilor.

Functionalitati Principale:

    Vizualizarea Biletelor Disponibile: Utilizatorii pot vedea toate biletele disponibile, inclusiv cele deja vandute.
    Achizitionarea Biletelor: Biletele disponibile pot fi cumparate direct din aplicatie.
    Extragerea Castigatorilor: Administratorii pot extrage un castigator din biletele vandute folosind un generator de numere aleatorii.

Tehnologii Folosite
Back-end:
    Python: Limbajul principal utilizat pentru dezvoltarea logicii aplicatiei.
    Flask: Framework web care faciliteaza dezvoltarea aplicatiei server-side si gestionarea rutelor.
    SQLAlchemy: ORM (Object-Relational Mapping) utilizat pentru interactiunea cu baza de date PostgreSQL, simplificand operatiunile CRUD si gestionarea relatiilor intre entitati.
    PostgreSQL: Sistem de gestionare a bazelor de date relationale care stocheaza informatiile despre bilete si achizitii.

Front-end:
    HTML: Limbaj de marcare utilizat pentru structura paginilor web.
    CSS: Folosit pentru stilizarea si designul paginilor web, creand o interfata placuta si usor de utilizat.

### Clonare repository

Clonare repository-ului în directorul local:

git clone https://github.com/pistiro/Veziv.ro.git
cd Veziv.ro

## Creare database Docker
docker run --name database_name -e POSTGRES_USER=database_user -e POSTGRES_PASSWORD=database_password -e POSTGRES_DB=My_database -p 5432:5432 -v postgres_data:/var/lib/postgresql/data -d postgres:latest

## Creare tabel in DB
CREATE TABLE ticket (
    id SERIAL PRIMARY KEY,
    number INTEGER UNIQUE NOT NULL,
    purchased BOOLEAN DEFAULT FALSE
);

## Popularea tabelului
INSERT INTO ticket (number, purchased) VALUES (1, FALSE);
INSERT INTO ticket (number, purchased) VALUES (2, TRUE);

## Instalare
pip install -r requirements.txt

## Creare mmediu virtual
python -m venv env

## Activare mediu virtual
source env/Scripts/activate
source venv/bin/activate - in cazul linux

## Rularea proiectului
In mediul virtual rulati urmatoarea comanda ./run.sh (este configurat)
