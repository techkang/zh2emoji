# -*- coding:utf-8 -*-

from emoji_dict import emoji_dict
import pypinyin


def get_first_dict():
    py_dict = {pypinyin.pinyin(key, heteronym=True)[0][0]:values for key, values in emoji_dict.iteritems()}
    print(py_dict)


def get_all_dict():
    all_dict = {}
    for key, values in emoji_dict.iteritems():
        py_list = pypinyin.pinyin(key)
        for py in py_list:
            if py[0] in all_dict:
                all_dict[py[0]].extend(values)
            else:
                all_dict[py[0]] = values
    print(all_dict)


if __name__ == '__main__':
    get_all_dict()