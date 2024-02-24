import datetime
tod = datetime.date.today()
yes = datetime.date.today() - datetime.timedelta(days=1)
tom = datetime.date.today() + datetime.timedelta(days=1)
print(f'Today is {tod}')
print(f'Yesterday is {yes}')
print(f'Tomorrow is {tom}')
