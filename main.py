# TextToImage 
# DipokalHHJ

from core import T2i

def main():
  CRH = T2i()
  pid_org = CRH.generatePrimaryId()
  pid_hex = CRH.createHex(pid_org)

  CRH.createEncryptionImage(pid_hex)

  hex_color = CRH.getHexFromImage('result')
  # hex_data = CRH.createRgbtoHex(rgb_color)

  print(pid_org)
  print(hex_color)
  # print(hex_data)
     
if __name__ == "__main__":
  main()
