#В соответствии с номером варианта перейти по ссылке на прототип. Реализовать его в IDE PyCharm Community с применением пакета tk. 
#Получить интерфейс максимально приближенный к оригиналу (см. таблицу 1).
# Задание 1. Форма регистрации (Вариант 8)
# Ссылка на прототип: https://i.pinimg.com/originals/73/c6/0d/73c60def8c55043f9fd27b370530a9cf.jpg
import tkinter as tk
from tkinter import ttk, messagebox

def create_entry(parent, label, row, placeholder, show=''):
    tk.Label(parent, text=label, bg='#0a1a3a', fg='#FFD700', font=('Arial', 11, 'bold')).grid(row=row, column=0, padx=(0,15), pady=8, sticky='e')
    entry = tk.Entry(parent, font=('Arial',11), width=28, bg='white', fg='gray', bd=0, highlightthickness=0, relief='flat', show=show)
    entry.grid(row=row, column=1, pady=8, ipady=6)
    entry.insert(0, placeholder)
    entry.bind('<FocusIn>', lambda e: entry.delete(0, tk.END) if entry.get() == placeholder else None)
    return entry

def submit_action():
    if not terms_var.get():
        return messagebox.showerror("Ошибка", "Вы должны согласиться с условиями использования.")
    if entry_password.get() != entry_confirm.get():
        return messagebox.showerror("Ошибка", "Пароли не совпадают.")
    if not all([entry_first_name.get(), entry_last_name.get(), entry_screen_name.get(), entry_email.get(), entry_phone.get(), entry_password.get()]):
        return messagebox.showerror("Ошибка", "Пожалуйста, заполните все обязательные поля.")
    messagebox.showinfo("Успех", f"Добро пожаловать, {entry_first_name.get()}!")

def cancel_action():
    for e in [entry_first_name, entry_last_name, entry_screen_name, entry_email, entry_phone, entry_password, entry_confirm]:
        e.delete(0, tk.END)
    month_cb.set('Month'); day_cb.set('Day'); year_cb.set('Year')
    gender_var.set(0); country_cb.set('USA'); terms_var.set(0)

def on_closing():
    if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
        root.destroy()

root = tk.Tk()
root.title("Регистрация")
root.geometry("550x750+300+50")
root.configure(bg='#0a1a3a')

style = ttk.Style()
style.configure('White.TCombobox', fieldbackground='white', background='white', foreground='gray', borderwidth=0)

tk.Frame(root, bg='#FF8C00', height=50).pack(fill='x', side='top')
tk.Label(root, text="Sign Up", font=('Arial',20,'bold'), bg='#FF8C00', fg='#FFD700').place(x=20,y=10)

main_frame = tk.Frame(root, bg='#0a1a3a')
main_frame.pack(expand=True, fill='both', padx=40, pady=20)

entry_first_name = create_entry(main_frame, "First Name", 0, "Enter First Name...")
entry_last_name = create_entry(main_frame, "Last Name", 1, "Enter Last Name...")
entry_screen_name = create_entry(main_frame, "Screen Name", 2, "Enter Screen Name...")

tk.Label(main_frame, text="Date of Birth", bg='#0a1a3a', fg='#FFD700', font=('Arial',11,'bold')).grid(row=3, column=0, padx=(0,15), pady=8, sticky='e')
frame_dob = tk.Frame(main_frame, bg='#0a1a3a')
frame_dob.grid(row=3, column=1, pady=8)
months = ['Month'] + ['January','February','March','April','May','June','July','August','September','October','November','December']
month_cb = ttk.Combobox(frame_dob, values=months, width=8, state='readonly', style='White.TCombobox')
month_cb.set('Month'); month_cb.pack(side='left', padx=(0,5))
day_cb = ttk.Combobox(frame_dob, values=['Day']+[str(i) for i in range(1,32)], width=5, state='readonly', style='White.TCombobox')
day_cb.set('Day'); day_cb.pack(side='left', padx=(0,5))
year_cb = ttk.Combobox(frame_dob, values=['Year']+[str(i) for i in range(1900,2026)], width=7, state='readonly', style='White.TCombobox')
year_cb.set('Year'); year_cb.pack(side='left')

tk.Label(main_frame, text="Gender", bg='#0a1a3a', fg='#FFD700', font=('Arial',11,'bold')).grid(row=4, column=0, padx=(0,15), pady=8, sticky='e')
frame_gender = tk.Frame(main_frame, bg='#0a1a3a')
frame_gender.grid(row=4, column=1, pady=8)
gender_var = tk.IntVar(value=0)
tk.Radiobutton(frame_gender, text="Male", variable=gender_var, value=1, bg='#0a1a3a', fg='white', selectcolor='#0a1a3a').pack(side='left', padx=(0,20))
tk.Radiobutton(frame_gender, text="Female", variable=gender_var, value=2, bg='#0a1a3a', fg='white', selectcolor='#0a1a3a').pack(side='left')

tk.Label(main_frame, text="Country", bg='#0a1a3a', fg='#FFD700', font=('Arial',11,'bold')).grid(row=5, column=0, padx=(0,15), pady=8, sticky='e')
country_cb = ttk.Combobox(main_frame, values=['USA','Canada','UK','Germany','France','Spain','Italy','Japan','China','Russia'], width=26, state='readonly', style='White.TCombobox')
country_cb.set('USA')
country_cb.grid(row=5, column=1, pady=8, ipady=4)

entry_email = create_entry(main_frame, "E-mail", 6, "Enter E-mail......")
entry_phone = create_entry(main_frame, "Phone", 7, "Enter Phone......")
entry_password = create_entry(main_frame, "Password", 8, "Enter Password", show='*')
entry_confirm = create_entry(main_frame, "Confirm Password", 9, "Confirm Password", show='*')

terms_var = tk.IntVar()
tk.Checkbutton(main_frame, text="I agree to the Terms of Use", variable=terms_var, bg='#0a1a3a', fg='white', selectcolor='#0a1a3a').grid(row=10, column=0, columnspan=2, pady=(15,10))

bottom_frame = tk.Frame(root, bg='#FF8C00', height=55)
bottom_frame.pack(fill='x', side='bottom')
btn_frame = tk.Frame(bottom_frame, bg='#FF8C00')
btn_frame.pack(pady=10, padx=20, anchor='e')
tk.Button(btn_frame, text="Submit", font=('Arial',11,'bold'), bg='#2ECC40', fg='green', padx=25, pady=4, bd=0, command=submit_action).pack(side='right', padx=(0,10))
tk.Button(btn_frame, text="Cancel", font=('Arial',11,'bold'), bg='#FF4136', fg='red', padx=25, pady=4, bd=0, command=cancel_action).pack(side='right')

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()