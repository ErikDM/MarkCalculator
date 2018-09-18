# MarkCalculator - Created for Noroff Education

This program is created to calculate your mark during the PBL course at Noroff Education. The calculator is designed to calculate your total mark based on your score on TAPs, Online Test and Assessment week. Only 12/15 TAPs are counted as points, since 4/5 are mandatory.

The calculator has been implemented with number adjustments, which means that if you type in 15 TAPs done, the calculator will only give you points for 12 TAPs. Entering for example 150 points on your assessment week will be automatically adjusted down to 100. The same goes for TAPs and Online Test. All limits exceeded will automatically adjust your score to "maximum".

The .exe file was created with Pyinstaller, and the setup wizard was created with "Inno Setup". For more information, see: http://www.jrsoftware.org/isinfo.php

-----------------------------------------------------------------------

# Windows
Use the MarkCalculator_Setup.exe file to install it on your Windows operating system. This will allow the user to choose installation path and create a desktop icon as a shortcut.
You can also execute the file MarkCalculatorWindows.exe directly without any installation if necessary.

# Linux
To run the program, use the following command:
python MarkCalculatorLinux.py

------------------------------------------------------------------------

Feel free to contact me about new features, adjustments, bugs and so on.

Incoming features:
* Allowing the user to click on which course to calculate their mark for (PBL, IIS, OFS and so on), since some courses have 15 TAPs, while others have 20 or more.
* Allowing the user to press "ENTER" after putting in numbers, instead of clicking the "Calculate" button.
* Removing a bug caused by simultaneously clicking the "Calculate" button. A ")" appears in the end of the score.
