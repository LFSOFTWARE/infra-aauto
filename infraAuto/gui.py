import tkinter as tk
from tkinter import filedialog
import importlib.util

def import_python_file():
  file_path = filedialog.askopenfilename(title="Selecione um arquivo Excel", filetypes=[("Arquivos Excel", "*.xlsx")])
  if file_path:
    print(file_path)

window = tk.Tk()
window.geometry("800x800") 

label = tk.Label(window, text="Infracomerce", font=("Arial", 24), width=30, height=10, justify="center")
label.pack()

button = tk.Button(window, text="Importar arquivo Python", command=import_python_file)
button.pack()

# Inicia o loop principal da interface gráfica
window.mainloop()
