number_list=[1, 2, -8, -2, 0]
if number_list!=[]:
    if len(number_list)==1:
        print("There is no second element in list")
    else:
        number_list.sort()
        if number_list[0]<number_list[1]:
            print("Second samllest in list  :",number_list[1])
        else:                     
            second_smallest=smallest=number_list[0]
            for index in range(1,len(number_list)):
                if(number_list[index]>smallest):
                    second_smallest=number_list[index]
            if(second_smallest==smallest):
                print("There is no second element in list") 
            else:
                print("Second samllest in list  :",second_smallest)   