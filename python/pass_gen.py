# simple password generator

import random
import string

def gen_pass(l=8):
  all_char = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(all_char) for i in range(l))
  return password

pass_len_str = input('input the length:')
if pass_len_str:
  pass_len = int(pass_len_str)
else:
  pass_len = 8

password = gen_pass(pass_len)
print(f"Generated password is {password}")

