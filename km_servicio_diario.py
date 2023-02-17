import json
import nbformat
import psycopg2
import numpy as np
from psycopg2.extensions import register_adapter, AsIs
def addapt_numpy_float64(numpy_float64):
    return AsIs(numpy_float64)
def addapt_numpy_int64(numpy_int64):
    return AsIs(numpy_int64)
register_adapter(np.float64, addapt_numpy_float64)
register_adapter(np.int64, addapt_numpy_int64)
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

query_prueba = "insert into flota_pbello.bh_kilometrajes_servicio_dia_auxiliar (id_registro) values ('69420')"
query_prueba_delete = "delete from flota_pbello.bh_kilometrajes_servicio_dia_auxiliar where id_registro = '69420'"
conn_sql = psycopg2.connect(user = "paul_bello",
                            password = "UAOZQ2Rr4t",
                            host = "192.168.40.239",
                            port = "5432",
                            database = "bidb",
                            options="-c search_path=dbo,taller")
cursor = conn_sql.cursor()
cursor.execute(query_prueba)
#cursor.execute(query_prueba_delete)#, tuple(list(df_nuevos_registros_n.iloc[i])))  
conn_sql.commit()
cursor.close()
conn_sql.close()
with open("C:\\Users\\Tomas Retamal\\OneDrive - BUSES HUALPEN\\Documentos\\Proyectos\\TomasRetamal\\Opti\\KM Vacío\\KM Pablo\\km_servicio_diario.ipynb", encoding="utf8") as f:
    nb = nbformat.read(f, as_version=4)

for cell in nb.cells:
    if cell.cell_type == "code":
        exec(cell.source)