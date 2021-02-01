score=int(input("please enter your grade  range in 0~100"))
if(score<0 or score > 100):
    print("請輸入介於0~100")
elif(score>=90 and score <=100):
    print("A")
elif(score>=80 and score <=89):
    print("B")
elif(score>=70 and score <=79):
    print("C")
elif(score>=60 and score <=69):
    print("D")
else:
     print("E")