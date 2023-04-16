import sys

run = True

while run:
    try:
        numberofCandy = int(input("Hay nhap so keo cua bac: "))
        numberofStudent = int(input("Hay nhap so hoc sinh: "))
        numberofCandyPerStudent = int(numberofCandy/numberofStudent)
        numberofCandyleft = numberofCandy% numberofStudent
        print("So keo moi hoc sinh nhan duoc: ",numberofCandyPerStudent)
        print("So keo thua: ",numberofCandyleft)
    except ZeroDivisionError:
        print("Co loi exception", sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
        print("Ban da import sys nhap so hoc sinh bang 0 nen chuong trinh khong thuc hien duoc: ")
    except ValueError:
        print("Co loi exception",sys.exc_info()[0],sys.exc_info()[1],sys.exc_info()[2])
        print("Ban can nhap so")
    option = input("Bam 'c' de tieo tuc , bam 'k' de dung:")
    run = True if option == 'c' else False
    
print("chuong trinh ket thuc")