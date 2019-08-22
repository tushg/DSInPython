#
#
#
# Dict = [
#           ('11013331', 'KAT'),
#           ('9085267',  'NOT'),
#           ('5238761',  'ETH'),
#           ('5349618',  'ETH'),
#           ('11788544', 'NOT'),
#           ('962142',   'ETH'),
#           ('7795297',  'ETH'),
#           ('7341464',  'ETH'),
#           ('9843236',  'KAT'),
#           ('5594916',  'ETH'),
#           ('1550003',  'ETH')
#         ]
#
# print('Print Dictionary')
# print(Dict)
#
# from collections import OrderedDict
#
# result = OrderedDict()
#
# for v , k in Dict:
#     if k in result : result[k].append(v)
#     else : result[k] = [v]
# print(result)

# Open the file for read mode

fileName = "i:/Orders.txt"

from collections import OrderedDict
result = OrderedDict()

with open(fileName) as fileHandle:
    for line in fileHandle:
        key, value = line.split(",")
        if key in result : result[key].append(value.strip("\n"))
        else: result[key] = [value.strip("\n")]

print('Print dictionary.....')
print(result)
result = result.items();
print(result)
#
# print('Doing the group by city')
# from collections import OrderedDict
#
# orderDict = OrderedDict()
#
# for k , v in result:
#     if k in orderDict : orderDict[k].append(v)
#     else : orderDict[k] = [v]
#
#
# print('----------------GroupBy city list-------------------')
# print(orderDict)
