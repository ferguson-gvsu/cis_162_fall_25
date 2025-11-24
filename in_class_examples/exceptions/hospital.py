def prompt_for_int():
    while True:
        try:
            val = int(input())
            return val
        except ValueError:
            print('Invalid integer. Please try again.')


def get_birth_year():
    year = prompt_for_int()
    if year > 2025:
        raise ValueError('Person born in the future?')
    
if __name__ == '__main__':
    try:
        get_birth_year()
    except Exception:
        print('issue!')