from hashlib import pbkdf2_hmac
import os
from secrets import token_hex


our_app_iters = 500_000 
salt = os.urandom(16)
def pbk(password):
    pbk = pbkdf2_hmac('sha256', bytes(password, 'utf-8'), bytes(salt)*2, our_app_iters)
    key = pbk.hex()
    return key


print(pbk('password'))

#info on pbk and hashing can be found here: https://docs.python.org/3.10/library/hashlib.html?highlight=pbkd#hashlib.pbkdf2_hmac
