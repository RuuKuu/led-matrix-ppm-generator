import sys
from ppm import create_ppm

try:
  file_name = input("Enter file name: ")
  text = input("Enter text you want to display: ")
  text_r = int(input("Enter the red value of the text: "))
  text_g = int(input("Enter the green value of the text: "))
  text_b = int(input("Enter the blue value of the text: "))
  bg_r = int(input("Enter the red value of the background: "))
  bg_g = int(input("Enter the green value of the background: "))
  bg_b = int(input("Enter the blue value of the background: "))
except KeyboardInterrupt:
  print("\n")
  sys.exit()
except:
  print("Failed. You entered a value that is invalid. RGB must be a number.")
  sys.exit()

color_value = [text_r, text_g, text_b, bg_r, bg_g, bg_b]

if all([0 <= x <= 255 for x in color_value]):
  create_ppm(file_name, text, text_r, text_g, text_b, bg_r, bg_g, bg_b)
  print("succeeded. The ppm file has been generated.")
else:
  print("Failed. You entered a value that is invalid. RGB must be between 0 and 255.")