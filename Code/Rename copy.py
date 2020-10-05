#Nhan file rename script
import os

file_location = "pushups"

number_file_jpg = 0
number_file_png = 0

for file in os.listdir("/Spotter/" + file_location):
    x = file.split(".")
    file_path = "/Spotter/" + file_location + "/" + str(file)
    if x[len(x)-1] == "jpg":
        number_file_jpg = number_file_jpg + 1
        if number_file_jpg <= 9:
            number_file_jpg_1 = "000" + str(number_file_jpg)
        elif number_file_jpg <= 99:
            number_file_jpg_1 = "00" + str(number_file_jpg)
        elif number_file_jpg <= 999:
            number_file_jpg_1 = "0" + str(number_file_jpg)
        elif number_file_jpg <= 9999:
            number_file_jpg_1 = str(number_file_jpg)
        new_file_name = "/Spotter/" + file_location + "/" + str(number_file_jpg_1) + ".jpg"
        os.rename(file_path, new_file_name)
    if x[len(x)-1] == "png":
        number_file_png = number_file_png + 1
        if number_file_png <= 9:
            number_file_png_1 = "000" + str(number_file_png)
        elif number_file_png <= 99:
            number_file_png_1 = "00" + str(number_file_png)
        elif number_file_png <= 999:
            number_file_png_1 = "0" + str(number_file_png)
        elif number_file_png <= 9999:
            number_file_png_1 = str(number_file_png)
        new_file_name = "/Spotter/" + file_location + "/" + str(number_file_png_1) + ".png"
        os.rename(file_path, new_file_name)
