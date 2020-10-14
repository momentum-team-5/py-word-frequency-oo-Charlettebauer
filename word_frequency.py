#! /usr/local/bin/python3

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]
 

class FileReader:
    def __init__(self, filename):
        pass
        self.filename = filename.open()


    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        raise NotImplementedError("FileReader.read_contents")
        contents = self.filename.read()
        return contents
        

class WordList:
    def __init__(self, text):
        pass
        self.text = text
        self.words = []
        

    def extract_words(self):
        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation.
        """
        raise NotImplementedError("WordList.extract_words")
        import string

        
        self.words = self.text.lower().split()
        self.words = [word.strip(string.punctuation) for word in self.words]
        #print(self.words)

        
    def remove_stop_words(self):
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words.
        """
        raise NotImplementedError("WordList.remove_stop_words")
        self.words = [
            word
            for word in self.words
            if not word in STOP_WORDS
        ]

    def get_freqs(self):
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """
        raise NotImplementedError("WordList.get_freqs")
        dictionary = {}
        for word in self.word_list:
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1    
        letter_sorted = sorted(dictionary.items(), key=lambda entry: entry[0])
        count_sorted = sorted(letter_sorted, key=lambda seq: seq[1], reverse=True)


class FreqPrinter:
    def __init__(self, freqs):
        pass
        self.freqs = freqs
        
    def print_freqs(self):
        """
        Prints out a frequency chart of the top 10 items
        in our frequencies data structure.

        Example:
          her | 33   *********************************
        which | 12   ************
          all | 12   ************
         they | 7    *******
        their | 7    *******
          she | 7    *******
         them | 6    ******
         such | 6    ******
       rights | 6    ******
        right | 6    ******
        """
        raise NotImplementedError("FreqPrinter.print_freqs")
        
        
        words = list(self.freqs)[0:10]
        print()
        for word in words:
            print(word[0].rjust(15) + " | " + str(word[1].ljust(3) +  " " + (word[1] * "*"))

if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
