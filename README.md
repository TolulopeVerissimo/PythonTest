# Python Assessment

-   Suppose you have files of unsorted data from Macys.com.
-   You want to sort the data into categories, so a Machine Learning algorithm can train on them.

### Write a class to do the following:

-   Read text files: words1.txt, words2.txt, words3.txt

-   Remove duplicate words.

-   Sort words into categories:

    -   urls - web address (i.e. https://www.abc.com)

    -   ints - integers (they will be read in from the files as strings. Convert to int)

    -   words - no need to check if they are valid dictionary words

    -   palindromes - words that are the same backwards and forwards

    -   phone numbers - numbers of the format xxx-yyy-zzzz
        -   (where x, y, and z range from 0 to 9)

-   Your class will organize the words into a data structure with the categories listed above.

-   Your class will have methods to print each category: print_urls(), print_ints() etc.

-   Elements will be sorted in ascending order. Ints should be printed 0, 1, 2, etc.

### Your class will have methods to print the number of elements in each category: int_count(), url_count() etc.

### Write a script or main routine to use your class to read all text files and print out each category.

-   All code can be in one file.

## Running

From a terminal with Python installed, run the following to start the script:

```
python3 main.py
```

## Requirement

My approach to the challenge was to create boolean validators for each parameter within the requirements -- then sorting and printing/counting each category.

I included a set to prevent duplicate storage, used regex to simplify string search, converted strings to integers when necessary, and sorted each set-List.

While checking for palindromes, I excluded the use of numbers because the directions explicitly mentioned words.

## Methods

### Boolean Validators

```
check_all(self)
is_palindrome(self, string)
is_urls(self, string)
is_phone_numbers(self, string)
is_ints(self, string)
is_words(self, string)
```

### Print/Count All Categories

```
count_all(self)
print_all(self)
```

### Print Categories

```
print_urls(self)
print_ints(self)
print_words(self)
print_palindromes(self)
print_phone_numbers(self)
```

### Count Elements within Categories

```
urls_count(self)
ints_count(self)
words_count(self)
palindromes_count(self)
phone_numbers_count(self)
```
