import random
import string

def random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    email = f'{username}@mail.com'
    return email

