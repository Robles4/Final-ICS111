import customtkinter as ctk
import random
import Final1
import Final2


LARGEFONT =("Verdana", 50)


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

        button2 = ctk.CTkButton(self, text="Credits",
                                command=lambda: controller.show_frame(Page2))
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ctk.CTkButton(self, text="Play game",
                                command=lambda: controller.show_frame(Page3))  # Corrected loop
        button3.grid(row=3, column=1, padx=10, pady=10)


class Page1(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = ctk.CTkLabel(self, text="How to Play", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ctk.CTkButton(self, text="Back",
                                command=lambda: controller.show_frame(Page1))
        button1.grid(row=1, column=1, padx=10, pady=10)

        button2 = ctk.CTkButton(self, text="Credits",
                                command=lambda: controller.show_frame(Page2))
        button2.grid(row=2, column=1, padx=10, pady=10)

        button3 = ctk.CTkButton(self, text="Play game",
                                command=lambda: controller.show_frame(Page3))
        button3.grid(row=3, column=1, padx=10, pady=10)


class Page2(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

         # Create a container element for centering
        container = ctk.CTkFrame(self)
        container.grid(column=0, row=0, columnspan=5, rowspan=6)  # Span all columns and rows

        # Centering logic using grid with negative margins
        label = ctk.CTkLabel(container, text="Thanks to My professor for the ideas", font=LARGEFONT)
        label.grid(row=8, column=1, padx=10 ,pady=10)  # Adjust row and column for placement

        # Make the row and column containing the label flexible
        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(2, weight=1)

        # Calculate negative margins for centering
        window_width = self.winfo_width()  # Get window width
        label_width = label.winfo_width()  # Get label width
        margin_x = (window_width - label_width) // 2  # Calculate horizontal margin

        # Apply negative margins to center the label
        label.grid(row=1, column=2, pady=20, padx=-margin_x)  # Add negative horizontal margin

        label = ctk.CTkLabel(self, text="Credits Page", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ctk.CTkButton(self, text="How to Play",
                                 command=lambda: controller.show_frame(Page1))
        button1.grid(row=1, column=5, padx=10, pady=10)

        button2 = ctk.CTkButton(self, text="Back",
                                 command=lambda: controller.show_frame(Page2))
        button2.grid(row=2, column=5, padx=10, pady=10)

        button3 = ctk.CTkButton(self, text="Play game",
                                 command=lambda: controller.show_frame(Page3))
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

        button3 = ctk.CTkButton(self, text="Back", command=lambda: controller.show_frame(Page3))
        button3.grid(row=3, column=1, padx=10, pady=10)

        button4 = ctk.CTkButton(self, text="Freeplay")
        button4.grid(row=4, column=5, padx=20, pady=20,)

        button5 = ctk.CTkButton(self, text="Racing mode")
        button5.grid(row=5, column=5, padx=20, pady=20,)
app = customtkinterApp()
app.mainloop()