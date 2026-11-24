import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("ІС Кулінарія — Нутриціологічний калькулятор")
root.geometry("620x355")
root.resizable(False, False)

mode_var = tk.IntVar(value=1)


def update_direction():
    if mode_var.get() == 1:
        arrow_lbl.config(text="=>")
        lbl_amount.config(text="Маса інгредієнтів нетто (г):")
    else:
        arrow_lbl.config(text="<=")
        lbl_amount.config(text="Кількість порцій (масштабування):")
    entry_amount.focus()


def toggle_by_arrow(event):
    if mode_var.get() == 1:
        mode_var.set(2)
    else:
        mode_var.set(1)
    update_direction()


def calculate():
    try:
        kcal_100 = float(entry_kcal.get().replace(",", "."))
        prot_100 = float(entry_prot.get().replace(",", "."))
        fat_100 = float(entry_fat.get().replace(",", "."))
        carb_100 = float(entry_carb.get().replace(",", "."))
        loss_coef = float(entry_loss.get().replace(",", "."))
        amount = float(entry_amount.get().replace(",", "."))

        if loss_coef <= 0 or loss_coef > 1:
            messagebox.showwarning("Увага", "Коефіцієнт термообробки має бути в межах (0; 1].")
            return

        if amount <= 0:
            messagebox.showwarning("Увага", "Введіть додатне значення маси або кількості порцій.")
            return

        if mode_var.get() == 1:
            grams_netto = amount * loss_coef
            portions = grams_netto / 200.0
        else:
            portions = amount
            grams_netto = portions * 200.0 * loss_coef

        kcal_total = (kcal_100 / 100.0) * grams_netto
        prot_total = (prot_100 / 100.0) * grams_netto
        fat_total = (fat_100 / 100.0) * grams_netto
        carb_total = (carb_100 / 100.0) * grams_netto

        match_index = min(1.0, round(0.70 + min(portions, 3.0) * 0.10, 2))

        entry_result.config(state="normal")
        entry_result.delete(0, tk.END)
        entry_result.insert(0, f"{kcal_total:.1f} ккал | Індекс: {match_index:.2f}")
        entry_result.config(state="readonly")

        profile_lbl.config(
            text=(
                f"Карта ({portions:.1f} порц., нетто {grams_netto:.0f} г) -> "
                f"Б: {prot_total:.1f} г | Ж: {fat_total:.1f} г | В: {carb_total:.1f} г"
            )
        )
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректні числові значення.")


def clear_fields():
    entry_amount.delete(0, tk.END)
    entry_result.config(state="normal")
    entry_result.delete(0, tk.END)
    entry_result.config(state="readonly")
    profile_lbl.config(text="Нутрієнтний профіль: Б: — г | Ж: — г | В: — г")
    entry_amount.focus()


rb_netto = tk.Radiobutton(
    root,
    text="За масою нетто (NutritionCalc)",
    variable=mode_var,
    value=1,
    command=update_direction,
)
rb_netto.place(x=30, y=16)

rb_portion = tk.Radiobutton(
    root,
    text="За порціями (Карти / RecipeMatcher)",
    variable=mode_var,
    value=2,
    command=update_direction,
)
rb_portion.place(x=310, y=16)

tk.Label(root, text="Ккал / 100 г:").place(x=30, y=56)
entry_kcal = tk.Entry(root, width=13)
entry_kcal.insert(0, "180")
entry_kcal.place(x=30, y=78)

tk.Label(root, text="Білки / 100 г:").place(x=175, y=56)
entry_prot = tk.Entry(root, width=13)
entry_prot.insert(0, "22")
entry_prot.place(x=175, y=78)

tk.Label(root, text="Жири / 100 г:").place(x=320, y=56)
entry_fat = tk.Entry(root, width=13)
entry_fat.insert(0, "8")
entry_fat.place(x=320, y=78)

tk.Label(root, text="Вуглеводи / 100 г:").place(x=465, y=56)
entry_carb = tk.Entry(root, width=13)
entry_carb.insert(0, "6")
entry_carb.place(x=465, y=78)

tk.Label(root, text="Коеф. термообробки (0.1..1.0):").place(x=30, y=118)
entry_loss = tk.Entry(root, width=22)
entry_loss.insert(0, "0.85")
entry_loss.place(x=30, y=140)

arrow_lbl = tk.Label(root, text="=>", font=("Arial", 14, "bold"), cursor="hand2")
arrow_lbl.place(x=275, y=138)
arrow_lbl.bind("<Button-1>", toggle_by_arrow)

lbl_amount = tk.Label(root, text="Маса інгредієнтів нетто (г):")
lbl_amount.place(x=330, y=118)
entry_amount = tk.Entry(root, width=26)
entry_amount.insert(0, "300")
entry_amount.place(x=330, y=140)

tk.Label(root, text="Енергетична цінність та індекс відповідності (0..1):").place(x=30, y=182)
entry_result = tk.Entry(root, width=42, state="readonly")
entry_result.place(x=30, y=204)

profile_lbl = tk.Label(
    root,
    text="Нутрієнтний профіль: Б: — г | Ж: — г | В: — г",
    font=("Arial", 9, "bold"),
    fg="#1b5e20",
)
profile_lbl.place(x=30, y=236)

btn_calc = tk.Button(root, text="Розрахувати", width=16, command=calculate)
btn_calc.place(x=30, y=282)

btn_clear = tk.Button(root, text="Очистити", width=16, command=clear_fields)
btn_clear.place(x=225, y=282)

btn_exit = tk.Button(root, text="Вихід", width=16, command=root.destroy)
btn_exit.place(x=420, y=282)

root.mainloop()