"""
This module contains the sample functions
"""
from datetime import date

print("Beginning of a new file")


def greet_me_with_date(name):
    """Greets user with current date

    The name of user is provided as parameter and date is taken from python
    standard date module

    Parameters
    ----------
    name : str
        Name provided by the user

    Returns
    -------
    str
        A greeting message that combines the user's name with current date

    """
    final_str = f"Hi {name}! Today's date is {date.today()}"
    return final_str


print(greet_me_with_date("John Doe"))
