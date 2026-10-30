import os
from pyairtable import Api
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

API_KEY = os.getenv("AIRTABLE_API_KEY")
BASE_ID = os.getenv("AIRTABLE_BASE_ID")
TABLE_NAME = "Tareas"  # Asegúrate de haber renombrado la tabla a "Tareas" en Airtable

def get_table():
    if not API_KEY or not BASE_ID:
        raise ValueError("Faltan credenciales en el archivo .env")
    api = Api(API_KEY)
    return api.table(BASE_ID, TABLE_NAME)

def probar_airtable():
    print("🚀 Conectando a Airtable...")
    
    try:
        tabla = get_table()
        
        # 1. Crear un registro (Tarea)
        # El parámetro typecast=True permite que Airtable cree la opción "Pendiente" si no existe
        nuevo_registro = tabla.create({
            "Name": "Tarea creada desde Codespace Web", 
            "Status": "Pendiente"
        }, typecast=True)
        
        print(f"✅ Registro creado con ID: {nuevo_registro['id']}")
        
        # 2. Leer todos los registros
        registros = tabla.all()
        print(f"📋 Total de tareas en la tabla: {len(registros)}")
        
        for reg in registros:
            print(f"   - {reg['fields'].get('Name', 'Sin nombre')}")

    except Exception as e:
        print(f"❌ Error: {e}")
        print("Revisa que el Token y el Base ID sean correctos, y que la tabla se llame 'Tareas'.")

if __name__ == "__main__":
    probar_airtable()