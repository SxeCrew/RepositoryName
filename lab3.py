#Names = ["Сережа", "Игорь","Петя", "Денис", "Виталик"]
Names = ["Сережа", "Игорь", "Денис", "Виталик"]
a= len(Names)
if (a % 2 == 0):

    step_slice1 = Names[::2]
    step_slice2 = Names[1::2]
    print("Все Игроки=",Names)
    print("Количество ребят = ",a)
    print("Команда 1=",step_slice1)
    print("Команда 2=",step_slice2)
else:
    print("Неполучится разделить ребят на равные команды")