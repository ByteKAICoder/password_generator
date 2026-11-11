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


def user_input(text:str='',
              some_type:str='str',
              values:tuple=()
              )-> str|int:
   '''Обрабатывает пользвательский ввод.'''
   if some_type == 'str':
       while True:
           some_param = input(text)
           if not some_param:
               print('Пустой ввод! Попробуйте снова.')
               continue
           if values and some_param not in values:
               print('Неверный ввод! Попробуйте снова.')
               continue
           break

   elif some_type == 'int':
       while True:
           try:
               some_param = int(input(text))
               if values and not(min(values) <= some_param <= max(values)):
                   print('Число не соответствует требованиям.\n'
                         'Попробуйте снова.'
                         )
                   continue
               break
           except ValueError:
               print('Введённый параметр не является числом.\n'
                     'Попробуйте снова.'
                     )

   return some_param
