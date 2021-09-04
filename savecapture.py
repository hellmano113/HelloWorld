import time
from PIL import ImageGrab
from datetime import date
from docx import Document,shared

list1 = str(date.today()).split('-')
documentname = list1[0]+list1[1]+list1[2]

path = "C:\\Users\\HaoLu\\Desktop\\"
filepath = path + documentname +'. docx'
#print(date.today())
doc = Document()

def capture_save_img():
    time.sleep(15)
    img = ImageGrab.grab()

    
    img.save('1.jpeg')
    doc.add_picture('1.jpeg',width=shared.Inches(10))

    doc.save(filepath)


def main():
    capture_save_img()

if __name__ == '__main__':
    main()



