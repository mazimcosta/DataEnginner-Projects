
import psycopg2
from dotenv import load_dotenv
from config.settings import ENV_FILE
load_dotenv(ENV_FILE)
import os

def conectar():
    conexao=psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )

    return conexao