import customtkinter as ctk
import Final1

LARGEFONT =("Verdana", 100)


class customtkinterApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.container = ctk.CTkFrame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=20)
        self.container.grid_columnconfigure(0, weight=20)
        

        self.frames = {}

        for F in (StartPage, Page1, Page2, Page3):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.lift()  # Use lift() for customtkinter

class StartPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = ctk.CTkLabel(self, text="Paint Rush", font=LARGEFONT)
        label.grid(row=0, column=10, padx=10, pady=10)

        button1 = ctk.CTkButton(self, text="How to Play",
                                command=lambda: controller.show_frame(Page1))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ctk.CTkButton(self, text="Settings",
                                command=lambda: controller.show_frame(Page2))
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ctk.CTkButton(self, text="Play game",
                                command=lambda: controller.show_frame(StartPage))  # Corrected loop
        button3.grid(row=3, column=1, padx=10, pady=10)


class Page1(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = ctk.CTkLabel(self, text="How to Play", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ctk.CTkButton(self, text="Back",
                                command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ctk.CTkButton(self, text="Settings",
                                command=lambda: controller.show_frame(Page2))
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ctk.CTkButton(self, text="Play game",
                                command=lambda: controller.show_frame(StartPage))
        button3.grid(row=3, column=1, padx=10, pady=10)


class Page2(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.switch1_var = ctk.StringVar(value="on")
        self.switch2_var = ctk.StringVar(value="off")  # Changed initial value to "off"

        label = ctk.CTkLabel(self, text="Settings Page", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ctk.CTkButton(self, text="Back",
                                 command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ctk.CTkButton(self, text="Settings",
                                 command=lambda: controller.show_frame(Page2))
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ctk.CTkButton(self, text="Play game",
                                 command=lambda: controller.show_frame(StartPage))
        button3.grid(row=3, column=1, padx=10, pady=10)

        # Switches placed in the middle rows
        switch1 = ctk.CTkSwitch(self, text="Color modes", variable=self.switch1_var, onvalue="on", offvalue="off", command=self)
        switch1.grid(row=4, column=2, padx=10, pady=10, sticky="nsew")  # Moved to center column

        switch2 = ctk.CTkSwitch(self, text="No Music", variable=self.switch2_var, onvalue="on", offvalue="off", command=self)
        switch2.grid(row=5, column=2, padx=10, pady=10, sticky="nsew")  # Moved to center column

    def switch1(self):
        print("Switch 1 is", self.switch1_var.get())
        if self.switch1_var.get() == "on":
            app._set_appearance_mode("light")
            self.configure(bg="white")
        else:
            app._set_appearance_mode("dark")
            self.configure(bg="black")
        self.update()

    def switch2(self):
        print("Switch 2 is", self.switch2_var.get())
        if self.switch2_var.get() == "on":
            # Implement functionality to turn music off (e.g., mute audio)
            print("Music off")
        else:
            # Implement functionality to turn music on (e.g., unmute audio)
            print("Music on")

class Page3(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = ctk.CTkLabel(self, text="Select game mode!", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ctk.CTkButton(self, text="Back",
                                command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ctk.CTkButton(self, text="Settings",
                                command=lambda: controller.show_frame(Page2))
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ctk.CTkButton(self, text="Play game",
                                command=lambda: controller.show_frame(StartPage))
        button3.grid(row=3, column=1, padx=10, pady=10)

app = customtkinterApp()
app.mainloop()