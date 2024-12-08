import os
import tkinter as tk
from tkinter import ttk
import threading
import time

class HackerInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("NanoxNet_corp v3.0")
        self.root.configure(bg='black')
        
        # Frame principal
        main_frame = tk.Frame(root, bg='black')
        main_frame.pack(padx=5, pady=5)
        
        # Configuración de estilo
        style = ttk.Style()
        style.configure("Hacker.TButton",
                       foreground="green",
                       background="black",
                       font=('Courier', 9, 'bold'))
        style.configure("Hacker.TEntry",
                       foreground="green",
                       fieldbackground="black",
                       font=('Courier', 9))
        
        # Frame para entradas
        input_frame = tk.Frame(main_frame, bg='black')
        input_frame.pack(pady=5)
        
        # Entradas para carpetas y archivos
        tk.Label(input_frame, text="Carpetas:", bg='black', fg='green', font=('Courier', 9)).pack(side=tk.LEFT)
        self.num_folders = ttk.Entry(input_frame, width=5, style="Hacker.TEntry")
        self.num_folders.pack(side=tk.LEFT, padx=5)
        self.num_folders.insert(0, "5")
        
        tk.Label(input_frame, text="Archivos:", bg='black', fg='green', font=('Courier', 9)).pack(side=tk.LEFT, padx=(10,0))
        self.num_files = ttk.Entry(input_frame, width=5, style="Hacker.TEntry")
        self.num_files.pack(side=tk.LEFT, padx=5)
        self.num_files.insert(0, "5")
        
        # Área de texto para logs
        self.log_area = tk.Text(main_frame, 
                               bg='black',
                               fg='#00FF00',
                               font=('Courier', 9),
                               height=15,
                               width=50)
        self.log_area.pack(pady=5)
        
        # Agregar barra de progreso ANTES de los botones
        self.progress = ttk.Progressbar(main_frame, length=300, mode='determinate')
        self.progress.pack(pady=5)
        
        # Frame para botones
        button_frame = tk.Frame(main_frame, bg='black')
        button_frame.pack(pady=5)
        
        # Botón de inicio
        self.start_button = ttk.Button(button_frame,
                                     text="EJECUTAR",
                                     style="Hacker.TButton",
                                     command=self.start_process)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        # Botón de cancelar
        self.cancel_button = ttk.Button(button_frame,
                                      text="CANCELAR",
                                      style="Hacker.TButton",
                                      command=self.cancel_process,
                                      state='disabled')
        self.cancel_button.pack(side=tk.LEFT, padx=5)
        
        # Firma
        signature = tk.Label(main_frame, 
                           text="By_NanoEspinoza",
                           bg='black',
                           fg='#008800',
                           font=('Courier', 8, 'italic'))
        signature.pack(pady=2)

    def log(self, mensaje):
        self.log_area.insert(tk.END, mensaje + "\n")
        self.log_area.see(tk.END)  # Desplaza al final del texto

    def validate_inputs(self):
        try:
            num_carpetas = int(self.num_folders.get())
            num_archivos = int(self.num_files.get())
            
            if num_carpetas <= 0 or num_archivos <= 0:
                self.log("ERROR: Los números deben ser mayores que 0")
                return False
            
            return True
        except ValueError:
            self.log("ERROR: Ingrese números válidos")
            return False

    def create_files(self):
        if not self.validate_inputs():
            self.finish_process()
            return
            
        # Crear carpeta principal
        carpeta_principal = "NanoxNet Corporation"
        try:
            os.makedirs(carpeta_principal, exist_ok=True)
            self.log(f"Creando carpeta principal: {carpeta_principal}")
            time.sleep(2)
        except Exception as e:
            self.log(f"ERROR al crear carpeta principal: {str(e)}")
            self.finish_process()
            return
            
        num_carpetas = int(self.num_folders.get())
        num_archivos = int(self.num_files.get())
        total_operations = num_carpetas * num_archivos
        completed = 0
        
        self.log("Iniciando proceso de creación...")
        
        for i in range(1, num_carpetas + 1):
            if not self.is_running:
                self.log("Proceso cancelado por el usuario")
                break
                
            carpeta = os.path.join(carpeta_principal, f"Carpeta_{i}")
            
            try:
                os.makedirs(carpeta, exist_ok=True)
                self.log(f"Generando: {carpeta}")
                time.sleep(2)
                
                for j in range(1, num_archivos + 1):
                    if not self.is_running:
                        break
                        
                    archivo = os.path.join(carpeta, f"Nanito_{j}.txt")
                    with open(archivo, 'w') as file:
                        file.write(f"Archivo Nanito en {archivo}")
                    self.log(f"Creado: {archivo}")
                    time.sleep(2)
                    
                    completed += 1
                    self.progress['value'] = (completed / total_operations) * 100
                    
            except Exception as e:
                self.log(f"ERROR: {str(e)}")
        
        self.finish_process()

    def start_process(self):
        self.is_running = True
        self.start_button.config(state='disabled')
        self.cancel_button.config(state='normal')
        self.progress['value'] = 0
        self.log_area.delete(1.0, tk.END)
        threading.Thread(target=self.create_files, daemon=True).start()

    def cancel_process(self):
        self.is_running = False
        self.cancel_button.config(state='disabled')
        self.log("Cancelando proceso...")

    def finish_process(self):
        self.is_running = False
        self.start_button.config(state='normal')
        self.cancel_button.config(state='disabled')
        self.log("\n[+] Proceso completado")
        
        # Agregar link clickeable en el área de log
        self.log_area.tag_config("link", foreground="#00FF00", underline=1)
        self.log_area.insert(tk.END, "\nVisita mi GitHub: ", "normal")
        self.log_area.insert(tk.END, "https://github.com/NanoxNet", "link")
        self.log_area.tag_bind("link", "<Button-1>", lambda e: self.open_github())
        self.log_area.tag_bind("link", "<Enter>", lambda e: self.log_area.config(cursor="hand2"))
        self.log_area.tag_bind("link", "<Leave>", lambda e: self.log_area.config(cursor=""))
        
        self.log("\n\n¡Gracias por usar NanoxNet_corp v3.0!")

    def open_github(self):
        import webbrowser
        webbrowser.open("https://github.com/NanoxNet")

def main():
    root = tk.Tk()
    root.geometry("600x400")
    app = HackerInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()