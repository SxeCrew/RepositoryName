def find_common_participants(list1, list2):
    team1 = list1.split(',')
    team2 = list2.split(',')
    team1.sort()
    team2.sort()
    return [element for element in team1 if element in team2]

list10 = ('Шеремет,Петров,Иванов')
list11 = ('Шереметов,Петров,Иванов')
print(find_common_participants(list10, list11))