from random import randint


for i in range(1,11):
    num1=randint(1,10)
    num2=randint(1,10)
    print(f" ques {i}-->  {num1}X{num2}")
    a=int(input("Enter answer of ques 1: "))
    if a == num1*num2 :
        print("Right !")
    else:
        print(f"Wrong , answer is {num1*num2}")