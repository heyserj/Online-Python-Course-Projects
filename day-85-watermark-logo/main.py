from tkinter import Tk, filedialog, Button, Label, Canvas
from PIL import Image, ImageTk
import tkinter

FONT_NAME = "Arial"
GREETING_FONT_SIZE = 16
BUTTON_FONT_SIZE = 12
IMAGE_PREVIEW_FONT_SIZE = 14

# class ImageEditor:
#     def __init__(self, window, main_image_path):
#         self.window = window
#         self.canvas = Canvas(window, width=self.window.winfo_screenwidth() * 0.6, height=self.window.winfo_screenheight() * 0.6)
#         self.canvas.pack()

#         self.original_image = Image.open(main_image_path)
#         self.display_image = self.original_image.copy()
#         self.tk_image = ImageTk.PhotoImage(self.display_image)

#         self.image_id = self.canvas.create_image(300, 300, image=self.tk_image, anchor="center")

#         self.canvas.tag_bind(self.image_id, "<ButtonPress-1>", func=self.on_press)
#         self.canvas.tag_bind(self.image_id, "<B1-Motion>", func=self.on_drag)

#         self.window.bind("<MouseWheel>", self.on_mouse_wheel)  # Windows
#         self.window.bind("<Button-4>", self.on_mouse_wheel)    # Linux scroll up
#         self.window.bind("<Button-5>", self.on_mouse_wheel)    # Linux scroll down

#         self.last_x = 0
#         self.last_y = 0
#         self.scale = 1.0

#     def on_press(self, event):
#         self.last_x = event.x
#         self.last_y = event.y

#     def on_drag(self, event):
#         dx = event.x - self.last_x
#         dy = event.y - self.last_y
#         self.canvas.move(self.image_id, dx, dy)
#         self.last_x = event.x
#         self.last_y = event.y

#     def on_mouse_wheel(self, event):
#         # Zoom in/out
#         if event.delta > 0 or event.num == 4:
#             self.scale *= 1.1
#         elif event.delta < 0 or event.num == 5:
#             self.scale *= 0.9

#         # Resize the image
#         new_size = (int(self.original_image.width * self.scale),
#                     int(self.original_image.height * self.scale))
#         self.display_image = self.original_image.resize(new_size)
#         self.tk_image = ImageTk.PhotoImage(self.display_image)

#         # Update canvas image
#         self.canvas.itemconfig(self.image_id, image=self.tk_image)


def upload_main_image():
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )

    if file_path:
        for widget in window.winfo_children():
            widget.destroy()

        header_label = Label(text="Image Preview:", font=(FONT_NAME, IMAGE_PREVIEW_FONT_SIZE, "normal"))
        header_label.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)

        canvas = Canvas(window, width=window.winfo_screenwidth() * 0.6, height=window.winfo_screenheight() * 0.6)
        canvas.place(relx=0.5, rely=0.44, anchor=tkinter.CENTER)                 
        canvas.update_idletasks()

        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()

        img = Image.open(file_path)
        img = img.resize((canvas_width, canvas_height))
        tk_img = ImageTk.PhotoImage(img)

        canvas.tk_img = tk_img
        canvas.create_image(canvas_width // 2, canvas_height // 2, image=tk_img, anchor="center")

        back_btn = Button(text="Re-Upload Image", font=(FONT_NAME, BUTTON_FONT_SIZE, "normal"), command=upload_main_image, bg="light blue")
        back_btn.place(relx=0.25, rely=0.85, anchor=tkinter.CENTER)
    

window = Tk()
window.title("Watermark Logo Application")
window.minsize(width=window.winfo_screenwidth(), height=window.winfo_screenheight())
window.config(padx=20, pady=20)

greeting_label = Label(text="Welcome! Please upload an image to get started.", font=(FONT_NAME, GREETING_FONT_SIZE, "normal"))
greeting_label.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

upload_btn = Button(text="Upload Image", font=(FONT_NAME, BUTTON_FONT_SIZE, "normal"), bg="light blue", command=upload_main_image)
upload_btn.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

window.mainloop()