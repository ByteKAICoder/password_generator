def main()-> None:
   '''Основная логика запуска скрипта.'''
   print('============= ГЕНЕРАТОР ПАРОЛЕЙ =============')
   print('--------------------------------------')

   while True:
       print('Выставите настройки генерации:')
       lower_case = user_input('- наличие нижнего регистра ("+"/"-"): ',
                                    values=("+", "-")
                               )
       upper_case = user_input('- наличие верхнего регистра ("+"/"-"): ',
                                    values=("+", "-")
                               )
       special_symbols = user_input('- наличие специальных символов ("+"/"-"): ',
                                         values=("+", "-")
                                    )
       numbers = user_input('- наличие цифр ("+"/"-"): ',  values=("+", "-"))
       config = (lower_case, upper_case, special_symbols, numbers)
       if config == ('-', '-', '-', '-'):
           print('Пароль из нуля символов не возможно создать. '
                 'Сброс настроек...'
                 )
           print('--------------------------------------')
           continue
       min_length = sum(1 for value in config
                        if value == '+'
                        )
       max_length = sum((26, 26, 32, 10)[index] for index in range(len(config))
                        if config[index] == '+'
                        )
       length = user_input('- желаемая длинна пароля'
                           f'(число от {min_length} до {max_length}): ',
                           'int', (min_length, max_length)
                           )
       print('Сохранение настроек генерации...')

       password = password_generator(lower_case,
                                     upper_case,
                                     special_symbols,
                                     numbers,
                                     length
                                     )
       print('--------------------------------------')
       print(f'Ваш уникальный пароль: {password}')
       
       break


if __name__ == '__main__':
   main()
