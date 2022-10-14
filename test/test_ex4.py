import tempfile
import unittest

from ex4 import FileProcessor


class TestEx4(unittest.TestCase):
    def test_filename_validation(self):
        with self.assertRaises(TypeError):
            FileProcessor(1234)
        with self.assertRaises(ValueError):
            FileProcessor('I am not a file')

    def test_units_counting(self):
        with tempfile.NamedTemporaryFile() as tmp:
            tmp.write(bytes('Hello ,world ... Python? is the&best\nlanguage_ever!\n\n', 'ascii'))
            tmp.flush()
            file_processor = FileProcessor(tmp.name)
            self.assertEqual(53, file_processor.count_chars())
            self.assertEqual(8, file_processor.count_words())
            self.assertEqual(3, file_processor.count_sentences())

    def test_empty_file(self):
        with tempfile.NamedTemporaryFile() as tmp:
            file_processor = FileProcessor(tmp.name)
            self.assertEqual(0, file_processor.count_chars())
            self.assertEqual(0, file_processor.count_words())
            self.assertEqual(0, file_processor.count_sentences())


if __name__ == '__main__':
    unittest.main()
