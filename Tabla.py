import pandas as pd

class Tabla(): 
    def __init__(self, path):
        self.path = path
        self.data = pd.read_csv(path)
    
    def get_data(self):
        return self.data
    
    def slice_by_column(self, list):
        self.data = self.data[list].drop_duplicates()
        return self

    def export_to_sql(self, cursor, table_name):
        for index, row in self.data.iterrows():
            placeholders = ', '.join(['?'] * len(row))
            columns = ', '.join(row.keys())
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            cursor.execute(sql, tuple(row))
        cursor.commit()