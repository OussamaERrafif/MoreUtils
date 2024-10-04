import re
from datetime import datetime



def text_to_number(text):
    """
    Converts a textual representation of a number into its numerical value.

    Args:
        text (str): The textual representation of the number.

    Returns:
        int: The numerical value of the input text.

    Raises:
        ValueError: If an invalid word is encountered in the input text.
    """
    num_words = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
        'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 
        'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 
        'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 
        'seventy': 70, 'eighty': 80, 'ninety': 90, 'hundred': 100, 'thousand': 1000, 'million': 1000000
    }

    words = text.split()
    total = 0
    current = 0

    for word in words:
        if word in num_words:
            num_val = num_words[word]
            if num_val == 100 or num_val == 1000 or num_val == 1000000:
                current *= num_val
            else:
                current += num_val
        elif word == 'and':
            continue
        else:
            raise ValueError(f"Invalid word: {word}")

        if word == 'thousand' or word == 'million':
            total += current
            current = 0

    total += current
    return total

def number_to_text(num):
    """
    Converts a number to its textual representation.

    Args:
        num (int): The number to be converted.

    Returns:
        str: The textual representation of the number.

    Raises:
        ValueError: If the input is not an integer or if the number is not between 0 and 999,999.
    """
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    def two_digit_number(n):
        if n < 10:
            return ones[n]
        elif 10 <= n < 20:
            return teens[n - 10]
        else:
            return tens[n // 10] + ('' if n % 10 == 0 else ' ' + ones[n % 10])
    
    def three_digit_number(n):
        if n < 100:
            return two_digit_number(n)
        else:
            return ones[n // 100] + ' hundred' + ('' if n % 100 == 0 else ' and ' + two_digit_number(n % 100))

    if not isinstance(num, int):
        raise ValueError("Invalid input: number must be an integer")
    
    if num < 0 or num >= 1000000:
        raise ValueError("Invalid input: number must be between 0 and 999,999")
    
    if num < 1000:
        return three_digit_number(num)
    
    thousands = num // 1000
    rest = num % 1000
    return three_digit_number(thousands) + ' thousand' + ('' if rest == 0 else ' ' + three_digit_number(rest))

def int_to_roman(num):
    """
    Converts an integer to a Roman numeral.

    Args:
        num (int): The integer to be converted. Must be between 1 and 3999.

    Returns:
        str: The Roman numeral representation of the input integer.

    Raises:
        ValueError: If the input is not an integer or if it is not within the valid range.

    Examples:
        >>> int_to_roman(9)
        'IX'
        >>> int_to_roman(2021)
        'MMXXI'
    """
    if not isinstance(num, int):
        raise ValueError("Invalid input: number must be an integer")
    if num <= 0 or num >= 4000:
        raise ValueError("Invalid input: number must be between 1 and 3999")

    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman = ''
    for i in range(len(val)):
        while num >= val[i]:
            roman += syb[i]
            num -= val[i]
    return roman

def roman_to_int(roman):
    """
    Converts a Roman numeral to an integer.

    Args:
        roman (str): The Roman numeral to be converted.

    Returns:
        int: The integer representation of the Roman numeral.

    Raises:
        ValueError: If the input Roman numeral is invalid.
    """
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in roman[::-1]:
        value = rom_val.get(char)
        if value is None:
            raise ValueError(f"Invalid Roman numeral: {roman}")
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total


def snake_to_camel(snake_str):
    """
    Convert a snake_case string to camelCase.

    Args:
        snake_str (str): The snake_case string to be converted.

    Returns:
        str: The camelCase string.

    Example:
        >>> snake_to_camel("hello_world")
        'helloWorld'
    """
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def camel_to_snake(camel_str):
    """
    Converts a camel case string to snake case.

    Args:
        camel_str (str): The camel case string to be converted.

    Returns:
        str: The snake case representation of the input string.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

def camel_to_pascal(camel_str):
    """
    Converts a camel case string to pascal case by capitalizing the first letter.

    Args:
        camel_str (str): The camel case string to convert.

    Returns:
        str: The pascal case string.

    Example:
        >>> camel_to_pascal("helloWorld")
        'HelloWorld'
    """
    return camel_str[0].upper() + camel_str[1:]

def seconds_to_text(seconds):
    """
    Converts the given number of seconds into a human-readable format.

    Args:
        seconds (int): The number of seconds to convert.

    Returns:
        str: A string representing the converted time in the format "hours hours, minutes minutes, seconds seconds".

    Raises:
        ValueError: If the input is not an integer.
    """
    if not isinstance(seconds, int):
        raise ValueError("Invalid input: seconds must be an integer")
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

def text_to_seconds(time_str):
    """
    Converts a string representation of time to seconds.

    Args:
        time_str (str): The string representation of time in the format "value unit".

    Returns:
        int: The total number of seconds.

    Raises:
        ValueError: If the time format is invalid.

    Example:
        >>> text_to_seconds("1 hour, 30 minutes, 45 seconds")
        5445
    """
    time_units = {'hours': 3600, 'minutes': 60, 'seconds': 1}
    total_seconds = 0
    for t in time_str.split(', '):
        if ' ' not in t:
            raise ValueError(f"Invalid time format: {time_str}")
        value, unit = t.split()
        if not value.isdigit():
            raise ValueError(f"Invalid time format: {time_str}")
        total_seconds += int(value) * time_units.get(unit)
    return total_seconds

def date_to_text(date_str):
    """
    Converts a date string in the format 'YYYY-MM-DD' to a text representation.

    Args:
        date_str (str): The date string to be converted.

    Returns:
        str: The text representation of the date in the format 'Month day, Year'.

    Raises:
        ValueError: If the date string is in an invalid format.

    Example:
        >>> date_to_text('2022-01-15')
        'January 15, 2022'
    """
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%B %d, %Y').replace(' 0', ' ').replace(',', '')
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}")

def text_to_date(text):
    """
    Converts a text representation of a date to a formatted date string.

    Args:
        text (str): The text representation of the date.

    Returns:
        str: The formatted date string in the format 'YYYY-MM-DD'.

    Raises:
        ValueError: If the text format is invalid.

    Example:
        >>> text_to_date('January 1 2022')
        '2022-01-01'
    """
    try:
        return datetime.strptime(text, '%B %d %Y').strftime('%Y-%m-%d')
    except ValueError:
        raise ValueError(f"Invalid text format: {text}")

def bytes_to_text(num_bytes):
    """
    Converts a number of bytes to a human-readable string representation.

    Args:
        num_bytes (int): The number of bytes to convert.

    Returns:
        str: The human-readable string representation of the number of bytes.

    Raises:
        ValueError: If the input `num_bytes` is not an integer or if it is too large.
    """
    if not isinstance(num_bytes, int):
        raise ValueError("Invalid input: num_bytes must be an integer")
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if num_bytes < 1024:
            return f"{num_bytes:.2f} {unit}"
        num_bytes /= 1024
    raise ValueError("Invalid input: num_bytes is too large")

def text_to_bytes(size_str):
    """
    Converts a string representation of a file size to bytes.

    Args:
        size_str (str): The string representation of the file size, e.g., "10 KB".

    Returns:
        int: The size in bytes.

    Raises:
        ValueError: If the size_str is not a valid size format.

    Example:
        >>> text_to_bytes("10 KB")
        10240
    """
    try:
        size, unit = size_str.split()
        if not size.replace('.', '').isdigit():
            raise ValueError(f"Invalid size format: {size_str}")
        size = float(size)
        if size < 0:
            raise ValueError(f"Invalid size format: {size_str}")
        size_units = {'B': 1, 'KB': 1024, 'MB': 1024**2, 'GB': 1024**3, 'TB': 1024**4}
        return int(size * size_units[unit])
    except ValueError:
        raise ValueError(f"Invalid size format: {size_str}")

def int_to_ordinal(n):
    """
    Converts an integer to its ordinal representation.

    Args:
        n (int): The integer to be converted.

    Returns:
        str: The ordinal representation of the input integer.

    Raises:
        ValueError: If the input is not an integer.

    Examples:
        >>> int_to_ordinal(1)
        '1st'
        >>> int_to_ordinal(2)
        '2nd'
        >>> int_to_ordinal(3)
        '3rd'
        >>> int_to_ordinal(4)
        '4th'
        >>> int_to_ordinal(11)
        '11th'
        >>> int_to_ordinal(21)
        '21st'
    """
    if not isinstance(n, int):
        raise ValueError("Invalid input: n must be an integer")
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)] if n % 100 not in {11, 12, 13} else 'th'
    return str(n) + suffix

def ordinal_to_int(ordinal):
    """
    Converts an ordinal string to an integer.

    Args:
        ordinal (str): The ordinal string to be converted.

    Returns:
        int: The corresponding integer value of the ordinal.

    Raises:
        ValueError: If the ordinal format is invalid.
    """
    try:
        return int(''.join([c for c in ordinal if c.isdigit()]))
    except ValueError:
        raise ValueError(f"Invalid ordinal format: {ordinal}")

def snake_to_camel(snake_str):
    """
    Converts a snake_case string to camelCase.

    Args:
        snake_str (str): The snake_case string to convert.

    Returns:
        str: The camelCase string.

    Example:
        >>> snake_to_camel('hello_world')
        'helloWorld'
    """
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def camel_to_snake(camel_str):
    """
    Converts a camel case string to snake case.

    Args:
        camel_str (str): The camel case string to convert.

    Returns:
        str: The snake case version of the input string.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

def camel_to_pascal(camel_str):
    """
    Converts a camelCase string to PascalCase by capitalizing the first letter.

    Args:
        camel_str (str): The camelCase string to be converted.

    Returns:
        str: The PascalCase string.

    Example:
        >>> camel_to_pascal("helloWorld")
        'HelloWorld'
    """
    return camel_str[0].upper() + camel_str[1:]

def seconds_to_text(seconds):
    """
    Converts the given number of seconds into a human-readable format.

    Args:
        seconds (int): The number of seconds to convert.

    Returns:
        str: A string representing the converted time in the format "hours hours, minutes minutes, seconds seconds".

    Raises:
        ValueError: If the input is not an integer.

    Example:
        >>> seconds_to_text(3665)
        '1 hours, 1 minutes, 5 seconds'
    """
    if not isinstance(seconds, int):
        raise ValueError("Invalid input: seconds must be an integer")
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

def text_to_seconds(time_str):
    """
    Converts a string representation of time to seconds.

    Args:
        time_str (str): The time string to be converted. The format should be "<value> <unit>, <value> <unit>, ...".

    Returns:
        int: The total number of seconds.

    Raises:
        ValueError: If the time string is in an invalid format.

    Example:
        >>> text_to_seconds("1 hour, 30 minutes, 45 seconds")
        5445
    """
    time_units = {'hours': 3600, 'minutes': 60, 'seconds': 1}
    try:
        return sum(int(t.split()[0]) * time_units[t.split()[1]] for t in time_str.split(', '))
    except (ValueError, KeyError):
        raise ValueError(f"Invalid time format: {time_str}")


