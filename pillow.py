import tkinter as tk
from PIL import Image,ImageTk
import tkinter as messagebox
window = tk.Tk()
def show_information():
    messagebox.showinfo(
        "Photo Information","The Photo has successfully loaded"
    )
def show_details():
    details_window = tk.Toplevel(window)
    details_window.title("Photo details")
    details_window.geometry("300 x 200")
    title_label = tk.Label(
        details_window,text = "Photo Details",font = ("Arial",16)
    )
    title_label.pack(pady=10)
    details_label = tk.Label(
        details_window,text = "File: images.jpg\nSize = 300x200 pixels"
    )
    details_label.pack(pady=10)
    close_button = tk.Button(
        details_window,text="close button",command = details_window.destroy
    )
    close_button.pack(pady=10)
window = tk.Tk()

window.title("Photo Viewer")

window.geometry("500x500")

image = Image.open("example.jpg")

image = image.resize((300, 200))

photo = ImageTk.PhotoImage(image)

image_label = tk.Label(

window, image=photo

)

image_label.pack(pady=20)

info_button = tk.Button(

window, text="Photo Information", command=show_information

)

info_button.pack(pady=10)

details_button = tk.Button(

window, text="Photo Details", command=show_details

)

details_button.pack(pady=10)

window.mainloop()