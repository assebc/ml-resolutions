import collections, math

class MultinomialNB:
    def __init__(self, articles_per_tag):
        # Don't change the following two lines of code.
        self.articles_per_tag = articles_per_tag  # See question prompt for details.
        self.train()

    def train(self):
        N = sum ([len(self.articles_per_tag[topic]) for topic in self.articles_per_tag])
        self.priors = { topic: math.log(len(self.articles_per_tag[topic])/N) for topic in self.articles_per_tag}
        vocab = { topic: [] for topic in self.articles_per_tag}
        for topic in self.articles_per_tag:
            for art in self.articles_per_tag[topic]:
                vocab[topic]+=art
        flat_vocab = []
        for topic in vocab:
            flat_vocab += vocab[topic]
        self.vocab = list(set(flat_vocab))

        self.tag_likelihoods = { topic : {} for topic in self.articles_per_tag}
        for topic in self.articles_per_tag:
            c = collections.Counter(vocab[topic])
            numWords = len(vocab[topic])
            for word in self.vocab:
                self.tag_likelihoods[topic][word] = (c[word] + 1) / (numWords + 2)

        
    def predict(self, article):
        # Write your code here.
        c = collections.Counter(article)
        c_article = { word:c[word] for word in self.vocab}
        results = {}
        for topic in self.articles_per_tag:
            likelihood = sum([math.log(self.tag_likelihoods[topic][word]) if word in self.tag_likelihoods[topic] else math.log(0.5) for word in article])
            results[topic] = self.priors[topic] + likelihood

        return results