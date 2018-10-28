# -*- coding:utf-8 -*-

from pyhanlp import *
import json

def predict(key):
    d = {}
    WordVectorModel = JClass('com.hankcs.hanlp.mining.word2vec.WordVectorModel')
    DocVectorModel = JClass('com.hankcs.hanlp.mining.word2vec.DocVectorModel')
    # word2vec = WordVectorModel(model_path)
    word2vec = WordVectorModel('hanlp-wiki-vec-zh.txt')
    doc2vec = DocVectorModel(word2vec)
    near = word2vec.nearest(key)
    for i in near:
        d[i.key] = i.value
    return d

def input_dict(path):
    with open(path) as f:
        dict = json.load(fp = f)
    return dict

def output_dict(dict,path):
    jsonObj = json.dumps(dict, ensure_ascii=False, indent=4)
    fileObject = open(path, 'w')
    fileObject.write(jsonObj)
    fileObject.close()

def get_key_dict(dict):
    key_list = [] 
    for i in dict:
        key_list.append(i)
    return key_list

def main():
    dd = {}
    dict = input_dict('./similar/more_normal.txt')
    key_list = get_key_dict(dict)
    length = len(key_list)
    index = 0
    for i in key_list:
        index = index + 1
        print("%s/%s"%(index,length))
        similar = predict(i)
        if predict(i) != {} :
            print(i)
            dd[i] = similar
            print(dd[i])
        else:
            print(i)
            print ('无相似词')
            print (similar)

    output_dict(dd, 'more_similar/more_normal.json')
    print('历经千辛万苦，终于完成啦~more_normal.json')
    # dd['机关枪'] = predict('机关枪')

main()