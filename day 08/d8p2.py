def code_to_digit(i,one,hook):
    match len(i):
            case 2:
                return "1"
            case 3:
                return "7"
            case 4:
                return "4"
            case 7:
                return "8"
            case 5:
                if (one[0] in i and one[1] in i):
                    return "3"
                elif (hook[0] in i and hook[1] in i):
                    return "5"
                else:
                    return "2"       
            case _:
                if (one[0] not in i or one[1] not in i):
                    return "6"
                elif (hook[0] in i and hook[1] in i):
                    return "9"
                else:
                    return "0"

file = open('./input.txt', 'r')

total = 0

line = file.readline().strip()
while line:

    # pull some info out of digit codes to help distiguish codes of same length
    check = line[0:line.index("|")].split()
    for i in check:
        # extract info from 1 digit
        if len(i)==2:
            one = i
        # extract info from 4 digit
        elif len(i)==4:
            hook = i
    # remove one elements to get hooky part of 4
    hook = hook.replace(one[0], "")
    hook = hook.replace(one[1], "")

    # decode and add to total
    out = line[line.index("|")+1:].split()
    number=""
    for code in out:
        number += code_to_digit(code, one, hook)

    total += int(number)

    line = file.readline().strip()

print(total)
