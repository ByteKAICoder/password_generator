import secrets
from string import ascii_lowercase, ascii_uppercase, punctuation, digits


def password_generator(lower_case:str,
                      upper_case:str,
                      special_symbols:str,
                      numbers:str,
                      length:int
                      )-> str:
   '''Генерирует пароль по выставленным настройкам.'''
   lower_letters = ascii_lowercase if lower_case == '+' else ''
   upper_letters = ascii_uppercase if upper_case == '+' else ''
   specials = punctuation if special_symbols == '+' else ''
   integers = digits if numbers == '+' else ''

   password = []
   all_symbols = ''
   for symbols in (lower_letters, upper_letters, specials, integers):
       if symbols:
           password.append(secrets.choice(symbols))
           all_symbols += symbols
   length = length - len(password)
   password += [secrets.choice(all_symbols) for _ in range(length)]
   secrets.SystemRandom().shuffle(password)

   return ''.join(password)
