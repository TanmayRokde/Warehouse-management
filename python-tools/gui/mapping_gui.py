import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from core.sku_mapper import SKUMappingTool
from core.config import MAPPED_OUTPUT_FILE
from gui.style import set_theme

class MappingApp:
    def __init__(self, root):
        self.root = root
        set_theme(root)
        self.mapper = SKUMappingTool()
        self.sales_df = None

        self.upload_button = tk.Button(root, text="Upload Sales File", command=self.load_file)
        self.upload_button.pack(pady=10)

        self.export_button = tk.Button(root, text="Export Mapped File", command=self.export_file)
        self.export_button.pack(pady=10)

        self.text = tk.Text(root, height=15)
        self.text.pack(padx=10, pady=10, fill="both", expand=True)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return
        try:
            self.sales_df = pd.read_csv(file_path)
            self.sales_df = self.mapper.map_sales_data(self.sales_df)
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, self.sales_df.head(20).to_string())
            messagebox.showinfo("Success", "File loaded and mapped!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def export_file(self):
        if self.sales_df is not None:
            self.sales_df.to_csv(MAPPED_OUTPUT_FILE, index=False)
            messagebox.showinfo("Exported", f"Saved to {MAPPED_OUTPUT_FILE}")
        else:
            messagebox.showwarning("No Data", "Please upload and map a file first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MappingApp(root)
    root.mainloop()
