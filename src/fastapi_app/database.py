import os
import psycopg2
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from dotenv import load_dotenv

load_dotenv()

def get_secret(secret_name):
    key_vault_name = os.getenv("KEY_VAULT_NAME")
    key_vault_uri = f"https://{key_vault_name}.vault.azure.net"
    credential = DefaultAzureCredential()
    secret_client = SecretClient(vault_url=key_vault_uri, credential=credential)
    return secret_client.get_secret(secret_name).value

def get_db_connection():
    host = get_secret("POSTGRES-HOST")
    port = get_secret("POSTGRES-PORT")
    database = get_secret("POSTGRES-DATABASE")
    username = get_secret("POSTGRES-USERNAME")
    password = get_secret("POSTGRES-PASSWORD")
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=username,
        password=password
    )
    return conn

def get_items():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, description, is_complete FROM todo_items")
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"id": item[0], "name": item[1], "description": item[2], "is_complete": item[3]} for item in items]