import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("ІС Кулінарія — Калькулятор порцій та КБЖВ")
root.geometry("460x260")
root.resizable(False, False)

mode_var = tk.IntVar(value=1)


def update_direction():
    if mode_var.get() == 1:
        arrow_lbl.config(text="=>")
        lbl_amount.config(text="Вага продукту (г):")
    else:
        arrow_lbl.config(text="<=")
        lbl_amount.config(text="Кількість порцій:")
    entry_amount.focus()


def toggle_by_arrow(event):
    if mode_var.get() == 1:
        mode_var.set(2)
    else:
        mode_var.set(1)
    update_direction()


def calculate():
    try:
        kcal_per_100 = float(entry_kcal100.get().replace(",", "."))
        portion_weight = float(entry_portion.get().replace(",", "."))
        amount = float(entry_amount.get().replace(",", "."))

        if mode_var.get() == 1:

            result = (kcal_per_100 / 100.0) * amount
        else:
            
            result = (kcal_per_100 / 100.0) * portion_weight * amount

        entry_result.config(state="normal")
        entry_result.delete(0, tk.END)
        entry_result.insert(0, f"{result:.1f}")
        entry_result.config(state="readonly")
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректні числові значення!")


def clear_fields():
    entry_amount.delete(0, tk.END)
    entry_result.config(state="normal")
    entry_result.delete(0, tk.END)
    entry_result.config(state="readonly")
    entry_amount.focus()



rb_weight = tk.Radiobutton(
    root, text="За вагою (г)", variable=mode_var, value=1, command=update_direction
)
rb_weight.place(x=55, y=20)

rb_portion = tk.Radiobutton(
    root, text="За порціями", variable=mode_var, value=2, command=update_direction
)
rb_portion.place(x=285, y=20)


lbl_kcal100 = tk.Label(root, text="Калорійність на 100 г:")
lbl_kcal100.place(x=45, y=60)
entry_kcal100 = tk.Entry(root, width=18)
entry_kcal100.insert(0, "165")
entry_kcal100.place(x=45, y=82)

lbl_portion = tk.Label(root, text="Вага 1 порції (г):")
lbl_portion.place(x=280, y=60)
entry_portion = tk.Entry(root, width=18)
entry_portion.insert(0, "250")
entry_portion.place(x=280, y=82)


arrow_lbl = tk.Label(root, text="=>", font=("Arial", 14, "bold"), cursor="hand2")
arrow_lbl.place(x=212, y=132)
arrow_lbl.bind("<Button-1>", toggle_by_arrow)


lbl_amount = tk.Label(root, text="Вага продукту (г):")
lbl_amount.place(x=45, y=120)
entry_amount = tk.Entry(root, width=18)
entry_amount.insert(0, "200")
entry_amount.place(x=45, y=142)

lbl_result = tk.Label(root, text="Результат (ккал):")
lbl_result.place(x=280, y=120)
entry_result = tk.Entry(root, width=18, state="readonly")
entry_result.place(x=280, y=142)


btn_calc = tk.Button(root, text="Розрахувати", width=13, command=calculate)
btn_calc.place(x=45, y=195)

btn_clear = tk.Button(root, text="Очистити", width=13, command=clear_fields)
btn_clear.place(x=175, y=195)

btn_exit = tk.Button(root, text="Вихід", width=13, command=root.destroy)
btn_exit.place(x=305, y=195)

root.mainloop()