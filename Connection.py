import psycopg2

class Connection:   

    def connect(self):
        dbname = "biblioteca"
        user = "postgres"
        password = "@postgres"
        host = "localhost"
        port = "5432"

        try:
            connection = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
            print("Conexão bem-sucedida!")

            cursor = connection.cursor()
            cursor.execute("SELECT version();")
            version = cursor.fetchone()
            print("Versão do PostgreSQL:", version[0])
            self.connection = connection
            return connection

        except psycopg2.Error as e:
            print("Erro ao conectar ao PostgreSQL:", e)