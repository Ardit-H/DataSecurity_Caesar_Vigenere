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