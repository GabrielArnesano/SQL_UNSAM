import os
import json
import pyodbc

class Cursor(): 

    def __init__(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_dir, 'config.json')

        try:
            with open(config_path) as archivo_config:
                self.configuracion = json.load(archivo_config)
            self.configuracion
        except Exception as e:
            print(f"Error al cargar el archivo de configuración: {e}")
            return None

    def db_connect_sql_auth(self):
        '''
        devuelve la conexión al servidor y base de datos especificados
        '''
        self.conn = pyodbc.connect(
        DRIVER='{ODBC Driver 18 for SQL Server}',
        SERVER= self.configuracion['server_connection']['server'],
        DATABASE= self.configuracion['server_connection']['database'],
        UID= self.configuracion['server_connection']['user'],
        PWD= self.configuracion['server_connection']['password'],
        )
        return self.conn.cursor()
    
    def db_connect_windows_local(self,server):
        '''
        devuelve la conexión al servidor y base de datos especificados
        '''
        self.conn = pyodbc.connect(
        DRIVER='{SQL Server}',
        SERVER= server,  
        DATABASE= self.configuracion['server_connection']['database'],
        Trusted_Connection='yes',
        )
        return self.conn.cursor()

    
