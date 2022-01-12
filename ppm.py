import os
import shutil
from PIL import Image, ImageFont, ImageDraw

def create_ppm(file_name, text="表示システムエラー", text_size = 16, text_r=255, text_g=255, text_b=255, bg_r=0, bg_g=0, bg_b=0):
  font = ImageFont.truetype("/usr/share/fonts/truetype/fonts-japanese-gothic.ttf", text_size)
  width, height = font.getsize(text)
  
  img = Image.new("RGB", (width, text_size), (bg_r, bg_g, bg_b))
  draw = ImageDraw.Draw(img)
  draw.text((0, 0), text, (text_r, text_g, text_b), font=font)

  IMAGE_DIR_PASS = "/home/pi/ElectricBoardContentsFolder/"

  img.save(IMAGE_DIR_PASS + str(file_name) + ".ppm")
  img.save(IMAGE_DIR_PASS + "png_files/" + str(file_name) + ".png")

def merge_ppm():
  shutil.copy("./ppm_files/0.ppm", "./ppm_files/merged.ppm")
  shutil.copy("./png_files/0.png", "./png_files/merged.png")

  DIR = "./ppm_files/"
  number_of_files = sum(os.path.isfile(os.path.join(DIR, name)) for name in os.listdir(DIR))


  for i in range(1, number_of_files - 1):
    img1 = Image.open("./ppm_files/" + "merged" + ".ppm")
    img2 = Image.open("./ppm_files/" + str(i) + ".ppm")

    if i == (number_of_files - 2):
      img = Image.new("RGB", (img1.width + 100 + img2.width + 100, img1.height))
      img.paste(img1, (0, 0))
      img.paste(img2 , (100 + img1.width, 0))
    else:  
      img = Image.new("RGB", (img1.width + 100 + img2.width, img1.height))
      img.paste(img1, (0, 0))
      img.paste(img2 , (100 + img1.width, 0))

    img.save("./ppm_files/merged.ppm")
    img.save("./png_files/merged.png")