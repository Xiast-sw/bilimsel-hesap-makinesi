import tkinter as tk
import math

class BilimselHesapMakinesi:
    def __init__(self, master):
        self.master = master
        master.title("Bilimsel Hesap Makinesi")

        self.equation = ""
        self.result_var = tk.StringVar()

        # Arka plan rengi
        master.configure(bg="#F0F8FF")  # Yumuşak mavi arka plan

        self.entry = tk.Entry(master, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=4, width=20, borderwidth=4, bg="#E6E6FA", fg="#000000")
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('C', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('log', 5, 3),
            ('sqrt', 6, 0), ('(', 6, 1), (')', 6, 2), ('=', 6, 3)
        ]

        for (text, row, column) in buttons:
            button_style = {
                'padx': 20,
                'pady': 20,
                'font': ("Arial", 14),
                'borderwidth': 2,  # Çizgi kalınlığı
                'relief': tk.RAISED,  # Yükseltilmiş görünüm
                'bg': '#ADD8E6',  # Varsayılan açık mavi rengi
                'fg': '#000000',  # Varsayılan siyah yazı rengi
                'activebackground': '#87CEFA',  # Butona basıldığında arka plan rengi
                'activeforeground': '#000000',  # Butona basıldığında yazı rengi
            }

            if text == '=':
                button_style.update({'bg': '#FF69B4', 'fg': '#FFFFFF', 'font': ("Arial", 18), 'command': self.calculate})  # Eşittir butonu
            elif text == 'C':
                button_style.update({'bg': '#FFB6C1', 'fg': '#000000', 'font': ("Arial", 14), 'command': self.clear})  # C butonu
            else:
                button_style['command'] = lambda t=text: self.append_to_equation(t)

            button = tk.Button(self.master, text=text, **button_style)
            button.grid(row=row, column=column, sticky="nsew")  # Butonları esnek bir şekilde yerleştir

        # Son satırdaki butonların genişliği ayarlanıyor
        self.master.grid_columnconfigure(3, weight=1)  # Eşittir butonunun bulunduğu sütunun genişlemesine izin ver

    def append_to_equation(self, value):
        self.equation += str(value)
        self.result_var.set(self.equation)

    def calculate(self):
        try:
            # Trigonometric and other functions
            if 'sin' in self.equation:
                self.equation = self.equation.replace('sin', 'math.sin(math.radians(') + '))'
            if 'cos' in self.equation:
                self.equation = self.equation.replace('cos', 'math.cos(math.radians(') + '))'
            if 'tan' in self.equation:
                self.equation = self.equation.replace('tan', 'math.tan(math.radians(') + '))'
            if 'log' in self.equation:
                self.equation = self.equation.replace('log', 'math.log10(') + ')'
            if 'sqrt' in self.equation:
                self.equation = self.equation.replace('sqrt', 'math.sqrt(') + ')'

            # Evaluate the equation
            result = eval(self.equation)
            self.result_var.set(result)
            self.equation = str(result)

        except Exception as e:
            self.result_var.set("HATA")
            self.equation = ""

    def clear(self):
        self.equation = ""
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = BilimselHesapMakinesi(root)
    root.mainloop()
