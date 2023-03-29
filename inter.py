import tkinter as tk
from tkinter import ttk

nombre = ''


def invok_ui(submit_function):
    window = tk.Tk()
    window.title('Reconocimiento')
    window.configure(background='white')
    window.geometry('300x150')
    window.resizable(False, False)

    frame = ttk.LabelFrame(window, text='Ingrese su nombre')
    frame.configure(borderwidth=2, relief=tk.GROOVE, padding=(10, 10))
    frame.pack(padx=10, pady=10, fill='both', expand=True)

    label = ttk.Label(frame, text='Nombre:', font=('Arial', 12))
    entry = ttk.Entry(frame, textvariable=nombre, font=('Arial', 12))

    label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
    entry.grid(row=0, column=1, sticky=tk.EW, padx=10, pady=10)

    button = ttk.Button(frame, text='Tomar foto', command=lambda: submit_function(entry.get()))
    button.grid(row=1, column=0, columnspan=2, sticky=tk.EW, padx=10, pady=10)

    close_button = ttk.Button(window, text='Cerrar', command=window.destroy)
    close_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    window.mainloop()
