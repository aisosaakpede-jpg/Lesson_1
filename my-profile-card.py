import tkinter as tk
window = tk.Tk()
window.title("My Profile Card")
window.geometry("400x380")
title = tk.Label(window,text="My Profile Card",fg = "white",bg="purple",width=40)
title.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
name_label = tk.Label(window,text="Name: ",fg="black",bg = "white")
name_label.grid(row=1,column=0,padx=10,pady=5)
name_entry = tk.Entry(window,fg="blue",bg="lightyellow",width=25)
name_entry.grid(row=1,column=1,padx=10,pady=5)

hobby_label = tk.Label(window,text="Hobby: ",fg="black",bg = "white")
hobby_label.grid(row=2,column=0,padx=10,pady=5)
hobby_entry = tk.Entry(window,fg="blue",bg="yellow",width=25)
hobby_entry.grid(row=2,column=1,padx=10,pady=5)

about_frame = tk.Frame(window,relief="raised",borderwidth=3)
about_frame.grid(row=3,column=0,columnspan=2,padx=10,pady=5)
about_label = tk.Label(about_frame,text="About Me: ")
about_label.pack()

about_text = tk.Text(about_frame,fg="green",bg="lightyellow",width=40,height=4)
about_text.pack()


submit = Button(window, text='Show My Card', bg='purple', fg='white', width=20)

submit.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()