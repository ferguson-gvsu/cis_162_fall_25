# Ignore everything until the comment at the end of the file!
import sys
import os

def check_answer(answer_dict):
    score = 0
    if not isinstance(answer_dict, dict):
        print('Problem: The argument you passed is not a dictionary!')
        return score
    else:
        print('You passed a dictionary! +1 point')
        score += 1
    if len(answer_dict) == 0:
        print('Problem: Your dictionary is empty. We can\'t continue :(')
        print(f'\nYour score: {score}')
        return score
    
    secret = os.path.split(sys.argv[-1])[-1]
    secret_num = len(secret)
    
    if 'part_1' in answer_dict:
        val = secret[8] + secret[1] + secret[-4] + secret[-5]
        if not isinstance(answer_dict['part_1'], str):
            print('Problem: The key "part_1" should map to an string, but it does not...')
        elif answer_dict['part_1'] == val:
            print('Your key "part_1" maps to the correct value, +1 point')
            score += 1
        else:
            print('Problem: Your key "part_2" maps to the incorrect value...')
    else:
        print('Problem: key "part_1" does not exist in your dictionary')

    if 'part_2' in answer_dict:
        if not isinstance(answer_dict['part_2'], int):
            print('Problem: The key "part_2" should map to an int, but it does not...')
        elif answer_dict['part_2'] == (secret_num % 5) * 9 + 2:
            print('Your key "part_2" maps to the correct value, +1 point')
            score += 1
        else:
            print('Problem: Your key "part_2" maps to the incorrect value...')
    else:
        print('Problem: key "part_2" does not exist in your dictionary')

    if 'part_3' in answer_dict:
        val = secret[3] + secret[-5] + secret[-4] + secret[3]
        if not isinstance(answer_dict['part_3'], str):
            print('Problem: The key "part_3" should map to an string, but it does not...')
        elif answer_dict['part_3'] == val:
            print('Your key "part_3" maps to the correct value, +1 point')
            score += 1
        else:
            print('Problem: Your key "part_3" maps to the incorrect value...')
    else:
        print('Problem: key "part_3" does not exist in your dictionary')
    
    if 'part_4' in answer_dict:
        val = str(secret_num * 3900041 + 16)
        if not isinstance(answer_dict['part_3'], str):
            print('Problem: The key "part_4" should map to an string, but it does not...')
        elif answer_dict['part_4'] == val:
            print('Your key "part_4" maps to the correct value, +1 point')
            score += 1
        else:
            print('Problem: Your key "part_4" maps to the incorrect value...')
    else:
        print('Problem: key "part_4" does not exist in your dictionary')

    print(f'\nYour score: {score}')

# Create a dictionary and pass it to check_answer below
D = {}
D['part_1'] = 'rise'
D['part_2'] = 38
D['part_3'] = 'test'
D['part_4'] = '93601000'
check_answer(D)