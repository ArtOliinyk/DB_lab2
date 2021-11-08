from db_processing import *


def first_query_data():
    result = query_result(1)
    data = {
        'Username': [i[0] for i in result],
        'Number of groups': [i[1] for i in result],
    }
    return data


def second_query_data():
    result = query_result(2)
    data = {
        'Year': [i[0] for i in result],
        'Number of groups': [i[1] for i in result],
    }
    return data


def third_query_data():
    result = query_result(3)
    data = {
        'Group name': [i[0] for i in result],
        'Subscribers': [i[1] for i in result],
    }
    return data


def print_result(data):
    keys = list(data.keys())
    print("{:<25} {:<10}".format(keys[0], keys[1]))
    for i in range(len(data[keys[0]])):
        print("{:<25} {:<10}".format(data[keys[0]][i], data[keys[1]][i]))
    print('\n')


if __name__ == '__main__':
    print("First query:\n")
    print_result(first_query_data())
    print("Second query:\n")
    print_result(second_query_data())
    print("Third query:\n")
    print_result(third_query_data())
