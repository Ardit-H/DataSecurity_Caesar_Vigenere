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





