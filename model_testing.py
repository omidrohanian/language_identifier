from model_training import ngrams, ranker, sorted_list
import pickle, os 

"""This assigns a class label to the input file based 
on the rank-order statistic called the 'out-of-place' measurement."""
def classifier(input_lang):
    langs = ['persian', 'arabic', 'portuguese', 'spanish']
    list_of_distances = []
    for lang in langs:
        dist = 0
        target_lang = pickle.load(open(lang, "rb"))[0]
        target_lang = [i[0] for i in target_lang]
        for i, ngram in enumerate(input_lang):
            try:
                j = target_lang.index(ngram)
            except ValueError:
                # if the ngram from the training is not found in the input language
                # then we assign to it a pre-defined maximum out-of-place distance 
                dist += 100
                continue
            dist += abs(i-j)
        list_of_distances.append((lang, dist))
    list_of_distances = sorted(list_of_distances, key=lambda x: x[1])
    return list_of_distances[0][0]

def main():
    cwd = os.getcwd() + '\\test set'
    langs = os.listdir(cwd)
    for lang in langs:
        new_cwd = cwd+'\\'+lang+'\\'
        files = os.listdir(new_cwd)
        for file in files:
            with open(new_cwd+file, 'r', encoding = 'utf8') as f:
                test = f.read().replace('\n', '')
                # here we first obtain the ranked ngrams for the test file
                input_lang = sorted_list(test)[0]
                # we then discard the number of occurences for each ngram
                input_lang = [i[0] for i in input_lang]

                detected_lang = classifier(input_lang)

                if lang in detected_lang:
                    print('Success!')
                else:
                    print('FAIL!')

                print('input language =', lang)
                print('detected language =', detected_lang)
                print('###')
                
if __name__ == "__main__":
    main()
