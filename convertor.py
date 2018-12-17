# -*- coding:utf-8 -*-

from emoji_pinyin_dict import first_dict, all_dict
import pypinyin
import random
from inverse_emoji_dict import inverse_emoji_dict

EMOJI_PER_LINE=10

def get_emoji(word, py):
    return first_dict[py][0] if py in first_dict else word


def get_random_emoji(word, py):
    return random.sample(all_dict[py], 1)[0] if py in all_dict else word

def hand_wirtten(word,py):
    print(word,' ',py)
    if not all_dict.get(py):
        return word
    else:
        temp_dict=all_dict[py]
        output=[]
        for i,item in enumerate(temp_dict):
            output.append("{}:{}{}".format(i,item,'  ' if (i+1)%EMOJI_PER_LINE else '\n'))
        print(''.join(output))
    return all_dict[py][int(input())]

METHOD = {
    0: get_emoji,
    1: get_random_emoji,
    2: hand_wirtten
}


def get_pinyin(word):
    print(word)
    return pypinyin.pinyin(word)


def get_converted(words, explain, method):
    emojis = []
    pys = get_pinyin(words)
    for word,py in zip(words,pys):
        emo = METHOD[method](word, py[0])
        emojis.append(emo)
    exp=[]
    if explain:
        exp.append('\n')
        for item in emojis:
            if inverse_emoji_dict.get(item):
                exp.append(item+':'+inverse_emoji_dict[item]+' ')
            else:
                exp.append(item)
        
    return ''.join(emojis+exp)

def create_inverse_dict(d):
    new_dict={}
    try:
        for k,v in d.items():
            for item in v:
                new_dict[item]=k
    except:
        print(k,v)
    return new_dict
def run(method=0,explain=True):
    # words = input("Please input text: ")
    words='文体两开花 弘扬中华文化'
    print(get_converted(words, explain,method))


if __name__ == '__main__':
    run(2)


