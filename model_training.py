# -*- coding: utf-8 -*-
import collections, pickle, os

"""This walks through all the files in the given directory, reads them
   all and appends them together to create a single merged file"""
def file_open(path):
    f =""
    listing = os.listdir(path)
    for file in listing:
        with open(path+file, 'r', encoding = 'utf8') as txt:
            f += txt.read().replace('\n', '')
    return f

def save_to_file(txt, lang):
    with open(lang,'wb') as f:
        pickle.dump(txt, f)
        
def ngrams(txt, n):
    return [txt[i:i+n] for i in range(len(txt)-n+1)]
def ranker(grams):
    return collections.Counter(grams).most_common()[:300]

def sorted_list(txt):
    total_list = []
    for i in range(1, 6):
        g = ngrams(txt, i)
        total_list.append(ranker(g))
    total_list = sorted(total_list, key=lambda x: x[1])[:300]
    return total_list

def main():
    cwd = os.getcwd() + '\\training set'
    langs = os.listdir(cwd)
    for lang in langs:
        li = sorted_list(file_open(cwd+'\\'+lang+'\\'))
        save_to_file(li, lang)

if __name__ == "__main__":
    main()
