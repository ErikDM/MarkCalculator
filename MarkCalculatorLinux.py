
import tkinter as tk
from tkinter import *
import tkMessageBox

PBLwindow = tk.Tk() # Setting the root window to open by default.

PBLwindow.geometry("250x300+775+425") # Main window size.
PBLwindow.resizable(0, 0) # Making sure the window can't be adjusted.
PBLwindow.title("PBL mark calculator") # Root window title.

def CalculateResults1():

	try:
		PBLtapsINPUT = PBLtaps.get()
		PBLotTotal = PBLot.get()
		PBLcpINPUT = PBLcp.get()

		if float(PBLtapsINPUT) >= 13:
			PBLtapsINPUT = 12

		if float(PBLotTotal) >= 31:
			PBLotTotal = 30

		if float(PBLcpINPUT) >= 101:
			PBLcpINPUT = 100

	except:
		tkMessageBox.showerror("Invalid input", "Please enter a number in every entry field to calculate")
		return

	PBLtapsTotal = float(PBLtapsINPUT) * 1.66666666666667
	PBLcpTotal = float(PBLcpINPUT) / 2

	PBLTotal = (float(PBLtapsTotal) + float(PBLotTotal) + float(PBLcpTotal))

	PBL_A_Label = Label(PBLwindow, text="A")
	PBL_B_Label = Label(PBLwindow, text="B")
	PBL_C_Label = Label(PBLwindow, text="C")
	PBL_D_Label = Label(PBLwindow, text="D")
	PBL_E_Label = Label(PBLwindow, text="E")
	PBL_F_Label = Label(PBLwindow, text="F")

	PBL_A_Label.place_forget()
	PBL_B_Label.place_forget()
	PBL_C_Label.place_forget()
	PBL_D_Label.place_forget()
	PBL_E_Label.place_forget()
	PBL_F_Label.place_forget()

	PBLScoreLabel = Label(PBLwindow, text="Total score:")
	PBLScoreLabel.place(x=78, y=220)
	PBLTotalLabel = Label(PBLwindow, text=int(PBLTotal))
	PBLTotalLabel.place(x=160, y=220)
	PBLMarkLabel = Label(PBLwindow, text="Mark:")
	PBLMarkLabel.place(x=100, y=250)

	if PBLTotal > 90:
		PBL_A_Label.place(x=145, y=250)

	if PBLTotal < 90:
		PBL_B_Label.place(x=145, y=250)

	if PBLTotal < 80:
		PBL_C_Label.place(x=145, y=250)

	if PBLTotal < 60:
		PBL_D_Label.place(x=145, y=250)

	if PBLTotal < 50:
		PBL_E_Label.place(x=145, y=250)

	if PBLTotal < 40:
		PBL_F_Label.place(x=145, y=250)

PBLtaps = StringVar()
PBLot = StringVar()
PBLcp = StringVar()

PBLInsertTap = Entry(PBLwindow, textvariable=PBLtaps, width=10) # Defining the IP address entry field into a variable.
PBLInsertTap.place(x=140, y=50)
PBLInsertTapLabel = Label(PBLwindow, text="TAPs completed:")
PBLInsertTapLabel.place(x=20, y=50)

PBLInsertOt = Entry(PBLwindow, textvariable=PBLot, width=10) # Defining the IP address entry field into a variable.
PBLInsertOt.place(x=140, y=90)
PBLInsertOtLabel = Label(PBLwindow, text="Online test score:")
PBLInsertOtLabel.place(x=14, y=90)

PBLInsertCp = Entry(PBLwindow, textvariable=PBLcp, width=10) # Defining the IP address entry field into a variable.
PBLInsertCp.place(x=140, y=130)
PBLInsertCpLabel = Label(PBLwindow, text="Assessment score:")
PBLInsertCpLabel.place(x=7, y=130)

CalculatePBL = Button(PBLwindow, text="Calculate", width=20, command=CalculateResults1)
CalculatePBL.place(x=35, y=170)

PBLwindow.mainloop()
