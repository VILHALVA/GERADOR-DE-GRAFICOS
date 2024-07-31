import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np

class GraficoApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("GERADOR DE GRAFICOS")

        self.frame_inputs = tk.Frame(self.janela)
        self.frame_inputs.pack(side=tk.LEFT, padx=10, pady=10)

        tk.Label(self.frame_inputs, text="VALORES X (SEPARADOS POR VÍRGULA):").pack(pady=5)
        self.entry_x = tk.Entry(self.frame_inputs, width=40)
        self.entry_x.pack(pady=5)

        tk.Label(self.frame_inputs, text="VALORES Y (SEPARADOS POR VÍRGULA):").pack(pady=5)
        self.entry_y = tk.Entry(self.frame_inputs, width=40)
        self.entry_y.pack(pady=5)

        tk.Label(self.frame_inputs, text="TÍTULO DO GRÁFICO:").pack(pady=5)
        self.entry_titulo = tk.Entry(self.frame_inputs, width=40)
        self.entry_titulo.pack(pady=5)

        tk.Label(self.frame_inputs, text="TIPO DE GRÁFICO:").pack(pady=5)
        self.tipo_grafico = tk.StringVar(value="BARRA")
        tipos = ["BARRA", "LINHA", "DISPERSÃO"]
        for tipo in tipos:
            tk.Radiobutton(self.frame_inputs, text=tipo, variable=self.tipo_grafico, value=tipo).pack(anchor=tk.W)

        self.botao_gerar = tk.Button(self.frame_inputs, text="GERAR", command=self.gerar_grafico)
        self.botao_gerar.pack(pady=10)

        self.frame_grafico = tk.Frame(self.janela)
        self.frame_grafico.pack(side=tk.RIGHT, padx=10, pady=10)

    def gerar_grafico(self):
        for widget in self.frame_grafico.winfo_children():
            widget.destroy()

        try:
            x = list(map(float, self.entry_x.get().split(',')))
            y = list(map(float, self.entry_y.get().split(',')))

            if len(x) != len(y):
                raise ValueError("ERRO: O NÚMERO DE VALORES X DEVE SER IGUAL AO NÚMERO DE VALORES Y!")

            self.figura = Figure(figsize=(8, 6), dpi=100)
            self.grafico = self.figura.add_subplot(111)

            tipo = self.tipo_grafico.get()
            if tipo == "BARRA":
                self.grafico.bar(x, y, color='blue')
            elif tipo == "LINHA":
                self.grafico.plot(x, y, label='Dados', color='blue')
                self.grafico.legend()
            elif tipo == "DISPERSÃO":
                self.grafico.scatter(x, y, color='blue')

            self.grafico.set_xlabel('EIXO X')
            self.grafico.set_ylabel('EIXO Y')
            self.grafico.set_title(self.entry_titulo.get() if self.entry_titulo.get() else 'GRÁFICO')

            self.canvas = FigureCanvasTkAgg(self.figura, master=self.frame_grafico)
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            toolbar = NavigationToolbar2Tk(self.canvas, self.frame_grafico)
            toolbar.update()
            self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        except ValueError as e:
            messagebox.showerror("ERRO DE DADOS", str(e))
        except Exception as e:
            messagebox.showerror("ERRO", f"OCORREU UM ERRO: {str(e)}")

janela = tk.Tk()

app = GraficoApp(janela)

janela.mainloop()
