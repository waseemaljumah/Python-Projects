import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import os

# دالة للحصول على المسار الصحيح للملفات داخل EXE
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # لما يكون ملف exe
    except AttributeError:
        base_path = os.path.abspath(".")  # لما يكون سكربت عادي
    return os.path.join(base_path, relative_path)

# ------------------- الدوال -------------------
def حساب_bmi():
    try:
        الطول = float(ادخال_الطول.get()) / 100  # من سم إلى متر
        الوزن = float(ادخال_الوزن.get())
        العمر = int(ادخال_العمر.get())
        الجنس = اختيار_الجنس.get()

        bmi = round(الوزن / (الطول ** 2), 1)

        if bmi < 18.5:
            الحالة = "نحيف"
            اللون = "#00BFFF"
        elif 18.5 <= bmi < 25:
            الحالة = "وزن صحي"
            اللون = "#3CB371"
        elif 25 <= bmi < 30:
            الحالة = "وزن زائد"
            اللون = "#FFD700"
        else:
            الحالة = "سمنة"
            اللون = "#FF4500"

        الوزن_المثالي = round(22 * (الطول ** 2), 1)
        الفرق = round(الوزن - الوزن_المثالي, 1)

        تفاصيل_النتيجة = f"\nمؤشر كتلة الجسم: {bmi}\nالحالة: {الحالة}\nالوزن المثالي: {الوزن_المثالي} كجم\nالفرق عن الوزن المثالي: {فرق_النص(الفرق)}"

        النتيجة_النص.config(text=تفاصيل_النتيجة, fg=اللون)
        رسم_الشريط(bmi)

    except ValueError:
        messagebox.showerror("خطأ", "يرجى إدخال القيم بشكل صحيح")

def فرق_النص(فرق):
    if فرق > 0:
        return f"+{فرق} كجم فوق المثالي"
    elif فرق < 0:
        return f"{فرق} كجم تحت المثالي"
    else:
        return "الوزن مثالي تمامًا"

def تغيير_النص():
    النص = "استمر" if اختيار_الجنس.get() == "ذكر" else "استمري"
    زر_النتيجة.config(text=النص)

def رسم_الشريط(bmi):
    canvas.delete("all")
    الألوان = [(0, 18.5, "#00BFFF"), (18.5, 25, "#3CB371"), (25, 30, "#FFD700"), (30, 50, "#FF4500")]
    x = 10
    for بداية, نهاية, لون in الألوان:
        عرض = (نهاية - بداية) * 10
        canvas.create_rectangle(x, 10, x + عرض, 30, fill=لون, outline="")
        x += عرض

    مؤشر = (min(bmi, 50)) * 10
    canvas.create_line(مؤشر, 5, مؤشر, 35, fill="black", width=2)

# ------------------- النافذة -------------------
نافذة = tk.Tk()
نافذة.title("حاسبة مؤشر كتلة الجسم")
نافذة.geometry("450x600")
نافذة.configure(bg="#ffe6f0")

# ------------------- صورة ترحيبية -------------------
صورة_الترحيب_الخام = Image.open(resource_path("welcome.jpg")).resize((350, 300))
صورة_ترحيب = ImageTk.PhotoImage(صورة_الترحيب_الخام)
تسمية_صورة = tk.Label(نافذة, image=صورة_ترحيب, bg="#ffe6f0")
تسمية_صورة.pack(pady=10)

# ------------------- مدخلات -------------------
اختيار_الجنس = tk.StringVar(value="أنثى")
إطار_الإدخال = tk.Frame(نافذة, bg="#ffe6f0")
إطار_الإدخال.pack(pady=10)

# الجنس
تسمية_جنس = tk.Label(إطار_الإدخال, text="الجنس:", bg="#ffe6f0", font=("Arial", 12))
تسمية_جنس.grid(row=0, column=0, padx=5, pady=5)

صورة_ذكر = ImageTk.PhotoImage(Image.open(resource_path("male_icon.png")).resize((50, 50)))
صورة_أنثى = ImageTk.PhotoImage(Image.open(resource_path("female_icon.png")).resize((50, 50)))

زر_ذكر = tk.Radiobutton(إطار_الإدخال, image=صورة_ذكر, variable=اختيار_الجنس, value="ذكر", command=تغيير_النص, bg="#ffe6f0")
زر_ذكر.grid(row=0, column=1, padx=5)
زر_أنثى = tk.Radiobutton(إطار_الإدخال, image=صورة_أنثى, variable=اختيار_الجنس, value="أنثى", command=تغيير_النص, bg="#ffe6f0")
زر_أنثى.grid(row=0, column=2, padx=5)

# العمر
tk.Label(إطار_الإدخال, text="العمر:", bg="#ffe6f0", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
ادخال_العمر = tk.Entry(إطار_الإدخال)
ادخال_العمر.grid(row=1, column=1, columnspan=2)

# الطول
tk.Label(إطار_الإدخال, text="الطول (سم):", bg="#ffe6f0", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5)
ادخال_الطول = tk.Entry(إطار_الإدخال)
ادخال_الطول.grid(row=2, column=1, columnspan=2)

# الوزن
tk.Label(إطار_الإدخال, text="الوزن (كجم):", bg="#ffe6f0", font=("Arial", 12)).grid(row=3, column=0, padx=5, pady=5)
ادخال_الوزن = tk.Entry(إطار_الإدخال)
ادخال_الوزن.grid(row=3, column=1, columnspan=2)

# ------------------- زر الحساب -------------------
زر_النتيجة = tk.Button(نافذة, text="استمري", command=حساب_bmi, bg="#ffb6c1", font=("Arial", 14, "bold"))
زر_النتيجة.pack(pady=10)

# ------------------- نتيجة النص -------------------
النتيجة_النص = tk.Label(نافذة, text="", bg="#ffe6f0", font=("Arial", 12))
النتيجة_النص.pack(pady=10)

# ------------------- شريط الألوان -------------------
canvas = tk.Canvas(نافذة, width=400, height=40, bg="#ffe6f0", highlightthickness=0)
canvas.pack(pady=10)

# ------------------- تشغيل البرنامج -------------------
نافذة.mainloop()