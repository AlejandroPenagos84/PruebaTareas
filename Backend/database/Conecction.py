import json
import psycopg2

def readProperties():
    try:
        # Abre el archivo JSON en modo lectura
        with open('database\config.json', 'r') as file:
            # Carga el contenido del archivo JSON en un objeto Python
            obj = json.load(file)
            return obj
    except FileNotFoundError:
        raise FileNotFoundError
    
def get_connection():
    try:
        data = readProperties()

        return(psycopg2.connect(
            host=data["PGSQL_HOST"],
            user=data["PGSQL_USER"],
            password=data["PGSQL_PASSWORD"],
            dbname=data["PGSQL_NAME"]
        ))  
    except psycopg2.DatabaseError as ex:
        raise ex

