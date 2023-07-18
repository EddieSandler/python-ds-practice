def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    result = phrase.split(,)
    for letter in phrase:

        if letter != "h" or "H"
            

        elif letter != letter.upper():
            result += (letter.lower())

        else:
            result += (letter)
    return result