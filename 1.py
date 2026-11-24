import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("ІС Кулінарія - Профіль користувача")
root.geometry("620x380")
root.resizable(False, False)

title_lbl = tk.Label(
    root,
    text="Профіль користувача - ІС «Кулінарія»",
    font=("Times New Roman", 15, "bold"),
    fg="purple",
)
title_lbl.place(x=135, y=14)

info_lbl = tk.Label(
    root,
    text=(
        "Користувач: Дмитро\n"
        "Роль: Користувач\n"
        "Модуль рецептурних карт: 12 збережених карт\n"
        "RecipeMatcher: кошик активний, індекс 0.94\n"
        "Обмеження: без глютену та лактози\n"
        "NutritionCalc: нормалізація + термообробка\n"
        "Ціль раціону: контроль ккал та БЖВ"
    ),
    font=("Arial", 10),
    justify="left",
)
info_lbl.place(x=25, y=58)

photo_frame = tk.Frame(root, width=230, height=205, bg="#d9d9d9", relief="solid", bd=1)
photo_frame.place(x=360, y=58)
photo_frame.pack_propagate(False)

photo_label = tk.Label(
    photo_frame,
    text="[Зображення приховано]",
    font=("Arial", 10),
    bg="#d9d9d9",
    fg="#333333",
)
photo_label.pack(expand=True, fill="both")

caption_lbl = tk.Label(root, text="Стан: не вибрано", font=("Arial", 9, "italic"))
caption_lbl.place(x=360, y=270)


def load_img(path):
    try:
        img = Image.open(path)
        img = img.resize((226, 201), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception:
        return None


avatar_img = load_img("avatar.jpg")
dish_img = load_img("dish.jpg")


def show_avatar():
    if avatar_img is not None:
        photo_label.config(image=avatar_img, text="")
    else:
        photo_label.config(
            image="",
            text="ПРОФІЛЬ КОРИСТУВАЧА\nДмитро (ІК-52)\nРежим: RecipeMatcher",
            bg="#cfe2f3",
            fg="#0b5394",
            font=("Arial", 10, "bold"),
        )
    caption_lbl.config(text="Показано: Аватар профілю користувача")
    btn_hide.config(state="normal")


def show_dish():
    if dish_img is not None:
        photo_label.config(image=dish_img, text="")
    else:
        photo_label.config(
            image="",
            text="ТЕХНОЛОГІЧНА КАРТА\nСтрава: Курячий стейк\nНетто: 250 г | БЖВ у нормі",
            bg="#d9ead3",
            fg="#274e13",
            font=("Arial", 10, "bold"),
        )
    caption_lbl.config(text="Показано: Карта страви (NutritionCalc)")
    btn_hide.config(state="normal")


def hide_photo():
    photo_label.config(
        image="",
        text="[Зображення приховано]",
        bg="#d9d9d9",
        fg="#333333",
        font=("Arial", 10),
    )
    caption_lbl.config(text="Стан: зображення приховано")
    btn_hide.config(state="disabled")


btn_avatar = tk.Button(root, text="Аватар користувача", width=26, command=show_avatar)
btn_avatar.place(x=25, y=205)

btn_dish = tk.Button(root, text="Карта страви / Фото", width=26, command=show_dish)
btn_dish.place(x=25, y=245)

btn_hide = tk.Button(
    root, text="Приховати зображення", width=26, state="disabled", command=hide_photo
)
btn_hide.place(x=25, y=285)

root.mainloop()