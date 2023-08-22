from tkinter import ttk
from tkinter import *

class Calculadora:

    def __init__(self, window):
        # Initializations 
        self.wind = window
        self.wind.title('Calculadora de IMC')

        # Creating a Frame Container 
        frame = LabelFrame(self.wind, text = 'Introduce los datos')
        frame.grid(row = 0, column = 0, columnspan = 3)

        # Peso Input
        Label(frame, text = 'Peso: ').grid(row = 1, column = 0)
        self.peso = Entry(frame)
        self.peso.focus()
        self.peso.grid(row = 1, column = 1)

        # Talla Input
        Label(frame, text = 'Talla: ').grid(row = 2, column = 0)
        self.talla = Entry(frame)
        self.talla.grid(row = 2, column = 1)

        # Button Add Product 
        ttk.Button(frame, text = 'Calcular', command = self.calcular).grid(row = 3, columnspan=2, sticky = W + E)

        # Output Messages 
        self.result = Label(text = '', fg = 'black', font=('arial',18))
        self.result.grid(row = 1, column = 0, columnspan= 2, sticky = NE + SW)

    # User Input Validation
    def validation(self):
        return len(self.peso.get()) != 0 and len(self.talla.get()) != 0

    def calcular(self):
        if self.validation():
            peso = float(self.peso.get())
            talla = float(self.talla.get())

            imc = round(peso / (talla ** 2),2)

            if imc < 18.5:
                self.result['text'] = "IMC = {}\nBajo peso\n".format(imc)
            elif 18.5 <= imc < 24.9:
                self.result['text'] = "IMC = {}\nPeso normal\n".format(imc)
            elif 25 <= imc < 29.9:
                self.result['text'] = "IMC = {}\nSobrepeso\n".format(imc) 
            else:
                self.result['text'] = "IMC = {}\nObesidad\n".format(imc)
        else:
            self.message['text'] = 'Peso y Talla son requeridos\npyth'

        self.peso.delete(0, END)
        self.talla.delete(0, END)

if __name__ == '__main__':
    window = Tk()
    application = Calculadora(window)
    window.mainloop()