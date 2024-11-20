import sys
sys.setrecursionlimit(10000)
index = 0
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

def regex_search(reg):
    if reg == '|' or len(reg) == 2:
        return regex(reg)
    skip = 1
    r_input, s_input = reg.split('|')

    if len(r_input) != len(s_input):
        tmp = []
        if len(r_input) == 0:
            x = len(r_input)
            skip = skip if x == 0 else x

        for i in range(0, len(s_input), skip):
            t = s_input[i:i+len(r_input)]
            tmp.append(t)

        processed = process_search_regex(r_input, tmp)
        return processed
    else:
        return process_search_regex(r_input, s_input)

def process_search_regex(reg, tmp):
    global index
    joined_str = None
    if len(tmp) == 0:
        return False
    if isinstance(tmp,list):
        if index < len(tmp):
            joined_str = reg + '|' + tmp[index]
        temp = recursion_regex(joined_str)
        index += 1
    else:
        if index < len(tmp):
            joined_str = reg + '|' + tmp
        temp = recursion_regex(joined_str)
        index += 1
    if index >= len(tmp):
        return temp
    if temp:
        return temp
    else:
        return process_search_regex(reg, tmp)


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
print(regex_search(regex_input))