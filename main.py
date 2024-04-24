from Tabla import Tabla
from Cursor import Cursor
import os

if __name__ == "__main__":
    cursor = Cursor().db_connect_windows_local(fr'SANTIAGO\SQLEXPRESS')
    for query in os.listdir(os.path.join(os.getcwd(),'sql_queries')):
        with open(os.path.join(os.getcwd(),'sql_queries',query)) as archivo_query:
            consulta = archivo_query.read()
            cursor.execute(consulta)
            cursor.commit()
    tabla_segunda_forma_normal = Tabla(fr"C:\Users\arsan\OneDrive\Documents\GitHub\SQL_UNSAM\Sales_Data\annex1.csv")
    dim_item = tabla_segunda_forma_normal.slice_by_column(['item_code','item_name']).export_to_sql(cursor,'dim_item')
    tabla_segunda_forma_normal = Tabla(fr"C:\Users\arsan\OneDrive\Documents\GitHub\SQL_UNSAM\Sales_Data\annex1.csv")
    dim_category = tabla_segunda_forma_normal.slice_by_column(['category_code','category_name']).export_to_sql(cursor,'dim_category')
    dim_loss = Tabla(fr"C:\Users\arsan\OneDrive\Documents\GitHub\SQL_UNSAM\Sales_Data\annex4.csv").export_to_sql(cursor,'dim_loss')
    fact_sales = Tabla(fr'C:\Users\arsan\OneDrive\Documents\GitHub\SQL_UNSAM\Sales_Data\annex2.csv').export_to_sql(cursor,'fact_sales')
    fact_wholesale = Tabla(fr'C:\Users\arsan\OneDrive\Documents\GitHub\SQL_UNSAM\Sales_Data\annex3.csv').export_to_sql(cursor,'fact_wholesale')
    
