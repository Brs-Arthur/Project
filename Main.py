from Rectangle import Rectangle

running = True
result = 'NON'
while running:
    list1 = []
    list2 = []
    try:
        loop = int(input("Veuillez rentrer le nombre de pair necessaire"))
        for i in range(loop):
            for a in range(8):
                if a < 4:
                    list1.append(int(input("Veuillez rentrer pour le premier rectangle le nombre numéro {}".format(a + 1))))
                else:
                    list2.append(int(input("Veuillez rentrer pour le second rectangle le nombre numéro {}".format(a - 3))))
                if a == 3:
                    rect1 = Rectangle(list1[0], list1[1], list1[2], list1[3])
                    rect1.addCoor()
                if a == 7:
                    rect2 = Rectangle(list2[0], list2[1], list2[2], list2[3])
                    rect2.addCoor()
            running = False
            for coor in rect1.listCoor:
                if coor in rect2.listCoor:
                    result = "OUI"
            print(result)
    except:
        break