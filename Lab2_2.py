EstimateCapital = 0
salary = 30000
spend = 35000
increase = 1.03
count = 0
# после первого месяца счетчик =1, после 10 станет =10

while count < 10:
    EstimateCapital = EstimateCapital + salary - spend
    spend = spend * increase
    count += 1

print("Минимальная подушка состоявляет :", round(-EstimateCapital, 2), "рублей")