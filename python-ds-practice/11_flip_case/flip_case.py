from curses.ascii import islower, isupper
from tkinter.messagebox import RETRY


def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    string = ""

    for item in phrase:
        if to_swap.lower() == item.lower():
            string += item.swapcase()
        else:
            string += item

    return string 
