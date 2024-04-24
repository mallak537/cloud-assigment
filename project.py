import nltk
from nltk.corpus import stopwords
from collections import Counter
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

with open('Random.txt', 'r') as file:
    para = file.read()
    words = nltk.word_tokenize(para)
    freq = {}
    filtered_words = [word for word in words if word.lower() not in stop_words]

    for word in filtered_words:
        if word in freq:
                freq[word] += 1
        else:
                freq[word] = 1  

for key, value in freq.items():
    print(key,':', value)