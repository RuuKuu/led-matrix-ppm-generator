import sys
from create_ppm import CreatePPM

class ManualCreatePPM:
  def manual_create_ppm(self):
    try:
      name = input("ファイル名を入力してください: ")
      text = input("表示する文章を入力してください: ")
      show_line = int(input("表示行を1か2で選択してください: "))
      show_no = int(input("表示番目を入力してください: "))
      show_sec = int(input("表示秒数を入力してください: "))
      text_r = int(input("文字色の「赤」の値を入力してください: "))
      text_g = int(input("文字色の「緑」の値を入力してください: "))
      text_b = int(input("文字色の「青」の値を入力してください: "))
      bg_r = int(input("背景色の「赤」の値を入力してください: "))
      bg_g = int(input("背景色の「緑」の値を入力してください: "))
      bg_b = int(input("背景色の「青」の値を入力してください: "))
    except KeyboardInterrupt:
      print("\n")
      sys.exit()
    except:
      print("エラーです。適切に値を入力してください。")
      sys.exit()

    color_value = [text_r, text_g, text_b, bg_r, bg_g, bg_b]

    if show_line not in [1, 2]:
      print("表示行は1か2で選択してください")
      sys.exit()
    else:
      pass

    if all([0 <= x <= 255 for x in color_value]):
      ob = CreatePPM()
      ob.create_ppm(show_line, show_no, show_sec, name, text, text_r, text_g, text_b, bg_r, bg_g, bg_b)
      print("表示画像の生成が完了しました。フォルダを確認してください。")

    else:
      print("エラーです。色の値は0~255の間で入力してください。")

if __name__ == "__main__":
  ob_main = ManualCreatePPM()
  ob_main.manual_create_ppm()