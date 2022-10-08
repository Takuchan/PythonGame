import random

def judge(old,defineage):
    old,defineage = int(old),int(defineage)
    #入力値がランダム数よりも小さければTrueを返す
    return old == define ,old < defineage
        
#文字が数字のみなのか判定
def is_str(value):
    return not value.isdigit()

# 変数初期化
define = int(random.randrange(0,99))
loop_question = True

print('AIの年齢を当ててみよう！ ワタシワナンサイデショウ？0~99サイノドコカダヨ')

while loop_question:
    #変数初期化
    selectold = ""
    while is_str(selectold):
        selectold = input('0~99の数字を入力:')

    correctBool,compareBool = judge(selectold,define)
    if correctBool:
        loop_question = False
    else:
        if compareBool:
            print("モットオオキイヨ！")
        else:
            print("モットチイサイヨ")

print('ソウ、ワタシハ{}サイダヨ！！'.format(define))