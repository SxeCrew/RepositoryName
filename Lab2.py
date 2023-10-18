symbolweight = 4
symbolInString = 25
stringOnPage = 50
pagesInBook = 100
FlashSize = 1509949.44 

BookSize = symbolweight*symbolInString*stringOnPage*pagesInBook

result = round(FlashSize/BookSize,0)
print("Количество книг, помещающихся на флешке = ",result)

