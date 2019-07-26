number_list=[1, 2, -8, -2, 0]
if number_list!=[]:
    number_list.sort()
    if len(number_list)==1:
        print("There is no second element in list")
    else:
        if(number_list[0]==number_list[1]):
            print("There is no second element in list")
        else:
            print("Second samllest in list  :",number_list[1])