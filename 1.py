import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("ІС Кулінарія — Профіль користувача")
root.geometry("540x340")
root.resizable(False, False)

title_lbl = tk.Label(
    root,
    text="Профіль користувача",
    font=("Times New Roman", 16, "bold"),
    fg="purple",
)
title_lbl.place(x=160, y=15)

info_lbl = tk.Label(
    root,
    text="Користувач: Дмитро\nРоль: Кулінар / Розробник\nМета: Контроль КБЖВ та рецепти\nУлюблена категорія: Білкові страви",
    font=("Arial", 10),
    justify="left",
)
info_lbl.place(x=25, y=60)

photo_frame = tk.Frame(root, width=210, height=190, bg="#d9d9d9", relief="solid", bd=1)
photo_frame.place(x=300, y=60)
photo_frame.pack_propagate(False)

photo_label = tk.Label(
    photo_frame,
    text="[Фото приховано]",
    font=("Arial", 10),
    bg="#d9d9d9",
    fg="#333333",
)
photo_label.pack(expand=True, fill="both")

caption_lbl = tk.Label(root, text="Зображення не вибрано", font=("Arial", 9, "italic"))
caption_lbl.place(x=300, y=258)


def load_img(path):
    img = Image.open(path)
    img = img.resize((206, 186), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)


avatar_img = load_img("avatar.jpg")
dish_img = load_img("dish.jpg")


def show_avatar():
    photo_label.config(image=avatar_img, text="")
    caption_lbl.config(text="Показано: Аватар користувача")
    btn_hide.config(state="normal")


def show_dish():
    photo_label.config(image=dish_img, text="")
    caption_lbl.config(text="Показано: Фото страви")
    btn_hide.config(state="normal")


def hide_photo():
    photo_label.config(image="", text="[Фото приховано]", bg="#d9d9d9", fg="#333333")
    caption_lbl.config(text="Зображення приховано")
    btn_hide.config(state="disabled")


btn_avatar = tk.Button(root, text="Аватар користувача", width=22, command=show_avatar)
btn_avatar.place(x=25, y=160)

btn_dish = tk.Button(root, text="Фото страви", width=22, command=show_dish)
btn_dish.place(x=25, y=200)

btn_hide = tk.Button(
    root, text="Забрати зображення", width=22, state="disabled", command=hide_photo
)
btn_hide.place(x=25, y=240)

root.mainloop()