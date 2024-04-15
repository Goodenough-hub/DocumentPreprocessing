from datetime import datetime

def drop_repeat(mylist):
    new_li1 = list(set(mylist))
    return new_li1


def cur_time():  # 只返回年月日
    current_time = datetime.now()
    formatted_time = current_time.strftime('%Y-%m-%d')
    return formatted_time


if __name__ == '__main__':
    li1 = [1, 2, 33, 33, 2, 5, 6]
    new_lis = drop_repeat(li1)
    print(new_lis)
    print(cur_time())
