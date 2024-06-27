#make a calender:
def day_of_date(S):
    Month_od=[0,0,3,3,6,8,11,13,16,19,21,24,26]
    Days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    X=int(S[0:2])
    Z=int(S[3:5])
    Y=int(S[6:10])
    if Z>12 and X>Days[Z]:
        if 0<Z<=12 and X<=Days[Z]:
            day=X
        if Y>400:
            A=Y%400
        else:
            A=Y
        if A>=300:
            day=day+1
            B=A-300-1
        elif A>=200:
            day=day+3
            B=A-200-1
        elif A>=100:
            day=day+5
            B=A-100-1
        else:
            day=day
            B=A-1
        C=B//4
        D=B-C
        day=day+(C*2)+(D*1)
        w=Y%100
        if (w%4)!=0:
            day=day+Month_od[Z]
        else:
            day=day+Month_od[Z]+1
        day=day%7
        ans=['Sunday','Monday','Tuesday','wednesday','Thursday','Friday','Saturday']
        print(S,"is",ans[day])                
    elif (Y%100)%4==0:
        if X<=29 and Z==2:
            day=X
        if Y>400:
            A=Y%400
        else:
            A=Y
        if A>=300:
            day=day+1
            B=A-300-1
        elif A>=200:
            day=day+3
            B=A-200-1
        elif A>=100:
            day=day+5
            B=A-100-1
        else:
            day=day
            B=A-1
        C=B//4
        D=B-C
        day=day+(C*2)+(D*1)
        w=Y%100
        if (w%4)!=0:
            day=day+Month_od[Z]
        else:
            day=day+Month_od[Z]
        day=day%7
        ans=['Sunday','Monday','Tuesday','wednesday','Thursday','Friday','Saturday']
        print(S,"is",ans[day])    
    else:
        print("The Date or Month entered are not acceptable")
S=input("Enter the date,Month,Year(DD-MM-YYYY): ")
day_of_date(S)
