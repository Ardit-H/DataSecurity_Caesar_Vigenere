import tkinter as tk
from tkinter import filedialog,messagebox
import os

def caesar_encrypt(text,key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char)-base+shift)%26+base)
        else:
            result +=char
    return  result

def caesar_decrypt(text,key):
    return caesar_encrypt(text,-key)

def vigenere_encrypt(text,key):
    result=""
    key=key.lower()
    key_index=0
    for char in text:
        if char.isalpha():
            shift=ord(key[key_index%len(key)])-ord('a')
            base=ord('A') if char.isupper() else ord('a')
            result+=chr((ord(char)-base+shift)%26+base)
            key_index+=1
        else:
            result+=char
    return  result

def vigenere_decrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = -(ord(key[key_index % len(key)]) - ord('a'))
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def process_file(encrypt=True):
    key = key_entry.get()
    algo = algo_var.get()
    try:
        if algo == "Caesar":
            key = int(key)
        elif algo == "Vigenere":
            if not key.isalpha():
                raise ValueError("Key for Vigenere must be letters only.")
    except ValueError as ve:
        messagebox.showerror("Error", f"Invalid key: {ve}")
        return

    input_path = input_file_entry.get()
    output_path = output_file_entry.get()


  if not os.path.exists(input_path):
        messagebox.showerror("Error", "Input file does not exist.")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        data = f.read()

    if algo == "Caesar":
        result = caesar_encrypt(data, key) if encrypt else caesar_decrypt(data, key)
    else:
        result = vigenere_encrypt(data, key) if encrypt else vigenere_decrypt(data, key)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)

    messagebox.showinfo("Success", "Operation completed successfully.")

def save_message_to_file():
    message = message_text.get("1.0", tk.END).strip()
    path = filedialog.asksaveasfilename(defaultextension=".txt")
    if path:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(message)
        messagebox.showinfo("Saved", "Message saved to file.")

root = tk.Tk()
root.title("File Encrypt/Decrypt - Caesar & Vigenère")

tk.Label(root, text="Key:").grid(row=0, column=0)
key_entry = tk.Entry(root, width=30)
key_entry.grid(row=0, column=1)

tk.Label(root, text="Algorithm:").grid(row=1, column=0)
algo_var = tk.StringVar(value="Caesar")
tk.OptionMenu(root, algo_var, "Caesar", "Vigenere").grid(row=1, column=1)

tk.Label(root, text="Input File Path:").grid(row=2, column=0)
input_file_entry = tk.Entry(root, width=50)
input_file_entry.grid(row=2, column=1)
tk.Button(root, text="Browse", command=lambda: input_file_entry.insert(0, filedialog.askopenfilename())).grid(row=2, column=2)

tk.Label(root, text="Output File Path:").grid(row=3, column=0)
output_file_entry = tk.Entry(root, width=50)
output_file_entry.grid(row=3, column=1)
tk.Button(root, text="Browse", command=lambda: output_file_entry.insert(0, filedialog.asksaveasfilename(defaultextension=".txt"))).grid(row=3, column=2)

tk.Button(root, text="Encrypt File", command=lambda: process_file(True)).grid(row=4, column=1)
tk.Button(root, text="Decrypt File", command=lambda: process_file(False)).grid(row=4, column=2)

tk.Label(root, text="Message Box:").grid(row=5, column=0, pady=10)
message_text = tk.Text(root, height=5, width=50)
message_text.grid(row=5, column=1, columnspan=2)

tk.Button(root, text="Save Message to File", command=save_message_to_file).grid(row=6, column=1, pady=10)

root.mainloop()


