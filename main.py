import binascii
import math
from PIL import Image, ImageDraw
import string 
import random

def generatePrimaryId():
  length = 28 # 10자리
  stringPool = string.ascii_lowercase+'1234567890' # 소문자
  result = "" # 결과 값
  for i in range(length) :
      result += random.choice(stringPool) # 랜덤한 문자열 하나 선택
  return result


def createHex(text):
  textEncode = text.encode("utf-8").hex()
  tempText = []

  for i in range(len(textEncode)+6):
    if i % 6 == 0:
      tempText.append(textEncode[int(i)-6:int(i)])
  
  return tempText



def createEncryptionImage(hexlist):
  # print(hexlist)
  w = 240 # 60w 60h 10c
  h = 240
  c = 40 # 블록 크기
  k = 0 # 라인 넘버 (첫번째 라인은 0번)
  img = Image.new('RGB', (w, h), color = 'black')
  img1 = ImageDraw.Draw(img)
  # shape = [(10, 10), (w - 60, h - 60)]
  # shape1 = [(20, 10), (w - 50, h - 60)]

  for i in range(len(hexlist)):
    if (hexlist[i] == ""):
      print('N1')
    elif (len(hexlist[i]) != 6):
      print('N2')
    elif (i % (h/c) == 0):
      print(hexlist[i], k, [((w), c*(k+1)), (w+(i%(w/c)-1)*c), (k*c)])
      img1.rectangle([((w), c*(k+1)), (w+(i%(w/c)-1)*c), (k*c)], fill ="#"+hexlist[i])
      k += 1
    elif (hexlist[i] != ""):
      print(hexlist[i], k, [(c*(i%(h/c)), c*(k+1)), ((i%(w/c)-1)*c), (k*c)])
      img1.rectangle([(c*(i%(h/c)), c*(k+1)), ((i%(w/c)-1)*c), (k*c)], fill ="#"+hexlist[i])


  img.show()
  img.save('pil_red.png')


pid = generatePrimaryId()

print(pid)
createEncryptionImage(createHex(pid))