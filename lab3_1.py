def findergoods(mylist, item):
    return mylist.index(item)
try:
    answer = findergoods([1,2,'ром',2,3,4,5,6,3],'ром')
    print('Индекс вхождения элемента:', answer)
except ValueError:
    print('none')
