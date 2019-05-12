import pandas as pd
import os
from tkinter import filedialog
from tkinter import *


#Select folder that include csv files
main = Tk()
main.withdraw()
folder_selected = filedialog.askdirectory()
root = filedialog.askdirectory()
print(root)


file_list = []

#This list all csv files in the folder and subfolders
for path, subdirs, files in os.walk(root):
    for name in files:
        if 'csv' in name:  
            file_list.append(os.path.join(path, name))
			




#Add more columns with exact name to list below to include more entries if required
cols = ['Date', 'Name', 'Email', 'Phone', 'Source', 'Sub Source', 'Listing Address', 'City', 'Zip'
        , 'Message', 'Historical Price', 'Date/Time', 'First Name', 'Last Name', 'Address']

frames = []
for csv_file in file_list:
    frames.append(pd.read_csv(csv_file,usecols=lambda x: x in cols, error_bad_lines=False))


frames[1:] = [df[1:] for df in frames[1:]]

combined = pd.concat(frames)

#Change 'filename' to change output file name
combined.to_csv('filename.csv')
