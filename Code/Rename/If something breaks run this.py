#Was too lazy to write the renaming scheme to 0001 0002
import os

number_file_jpg = 0
number_file_png = 0
for file in os.listdir("/Spotter/.Images/New Folder (3)"):
    file_path = "/Spotter/.Images/New Folder (3)" + file
    file_name_new = "/Spotter/.Images/New Folder (3)/retry6233338834" + file 
    os.rename(file_path, file_name_new)
