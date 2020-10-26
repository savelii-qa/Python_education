#def luckyTickets(num):
 #   if num % 2 != 0 or num <= 0: return '# Error: invalid number'
  #  array = [1] * 10 + [0] * (num // 2 * 9 - 9)
 #   for i in range(num // 2 - 1):
 #       array = [sum(array[x::-1]) if x < 10 else sum(array[x:x - 10:-1]) for x in range(len(array))]
 #   return sum([x ** 2 for x in array])

#print(luckyTickets(6))



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

