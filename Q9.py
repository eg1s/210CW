list123 = [1, 2, 9, 19, 25, 36, 53]
lownumber= int(input('Enter LOW value\n'))
highnumber = int(input('Enter HIGH value\n'))

def binary(list123, lownumber, highnumber,):
    lenght = len(list123)                     
    midpoint = round(lenght / 2)            
    if lenght == 0:
        return False
    if lenght == 1 and list123[midpoint] != (lownumber or highnumber):
        return False
    if list123[midpoint] >= lownumber and list123[midpoint] <= highnumber:
        return True
    elif list123[midpoint] > highnumber:
        return binary(list123[:midpoint], lownumber, highnumber)
    elif list123[midpoint] < lownumber:
        return binary(list123[midpoint:], lownumber, highnumber)
    else:
        return False

    
print(binary(list123, lownumber, highnumber,))
