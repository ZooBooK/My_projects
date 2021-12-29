""" Банковский счёт, реализация внесения, снятия и проверки баланса."""

# Создаем экземпляр класса
class Account():

    def __init__(self, owner, balance):

        #Создание атрибутов
        self.owner = owner
        self.balance = balance

    """ Функция для выбора 'w'- снятия, 'd' - депозита, 'b' - Проверка баланса """
    def dep_or_with(self):
        inp = input('Выберите действие d - внести наличные / w - снять наличные / b - проверить баланс:')
        print(f'Вы выбрали: {inp}')
        return inp

    """ Функция для расчета депозита """
    def make_deposit(self):
        inp_sum = int(input('Введите сумму депозита: '))
        result_dep = self.balance + inp_sum
        return result_dep

    """ Функция для расчета снятия средств """
    def make_withdrawal(self):
        inp_sum = int(input('Введите сумму снятия: '))
        print(f'Сумма снятия: {inp_sum}')
        result = self.balance - inp_sum
        return result

    """ Функция проверки баланса """
    def check_balance(self):
        print(f'Ваш баланс: ', self.balance)

my_account = Account(owner = 'Влад', balance = 100)

print(f'Владелец банковского счета: ', my_account.owner)

# Вызов функции выбора снятия/депозита/проверки баланса
result_inp = my_account.dep_or_with()

# Вызов функции снятия средств и вывод баланса / Вывод ошибки о превышения лимита снятия
if result_inp == 'w':
    withdrawal = my_account.make_withdrawal()
    if withdrawal > 0:
        print(f'Остаток на балансе: ', withdrawal)
    else:
        print('Сумма снятия превышает допустимый баланс')

# вызов функции проверки баланса
if result_inp == 'b':
    my_account.check_balance()

# Вызов функции депозита и вывод баланса
else:
    deposit = my_account.make_deposit()
    print(f'Ваш баланс после зачисления: ', deposit)