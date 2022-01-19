from cgi import test
import os
import shutil
import sys
from PIL import Image, ImageFont, ImageDraw

class CreatePPM():
  LINE_1_TEXT_SIZE = 12
  LINE_2_TEXT_SIZE = 20

  SAVE_IMG_DIR = "/home/pi/ElectricBoardContentsFolder/"

  def create_ppm(self, show_line=2, show_no=10, show_sec=5, name="contents", text="表示システムエラー",  text_r=255, text_g=255, text_b=255, bg_r=0, bg_g=0, bg_b=0):
    if show_line == 1:
      text_size = self.LINE_1_TEXT_SIZE
      show_line = "Line1"

    elif show_line == 2:
      text_size = self.LINE_2_TEXT_SIZE
      show_line = "Line2"
    else:
      print("表示するLINEは1か2で指定してください")
      sys.exit()

    if show_sec == 0:
      print("表示秒数が0なので表示されません")
      sys.exit()
    else:
      pass

    font = ImageFont.truetype("/usr/share/fonts/truetype/fonts-japanese-gothic.ttf", text_size)
    width, height = font.getsize(text)
    
    img = Image.new("RGB", (width, text_size), (bg_r, bg_g, bg_b))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, (text_r, text_g, text_b), font=font)


    img.save(self.SAVE_IMG_DIR + show_line + "/" + str(show_no) + "_" + str(show_sec) + "_" + str(name) + ".ppm")
    img.save(self.SAVE_IMG_DIR + "png_files" + "/" + show_line + "/" + str(show_no) + "_" + str(show_sec) + "_" + str(name) + ".png")