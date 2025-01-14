import json
import re

def generate_postman_collection(input_file, output_file):
    # Plantilla base de la colección Postman
    collection = {
        "info": {
            "name": "API Collection",
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        },
        "item": []
    }
    
    with open(input_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Extraer la ruta y los métodos
        match = re.match(r"(/[\w\-/?=&]+)\s*-\s*([\w,]+)", line)
        if match:
            path, methods = match.groups()
            methods = methods.split(',')
            
            # Crear una entrada por cada método
            for method in methods:
                method = method.strip().upper()
                endpoint = {
                    "name": f"{method} {path}",
                    "request": {
                        "method": method,
                        "header": [],
                        "url": {
                            "raw": f"{{{{baseUrl}}}}{path}",
                            "host": ["{{baseUrl}}"],
                            "path": path.lstrip('/').split('/'),
                            "query": []
                        }
                    }
                }
                collection["item"].append(endpoint)

    # Guardar la colección en un archivo JSON
    with open(output_file, 'w') as outfile:
        json.dump(collection, outfile, indent=4)
    
    print(f"Archivo Postman generado en: {output_file}")

# Rutas de entrada y salida
input_file = "result.txt"  # Ruta del archivo de entrada proporcionado
output_file = "postman_collection.json"  # Ruta del archivo de salida

# Ejecutar la generación
generate_postman_collection(input_file, output_file)
