# Controle_de_Estoque
 Projetinho desenvolvido com django, com base em um tutorial do canal Regis do Python, no Youtube

## Como rodar o projeto?
- Clone esse repositório.
- Crie um virtualenv com Python 3.
- Ative o virtualenv.
- Instale as dependências.
- Rode as migrações.

```
git clone https://github.com/RamonAlves1357/Controle_de_Estoque
cd Controle_de_Estoque
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
