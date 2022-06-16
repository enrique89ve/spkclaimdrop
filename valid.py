import random
import re
import string
from beem import Hive
from beem.account import Account
from beem.exceptions import AccountDoesNotExistsException
from beem.exceptions import AccountDoesNotExistsException
from pprint import pprint



def username_is_valid(username):
    # regex pattern is found at
    # https://steemit.com/programming/@cryptosharon/the-5-rules-of-a-valid-username-on-the-steem-blockchain-and-a-3-sbd-contest-to-make-an-account-name-validation-regex#@cryptosharon/re-eonwarped-re-cryptosharon-re-eonwarped-re-cryptosharon-re-eonwarped-re-cryptosharon-re-artopium-re-cryptosharon-the-5-rules-of-a-valid-username-on-the-steem-blockchain-and-a-3-sbd-contest-to-make-an-account-name-validation-regex-20180313t214044982z
    return bool(re.search('^[a-z](-[a-z0-9](-[a-z0-9])*)?(-[a-z0-9]|[a-z0-9])'
                          '*(?:\.[a-z](-[a-z0-9](-[a-z0-9])*)?(-[a-z0-9]|'
                          '[a-z0-9])*)*$', username))



def username_ready(username):

    user = username
    
    try:
        acc = Account(user)
    except TypeError as err:
        print(err)
        return -1
    except AccountDoesNotExistsException:
        print("account does not exist")
        return-1


