import math

# keys = ['digit', 'point', 'mines operation',
#         'operation', 'open', 'close']
operations = ['^', '*', '/', '+', '-']
float_sign = '.'
parentheses = ['(', ')']


def unified_numbers(phrases, interpretations):
    size_of_phrase = len(phrases)
    new_phrases = []
    new_interpretation = []
    i = 0
    while (i<size_of_phrase):
        if interpretations[i] == 'digit':
            number = []
            number.append(phrases[i])
            for j in range(i+1, size_of_phrase):
                if interpretations[j] == 'digit' or interpretations[j] == 'point':
                    number.append(phrases[j])


                else:
                    number = ''.join(number)
                    new_phrases.append(float(number))
                    new_interpretation.append('digit')
                    i = j
                    break
        else:
            new_phrases.append(phrases[i])
            new_interpretation.append(interpretations[i])
            i += 1
    return new_phrases, new_interpretation


def cal_operations(phrases, interpretations):
    size_of_phrase = 0
    sum_of_phrase = 0
    i = 0

    while interpretations.count('operation') > 0:

        if '^' in phrases:
            opr_index = phrases.index('^')
            num = phrases[opr_index - 1] ** phrases[opr_index + 1]
        elif '*' in phrases or '/' in phrases:
            if '*' in phrases:
                opr_index = phrases.index('*')
                num = phrases[opr_index - 1] * phrases[opr_index + 1]
            if '/' in phrases:
                opr_index = phrases.index('/')
                num = phrases[opr_index - 1] / phrases[opr_index + 1]
        elif '+' in phrases or '-' in phrases:
            if '+' in phrases:
                opr_index = phrases.index('+')
                num = phrases[opr_index - 1] + phrases[opr_index + 1]
            if '-' in phrases:
                opr_index = phrases.index('-')
                num = phrases[opr_index - 1] - phrases[opr_index + 1]

        del phrases[opr_index - 1: opr_index + 2]
        del interpretations[opr_index - 1: opr_index + 2]
        phrases.insert(opr_index - 1, num)
        interpretations.insert(opr_index - 1, 'digit')

    output = phrases[0]
    return output


def calculating(phrases, interpretations):

    # this part gives priority to parenthesis
    size_of_phrase = len(phrases)
    while interpretations.count('open') > 0:
        for start in range(size_of_phrase):
            if interpretations[start] == 'open':
                for end in range(size_of_phrase - 1, 0, -1):
                    if interpretations[end] == 'close':
                        output = calculating(phrases[start + 1: end], interpretations[start + 1: end])
                        phrases[start] = output
                        interpretations[start] = 'digit'
                        for i in range(start+1, end+1):
                            phrases[i] = '#'
                            interpretations[i] = '#'
    while phrases.count("#"):
        phrases.remove("#")
        interpretations.remove("#")

    #calculating other operations
    output = cal_operations(phrases, interpretations)
    return output



# Getting input from user and remove all spaces
print("Welcome!")
phrase = input("Enter our phrase:\n")
phrase = list(phrase.replace(' ', ''))

interpreting_list = []

# interpreting our elements.
# bc we need to know which is which, so we can work with it.

for element in phrase:
    if element.isdigit():
        interpreting_list.append('digit')
    elif element is float_sign:
        interpreting_list.append('point')
    elif element in operations:
        interpreting_list.append('operation')
    elif element is parentheses[0]:
        interpreting_list.append('open')
    elif element is parentheses[1]:
        interpreting_list.append('close')
    else:
        interpreting_list.append('non')

phrase.append('#')
interpreting_list.append("#")
# numbers are seperated. let's concatenate them
phrase, interpreting_list = unified_numbers(phrase, interpreting_list)

final_output = calculating(phrase, interpreting_list)
print(f"output is : {final_output}")
