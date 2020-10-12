#Nhan file rename script
import os

#Change it to the folder with in spotter
file_location = "Images"

number_file_jpg = 0
number_file_png = 0

for file in os.listdir(file_location):
    x = file.split(".")
    file_path =file_location + "/" + str(file)
    if x[len(x)-1] == "jpg":
        number_file_jpg = number_file_jpg + 1
        if number_file_jpg <= 9:
            number_file_jpg_1 = "Correct_000" + str(number_file_jpg)
        elif number_file_jpg <= 99:
            number_file_jpg_1 = "Correct_00" + str(number_file_jpg)
        elif number_file_jpg <= 999:
            number_file_jpg_1 = "Correct_0" + str(number_file_jpg)
        elif number_file_jpg <= 9999:
            number_file_jpg_1 = str(number_file_jpg)
        new_file_name = file_location + "/" + str(number_file_jpg_1) + ".jpg"
        os.rename(file_path, new_file_name)
    if x[len(x)-1] == "png":
        number_file_png = number_file_png + 1
        if number_file_png <= 9:
            number_file_png_1 = "Correct_000" + str(number_file_png)
        elif number_file_png <= 99:
            number_file_png_1 = "Correct_00" + str(number_file_png)
        elif number_file_png <= 999:
            number_file_png_1 = "Correct_0" + str(number_file_png)
        elif number_file_png <= 9999:
            number_file_png_1 = str(number_file_png)
        new_file_name = file_location + "/" + str(number_file_png_1) + ".png"
        os.rename(file_path, new_file_name)
