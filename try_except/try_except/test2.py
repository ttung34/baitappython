import pytube
import os

class vid:
   def __init__(self, url):
      self.url = url

   def is_valid_url(self):
      try:
         pytube.Youtube(self.url)
         return True
      except pytube.exceptions.RegexMatchError:
         return False
      
   def download_video(self, video):
      while True:
         format_dict ={}
         os.system("cls")
         total = 0
         for i, stream in enumerate(video.streams.filter().oder_by('resolution')):
            format_dict[i] = stream
            print(f"{i}: {stream.resolution} ({stream.mine_type})")
            toatl += 1
         
         try:
            format_index = int(input("Chon so thu tu cua chat luong dinh dang muon tai ve: "))
         except:
            continue

         if format_index < 0 or format_index >total:
            continue
         stream = format_dict[format_index]
         break

      stream.download()
      print("Tai audio thanh cong")

def InvalidChoice():
   os.system("cls")
   os.system("color 4")
   print("="*30)
   print("      Invalid Choice     ")
   print("="*30)
   os.system("pause")
   os.system("color 7")

def main():
   while True:
      os.system("cls")
      url = input("Nhap URL cua video tren Youtube: ")
      os.system("cls")
      if not vid(url).is_valid_url():
         print("URL khong hop le, vui long nhap lai.")
         os.system("pause")
         continue
      video = pytube.Youtube(url)
      while True:
         os.system("cls")
         print("="*30)
         print("[1] Audio")
         print("[2] Video")
         print("[3] Other URL")
         print("="*30)
         download_type = input("Your Choice: ")
         if download_type == "1":
            vid(url).download_audio(video=video)
         elif download_type == "2":
            vid(url).download_video(video=video)
         elif download_type == "3":
            break
         else:
            InvalidChoice()
            continue

if __name__ == "__main__":
   main()   