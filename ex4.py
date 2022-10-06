import re


class FileProcessor:
    filename: str
    n_chars: int
    n_words: int
    n_sentences: int

    def __init__(self, filename: str):
        self.filename = filename

    def process(self):
        with open(self.filename, 'r') as file:
            data = file.read()
            self.n_chars = len(data)
            self.n_words = self.count_words(data)
            self.n_sentences = self.count_sentences(data)

    @staticmethod
    def count_words(data: str):
        words_regex = re.compile(r'[^А-ЯЁҐЄЇа-яёґєїA-Za-z\d]+')
        if data == '' or re.match(words_regex, data) is not None:
            return 0
        n_words = len(re.findall(words_regex, data))
        # if the last symbol belongs to word (we have no splitter at the end)
        if re.match(words_regex, data[-1]) is None:
            n_words += 1
        return n_words

    @staticmethod
    def count_sentences(data: str):
        return len(re.findall(r'\.\.\.|\.|!|\?', data))
