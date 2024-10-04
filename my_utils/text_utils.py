
import csv
import random
import string
from typing import Counter


def is_palindrome(s):
    """
    Check if a string is a palindrome.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    s = str(s).lower().replace(' ', '') 
    return s == s[::-1]

def are_anagrams(str1, str2):
    """
    Check if two strings are anagrams.

    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    return sorted(str1.replace(' ', '').lower()) == sorted(str2.replace(' ', '').lower())

def count_vowels(s):
    """
    Count the number of vowels in a string.

    Args:
        s (str): The string to count vowels in.

    Returns:
        int: The number of vowels in the string.
    """
    return sum(1 for char in s if char.lower() in 'aeiou')

def count_consonants(s):
    """
    Count the number of consonants in a string.

    Args:
        s (str): The string to count consonants in.

    Returns:
        int: The number of consonants in the string.
    """
    return sum(1 for char in s if char.isalpha() and char.lower() not in 'aeiou')

def reverse_words(s):
    """
    Reverse the words in a string.

    Args:
        s (str): The string to reverse words in.

    Returns:
        str: The string with words reversed.
    """
    return ' '.join(word[::-1] for word in s.split())

def reverse_string(s):
    """
    Reverse a string.

    Args:
        s (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    return s[::-1]

def remove_duplicates(s):
    """
    Remove duplicate characters from a string.

    Args:
        s (str): The string to remove duplicates from.

    Returns:
        str: The string with duplicates removed.
    """
    return ''.join(sorted(set(s), key=s.index))

def is_pangram(s):
    """
    Check if a string is a pangram.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a pangram, False otherwise.
    """
    return set('abcdefghijklmnopqrstuvwxyz') <= set(s.lower())

def is_isogram(s):
    """
    Check if a string is an isogram.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is an isogram, False otherwise.
    """
    return len(s) == len(set(s.lower()))

def is_palindrome_permutation(s):
    """
    Check if a string is a palindrome permutation.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome permutation, False otherwise.
    """
    return sum(1 for count in Counter(s.lower().replace(' ', '')).values() if count % 2 != 0) <= 1

def is_anagram_of_palindrome(s):
    """
    Check if a string is an anagram of a palindrome.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is an anagram of a palindrome, False otherwise.
    """
    return sum(1 for count in Counter(s.lower().replace(' ', '')).values() if count % 2 != 0) <= 1

def is_valid_palindrome(s):
    """
    Check if a string is a valid palindrome.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a valid palindrome, False otherwise.
    """
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True

def is_valid_pangram(s):
    """
    Check if a string is a valid pangram.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a valid pangram, False otherwise.
    """
    return set('abcdefghijklmnopqrstuvwxyz') <= set(s.lower())

def levenshtein_distance(s1, s2):
    """
    Calculates the Levenshtein distance between two strings.

    The Levenshtein distance is a measure of the difference between two strings.
    It is defined as the minimum number of single-character edits (insertions,
    deletions, or substitutions) required to change one string into the other.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        int: The Levenshtein distance between the two strings.
    """
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def longest_common_subsequence(s1, s2):
    """
    Finds the longest common subsequence between two strings.

    A subsequence is a sequence that can be derived from another sequence by
    deleting some or no elements without changing the order of the remaining
    elements. A common subsequence is a subsequence that is common to two
    sequences.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        str: The longest common subsequence between the two strings.
    """
    m, n = len(s1), len(s2)
    dp = [[''] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)

    return dp[m][n]

def longest_common_substring(s1, s2):
    """
    Finds the longest common substring between two strings.

    A substring is a contiguous sequence of characters within a string. A common
    substring is a substring that is common to two strings.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        str: The longest common substring between the two strings.
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length, end_index = 0, 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0

    return s1[end_index - max_length:end_index]

def generate_password(length=12):
    """
    Generates a random password of the specified length.

    Parameters:
    length (int): The length of the password to generate. Default is 12.

    Returns:
    str: The randomly generated password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def json_to_csv(json_data, csv_file):
    """
    Convert JSON data to CSV format and write it to a file.

    Args:
        json_data (list[dict]): The JSON data to be converted.
        csv_file (str): The path to the CSV file to be created.

    Returns:
        None
    """
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=json_data[0].keys())
        writer.writeheader()
        writer.writerows(json_data)

def csv_to_json(csv_file):
    """
    Converts a CSV file to a list of dictionaries in JSON format.

    Args:
        csv_file (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries representing the CSV data in JSON format.
    """
    with open(csv_file, 'r') as file:
        return list(csv.DictReader(file))


