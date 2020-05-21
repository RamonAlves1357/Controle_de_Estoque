# Controle_de_Estoque
 Projetinho desenvolvido com django, com base em um tutorial do canal Regis do Python, no Youtube

## Este projeto foi feito com:
- Python 3.8.2
- Django 3.0.6
- SQLparse 0.3.1

## Como rodar o projeto?
1. Clone esse repositório.
    ```
    1. git clone https://github.com/RamonAlves1357/Controle_de_Estoque
    2. cd Controle_de_Estoque
    ```
2. Crie um virtualenv com Python 3.
    ```
    3. python3 -m venv .venv
    ```
3. Ative o virtualenv.
    - No linux: 
        ```
        4. source .venv/bin/activate
        ```
    - No Windows:
        ```
        4. .venv\scripts\activate
        ```

4. Instale as dependências.
    ```
    5. pip install --upgrade pip
    6. pip install django
    7. pip install -r requirements.txt
    8. python contrib/env_gen.py
    ```

5. Rode as migrações.
    ```
    9. python manage.py migrate
    10. python manage.py createsuperuser
    11. python manage.py runserver
    ```
