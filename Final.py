from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk



LARGEFONT =("Verdana", 175)
class tkinterApp(tk.Tk):
	# __init__ function for class tkinterApp 
	def __init__(self, *args, **kwargs): 
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self) 
		container.pack(side = "top", fill = "both", expand = True) 

		container.grid_rowconfigure(0, weight = 20)
		container.grid_columnconfigure(0, weight = 20)

		# initializing frames to an empty array
		self.frames = {} 

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage, Page1, Page2):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with 
			# for loop
			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# first window frame startpage

class StartPage(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)

		# label of frame Layout 2
		label = ttk.Label(self, text ="Paint Rush", font = LARGEFONT)
		
		# putting the grid in its place by using
		# grid
		label.grid(row = 0, column = 10, padx = 10, pady = 10) 

		button1 = ttk.Button(self, text ="How to Play",
		command = lambda : controller.show_frame(Page1))
	
		# putting the button in its place by
		# using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		## button to show frame 2 with text layout2
		button2 = ttk.Button(self, text ="Settings",
		command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)

        # button to show frame 3 with text
		# layout3
		button3 = ttk.Button(self, text ="Play game",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by
		# using grid
		button3.grid(row = 3, column = 1, padx = 10, pady = 10)
		


# second window frame page1 
class Page1(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="How to Play", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="Back",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place 
		# by using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)
		
		# button to show frame 2 with text
		# layout2
		button2 = ttk.Button(self, text ="Settings",
							command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by 
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        
        # button to show frame 3 with text
		# layout3
		button3 = ttk.Button(self, text ="Play game",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by
		# using grid
		button3.grid(row = 3, column = 1, padx = 10, pady = 10)



# third window frame page2
class Page2(tk.Frame): 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Settings", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="How to Play",
							command = lambda : controller.show_frame(Page1))
	
		# putting the button in its place by 
		# using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 3 with text
		# layout3
		button2 = ttk.Button(self, text ="Back",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)

        # button to show frame 3 with text
		# layout3
		button3 = ttk.Button(self, text ="Play game",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by
		# using grid
		button3.grid(row = 3, column = 1, padx = 10, pady = 10)
		
		frame = tk.Frame(self)
		


# third window frame page2
class Page3(tk.Frame): 
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Play Game", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# button to show frame 3 with text
		# layout3
		button1 = ttk.Button(self, text ="Main menu",
							command = lambda : controller.show_frame(Page1))
	
		# putting the button in its place by 
		# using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 3 with text
		# layout3
		button2 = ttk.Button(self, text ="Settings",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)
		
        # button to show frame 3 with text
		# layout3
		button3 = ttk.Button(self, text ="Play game",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by
		# using grid
		button3.grid(row = 3, column = 1, padx = 10, pady = 10)
		# Centering the buttons
  
app = tkinterApp()
app.mainloop()
