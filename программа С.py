a = int(input("Пожалуйста, введите количество элементов "))
b = []
c = 0
for i in range(1,a+1):
    print("Пожалуйста, введите ",i,"элемент")
    c = int(input())
    b.append(int(c))
for i in b:
    if i%2==1:
        print('Нечетные элементы',i)
    
    
    
    
