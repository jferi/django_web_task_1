# UtazzNézd

Az UtazzNézd egy utazási cég Django-alapú weboldala: városnéző programokat listáz, a látogatók pedig véleményt írhatnak.

## Oldalak

| Útvonal        | Tartalom                               |
| -------------- | -------------------------------------- |
| `/`            | Rólunk                                 |
| `/programok/`  | Városnéző programok                    |
| `/velemenyek/` | Vélemények és új vélemény beküldése    |
| `/kapcsolat/`  | Kapcsolat                              |

## Technológia

- Python 3.9+
- Django 4.2
- Bootstrap 5 (`django-bootstrap-v5`)
- SQLite

## Futtatás

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cd projekt
python manage.py runserver
```

Az oldal ezután itt érhető el: <http://127.0.0.1:8000/>

## Adatok

A `projekt/db.sqlite3` már tartalmazza a mintaadatokat (6 program, 2 vélemény), így külön lépés nem kell.

Üres adatbázist így lehet újra feltölteni:

```bash
cd projekt
python manage.py migrate
python manage.py shell < pythonshell.py
```
