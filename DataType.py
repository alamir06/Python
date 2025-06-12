# meas the type of data that we use in programming language

# 1. mutable and immutabel data type
# mutable means modify or change the datatype once declare e.g list,dectionary...
# immutable means we can not change once we define e.g int ,touple,string,float...

# to declare list must use square bracket
list=[1,2,3,4,5,6,7,8] 
# value is accessed by index of the items 
# index is start at 0 and end at n-1 where n is number of items in list
# print(list)  #[1, 2, 3, 4, 5, 6, 7, 8]
# print(list[0]) #1
# print(list[1]) #2
# print(list[2]) #3
# ...
# print(list[7]) #8

list[2]=34
# print(list[2]) #34 not 2 that is what we say list datatype is mutable . 
# the differnce between list and array is that list can store diffrent data type value
#  but array store same data type  value
# e.g. 

list=[1,"alamure",2,'A',True]
# print(list)#[1, 'alamure', 2, 'A', True]
array=[1,2,3,4,5]# in another programming language


# touple is one of immutable data type
# e.g
touple=(1,2,3,4,5,6,7)
# touple[2]=6
# print(touple[2])


# sequence ns non sequence datatype
# sequence datatype is a datatype that each item is well organized and have thier own index to access.e.g: list,touple...
# non sequence datatype is  a datatype that is not organized well and can not access it's value by index. e.g.set,dectionary...
# e.g 
lists=[2,1,2,3,4,5,6,7,4,56]
# on this each item has it own index to access from 0 to n-1 where n number of item.
# print(lists[0])#2
# print(lists[1])#1
# print(lists[2])#.
# print(lists[3])#>
# print(lists[4])#.
# print(lists[5])#.
# print(lists[6])

touple=(1,2,3,5,5)
# also those have similar with above index until n-1
# so list nd touple has thier own organized data and each item is acceessed by index we called sequence 

# non sequence
set={1,2,3,4,5,6}
# print(set)
# set is....
# dictionary is key and value pair
dict={"id":"iunsr/0068/23","name":"alamirew wagaw","age":23}
print(dict)
print(dict["name"])
# set is used to store multiple value which is unordered ,unindexed and non duplicate data item.