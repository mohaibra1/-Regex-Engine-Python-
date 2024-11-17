def regex(reg): # write your code here
    reg = reg.split('|')
    if reg[1] == '' and reg[0] != '':
        return False
    elif reg[0] != reg[1]:
        if reg[0] == '.' or reg[0] == '':
            return True
        return False

    return True
regex_input = input()
print(regex(regex_input))