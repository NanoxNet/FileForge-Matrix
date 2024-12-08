import os
import tkinter as tk
from tkinter import ttk
import threading
import time
import webbrowser  # Importar el módulo webbrowser

class HackerInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Archivos - Modo Hacker")
        self.root.configure(bg='black')
        
        # Establecer tamaño mínimo de la ventana
        self.root.minsize(400, 300)
        
        # Frame para el botón con fondo negro
        self.button_frame = tk.Frame(root, bg='black')
        self.button_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
        
        # Estilo personalizado para el botón
        style = ttk.Style()
        style.configure("Hacker.TButton",
                       background="black",
                       foreground="#00FF00",
                       borderwidth=1)
        
        # Botón de inicio centrado
        self.start_button = ttk.Button(self.button_frame,
                                     text="INICIAR PROCESO",
                                     style="Hacker.TButton",
                                     width=20,
                                     command=self.start_process)
        self.start_button.pack(anchor=tk.CENTER)
        
        # Área de texto para logs con soporte para hipervínculos
        self.log_area = tk.Text(root, 
                               bg='black',
                               fg='#00FF00',
                               font=('Courier', 10),
                               wrap=tk.WORD,
                               cursor="arrow")  # Cursor predeterminado
        self.log_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.log_area.tag_configure("hyperlink", foreground="#00FF00", underline=1)
        self.log_area.tag_bind("hyperlink", "<Button-1>", self.open_github)  # Asociar clic al enlace
        self.log_area.tag_bind("hyperlink", "<Enter>", lambda e: self.log_area.configure(cursor="hand2"))
        self.log_area.tag_bind("hyperlink", "<Leave>", lambda e: self.log_area.configure(cursor="arrow"))

    def log(self, message):
        self.log_area.insert(tk.END, f"[*] {message}\n")
        self.log_area.see(tk.END)
        self.root.update()
        time.sleep(0.1)  # Efecto de escritura retardada

    def create_files(self):
        self.log("Iniciando proceso de creación...")
        
        # Crear carpeta principal 'peaw'
        carpeta_principal = "peaw"
        try:
            os.makedirs(carpeta_principal, exist_ok=True)
            self.log(f"Generando carpeta principal: {carpeta_principal}")
            
            for i in range(1, 6):
                carpeta = os.path.join(carpeta_principal, f"Carpeta_{i}")
                
                try:
                    os.makedirs(carpeta, exist_ok=True)
                    self.log(f"Generando carpeta: {carpeta}")
                    
                    for j in range(1, 6):
                        archivo = os.path.join(carpeta, f"Nanito_{j}.txt")
                        
                        with open(archivo, 'w') as file:
                            file.write(f"Archivo Nanito en {archivo}")
                        
                        self.log(f"Archivo creado: {archivo}")
                        
                except Exception as e:
                    self.log(f"ERROR en carpeta {carpeta}: {str(e)}")
                    
        except Exception as e:
            self.log(f"ERROR en carpeta principal {carpeta_principal}: {str(e)}")
        
        self.log("==========================")
        self.log("Proceso completado con éxito")
        self.log("==========================")
        self.log("¡Gracias por usar este programa!")
        
        # Crear un hipervínculo en el área de texto
        self.log_area.insert(tk.END, "[*] Visita mi GitHub: ")
        self.log_area.insert(tk.END, "https://github.com/NanoxNet", "hyperlink")
        self.log_area.insert(tk.END, "\n")
        self.log("==========================")
        self.start_button.config(state='normal')

    def start_process(self):
        self.start_button.config(state='disabled')
        self.log_area.delete(1.0, tk.END)
        # Ejecutar en un hilo separado para no bloquear la interfaz
        threading.Thread(target=self.create_files, daemon=True).start()

    def open_github(self, event=None):
        # Abrir la URL de GitHub en el navegador predeterminado
        webbrowser.open("https://github.com/NanoxNet")

def main():
    root = tk.Tk()
    root.geometry("600x400")
    app = HackerInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
