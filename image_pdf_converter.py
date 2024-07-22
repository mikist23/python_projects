import tkinter as tk
from tkinter import filedialog
import os

class ImageToPDFConverter:
    def __init__(self,root):
        self.root = root
        self.image_paths = []
        self.output_pdf_name = tk.StringVar()
        self.selected_images_listbox = tk.Listbox(root,selectmode=tk.MULTIPLE)

        self.initialize_ui()

    def initialize_ui(self):
        title_label = tk.Label(self.root,text="Image to PDF Converter", font=("Halvetica",16,"bold"))
        title_label.pack(pady=10)

        select_image_button = tk.Button(self.root,text='Select Images', command = self.select_images)
        select_image_button.pack(pady=(0,10))

        self.selected_images_listbox.paack(pady = (0,10), fill = tk.BOTH, expand = True)

        label = tk.Label(self.root,text ="Enter output PDF name:")
        label.pack()

        pdf_name_entry = tk.Entry(self.root, textvariable=self.output_pdf_name, widh = 40, justify="center")
        pdf_name_entry.pack()


def main():
    root =tk.Tk()
    root.title("Image To PDF")
    converter = ImageToPDFConverter(root)
    root.geometry("400x400")
    root.mainloop()

if __name__ == "__main__":
    main()