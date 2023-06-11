# importing os module
import os

### Directory ###
# change var "directory" and "num" that you want to name.
directory = "A-"
num = 0

# if you want to creat file more than 20 or less than 20 change range number "(20)".
for dir_list in range(20):
 num += 1
 output_dir = directory + str(num)
 os.mkdir(output_dir)

print("####### Done #######")
