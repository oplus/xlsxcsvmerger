import pandas as pd
import os


#Select folder that include xlsx files
main = Tk()
main.withdraw()
folder_selected = filedialog.askdirectory()
root = filedialog.askdirectory()
file_list = []

#This list all xlsx files in the folder and subfolders
for path, subdirs, files in os.walk(root):
    for name in files:
        if 'xlsx' in name: 
            file_list.append(os.path.join(path, name))
			




#Add more columns with exact name to list below to include more entries if required
cols = ['Lead Generated Month', 'Lead Generated Date', 'Source', 'First Name', 'Last Name', 'Phone', 'Email',
        'Listing MLS Source', 'Listing Address', 'Listing City', 'Listing State', 'Listing Zip',
        'Listing Status', 'Listing Price', 'Message', 'Proprty Type']

frames = []
for xlsx_file in file_list:
	frames.append(pd.read_excel(xlsx_file,usecols=lambda x: x in cols, skiprows=2))

frames[1:] = [df[1:] for df in frames[1:]]

combined = pd.concat(frames)

#Change 'filename' to change output file name
combined.to_excel('filename.xlsx')
