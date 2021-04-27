import pandas as pd
import numpy as np
from PIL import Image
from importlib.metadata import metadata
# creating the main class stack


class Stack:
    def __init__(self, cell_voltage, cell_power):
        self.cell_voltage = cell_voltage
        self.cell_power = cell_power
        self.filename= ''
        file1 = 'test.csv'
        file2 = 'test2.csv'
        data_cell_voltage = pd.read_csv(file1)
        data_cell_power = pd.read_csv(file2)
        # define a function to calculate Cell Voltage
        # def cell_voltage(self, x, temp):
        # interpolate cell voltage for current density

        def cell_voltage(self):
            x = float(input("Enter Current Density: "))
            cv = data_cell_voltage['x'].values.astype(float)
            if x > min(cv) and x < max(cv):
                x_right = np.searchsorted(cv, x, side='right')
                x_left = x_right - 1
                # print(x_left, x_right)  #printing index
                print(cv[x_left], cv[x_right])
                left_row = data_cell_voltage.loc[x_left]
                right_row = data_cell_voltage.loc[x_right]
                # left_row, right_row
                y = left_row + ((right_row - left_row) / (cv[x_right] - cv[x_left])) * (x - cv[x_left])
                y[0] = x
                print("The Cell Voltage for Current Density " + str(x) + " is: " + "\n" + str(y))
                # interpolate cell voltage for temperature
                temp = float(input("Enter Temperature: "))
                temps = data_cell_voltage.columns.values[1:].astype(float)
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
                return cell_voltage(self)

            # Interpolation function to calculate Power
        def cell_power(self):
            x = float(input("Enter Current Density: "))
            cp = data_cell_power['x'].values.astype(float)
            if x > min(cp) and x < max(cp):
                x_right = np.searchsorted(cp, x, side='right')
                x_left = x_right - 1
                # print(x_left, x_right)  #printing index
                print(cp[x_left], cp[x_right])
                left_row = data_cell_power.loc[x_left]
                right_row = data_cell_power.loc[x_right]
                # left_row, right_row
                py = left_row + ((right_row - left_row) / (cp[x_right] - cp[x_left])) * (x - cp[x_left])
                py[0] = x
                print("The Cell Power for Current Density " + str(x) + " is: " + "\n" + str(py))
                # interpolate cell power for temperature
                temp = float(input("Enter Temperature: "))
                temps = data_cell_power.columns.values[1:].astype(float)
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
                return cell_power(self)


# create the child class Allagash
class Allagash (Stack):
    CV_Graph = Image.open( 'Polarisationskurven_Rev_00A16.PNG' )
    Image._show(CV_Graph)
    #saving the image specification
    A = metadata['Allagash'].keys()
    metadata = {'Allagash': {
            1: {
                    cathod: 30,
                    anode: 100,
                    graph_path: "",
                    csv_path: "",
                },
    super().cell_voltage():
    super().cell_power()
# calling the function cell voltage and cell power and storing the graph data


# create the child class Merrimack
class Merrimack (Stack):
    super().cell_voltage()
    super().cell_power()
# calling the function cell voltage and cell power and storing the graph data
