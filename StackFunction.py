import pandas as pd
import numpy as np
from PIL import Image


# creating the main class stack
class Stack:
    def __init__(self, file1, file2):
        self.file1 = ''
        self.file2 = ''
        self.data_cell_voltage = pd.read_csv(file1)
        self.data_cell_power = pd.read_csv(file2)
        # define a function to calculate Cell Voltage
        # def cell_voltage(self, x, temp):
        # interpolate cell voltage for current density

    def cell_voltage(self):
        x = float(input("Enter Current Density to calculate cell voltage: "))
        cv = self.data_cell_voltage['x'].values.astype(float)
        if x > min(cv) and x < max(cv):
            x_right = np.searchsorted(cv, x, side='right')
            x_left = x_right - 1
            # print(x_left, x_right)  #printing index
            print(cv[x_left], cv[x_right])
            left_row = self.data_cell_voltage.loc[x_left]
            right_row = self.data_cell_voltage.loc[x_right]
            # left_row, right_row
            y = left_row + ((right_row - left_row) / (cv[x_right] - cv[x_left])) * (x - cv[x_left])
            y[0] = x
            print("The Cell Voltage for Current Density " + str(x) + " is: " + "\n" + str(y))
            # interpolate cell voltage for temperature
            temp = float(input("Enter Temperature: "))
            temps = self.data_cell_voltage.columns.values[1:].astype(float)
            temp_right = np.searchsorted(temps, temp, side='right')
            temp_left = temp_right - 1
            # temp_left, temp_right
            temp_left_row = temps[temp_left]
            temp_right_row = temps[temp_right]
            # temp_left_row, temp_right_row
            y1 = y[temp_left + 1]
            y2 = y[temp_right + 1]
            temp_y = y1 + (temp - temp_left_row) * ((y2 - y1) / (temp_right_row - temp_left_row))
            print(temp_y)
            print("The Cell Voltage for Current Density " + str(x) + " and temperature " + str(temp) + " is: " + str(temp_y))

    # Interpolation function to calculate Power
    def cell_power(self):
        x = float(input("\n Enter Current Density to calculate power: "))
        cp = self.data_cell_power['x'].values.astype(float)
        if x > min(cp) and x < max(cp):
            x_right = np.searchsorted(cp, x, side='right')
            x_left = x_right - 1
            # print(x_left, x_right)  #printing index
            print(cp[x_left], cp[x_right])
            left_row = self.data_cell_power.loc[x_left]
            right_row = self.data_cell_power.loc[x_right]
            # left_row, right_row
            py = left_row + ((right_row - left_row) / (cp[x_right] - cp[x_left])) * (x - cp[x_left])
            py[0] = x
            print("The Cell Power for Current Density " + str(x) + " is: " + "\n" + str(py))
            # interpolate cell power for temperature
            temp = float(input("Enter Temperature: "))
            temps = self.data_cell_power.columns.values[1:].astype(float)
            temp_right = np.searchsorted(temps, temp, side='right')
            temp_left = temp_right - 1
            # temp_left, temp_right
            temp_left_row = temps[temp_left]
            temp_right_row = temps[temp_right]
            # temp_left_row, temp_right_row
            y1 = py[temp_left + 1]
            y2 = py[temp_right + 1]
            temp_py = y1 + (temp - temp_left_row) * ((y2 - y1) / (temp_right_row - temp_left_row))
            print(temp_py)
            print("The Power for Current Density " + str(x) + " and temperature " + str(temp) + " is: " + str(temp_py))


class Allagash (Stack):
    def __init__(self):
        file1 = 'Allagash_Polarisationskurven.csv'
        file2 = 'Allagash_Energiebedarf.csv'
        #file1 = Image.open('Polarisationskurven_Rev_00A16.PNG')
        #Image._show(file1)
        super().__init__(file1, file2)
        # super().cell_voltage()
        # super().cell_power()


print("This is Allagash Class")
A1 = Allagash()
A1.cell_voltage()
with open('Allagash_CellVoltage_Output.txt', 'w') as f:
    print(A1.cell_voltage, file=f)
A1.cell_power()
with open('Allagash_CellPower_Output.txt', 'w') as f:
    print(A1.cell_voltage, file=f)


class Merrimack (Stack):
    def __init__(self):
        file1 = 'Merrimack_Rev4_1_CV.csv'
        file2 = 'Merrimack_Spez_energie_bedarf.csv'
        # file1 = Image.open('.PNG')
        # Image._show(file1)
        super().__init__(file1, file2)


print("\n This is Merrimack Class")
M1 = Merrimack()
M1.cell_voltage()
with open('Merrimack_CellVoltage_Output.txt', 'w') as f:
    print(M1.cell_voltage, file=f)
M1.cell_power()
with open('Merrimack_CellPower_Output.txt', 'w') as f:
    print(M1.cell_voltage, file=f)
