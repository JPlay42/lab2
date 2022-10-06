import tempfile
import unittest

from ex4 import FileProcessor


class TestEx4(unittest.TestCase):
    def test_units_counting(self):
        with tempfile.NamedTemporaryFile() as tmp:
            tmp.write(bytes('Hello ,world ... Python is the&best\nlanguage_ever!', 'ascii'))
            tmp.flush()
            file_processor = FileProcessor(tmp.name)
            file_processor.process()
            self.assertEqual(50, file_processor.n_chars)
            self.assertEqual(8, file_processor.n_words)
            self.assertEqual(2, file_processor.n_sentences)


if __name__ == '__main__':
    unittest.main()
