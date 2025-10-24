teams = {'basketball': 'gold', 'volleyball': 'rise', 'hockey': 'griffons'}


grade_weights = {}
grade_weights['Midterm 1'] = 13
grade_weights['Midterm 2'] = 13
grade_weights['Lab Exam'] = 13
grade_weights['Final Exam'] = 15
grade_weights['Projects'] = 18
grade_weights['Labs'] = 18
grade_weights['Activities'] = 10

a = grade_weights['Labs']
b = grade_weights['Midterm 1']
c = len(grade_weights)
print(a, b, c, a+b+c)


toys = {
    'teddy':'bear',
    'ellie':'elephant',
    'stan':'spider',
    'ty':'tasmanian tiger'
}
for val in toys:
    print(val[0], end = '')
print()

min_grades = { # + and - exists, but I want this example to be simple
    'a':93,
    'b':83,
    'c':73,
    'd':60,
    'f':0
}
min_grades.pop('f')
min_grades.pop('c')
min_grades['s'] = 1000
min_grades.pop('b')

result = ''
for k, v in min_grades.items():
    result += str(v)
print(result)
