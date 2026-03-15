#凯撒密码加密过程
def caesar_encryption():
    Text = input("请输入未加密文本：")
    n = int(input("请输入偏移位数："))
    for index in Text:
        if "a" <= index <= "z":
            print(chr(ord("a") + (ord(index) - ord("a") + n) % 26), end='')
        elif "A" <= index <= "Z":
            print(chr(ord("A") + (ord(index) - ord("A") + n) % 26), end='')
        else:
            print(index, end='')

#凯撒密码解密过程
def caesar_decryption():
    Text = input("请输入已加密文本：")
    n = int(input("请输入偏移位数："))
    for index in Text:
        if "a" <= index <= "z":
            print(chr(ord("a") + (ord(index) - ord("a") - n) % 26), end='')
        elif "A" <= index <= "Z":
            print(chr(ord("A") + (ord(index) - ord("A") - n) % 26), end='')
        else:
            print(index, end='')

if __name__ == '__main__':
    x = input("请输入加密或解密：")
    if x == "加密":
        caesar_encryption()
    elif x == "解密":
        caesar_decryption()

