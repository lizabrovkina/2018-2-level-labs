"""
Labour work #3
 Building an own N-gram model
"""

import math
 REFERENCE_TEXT = ''
if __name__ == '__main__':
    with open('not_so_big_reference_text.txt', 'r') as f:
        REFERENCE_TEXT = f.read()
 def split_by_sentence(sample_text):
    if type(sample_text) != str:
        return list()
    text = sample_text
    eofs = ".!?"  
    tmp = str()
    lofs = []  # list of sentences
    lofw = []  # list of words
    ind = 0  
    for sym in text:
        if len(lofw) == 0 and len(lofs) == 0:
            lofw.append("<s>")
        if "A" <= sym <= "Z":
            if ind == 0:
                tmp += sym
            if ind == 1:
                if len(lofw) != 0:
                    lofw.append("</s>")
                    lofs.append(lofw)
                    lofw = []
                    lofw.append("<s>")
                ind = 0
                tmp += sym
        elif "a" <= sym <= "z":
            tmp += sym
            if ind == 1:
                ind = 0
        elif sym == " " and ind == 0:
            if tmp != "":
                lofw.append(tmp.lower())
                tmp = ""
        elif eofs.find(sym) >= 0:
            if tmp != "":
                lofw.append(tmp.lower())
                tmp = ""
            ind = 1
    if len(lofw) - 1 != 0 and ind == 1:
        lofw.append("</s>")
        lofs.append(lofw)
     return lofs
 class WordStorage:
    storage = dict()
    now = int()  # number of words
     def __init__(self):
        pass
     def put(self, word):
        if type(word) != str:
            return
        for k, v in self.storage.items():
            if word == k:
                return v
        self.storage[word] = self.now
        self.now += 1
        return self.get_id_of(word)
     def get_id_of(self, word):
        if type(word) != str:
            return -1
        if type(word) != str:
            return
        for k, v in self.storage.items():
            if word == k:
                return v
        return -1
     def get_original_by(self, id):
        if type(id) is None:
            return "UNK"
        if type(id) != int:
            return "UNK"
        for k, v in self.storage.items():
            if id == v:
                return k
        return "UNK"
     def from_corpus(self, corpus):
        if type(corpus) != tuple:
            return
        for word in corpus:
            self.put(word)
        return self.storage
 def encode(storage_instance, corpus):
    cod = list()
    list_2 = list()
    for list_1 in corpus:
        for word in list_1:
            if word == "<s>" or word == "</s>":
                list_2.append(word)
                if word == "</s>":
                    cod.append(list_2)
                    list_2 = []
            else:
                for k, w in storage_instance.items():
                    if w == word:
                        list_2.append(k)
     return cod
 class NGramTrie:
    size = 0
    gram_frequencies = dict()
    gram_log_probabilities = dict()
     def __init__(self, size):
        self.size = size
     def fill_from_sentence(self, sentence):
        if type(sentence) is None:
            return {}
        if type(sentence) != tuple:
            return {}
        indicator = "OK" 
        gram = dict()
        i = -1
        for word in sentence:
            buf = list()
            i += 1
            if i + 1 != len(sentence):
                ind = 0
                buf.append(sentence[i])
                buf.append(sentence[i+1])
                for k in gram.keys():
                    if k == tuple(buf):
                        ind = 1
                if ind == 0:
                    gram[tuple(buf)] = 1
                else:
                    gram[tuple(buf)] += 1
        if indicator == "OK":
            self.gram_frequencies = gram
     def calculate_log_probabilities(self):
        print (self.gram_frequencies)
        for k, v in self.gram_frequencies.items():
            buft = k
            bufc = v
            bufz = 0.0
            for kk, vv in self.gram_frequencies.items():
                if k[0] == kk[0]:
                    bufz += vv
            self.gram_log_probabilities[buft] = math.log(bufc / bufz)
     def predict_next_sentence(self, prefix):
        if prefix is None:
            return []
        if type(prefix) != tuple:
            return []
        if len(prefix) == 1:
            ind1 = 0
            Res = [prefix[0]]
            search = prefix[0]
            buf = list()
            while ind1 != 1:
                ind1 = 1
                maxk = list()
                maxv = -10000.0
                ind2 = 0
                for k, v in self.gram_log_probabilities.items():
                    if k[0] == search:
                        for elem in buf:
                            if elem == k[1]:
                                ind2 = 1
                        if ind2 != 1:
                            if v > maxv:
                                ind1 = 0
                                maxv = v
                                maxk = k
                if (ind1 == 0):
                    Res.append(maxk[1])
                    search = maxk[1]
            return Res
        return []

