import tkinter as tk
from tkinter import messagebox

def resolver():
    try:
        expresion = entrada.get()
        resultado = eval(expresion, {"__builtins__": None}, {})
        salida.config(text=f"Resultado: {resultado}")
    except Exception as e:
        messagebox.showerror("Error", f"Expresión inválida:\n{e}")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Resolvé tu ejercicio")
ventana.geometry("300x180")
ventana.resizable(False, False)

# Entrada
tk.Label(ventana, text="Ingresá una expresión matemática:").pack(pady=10)
entrada = tk.Entry(ventana, font=("Arial", 14), justify="center")
entrada.pack(pady=5)

# Botón
tk.Button(ventana, text="Resolver", command=resolver).pack(pady=5)

# Resultado
salida = tk.Label(ventana, text="", font=("Arial", 14), fg="green")
salida.pack(pady=10)

ventana.mainloop()
