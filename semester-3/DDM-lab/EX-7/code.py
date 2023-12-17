import tkinter as tk
import cx_Oracle as db
connection = db.connect(user="system",password="grace",dsn="XE")

root = tk.Tk()
root.geometry("300x200")
tk.Label(root, text='Name:').pack(padx="40 120", pady="20 0")
name = tk.Entry(root)
name.pack(fill="y", padx=40, side="top")
tk.Label(root, text='Age:').pack(padx="40 130", pady="5 0")
age = tk.Entry(root)
age.pack(fill="y", padx=40, side="top")

def callback():
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO Student (Name, Age) VALUES (:1, :2)"
            cursor.execute(sql, (name.get(), age.get()))
            connection.commit()
            log.set(f"Success!\n Name: {name.get()} age: {age.get()}")
    except Exception:
        log.set('Failed!')
        
tk.Button(root, text="Submit", width=10, command=callback).pack(pady=10)
log = tk.StringVar(value='Enter the data')
tk.Label(root, textvariable=log).pack(pady=10, side="bottom")
root.mainloop()