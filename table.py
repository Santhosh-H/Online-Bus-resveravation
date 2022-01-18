#Giving a nice Menu Driven Program
def tableprinting(heading,subheadings,gap=1):
    
    print("\t\t\t__________________________________________________________________________")
    print()
    print("\t\t\t|"," "*70,"|")
    print("\t\t\t|"," "*31,heading," "*(37-len(heading)),"|")
    print("\t\t\t|"," "*70,"|")
    print("\t\t\t__________________________________________________________________________")
    print()
    print("\t\t\t|"," "*70,"|")
    print("\t\t\t|"," "*70,"|")
    
    num = 0
    for s in subheadings :
        print("\t\t\t|"," "*26,"",num+1," FOR ",s," "*(33-len(s)),"|")
        for k in range(gap):
            print("\t\t\t|"," "*70,"|")
        num = num+1
    print("\t\t\t|"," "*70,"|")
    print("\t\t\t__________________________________________________________________________")
    print("\t\t\t")
        
    