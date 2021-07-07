from unittest import TestCase



def read_real_data(max_number):
    read_data = []
    with open('test_data.txt') as f:
        read_data = f.read().replace('\n', '').split(',')
    
    return [int(d) for d in read_data if d!='' and int(d) <= max_number]


def test_solution(solutions, max_number):
    case = TestCase()
    real_data = read_real_data(max_number)
    real_data.sort()
    
    case.assertListEqual(solutions, real_data)
    #case.assertEqual(solutions, real_data)
    