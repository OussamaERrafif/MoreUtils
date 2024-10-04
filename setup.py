from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.12'
DESCRIPTION = 'a package containing more utilities for python'
LONG_DESCRIPTION = '''
# MoreUtilspy

`moreutils` is a Python utility package designed to handle a variety of text, number, and data transformations. It includes features for converting between different formats (e.g., numbers, dates, Roman numerals), working with text (e.g., anagrams, palindromes), and handling JSON/CSV conversions.

## Installation

To install `moreutilspy`, use pip:

```bash
pip install moreutilspy
```

## Usage

After installation, you can import and use the functions directly:

```python
from moreutils import text_to_number, is_palindrome
```

### Module: `converter_utils`

This module provides functions for converting numbers, dates, bytes, and more.

#### Functions

##### `text_to_number(text: str) -> int`
Converts a textual representation of a number into its numerical value.

**Example:**
```python
text_to_number("one hundred twenty-three")  # Returns: 123
```

##### `number_to_text(num: int) -> str`
Converts a number to its textual representation.

**Example:**
```python
number_to_text(123)  # Returns: "one hundred twenty-three"
```

##### `int_to_roman(num: int) -> str`
Converts an integer to a Roman numeral.

**Example:**
```python
int_to_roman(2024)  # Returns: "MMXXIV"
```

##### `roman_to_int(roman: str) -> int`
Converts a Roman numeral to an integer.

**Example:**
```python
roman_to_int("MMXXIV")  # Returns: 2024
```

##### `snake_to_camel(snake_str: str) -> str`
Converts a snake_case string to camelCase.

**Example:**
```python
snake_to_camel("hello_world")  # Returns: "helloWorld"
```

##### `camel_to_snake(camel_str: str) -> str`
Converts a camelCase string to snake_case.

**Example:**
```python
camel_to_snake("helloWorld")  # Returns: "hello_world"
```

##### `seconds_to_text(seconds: int) -> str`
Converts seconds into a human-readable format.

**Example:**
```python
seconds_to_text(3665)  # Returns: "1 hours, 1 minutes, 5 seconds"
```

##### `text_to_seconds(time_str: str) -> int`
Converts a text representation of time to seconds.

**Example:**
```python
text_to_seconds("1 hour, 1 minute, 5 seconds")  # Returns: 3665
```

##### `date_to_text(date_str: str) -> str`
Converts a date in `YYYY-MM-DD` format to a human-readable text.

**Example:**
```python
date_to_text("2024-01-01")  # Returns: "January 1, 2024"
```

##### `text_to_date(text: str) -> str`
Converts a text representation of a date into `YYYY-MM-DD` format.

**Example:**
```python
text_to_date("January 1 2024")  # Returns: "2024-01-01"
```

##### `bytes_to_text(num_bytes: int) -> str`
Converts bytes into a human-readable string.

**Example:**
```python
bytes_to_text(10240)  # Returns: "10.00 KB"
```

##### `text_to_bytes(size_str: str) -> int`
Converts a string representation of file size into bytes.

**Example:**
```python
text_to_bytes("10 KB")  # Returns: 10240
```

---

### Module: `text_utils`

This module contains utilities for working with text strings, including palindromes, anagrams, and generating random passwords.

#### Functions

##### `is_palindrome(s: str) -> bool`
Checks if a string is a palindrome.

**Example:**
```python
is_palindrome("racecar")  # Returns: True
```

##### `are_anagrams(str1: str, str2: str) -> bool`
Checks if two strings are anagrams.

**Example:**
```python
are_anagrams("listen", "silent")  # Returns: True
```

##### `count_vowels(s: str) -> int`
Counts the number of vowels in a string.

**Example:**
```python
count_vowels("hello world")  # Returns: 3
```

##### `count_consonants(s: str) -> int`
Counts the number of consonants in a string.

**Example:**
```python
count_consonants("hello world")  # Returns: 7
```

##### `reverse_words(s: str) -> str`
Reverses the words in a string.

**Example:**
```python
reverse_words("hello world")  # Returns: "olleh dlrow"
```

##### `reverse_string(s: str) -> str`
Reverses a string.

**Example:**
```python
reverse_string("hello")  # Returns: "olleh"
```

##### `remove_duplicates(s: str) -> str`
Removes duplicate characters from a string.

**Example:**
```python
remove_duplicates("mississippi")  # Returns: "misp"
```

##### `is_pangram(s: str) -> bool`
Checks if a string contains all letters of the alphabet.

**Example:**
```python
is_pangram("The quick brown fox jumps over the lazy dog")  # Returns: True
```

##### `levenshtein_distance(s1: str, s2: str) -> int`
Calculates the Levenshtein distance (edit distance) between two strings.

**Example:**
```python
levenshtein_distance("kitten", "sitting")  # Returns: 3
```

##### `generate_password(length: int = 12) -> str`
Generates a random password of the specified length.

**Example:**
```python
generate_password(16)  # Returns: A 16-character random password
```

##### `json_to_csv(json_data: list[dict], csv_file: str)`
Converts JSON data to CSV and writes it to a file.

**Example:**
```python
json_to_csv(json_data, "output.csv")
```

##### `csv_to_json(csv_file: str) -> list[dict]`
Converts a CSV file into JSON format.

**Example:**
```python
data = csv_to_json("input.csv")
```

---

### Examples

Here are a few quick examples to demonstrate how to use `moreutils`:

```python
from moreutils import text_to_number, is_palindrome, generate_password

# Convert text to number
print(text_to_number("one hundred twenty-three"))  # Output: 123

# Check if a string is a palindrome
print(is_palindrome("A man a plan a canal Panama"))  # Output: True

# Generate a random password
print(generate_password(16))  # Output: A randomly generated password
```

---

## License

`moreutils` is open source and licensed under the [MIT License](https://opensource.org/licenses/MIT).


'''

setup(
    name="MoreUtilspy",
    version=VERSION,
    author="oussama errafif",
    author_email="oussamaerra2002@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        'csv','random','string','json','re','datetime','math'
    ], 
    keywords=['python', 'utils'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
