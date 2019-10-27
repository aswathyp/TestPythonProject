
# 1. Reverse the inputted words

class SentenceReverser:
    def __init__(self, sentence):
        self.sentence = sentence

    def displaySentence(self):
        print(self.sentence)

    def reverseWords(self):
        self.sentence = self.sentence.__reversed__()

if __name__ == '__main__':
    s = ''
    s.__reversed__()
    sentence = SentenceReverser(input('Enter the sentence: '))
    sentence.displaySentence()
    sentence.reverseWords()
    sentence.displaySentence()