#День и год рождения Пушкина А.С.

def born_pushkin (queston, date):
    answere = input(queston)
    while answere != date:
        print('Неверно')
        answere = input(queston)

born_pushkin ('В каком году родился А.С.Пушкин ?', '1799')
born_pushkin ('Когда у А.С.Пушкина день рождения ?', '06.06')
print("Верно")


