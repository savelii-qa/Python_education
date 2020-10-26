start = 0     # первое значение
finish = 999999    # последнее значение
cnt = 0  # счетчик
for i in range(start, finish+1):
    i_str = str(i)
    while len(i_str) < 6:
        i_str = '0' + i_str    # добавляем строкой 0 если значение не 6 значное
    i = list(i_str)
    first = i[0:3]   #  делаем срез первых трех значений
    last = i[3:]   #  срез последних трех значений
    if sum(map(int, first)) == sum(map(int, last)):    #  если сумма первых трех равна последним трем
        cnt += 1                                       #   тогда добавляем в счетчик +1
print(cnt)

