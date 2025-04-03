import random
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-='
def gen_pass(lenght):
    password = ''
    for i in range(lenght):
        password += random.choice(characters)
    return password