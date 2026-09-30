#weather a student can sit in examination 
a=int(input("Your current attendence percentage: "))
ReqAtt= 75

if(101>a>=ReqAtt):
    print("Your are eligible for giving exam")

elif(50<a<=75):
    if(50<a<=60):
        print("have to bring medical certificate")
        print("1500/- fine will be charged")
    else:
        print("submit your medical certificate")
elif(100<a):
    print("Invalid entry")

else:
    print("You are not eligible")
