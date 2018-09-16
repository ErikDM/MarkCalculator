
import tkinter as tk
from tkinter import *
from tkinter import messagebox

PBLwindow = tk.Tk() # Setting the root window to open by default.

PBLwindow.geometry("250x300+825+425") # Main window size.
PBLwindow.resizable(0, 0) # Making sure the window can't be adjusted.
PBLwindow.title("PBL calculator") # Root window title.

def CalculateResults1():

	# Trying to read the user input. If not, an error box will be displayed.
	try:
		PBLtapsINPUT = PBLtaps.get()
		PBLotTotal = PBLot.get()
		PBLcpINPUT = PBLcp.get()

	# Only a total of 12 TAPs will count as points, since 4 TAPs every week counts on your total mark.
	# The operators below will change any TAP value over 12 automatic back to 12. Example: 15 TAPs done = 12 TAPs score.
	# The same operations goes for Online Test and Assessment week. If the user tries to enter a larger value, it will automatically be adjusted down to the maximum value.

		if float(PBLtapsINPUT) >= 13:
			PBLtapsINPUT = 12

		if float(PBLotTotal) >= 31:
			PBLotTotal = 30

		if float(PBLcpINPUT) >= 101:
			PBLcpINPUT = 100

	# Displays an error popup if invalid input was sent to the calculator.
	except:
		messagebox.showerror("Invalid input", "Please enter a number in every entry field to calculate")
		return

	# Calculates the different values. Each TAP is 1.66666666666667 points. Assessment week is their score / 2.
	PBLtapsTotal = float(PBLtapsINPUT) * 1.66666666666667
	PBLcpTotal = float(PBLcpINPUT) / 2

	# Adding the score together
	PBLTotal = (float(PBLtapsTotal) + float(PBLotTotal) + float(PBLcpTotal))
	PBLTotalRounded = round(PBLTotal, 1)

	# Mark labels
	PBL_A_Label = Label(PBLwindow, text="A")
	PBL_B_Label = Label(PBLwindow, text="B")
	PBL_C_Label = Label(PBLwindow, text="C")
	PBL_D_Label = Label(PBLwindow, text="D")
	PBL_E_Label = Label(PBLwindow, text="E")
	PBL_F_Label = Label(PBLwindow, text="F")

	# Removing all mark labels before placing a new one. This is used in case the user adjusts his/her points frequently.
	PBL_A_Label.place_forget()
	PBL_B_Label.place_forget()
	PBL_C_Label.place_forget()
	PBL_D_Label.place_forget()
	PBL_E_Label.place_forget()
	PBL_F_Label.place_forget()

	# Placing out the Total Score label, Mark label etc.
	PBLScoreLabel = Label(PBLwindow, text="Total score:")
	PBLScoreLabel.place(x=78, y=220)
	PBLTotalLabel = Label(PBLwindow, text=(PBLTotalRounded))
	PBLTotalLabel.place(x=147, y=220)
	PBLMarkLabel = Label(PBLwindow, text="Mark:")
	PBLMarkLabel.place(x=100, y=250)

	# Calculating which mark to place out, depending on the total score. All above 90 = A, 89-80 = B and so on.
	if PBLTotal > 90:
		PBL_A_Label.place(x=138, y=250)

	if PBLTotal < 90:
		PBL_B_Label.place(x=138, y=250)

	if PBLTotal < 80:
		PBL_C_Label.place(x=138, y=250)

	if PBLTotal < 60:
		PBL_D_Label.place(x=138, y=250)

	if PBLTotal < 50:
		PBL_E_Label.place(x=138, y=250)

	if PBLTotal < 40:
		PBL_F_Label.place(x=138, y=250)

# Making sure the user input is stored as a string variable.
PBLtaps = StringVar()
PBLot = StringVar()
PBLcp = StringVar()

# Placing out the entry field
PBLInsertTap = Entry(PBLwindow, textvariable=PBLtaps, width=10)
PBLInsertTap.place(x=145, y=50)
PBLInsertTapLabel = Label(PBLwindow, text="TAPs completed:")
PBLInsertTapLabel.place(x=35, y=48)

# Placing out the entry field
PBLInsertOt = Entry(PBLwindow, textvariable=PBLot, width=10)
PBLInsertOt.place(x=145, y=90)
PBLInsertOtLabel = Label(PBLwindow, text="Online test score:")
PBLInsertOtLabel.place(x=34, y=88)

# Placing out the entry field
PBLInsertCp = Entry(PBLwindow, textvariable=PBLcp, width=10)
PBLInsertCp.place(x=145, y=130)
PBLInsertCpLabel = Label(PBLwindow, text="Assessment score:")
PBLInsertCpLabel.place(x=30, y=128)

# Placing out the "Calculate" button
CalculatePBL = Button(PBLwindow, text="Calculate", width=20, command=CalculateResults1)
CalculatePBL.place(x=50, y=170)

PBLwindow.mainloop()
