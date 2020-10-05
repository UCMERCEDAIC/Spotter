#Was too lazy to write the renaming scheme to 0001 0002
import os

number_file_jpg = 0
number_file_png = 0
for file in os.listdir("/Spotter/Nhan"):
    file_path = "/Spotter/Nhan/" + file
    file_name_new = "/Spotter/Nhan/retry" + file 
    os.rename(file_path, file_name_new)
