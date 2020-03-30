# -*- coding=utf8 -*-
"""
    viterbi算法实现
"""
from pinyin.model import Emission, Transition
import sys


def viterbi(pinyin_list):
    """
    viterbi算法实现输入法

    Args:
        pinyin_list (list): 拼音列表
    """
    start_char = Emission.join_starting(pinyin_list[0])
    V = {char: prob for char, prob in start_char}

    for i in range(1, len(pinyin_list)):
        pinyin = pinyin_list[i]

        prob_map = {}
        for phrase, prob in V.iteritems():
            character = phrase[-1]
            result = Transition.join_emission(pinyin, character)
            if not result:
                continue

            state, new_prob = result
            prob_map[phrase + state] = new_prob + prob

        if prob_map:
            V = prob_map
        else:
            return V
    return V


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    input_file_name = 'input.txt'
    output_file_name = 'output.txt'
    input_file = open(input_file_name, 'r')
    output_file = open(output_file_name, 'w')
    one_line = input_file.readline()
    while one_line != '':
        pinyin_list = one_line.split()
        V = viterbi(pinyin_list)
        phrase, prob = sorted(V.items(), key=lambda d: d[1], reverse=True)[0]
        output_file.write(phrase + '\n')
        one_line = input_file.readline()
    input_file.close()
    output_file.close()