import os.path
import re


class FileProcessor:
    __sentences_end_regex = re.compile(r'\.\.\.|\.|!|\?')
    __words_regex = re.compile(r'[А-ЯЁҐЄЇа-яёґєїA-Za-z\d]+')

    def __init__(self, filename: str):
        if not isinstance(filename, str):
            raise TypeError('Filename should be str')
        if not os.path.isfile(filename):
            raise ValueError('Provided filename is not a filename')
        self.__filename = filename

    def count_chars(self):
        n_chars = 0
        with open(self.__filename, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                n_chars += len(line)
        return n_chars

    def count_words(self):
        n_words = 0
        with open(self.__filename, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                matches = re.findall(self.__words_regex, line)
                n_words += len(matches)
        return n_words

    def count_sentences(self):
        n_sentences = 0
        with open(self.__filename, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                n_sentences += len(re.findall(self.__sentences_end_regex, line))
        return n_sentences

    @property
    def filename(self):
        return self.__filename
