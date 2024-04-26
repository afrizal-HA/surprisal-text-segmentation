### Define the functions
import math

# Define a function to clean the text
def clean_text(text, withdots=True):
    text = text.lower()
    allowed = "- "
    if withdots:
        allowed +='.'
    return ''.join(char for char in text if char.isalnum() or char in allowed)

# Get a dictionary of word frequency
def wordfreq(text: str):
    freq = {}
    text = clean_text(text, withdots=False)
    text = text.split()
    for word in text:
        word = str(word).lower()
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] +=1
    return freq

# Word-level surprisal
def surprisal(word: str, freq: dict, totcount=None):
    if totcount is None:
        totcount = sum(freq.values())
    word = word.lower()
    word = clean_text(word, withdots=False)
    surprisal = 0
    
    if word not in freq:
        surprisal += float('inf')
    else:
        prob = freq[word] / totcount
        surprisal += -math.log2(prob)
    return surprisal

# Sentence-level surprisal
def surprisalSent(sentence: str, freq:dict, totcount=None):
    if totcount is None:
        totcount = sum(freq.values())
    sentence = clean_text(sentence)
    sentence = sentence.split()
    sentence_surprisal = 0
    if totcount is None: totcount = sum(freq.values())
    for words in sentence:
        sentence_surprisal += surprisal(words, freq, totcount)
    return sentence_surprisal

# Function to segment the text
def segment(text:str, k:int, segloc='none'):
    if segloc not in ['start','end', 'none']:
        raise ValueError('''"segloc" argument must be "start", "end", or "none"''')
    text = clean_text(text)
    text = text.split('.')
    sentences = [s for s in text if s!='']
    idxRank = []
    for idx, t in enumerate(sentences):
        t = t.strip()
        if idx == 0:
            idxRank.append((idx,t,float('-inf')))
        elif idx == len(sentences)-1:
            idxRank.append((idx,t,float('-inf')))
        else:
            FIRST = ''.join(str(s) for s in sentences[:idx+1]).strip()
            FIRSTFREQ = wordfreq(FIRST)
            INFO_ONE = surprisalSent(t, FIRSTFREQ)

            SECOND = ''.join(s for s in sentences[idx:]).strip()
            SECONDFREQ = wordfreq(SECOND)
            INFO_TWO = surprisalSent(t, SECONDFREQ)

            SCORE = (INFO_ONE /((INFO_TWO+1)))*INFO_TWO /((INFO_ONE+1))
            idxRank.append((idx, t, SCORE))
    idxRank.sort(key=lambda x: x[2], reverse=True)
    separator = [x[1] for x in idxRank[:k]]
    idxRank.sort(key=lambda x: x[0])
    if segloc != 'none': print('SECTION 1')
    i = 2
    for s in idxRank:
        t = s[1]
        surprisal = s[2]
        if t in separator:
            if segloc=='start':
                print(f'\nSECTION {abs(k-(k-i))}')
                i +=1
            t = '\033[32m'+t+'.'+'\033[0m'.strip()
            print(f'({surprisal:.6f}) {t}')
            if segloc=='end':
                print(f'\nSECTION {abs(k-(k-i))}')
                i +=1
        else: 
            t = t+'.'.strip()
            print(f'({surprisal:.6f}) {t}')
