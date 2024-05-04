import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTK()
root.geometry("500x350")


def login():
  print("Test")


frame = customtkinter.CTKFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTKLabel(master=frame, text="Login System", text_font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 =customtkinter.CTKEntry(master=frame, placeholder_text= "Username")
entry1.pack(pady=12, padx=10)

entry2 =customtkinter.CTKEntry(master=frame, placeholder_text= "Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTKButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTKCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()