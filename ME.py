SCORE_E=int(input("英文成績?"))
if(SCORE_E<0 or SCORE_E > 100):
    print("請輸入介於0~100")
SCORE_M=int(input("數學成績?"))
if(SCORE_M<0 or SCORE_M > 100):
    print("請輸入介於0~100")
elif(SCORE_E>=90 and SCORE_M>=90):
    print("有獎勵")
else:
    print("有懲罰")