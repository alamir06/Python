# nested or nesting means a matter of putting one data structure  in another 

#nested list in dictionary
dictionarys={
    "key":"value",
    "key1":["value","value1","value2","value3333333"],
    "key2":{
        "key":"value",
        "key1":"value2",
        "key":["put1","put2","put3"]
        }
}
# so te get value3333333
value3=dictionarys["key1"][3]
# print(value3)
# so te get put3
put3=dictionarys["key2"]["key"][2]
# print(put3)

# nesting dictinar in list
lists=[
    "value1",
    {
        "key":"value",
        "key1":"value1",
        "key2":"value2",
        "key3":["key3value","key3value1","key3value2",
                {
                    "key3value2":"key3value",
                    "key3value":"key3value",
                    "keyn":"nested"
                }
                ],
        "key4":{
            "key3value1":"ggggg",
            "key3value":"ffff"
        }
    },
    {
        "key3value":"key3value",
        "key3value1":"yyyyyyy"
    }
]
# to get the yyyyyyy
yyy=lists[2]["key3value1"]
print(yyy)
# to get the nested
keyn=lists[1]["key3"][3]["keyn"]
print(keyn)