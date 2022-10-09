from time import sleep
import random
import os
def calcProduct(product_keylist,defined_keylist,setprice):
    count = 0
    setprice = int(setprice)
    for text in product_keylist:
        putCount = int(product_keylist[text])
        price = int(defined_keylist[text])
        count += putCount * price
    return int(setprice- count)
        
def showverticalList(getlist,dictvalue = False):
    if isinstance(getlist,dict):
        for text in getlist:
            if dictvalue:
                print(text)
            else:
                print(text,'{}円'.format(getlist[text]))
    if isinstance(getlist,list):
        for count in range(len(getlist)):
            print(getlist[count])
#文字が数字のみなのか判定
def is_str(value):
    return not value.isdigit()
asciiTitle = ['                                                                                                            ######'
,'              ########                                                        ######                                ####                                                ####'
,'                  ######                                                        ####                                ####                                                ######'
,'                                                        ####            ######  ####                                ####                                                ######'
,'                      ####                              ####            ########                                    ########                                            ####'
,'            ################                            ####  ##        ######                                  ############                                          ############'
,'            ##############                              ######        ##############                                ######                                          ##################'
,'                ####                                ########        ##########      ####                            ####                                      ############        ######'
,'                ##                            ############    ##  ####    ####  ########                          ######  ##                                    ########          ######'
,'                ####                            ##    ####    ####        ########                                  ############                                  ####            ######'
,'              ############                            ####    ##        ########  ##                              ############                                  ######            ####'
,'          ##################                            ########      ########    ##                        ############                                      ######              ####'
,'        ##################                                ######          ##    ####                            ########                                    ######              ######'
,'        ##      ########                                ########          ##  ######                            ####    ##                                ######                ######'
,'                ######                              ######    ####        ########                            ####      ####                            ####                  ######'
,'            ##########                                          ##        ######                              ##          ####                        ##                    ########'
,'          ########################                                        ##                                ####            ####                                  ##      ########'
,'  ####################################                                    ##                            ####                ########                                ############'
,'##########                  ##########                                    ##                        ####                      ##########                            ############'
,'####                                                                      ##                                                      ########                            ######'
,'                                                                                                                                                                        ##'                                                                                                                                
]
for text in asciiTitle:
    print(text)

#初期化
product_name = ('キャベツ１玉','人参1個','トマト1個','カレー粉','冷凍うどん5袋','冷凍うどん1袋','牛肉200g','ラム肉100g','たこ焼き粉')
product_price_dict = {}
input_product_price_dict={}
limitTime = ""
limitPrice = ""

print('計算力が問われるお買い物。すんげえ中途半端な商品の金額を時間内に所持金ぎりぎりで払えるように時間内に計算せよ！')
while is_str(limitPrice):
    limitPrice = input('君の所持金は？を0~の数字で入力:')
while is_str(limitTime):
    limitTime = input('制限時間（秒）を0~の数字で入力:')


print("それでは{}秒の間、所持金ぎりぎりの金額になるように計算してください。".format(limitTime))
for a in range(4):
    print(4-a)
    sleep(1)
os.system('cls')
print('スタート!!')


for create_price in product_name:
    price = random.randrange(100,648)
    product_price_dict[create_price] = price
showverticalList(product_price_dict)
limitTime = int(limitTime)
sleep(limitTime)
os.system('cls')
print('ストーーーープ!!')
showverticalList(product_price_dict,True)
print()

for productname in product_price_dict:
    #初期化
    input_price = ""
    while is_str(input_price):
        input_price = input('{}は何コ買う？0～の数字で入力:'.format(productname))
    input_product_price_dict[productname] = int(input_price)

summary = calcProduct(input_product_price_dict,product_price_dict,limitPrice)
print('あなたの残りの所持金は{}円です。'.format(summary))

if(summary > 0):
    print('まずはマイナスにならなかっただけすごいね！')
else:
    print('計算ミスしてるやんｗ。おつかれ')

