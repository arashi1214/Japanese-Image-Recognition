import pytesseract
from PIL import Image
# import module
from pdf2image import convert_from_path
 
 # ===== 轉 pdf to png =====#
# Store Pdf with convert_from_path function
def pdf_to_png(path):
  images = convert_from_path(path, poppler_path='C:\\Program Files\\poppler-0.68.0\\bin')
  page_list = []
  for i in range(len(images)):
        # Save pages as images in the pdf
      images[i].save('page'+ str(i) +'.png', 'PNG')
      page_list.append('page'+ str(i) +'.png')
  return page_list

# ===== 圖像辨識 =====#
def image_to_txt(path_list, file_name):
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  file = open(file_name, "a", encoding="utf-8")

  for page in path_list:
      img = Image.open(page)
      text = pytesseract.image_to_string(img, lang='jpn_vert', config='--psm 3 -c preserve_interword_spaces=1')
      file.write(text)

# page_list = pdf_to_png('messageImage_1679045745113.pdf')
page_list = ['messageImage_1679045745113.jpg']
image_to_txt(page_list, "output2.txt")