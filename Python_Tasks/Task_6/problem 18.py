# Problem 18: Set Mutations
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-mutations/problem

if __name__ == '__main__':
    len_set_A = int(input())
    set_A = set(map(int, input().split()))
    num_operations = int(input())
    
    for _ in range(num_operations):
        operation_name, incoming_set_size = input().split()
        incoming_set = set(map(int, input().split()))
        if operation_name == 'update':
            set_A.update(incoming_set)
        elif operation_name == 'intersection_update':
            set_A.intersection_update(incoming_set)
        elif operation_name == 'difference_update':
            set_A.difference_update(incoming_set)
        elif operation_name == 'symmetric_difference_update':
            set_A.symmetric_difference_update(incoming_set)
    print(sum(set_A))
