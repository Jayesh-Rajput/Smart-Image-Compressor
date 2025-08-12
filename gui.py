import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from smart_image_compressor import batch_compress, get_preview

def select_folder(entry):
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry.delete(0, tk.END)
        entry.insert(0, folder_selected)

def select_file(entry):
    file_selected = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.webp")])
    if file_selected:
        entry.delete(0, tk.END)
        entry.insert(0, file_selected)

def update_preview():
    src = preview_entry.get()
    try:
        max_w = int(width_entry.get())
        max_h = int(height_entry.get())
        quality = int(quality_entry.get())
        fmt = format_var.get() if format_var.get() != "Auto" else None

        # Original image
        original = Image.open(src)
        original.thumbnail((250, 250))
        original_tk = ImageTk.PhotoImage(original)
        original_label.config(image=original_tk)
        original_label.image = original_tk

        # Compressed preview
        buf = get_preview(src, max_w, max_h, quality, fmt)
        compressed = Image.open(buf)
        compressed.thumbnail((250, 250))
        compressed_tk = ImageTk.PhotoImage(compressed)
        compressed_label.config(image=compressed_tk)
        compressed_label.image = compressed_tk

    except Exception as e:
        messagebox.showerror("Preview Error", str(e))

def run_compression():
    src = src_entry.get()
    dest = dest_entry.get()
    try:
        max_w = int(width_entry.get())
        max_h = int(height_entry.get())
        quality = int(quality_entry.get())
        fmt = format_var.get() if format_var.get() != "Auto" else None
        batch_compress(src, dest, max_width=max_w, max_height=max_h, quality=quality, format=fmt)
        messagebox.showinfo("Success", "Compression completed!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Smart Image Compressor")

# Source Folder
tk.Label(root, text="Source Folder").grid(row=0, column=0)
src_entry = tk.Entry(root, width=40)
src_entry.grid(row=0, column=1)
tk.Button(root, text="Browse", command=lambda: select_folder(src_entry)).grid(row=0, column=2)

# Destination Folder
tk.Label(root, text="Destination Folder").grid(row=1, column=0)
dest_entry = tk.Entry(root, width=40)
dest_entry.grid(row=1, column=1)
tk.Button(root, text="Browse", command=lambda: select_folder(dest_entry)).grid(row=1, column=2)

# Max Width
tk.Label(root, text="Max Width").grid(row=2, column=0)
width_entry = tk.Entry(root, width=10)
width_entry.insert(0, "1024")
width_entry.grid(row=2, column=1, sticky="w")

# Max Height
tk.Label(root, text="Max Height").grid(row=3, column=0)
height_entry = tk.Entry(root, width=10)
height_entry.insert(0, "1024")
height_entry.grid(row=3, column=1, sticky="w")

# Quality
tk.Label(root, text="Quality (JPEG)").grid(row=4, column=0)
quality_entry = tk.Entry(root, width=10)
quality_entry.insert(0, "90")
quality_entry.grid(row=4, column=1, sticky="w")

# Format Option
tk.Label(root, text="Format").grid(row=5, column=0)
format_var = tk.StringVar(value="Auto")
tk.OptionMenu(root, format_var, "Auto", "JPEG", "PNG", "WEBP").grid(row=5, column=1, sticky="w")

# Image Preview Section
tk.Label(root, text="Preview Image File").grid(row=6, column=0)
preview_entry = tk.Entry(root, width=40)
preview_entry.grid(row=6, column=1)
tk.Button(root, text="Browse", command=lambda: select_file(preview_entry)).grid(row=6, column=2)
tk.Button(root, text="Update Preview", command=update_preview).grid(row=6, column=3)

preview_frame = tk.Frame(root)
preview_frame.grid(row=7, column=0, columnspan=4, pady=10)
tk.Label(preview_frame, text="Original").grid(row=0, column=0)
tk.Label(preview_frame, text="Compressed Preview").grid(row=0, column=1)

original_label = tk.Label(preview_frame)
original_label.grid(row=1, column=0, padx=10)
compressed_label = tk.Label(preview_frame)
compressed_label.grid(row=1, column=1, padx=10)

# Compress Button
tk.Button(root, text="Compress Images", command=run_compression, bg="lightgreen").grid(row=8, column=0, columnspan=4, pady=10)

root.mainloop()