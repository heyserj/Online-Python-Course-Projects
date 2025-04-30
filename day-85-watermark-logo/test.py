import tkinter as tk
from tkinter import filedialog, colorchooser, font
from PIL import Image, ImageTk, ImageDraw

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text & Logo Editor")
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.text_items = []   # Stores (text, x, y, font, color)
        self.image_overlays = []  # Stores (image, x, y)

        self.font_family = tk.StringVar(value="Arial")
        self.font_size = tk.IntVar(value=24)
        self.font_color = "#000000"

        self.load_base_image()

        self.setup_controls()

    def load_base_image(self):
        path = filedialog.askopenfilename(title="Select base image")
        if not path:
            return
        self.base_image = Image.open(path)
        self.tk_base_image = ImageTk.PhotoImage(self.base_image)
        self.canvas.config(width=self.tk_base_image.width(), height=self.tk_base_image.height())
        self.canvas.create_image(0, 0, image=self.tk_base_image, anchor="nw")

    def setup_controls(self):
        control_frame = tk.Frame(self.root)
        control_frame.pack(fill="x", pady=5)

        tk.Label(control_frame, text="Font:").pack(side="left")
        font_menu = tk.OptionMenu(control_frame, self.font_family, *font.families())
        font_menu.pack(side="left")

        tk.Label(control_frame, text="Size:").pack(side="left")
        size_entry = tk.Entry(control_frame, textvariable=self.font_size, width=4)
        size_entry.pack(side="left")

        color_btn = tk.Button(control_frame, text="Font Color", command=self.choose_color)
        color_btn.pack(side="left")

        add_text_btn = tk.Button(control_frame, text="Add Text", command=self.add_text)
        add_text_btn.pack(side="left")

        logo_btn = tk.Button(control_frame, text="Add Logo", command=self.add_logo)
        logo_btn.pack(side="left")

        save_btn = tk.Button(control_frame, text="Save", command=self.save_image)
        save_btn.pack(side="right")

    def choose_color(self):
        color = colorchooser.askcolor(title="Pick Font Color")
        if color:
            self.font_color = color[1]

    def add_text(self):
        entry = tk.Entry(self.canvas, font=(self.font_family.get(), self.font_size.get()))
        entry_window = self.canvas.create_window(100, 100, window=entry, anchor="nw")

        def finish_text(event=None):
            text = entry.get()
            self.canvas.delete(entry_window)
            x, y = self.canvas.coords(entry_window)
            canvas_text = self.canvas.create_text(x, y, text=text,
                                                  font=(self.font_family.get(), self.font_size.get()),
                                                  fill=self.font_color, anchor="nw")
            self.text_items.append((text, x, y, self.font_family.get(), self.font_size.get(), self.font_color))
            self.make_draggable(canvas_text, "text")

        entry.bind("<Return>", finish_text)
        entry.focus_set()

    def add_logo(self):
        logo_path = filedialog.askopenfilename(title="Select Logo Image")
        if not logo_path:
            return
        logo_img = Image.open(logo_path).convert("RGBA")
        logo_img = logo_img.resize((100, 100))
        tk_logo = ImageTk.PhotoImage(logo_img)
        logo_id = self.canvas.create_image(150, 150, image=tk_logo, anchor="nw")
        self.canvas.image = tk_logo  # prevent garbage collection
        self.image_overlays.append((logo_img, 150, 150))
        self.make_draggable(logo_id, "image")

    def make_draggable(self, item_id, item_type):
        def on_drag(event):
            x, y = event.x, event.y
            self.canvas.coords(item_id, x, y)

            if item_type == "image":
                for i, (img, _, _) in enumerate(self.image_overlays):
                    if self.canvas.find_withtag(item_id):
                        self.image_overlays[i] = (img, x, y)
                        break
            elif item_type == "text":
                for i, (text, _, _, fnt, size, color) in enumerate(self.text_items):
                    if self.canvas.find_withtag(item_id):
                        self.text_items[i] = (text, x, y, fnt, size, color)
                        break

        self.canvas.tag_bind(item_id, "<B1-Motion>", on_drag)

    def save_image(self):
        output = self.base_image.copy()
        draw = ImageDraw.Draw(output)

        # Draw text
        for text, x, y, font_name, font_size, color in self.text_items:
            draw.text((x, y), text, fill=color)

        # Draw image overlays
        for img, x, y in self.image_overlays:
            output.paste(img, (int(x), int(y)), img)

        save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if save_path:
            output.save(save_path)
            print(f"Saved to {save_path}")

# Run the editor
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()