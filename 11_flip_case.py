def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    #s.replace(t,u,count) 	Replace count (default: all) occurrences of t in s with u

    #iterate through string

    result = ''
    for letter in phrase:
        if letter.lower() == to_swap.lower():
            if letter.islower():
                result += letter.upper()
            else:
                result += letter.lower()
        else:
            result += letter
    return result
