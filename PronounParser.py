from nltk import pos_tag
import Constants

BLACKLIST = [i.lower() for i in Constants.BLACKLIST]

def is_cap(t):
    return t[0] == t[0].upper()

def sum_lo_str(ls):
    s= ""
    for i in ls:
        s+=i+" "
    return s.strip()

def handle_bank(text,tokenizer):
    s = text.split('Bank of')
    if len(s)==1:
        return [], text
    first = s[0]
    lo_bnk = []
    txt_wo_bnk = ""

    for i in range(1,len(s)):
        t = tokenizer.tokenize(s[i])
        f = t[0]
        txt_wo_bnk += sum_lo_str(t[1:])
        lo_bnk.append("Bank of "+f)

    return lo_bnk, first+ " " + txt_wo_bnk.strip()


def _is_noun(pos):
    return pos[:2] == 'NN'
    #return pos[:3] == 'NNP'

def extract_unique_noun_list(tokenized):
    return list(set([word for (word, pos) in pos_tag(tokenized) if _is_noun(pos)]))


def extract_list_of_pronoun(text, tokenizer):
    lo_bnk,text = handle_bank(text,tokenizer)

    tokenized = tokenizer.tokenize(text)
    lo_noun = extract_unique_noun_list(tokenized)

    glue = ""
    all_combo_cap = []
    prev_cap = False
    for token in tokenized:
        if is_cap(token) and token in lo_noun:
            glue += token + " "
            prev_cap = True
        else:
             if prev_cap:
                 prev_cap = False
                 all_combo_cap.append(glue.strip())
                 glue = ""

    if prev_cap:
        all_combo_cap.append(glue.strip())

    all_combo_cap = [i for i in all_combo_cap if i.lower() not in BLACKLIST]
    return all_combo_cap+lo_bnk

