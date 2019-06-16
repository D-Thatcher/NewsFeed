from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import matplotlib.colors



class Sentient(SentimentIntensityAnalyzer):
    def __init__(self):
        super().__init__()
        self.cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["red","yellow","green"])

    def _align(self, v):
        return int(((v + 1) / 2.0) * 255.0)

    def rgb_from_score(self,score):
        rgba_111 = list(self.cmap(self._align(float(score))))
        rgba_111 = rgba_111[:-1]
        return [255*i for i in rgba_111]

    def process_paragraph(self, paragraph):
        sentences = tokenize.sent_tokenize(paragraph)
        sum_so_far = 0
        n = 0
        for sentence in sentences:
            ss = self.polarity_scores(sentence)
            sum_so_far+=ss['compound']
            n+=1
        return sum_so_far/float(n)





