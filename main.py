import glob, os
import re

class Organize:
    def __init__(self, wordList):
     self.map = {
          'palindrome': [],
          'urls': [],
          'phone_numbers': [],
          'ints': [],
          'words': [],
     }
     self.wordList = wordList

    def count_all(self):
     self.urls_count()
     self.ints_count()
     self.words_count()
     self.palindromes_count()
     self.phone_numbers_count()
     
    def print_all(self):
     self.print_urls()
     self.print_ints()
     self.print_words()
     self.print_palindromes()
     self.print_phone_numbers()

    def check_all(self):
     for word in self.wordList:
          if word is not int and self.is_palindrome(word) is True:
            self.map['palindrome'].append(word)

          if self.is_urls(word) is True:
            self.map['urls'].append(word)

          if self.is_phone_numbers(word) is True:
            self.map['phone_numbers'].append(word)

          if self.is_ints(word) is True:
            self.map['ints'].append(int(word))

          if self.is_words(word) is True:
            self.map['words'].append(word)
     for k in self.map:
       self.map[k].sort()
       
    def urls_count(self):
     print(len(self.map['urls']))
    def ints_count(self):
     print(len(self.map['ints']))
    def words_count(self):
     print(len(self.map['words']))
    def palindromes_count(self):
     print(len(self.map['palindrome']))
    def phone_numbers_count(self):
     print(len(self.map['phone_numbers']))
    
    def print_urls(self):
     print(self.map['urls'])
    def print_ints(self):
     print(self.map['ints'])
    def print_words(self):
     print(self.map['words'])
    def print_palindromes(self):
     print(self.map['palindrome'])
    def print_phone_numbers(self):
     print(self.map['phone_numbers'])

    
        
    def is_palindrome(self, s:str) -> bool:
     s = [char.lower() for char in s if char.isalnum()]
     return s == s[::-1]

    def is_urls(self, s:str) -> bool:
     pattern = 'http[s]?://[3a-z]+.'
     return bool(re.search(pattern, s))
        
    def is_phone_numbers(self, s:str) -> bool:
     pattern = '^(\+\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
     return bool(re.search(pattern, s))

    def is_ints(self, s:str) -> bool:
     return s.isnumeric()
        
    def is_words(self, s:str) -> bool:
     return s.isalpha()


os.chdir("./assets")
wordList = set()
for file in glob.glob("*.txt"):
     with open(file) as f:
          for line in f:
            wordList.add(line.strip())

element = Organize(wordList)
element.check_all()

# element.print_all()
# element.print_urls()
# element.print_ints()
# element.print_words()
# element.print_palindromes()
# element.print_phone_numbers()

# element.count_all()
# element.urls_count()
# element.ints_count()
# element.words_count()
# element.palindromes_count()
# element.phone_numbers_count()

