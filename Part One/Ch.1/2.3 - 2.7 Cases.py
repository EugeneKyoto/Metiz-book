# 2.3 Личное сообщение.
name = 'Eugene'
lan = 'Python'
print(f'Hello {name}, would you like to learn some {lan} today?\n')

# 2.4 Регистр символов в именах.
us_1 = 'eugene'
lan_1 = 'python'
country_1 = 'russia'
print(f'Сегодня продолжаю изучать {lan_1.lower()}.\nЯ {us_1.upper()} из {country_1.capitalize()}!\n')

# 2.5 Знаменитая цитата.
print('''Albert Einstein once said, "A person who never made
a mistake never tried anything new.\n"''') # Multiline text

# 2.6 Знаменитая цитата 2.
famous_person = 'Albert Einstein'
message = '"A person who never made a mistake never tried anything new."'
print(f'{famous_person} once said, {message}')

#2.7 Удаление пропусков.
name_us0 = '                   Gvido              '
print(f'Hi, {name_us0.lstrip()}!')
print(f'Hi, {name_us0.rstrip()}!')
print(f'Hi, {name_us0.strip()}!')