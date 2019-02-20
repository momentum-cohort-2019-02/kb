# Word Frequency

## Directions

In this project, you will use `open` to read in a text file and calculate the frequency of words in that file.

To calculate the frequency of words, you must:

- remove punctuation
- normalize all words to lowercase
- remove "stop words" -- words used so frequently they are ignored
- go through the file word by word and keep a count of how often each word is used

When your program is complete, you should be able to run `python3 wordfreq.py seneca_falls.txt` and get a printed report like this:

```
     her | 33 *********************************
     all | 12 ************
   which | 12 ************
     she | 7  *******
   their | 7  *******
    they | 7  *******
   right | 6  ******
  rights | 6  ******
    such | 6  ******
    them | 6  ******
```

## Starter Files

A starting program is located in `word_frequency.py`.

## Links

* [The `dict` type in Python 3](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
* [Pyformat](https://pyformat.info/) - covers two ways of formatting strings with Python, neither of which are f-strings
* [f-strings in Python 3](https://realpython.com/python-f-strings/)
