score=input("分數?")
if not(score>-1 and <101):
    score=input("分數?")
score=int(score)
if(score>=60):
    print("及格")
else:
    print("不及格")
    if(score<101 and score>=90):
    print("A")
    
    if(score<90 and score>=80):
    print("B")
    
    if(score<80 and score>=70):
    print("C")
    
    if(score<70 and score>=60):
    print("D")