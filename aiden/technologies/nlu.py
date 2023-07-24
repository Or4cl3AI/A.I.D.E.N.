```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

class NLU:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))

    def understand(self, text):
        tokenized = sent_tokenize(text)
        for i in tokenized:
            words = nltk.word_tokenize(i)
            words = [word for word in words if not word in self.stop_words]
            tagged = nltk.pos_tag(words)
            return tagged
```