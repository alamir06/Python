# list is 
'''
 is a datatype in python
 is a mutable datatype 
 is a sequence datatype
 can concatenate +
 can repear with *
 can access by index
 genrally like array but store different datatype.
'''
# list=[1,2,3,4,5,"alamirw",True]
# print(list)
# for i in list:
#     print(i)
# print(list[6]) #true
'''
 list1=[1,2,3]
 list2=[4,5,6]
 concat=list1+list2
 concat=list1 * 3
 check=list1 in list
 print(check)'''


# The most list method 
general_list=[1,2,3,4,5,6,7,8,9]
'''
1. append(): add element at end of the list like push at array
Syntax:list.append(element)
general_list.append(10)
print(general_list)
'''
'''
2. remove(): remove element at first occurance of the list
Syntax:list.remove(element)
general_list.remove(3)
print(general_list)
'''
'''
3. clear(): remove all element from the list
Syntax:list.clear()
general_list.clear()
print(general_list)
'''

'''
4.copy(): copy the existing list and keep it without affect even if the originl list change
Syntax:list.copy()
copy_list=general_list.copy()
print(copy_list)
general_list.clear()
print(general_list)
'''
'''
5. count(): get the number of specific value in the list
Syntax:list.count(element)
print(general_list.count(3))
'''
"""
6. len(): get the total occurance in the list
Syntax:len(list)
print(len(general_list))
"""
'''
7. index(): get the index of the specific element in the list
Syntax:list.index(element)
print(general_list.index(5))
'''
'''
8. insert(): add element to the list at psecific position
Syntax:list.insert(element)
general_list.insert(0,0)
general_list.insert(10,10)
print(general_list)
'''
'''
9. pop(): remove and get specific value at list
Syntax:list.pop(index)
n=general_list.pop(4)
print(n)
'''
'''
10. max():to get the maximum value at list
Syntax:max(list)
n=max(general_list)
print(n)
'''
'''
11. min():to get the minimum value at list
Syntax:min(list)
n=min(general_list)
print(n)
'''
'''
12.reverse(): get the reverse order of the list
print(general_list.reverse()) // not clear
'''
'''
13. extend(): add or extend another value in list
Syntax:list.extend(list)
list1=[12,13,14]
general_list.extend(list1)
print(general_list)
'''
'''
14. sort():arrange the list in ascending or descending order
Syntax:sorted(list)
    :sorted(list,reverse=True)
n = sorted(general_list)
n = sorted(general_list, reverse=True)
print(n)
'''
'''
15.slicing(): get the specific list value besed in spec.
Syntax:list.slice(start:end:step)
n=general_list[3:6:1]
print(n)
'''
# 16.list(): add another list to a given list
# list2=[16,17,18]
# print(n)
'''
 17. in: membership of the list
 Syntax:element in list
print(7 in general_list)
print(20 in general_list)
'''
'''
 18. iteration: list can be iterate by for loop
 Syntax:for i in list:
for i in general_list:
    print(f"value of index {i}=",i)
'''
