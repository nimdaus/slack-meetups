import re

# http://code.activestate.com/recipes/303060-group-a-list-into-sequential-n-tuples/
def group(lst, n):
    """group a list into consecutive n-tuples
    
    >>> group(range(10), 3)
    [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    
    >>> group([0, 3, 4, 10, 2, 3], 2)
    [(0, 3), (4, 10), (2, 3)]
    """
    if (len(lst) % n != 0):
        raise ValueError(f"Provided list of length {len(lst)} is not "
            f"divisible by {n}")
    return zip(*[lst[i::n] for i in range(n)]) 

def get_person_from_match(user_id, match):
    """given a Match, return the Person corresponding to the passed user ID
    """
    if match.person_1.user_id == user_id:
        return match.person_1
    elif match.person_2.user_id == user_id:
        return match.person_2
    else:
        raise Exception(f"Person with user ID \"{user_id}\" is not part of "
            f"the passed match ({match}).")

def get_other_person_from_match(user_id, match):
    """given a Match, return the Person corresponding to the user who is NOT
    the passed user ID (i.e. the other Person)
    """
    if match.person_1.user_id == user_id:
        return match.person_2
    elif match.person_2.user_id == user_id:
        return match.person_1
    else:
        raise Exception(f"Person with user ID \"{user_id}\" is not part of "
            f"the passed match ({match}).")

def determine_yes_no_answer(message):
    """Given a message string from a user, determine if they are responding in
    the affirmative (True), or in the negative (False). Raises a ValueError if
    unable to determine.
    """
    yes_words = ["yes", "y", "yeah", "yea", "yep", "yus", "yas"]
    no_words = ["no", "n", "nope", "nah"]
    yes_response = False
    no_response = False
    # lowercase all characters in the string
    message = message.lower()
    # replace non-word characters with spaces
    message = re.sub(r"\W", " ", message)
    # remove leading and trailing whitespace
    message = message.strip()
    # loop through the message, removing duplicate spaces between words
    for word in message.split():
        if word in yes_words:
            yes_response = True
        if word in no_words:
            no_response = True
    if yes_response == no_response:
        # if the responses were equal, we either didn't match any "yes" or
        # "no" words, or we matched both so we can't determine what the user
        # user meant
        raise ValueError("Unable to determine response from message")
    else:
        return yes_response
