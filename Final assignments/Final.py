import customtkinter as ctk
import pygame  # Ensure pygame is imported

LARGEFONT = ("Verdana", 50)

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

        self.show_frame(StartPage)  # Show StartPage initially

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.lift()

class StartPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = ctk.CTkLabel(self, text="Paint Rush", font=LARGEFONT)
        label.grid(row=0, column=10, padx=10, pady=10)

        button1 = ctk.CTkButton(self, text="How to Play", command=lambda: controller.show_frame(Page1))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ctk.CTkButton(self, text="Credits", command=lambda: controller.show_frame(Page2))
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ctk.CTkButton(self, text="Play game", command=lambda: controller.show_frame(Page3))
        button3.grid(row=3, column=1, padx=10, pady=10)

class Page1(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = ctk.CTkLabel(self, text="How to Play", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ctk.CTkButton(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ctk.CTkButton(self, text="Credits", command=lambda: controller.show_frame(Page2))
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ctk.CTkButton(self, text="Play game", command=lambda: controller.show_frame(Page3))
        button3.grid(row=3, column=1, padx=10, pady=10)

class Page2(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = ctk.CTkLabel(self, text="Credits Page", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ctk.CTkButton(self, text="How to Play", command=lambda: controller.show_frame(Page1))
        button1.grid(row=1, column=5, padx=10, pady=10)

        button2 = ctk.CTkButton(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button2.grid(row=2, column=5, padx=10, pady=10)

        button3 = ctk.CTkButton(self, text="Play game", command=lambda: controller.show_frame(Page3))
        button3.grid(row=3, column=5, padx=10, pady=10)

class Page3(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = ctk.CTkLabel(self, text="Choose Game mode", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ctk.CTkButton(self, text="How to Play", command=lambda: controller.show_frame(Page1))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ctk.CTkButton(self, text="Credits", command=lambda: controller.show_frame(Page2))
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ctk.CTkButton(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button3.grid(row=3, column=1, padx=10, pady=10)

        button4 = ctk.CTkButton(self, text="Freeplay", command=self.run_freeplay_game)
        button4.grid(row=4, column=5, padx=20, pady=20)

        button5 = ctk.CTkButton(self, text="Racing mode", command=self.run_racing_game)
        button5.grid(row=5, column=5, padx=20, pady=20)

    def run_freeplay_game(self):
        try:
            import Final1
            pygame.init()
            Final1.main()
        except Exception as e:
            print("Error running freeplay game:", e)

    def run_racing_game(self):
        try:
            import Final2
            pygame.init()
            Final2.main()
        except Exception as e:
            print("Error running racing game:", e)

if __name__ == "__main__":
    app = customtkinterApp()
    app.mainloop()
