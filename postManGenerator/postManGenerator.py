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

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <ruta_del_fichero_entrada> <ruta_del_fichero_salida>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    generate_postman_collection(input_file, output_file)
