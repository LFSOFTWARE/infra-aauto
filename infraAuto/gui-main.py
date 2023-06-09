import tkinter as tk
from tkinter import filedialog


class Gui:
    def __init__(self, width=800, height=800):
      self.width = width
      self.height = height
      self.window = tk.Tk()
      self.window.geometry("800x800")

   
  
    def concluir_etapa(etapa):
      etapa.config(background='green', text="✔️ " + etapa['text'])

    def criar_linha_tempo(self):
        self.window.title("Linha do Tempo")
      # Configuração do estilo
        estilo_label = {"font": ("Helvetica", 14), "pady": 10}

        # Importação da tabela
        lbl_importacao = tk.Label(self.window, text="Importação da tabela", **estilo_label)
        lbl_importacao.pack()

        # Criação da entidade
        lbl_entidade = tk.Label(self.window, text="Criação da entidade", **estilo_label)
        lbl_entidade.pack()

        # Criação do depositante
        lbl_depositante = tk.Label(self.window, text="Criação do depositante", **estilo_label)
        lbl_depositante.pack()

        # Configuração da API
        lbl_api = tk.Label(self.window, text="Configuração da API", **estilo_label)
        lbl_api.pack()

        # Botão para concluir a etapa
        # btn_concluir = tk.Button(window, text="Concluir", command=lambda: concluir_etapa(lbl_api))
        # btn_concluir.pack()

        rotulos = [lbl_importacao, lbl_entidade, lbl_depositante, lbl_api]
        return rotulos    

    def main(self):
      def import_python_file():
        file_path = filedialog.askopenfilename(title="Selecione um arquivo Excel", filetypes=[("Arquivos Excel", "*.xlsx")])
        if file_path:
          print(file_path)

      label = tk.Label(self.window, text="Infracomerce", font=("Arial", 24), width=30, height=10, justify="center")
      label.pack()

      self.criar_linha_tempo()

      button = tk.Button(self.window, text="Importar planilha", command=import_python_file)
      button.pack()
      pass

    def start(self):
      self.main()
      self.window.mainloop()
        
  


page = Gui()

page.start()
