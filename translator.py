import tkinter as tk
from googletrans import Translator
from tkinter import messagebox

def translata():
    text =entry.get("1.0",tk.END).strip()

    if not text:
        messagebox.showwarning('enter your text',)
        
        return

    try:
        result = translator.translate(text,dest='fa')
        result_box.delete("1.0",tk.END)
        result_box.insert("1.0",result.text)
    except Exception as e:
        result_box.delete("1.0",tk.END)
        result_box.insert("1.0",f"error in translate {e}")


root = tk.Tk()
root.title("translator")
root.geometry("400x300")
root.configure(bg="#0E483E")


translator = Translator()

entry = tk.Text(root,font=("Arial",12),width=30,height=5,bg="#ffffff",fg="black")
entry.pack(pady=15)
entry.bind("<Return>",lambda event:translata())



btn = tk.Button(root, text="translate", command=translata, font=("Arial",11,"bold"),bg="#3b82f6",fg="white",padx=15,pady=3)
btn.pack(pady=5)

def clear():
    entry.delete("1.0",tk.END)
    result_box.delete("1.0",tk.END)

    clear_btn = tk.Button(root,text="clear",command=clear,font=("Comic Sans MS",12))
    clear_btn.pack

result_box =tk.Text(root,font=("B Nazanin",13),width=30,height=5,wrap="word",bg="#dcfcef",fg="black")
result_box.pack(pady=15)

root.mainloop()