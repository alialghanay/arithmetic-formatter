def arithmetic_arranger(problems, show_answers=False):
    problems = [problem.split() for problem in problems]
    formated_problems = []
    answer = None
    for problem in problems:
        if len(problem) != 3:
            raise ValueError('Each problem should have two numbers and an operator.')
        first_num, operator, second_num = problem
        if operator not in ['+', '-']:
            raise ValueError('Operator must be "+" or "-".')
        if not first_num.isdigit() or not second_num.isdigit():
            raise ValueError('Numbers must only contain digits.')
        if len(first_num) > 4 or len(second_num) > 4:
            raise ValueError('Numbers cannot be more than four digits.')
        if operator == '+':
            answer = int(first_num) + int(second_num)
        else:
            answer = int(first_num) - int(second_num)
        longest_num = max(len(first_num), len(second_num))
        formated_problems.append(f'{first_num.rjust(longest_num + 2)}\n{operator} {second_num.rjust(longest_num)}\n{"-" * (longest_num + 2)}')
        if show_answers:
            formated_problems[-1] += f'\n{str(answer).rjust(longest_num + 2)}'
    problems = '    '.join(formated_problems)
    return formated_problems[1]



print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')


# final output: 
# 32
# + 698
# -----