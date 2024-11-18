
def regex(reg): # write your code here
    reg = reg.split('|')
    if reg[1] == '' and reg[0] != '':
        return False
    elif reg[0] != reg[1]:
        if reg[0] == '.' or reg[0] == '':
            return True
        return False

    return True

def recursion_regex(reg):
    str_reg, reg = process_regex(reg)
    temp = regex(str_reg)
    if reg[0] == '|':
        return temp
    if temp:
        return recursion_regex(reg)
    return False

def process_regex(reg):
    first, second = reg.split('|')
    first = [*first]
    second = [*second]
    if len(first) == 0:
        first.append('')
    if len(second) == 0:
        second.append('')
    str_reg = first[0] + '|' + second[0]
    first.pop(0)
    second.pop(0)
    first = ''.join(first)
    second = ''.join(second)
    reg = first + '|' + second
    return str_reg, reg

regex_input = input()
print(recursion_regex(regex_input))