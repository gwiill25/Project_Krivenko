#Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ №№ 1 – 9.
#Вариант 7 дана масса в килограммах, нужно найти количество полных тонн
import tkinter as tk
from tkinter import messagebox

def calc():
    try:
        m = int(entry.get())
        if m < 0:
            messagebox.showerror("Ошибка", "Масса не может быть отрицательной")
            return
        tons = m // 1000
        label.config(text=f"Полных тонн: {tons}")
    except:
        messagebox.showerror("Ошибка", "Введите целое число")

root = tk.Tk()
root.title("Кг в тонны")
root.geometry("350x200")

tk.Label(root, text="Введите массу в килограммах:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12), width=15)
entry.pack(pady=5)

tk.Button(root, text="Вычислить", command=calc, font=("Arial", 11)).pack(pady=5)

label = tk.Label(root, text="Результат: ", font=("Arial", 12, "bold"))
label.pack(pady=10)

root.mainloop()