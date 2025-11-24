def prompt_for_int(min_val, max_val):
    val = int(input())
    if val < min_val:
        raise ValueError("User returned integer below our minimum")
    if val > max_val:
        raise ValueError("User returned integer above our minimum")

def collect_user_info():
    info = {}
    info['age'] = prompt_for_int(0, 100)

if __name__ == '__main__':
    collect_user_info()