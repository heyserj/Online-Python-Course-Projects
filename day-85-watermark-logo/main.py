from tkinter import Tk, filedialog, Button, Label
from PIL import Image, ImageTk
import tkinter

FONT_NAME = "Arial"
GREETING_FONT_SIZE = 16
UPLOAD_BUTTON_FONT_SIZE = 12

def upload_image():
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )

    if file_path:
        print(file_path)
        img = Image.open(file_path)
        img = img.resize((300, 300))
        tk_img = ImageTk.PhotoImage(img)
        label = Label(window, image=tk_img)
        label.image = tk_img
        label.pack()

    

window = Tk()
window.title("Watermark Logo Application")
window.minsize(width=800, height=800)

greeting_label = Label(text="Welcome! Please upload an image to get started.", font=(FONT_NAME, GREETING_FONT_SIZE, "normal"))
greeting_label.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

upload_btn = Button(text="Upload Image", font=(FONT_NAME, UPLOAD_BUTTON_FONT_SIZE, "normal"), bg="light blue", command=upload_image)
upload_btn.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)







window.mainloop()