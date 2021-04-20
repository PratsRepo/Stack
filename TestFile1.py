import matplotlib.image as mpimg
import classes
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import numpy as np
from scipy.interpolate import interp1d
from matplotlib import pyplot as plt
imp_class = classes.import_files()
# data_cell_voltage = imp_class.engauge_file()
file1 = 'C:/Users/Adhwaryu/PycharmProjects/pythonProject/pythonProject1/Task3/Polarization_Curves.xlsx'
data_cell_voltage = pd.read_excel(file1, sheet_name=0, header=1,
                                 index_col=0, keep_default_na=True)
df_data_cell_voltage = pd.DataFrame(data_cell_voltage, columns=['X', 'Y20,' 'Y30,' 'Y40,' 'Y50,' 'Y60,' 'Y70'])
if df_data_cell_voltage.empty:
    print("DataFrame is empty!")
else:
    print(df_data_cell_voltage)
# interpolate_X = 55
# Y20_interp = interp1d(X, Y20)
# print("Value of Cell Voltage at X =  is".format(interpolate_X), Y20_interp(interpolate_X))
# data_power = imp_class.engauge_file()
# print(data_power)
