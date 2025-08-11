def listMutation(first_list):
    mutate_list=[]
    for i in first_list:
        new_item=i*2
    mutate_list.append(new_item)
    print(mutate_list)

listMutation([1, 2, 3, 4, 5])