print("EMPLOYEE MANAGMENT")
emp,sal,ocu,id=[],[],[],[]
a=5
q=0
while True:
    try:
        a=int(input("please choose what you would like to do from below\n1)see the list\n2)add to the list\n3)delet from the list\n4)search from the list\n : "))
        while a>4 or a<1:
            if a>4 or a<1:
                print("please choose only from 1 to 4")
                a=int(input("1)see the list\n2)add to the list\n3)delet from the list\n4)search from the list\n : "))
                break  
        if a==1:
            if len(emp)==0:
                print("the list is empty!")
                m=input("press enter to continue")
            else:
                print("HERE:")
                print("{:>16}{:>16}{:>16}{:>16}\n-----------------------------------------------------------------------".format("NAME","SALLARY","OCCUPATION","ID"))
                while q!=len(emp):
                    print("{:>16}{:>16}{:>16}{:>16}\n-----------------------------------------------------------------------".format(emp[q],sal[q],ocu[q],id[q]))
                    q+=1
                q=0
                g=input("press enter to continue")
        if a==2:
            print("ok lets add eployees")
            f=int(input("how many would you like to add : "))
            for j in range(f):
                print("employee ",j+1)
                b,c,d,e=input("name : ").capitalize(),int(input("salary : ")),input("occupation : ").capitalize(),str(input("id : "))
                emp.append(b)
                sal.append(c)
                ocu.append(d)
                id.append(e)
                print("employee added")
            print("############\nDONE\n############")
        if a==3:
            print("ooo sombody is getting fired\nDAMN!!!!")
            h=input("enter the name of the employee you want to delete : ").capitalize()
            if h in emp:
                k=emp.index(h)
                emp.remove(emp[k])
                sal.remove(sal[k])
                ocu.remove(ocu[k])
                id.remove(id[k])
                print("#####DONE#####")
            else:
                print("employee not found !!!")
            l=input("press enter to continue") 
        if a==4:
            n=input("search here : ").capitalize()
            if n in emp :
                o=emp.index(n)
                print("{:>16}{:>16}{:>16}{:>16}\n-----------------------------------------------------------------------".format("NAME","SALLARY","OCCUPATION","ID"))
                print("{:>16}{:>16}{:>16}{:>16}".format(emp[o],sal[o],ocu[o],id[o]))
            else:
                print("name doesnt exist!!")
                p=input("press enter to continue") 
    except Exception:
        print("something went wrong please try again")