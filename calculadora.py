"""
No license
"""
import tkinter as tk 
from tkinter import messagebox

def click_boton(valor):
    actual = str(entrada.get())
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + valor)

def limpiar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        messagebox.showerror("Error", "Operación inválida")

ventana = tk.Tk()
ventana.title("Calculadora GUI")
ventana.geometry("300x400")

entrada = tk.Entry(ventana, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botones = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

fila = 1
col = 0

for boton in botones:
    if boton == "=":
        tk.Button(ventana, text=boton, width=5, height=2, font=("Arial", 18),
                  command=calcular).grid(row=fila, column=col, padx=5, pady=5)
    else:
        tk.Button(ventana, text=boton, width=5, height=2, font=("Arial", 18),
                  command=lambda b=boton: click_boton(b)).grid(row=fila, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        fila += 1

tk.Button(ventana, text="C", width=22, height=2, font=("Arial", 18), command=limpiar).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

ventana.mainloop()
