#Nhan file rename script
import os

file_location = input("Type the name of the folder")

number_file_jpg = 0
number_file_png = 0

for file in os.listdir("/Spotter/" + file_location):
    x = file.split(".")
    file_path = "/Spotter/" + file_location + "/" + str(file)
    if x[len(x)-1] == "jpg":
        number_file_jpg = number_file_jpg + 1
        new_file_name = "/Spotter/" + file_location + "/" + str(number_file_jpg) + ".jpg"
        os.rename(file_path, new_file_name)
    if x[len(x)-1] == "png":
        number_file_png = number_file_png + 1
        new_file_name = "/Spotter/" + file_location + "/" + str(number_file_png) + ".png"
        os.rename(file_path, new_file_name)
