upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_case = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(letter):

    if letter.isupper():
      new = upper_case.index(letter)
    elif letter.isalpha():
      new = lower_case.index(letter)
    else:
      new = -1
    
    return new

def rotate_character(char, rot):
    position = (alphabet_position(char) + rot) % 26

    if char.isalpha() == False:
      new_char = char
    elif char.isupper():
      new_char = upper_case[position]
    elif char.islower():
      new_char = lower_case[position]
    return new_char
    
def encrypt(text, rot):
  enc_text = ""
  for char in text:
    enc_text += rotate_character(char, rot)
  return enc_text

def main():
  user_mess = input("Type a message: ")
  rotate = int(input("Rotate by: "))
  #print(alphabet_position('t'))
  print(encrypt(user_mess, rotate))


    
if __name__ == "__main__":
  main()