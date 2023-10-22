
money_capital = 100000
salary = 30000
spend = 35000
increase = 1.05
count = 0
budget = money_capital + salary

while budget >= spend:
    budget = budget + salary - spend
    if budget < 0:
        break
    spend = spend * increase
    count += 1

print("Мы сможем прожить на финансовой подушке:", count, "месяцев")