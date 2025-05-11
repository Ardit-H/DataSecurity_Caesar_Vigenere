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



