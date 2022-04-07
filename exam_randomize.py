﻿import io
from random import shuffle
import re

EXAM_FORMS = ['A','B']
ANSWER_MARKER = '***'

''' 
example input file

1. According to Behaviourists like Skinner, how can an experimenter best measure the internal 'cognitive maps' that animals use to perform complex tasks?
(A)  Through the use of a 'Skinner Box'	
(B)  By examining stimulus-response learning
(C)  These cannot be measured or even inferred***
(D)  With neurophysiological recordings

2. A crucial determinant of any artificial intelligence-based solution to a problem, according to Minsky is the:
a. Structure of the representation of the problem***
b. Programming language used to implement the solution
c. Amount of information that needs to be stored
d. Physical hardware that the machine is implemented with	
e. All of the above
'''

items_txt = io.open('items.txt', 'r').read() 

items_txt = items_txt[1:]



items = []
for item_txt in items_txt.split('\n\n'): 
    item_txt = re.sub(r'^\d+\.', '', item_txt)
    items.append(item_txt)

print(len(items), 'items')


for exam_form in EXAM_FORMS:
    shuffle(items)

    output = ''
    output_with_answers = ''
    answer_key = ''
    for item in items:
        if(len(item)==0):
            print('bad item following:', items[items.index(item)-1])
            raise SystemExit

        output += str(items.index(item) + 1) + '. '+  item.strip().split('\n')[0] + '\n'
        output_with_answers += str(items.index(item) + 1) + '. '+  item.strip().split('\n')[0] + '\n'

        options = item.strip().split('\n')[1:]
        for option in options:
            if(option[0]=='('):
                output+=['(A)','(B)','(C)','(D)','(E)'][ options.index(option)] + '\t'+  option.split(')')[1:][0].strip().replace(ANSWER_MARKER,'') + '\n'
                output_with_answers+=['(A)','(B)','(C)','(D)','(E)'][ options.index(option)] + '\t'+  option.split(')')[1:][0].strip() + '\n'
            else:
                output+=['(A)','(B)','(C)','(D)','(E)'][ options.index(option)] + '\t' + option.split('.')[1:][0].strip().replace(ANSWER_MARKER,'') + '\n'
                output_with_answers+=['(A)','(B)','(C)','(D)','(E)'][ options.index(option)] + '\t'+  option.split('.')[1:][0].strip() + '\n'

                
        output += '\n'
        output_with_answers += '\n'

        answer_key += str(items.index(item) + 1) + '.\t' + ['A', 'B', 'C', 'D', 'E'][item.strip().split('\n')[1:].index(list(filter(lambda x:ANSWER_MARKER in x, item.strip().split('\n')[1:]))[0])] + '\n'

    temp = io.open('shuffled_items_form_'+exam_form+'.txt', 'w')#, encoding='utf-8')
    temp.write(output)
    temp.close()

    temp = io.open('shuffled_items_with_answers_form_'+exam_form+'.txt', 'w') #,encoding='utf-8')
    temp.write(output_with_answers)
    temp.close()

    temp = open('answer_key_form_'+exam_form+'.txt', 'w')
    temp.write(answer_key)
    temp.close()
