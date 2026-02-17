from decouple import config
import psycopg2
import sys


def main():
    db_name = config('DB_NAME', default='semillero_db')
    db_user = config('DB_USER', default='postgres')
    db_password = config('DB_PASSWORD', default='')
    db_host = config('DB_HOST', default='localhost')
    db_port = config('DB_PORT', default='5432')

    # Connect to default maintenance DB to create the target database if needed
    conn = None
    try:
        conn = psycopg2.connect(
            dbname='postgres', user=db_user, password=db_password, host=db_host, port=db_port
        )
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (db_name,))
        exists = cur.fetchone()
        if exists:
            print(f"La base de datos '{db_name}' ya existe. No se requiere acción.")
        else:
            cur.execute(f"CREATE DATABASE \"{db_name}\" WITH ENCODING 'UTF8'")
            print(f"Base de datos '{db_name}' creada correctamente.")
        cur.close()
    except Exception as e:
        print("Error al crear/verificar la base de datos:", e)
        sys.exit(1)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    main()
