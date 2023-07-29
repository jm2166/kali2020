# 实现摩斯密码翻译器的 Python 程序

'''
VARIABLE KEY
'cipher' -> '存储英文字符串的摩斯翻译形式'
'decipher' -> '存储摩斯字符串的英文翻译形式'
'citext' -> '存储单个字符的摩斯密码'
'i' -> '计算摩斯字符之间的空格'
'message' -> '存储要编码或解码的字符串
'''

# 表示摩斯密码图的字典
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# 根据摩斯密码图对字符串进行加密的函数
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # 查字典并添加对应的摩斯密码
            # 用空格分隔不同字符的摩斯密码
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1个空格表示不同的字符
            # 2表示不同的词
            cipher += ' '

    return cipher

# 将字符串从摩斯解密为英文的函数
def decrypt(message):

    # 在末尾添加额外空间以访问最后一个摩斯密码
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        # 检查空间
        if (letter != ' '):

            # 计数器来跟踪空间
            i = 0

            # 在空格的情况下
            citext += letter

        # 在空间的情况下
        else:
            # 如果 i = 1 表示一个新字符
            i += 1

            # 如果 i = 2 表示一个新词
            if i == 2 :

                 # 添加空格来分隔单词
                decipher += ' '
            else:

                # 使用它们的值访问密钥（加密的反向）
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''

    return decipher

# 硬编码驱动函数来运行程序
def main():
    message = "JUEJIN-HAIYONG"
    result = encrypt(message.upper())
    print (result)

    message = ".--- ..- . .--- .. -. -....- .... .- .. -.-- --- -. --."
    result = decrypt(message)
    print (result)

    message = "I LOVE YOU"
    result = encrypt(message.upper())
    print (result)

    message = "..  .-.. --- ...- .  -.-- --- ..-"
    result = decrypt(message)
    print (result)

# 执行主函数
if __name__ == '__main__':
    main()

