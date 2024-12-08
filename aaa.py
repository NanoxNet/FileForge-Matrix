import os

# Crear la carpeta principal 'peaw1'
try:
    os.makedirs("peaw1", exist_ok=True)
    print("Carpeta principal creada: peaw1")
    
    # Crear las subcarpetas y los archivos dentro de ellas
    for i in range(1, 6):
        carpeta = os.path.join("peaw1", f"Carpeta_{i}")
        
        # Crear la carpeta
        try:
            os.makedirs(carpeta, exist_ok=True)
            print(f"Carpeta creada: {carpeta}")
            
            for j in range(1, 6):
                archivo = os.path.join(carpeta, f"Nanito_{j}.txt")
                
                # Crear y escribir en el archivo
                with open(archivo, 'w') as file:
                    file.write(f"Archivo Nanito en {archivo}")
                
                print(f"Archivo creado: {archivo}")
        
        except Exception as e:
            print(f"Error al crear la carpeta {carpeta}: {e}")
   
    # Mostrar solo el link en la consola
    github_url = "https://github.com/Nanoxnet"
    print(f"\nVisita mi GitHub aquí → {github_url}")
    
except Exception as e:
    print(f"Error al crear la carpeta principal 'peaw1': {e}")

print("Proceso completado.")
