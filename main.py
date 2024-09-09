def validate_problem(problem):
    if len(problem) != 3:
        return 'Error: Each problem should have two numbers and an operator.'
    
    first_num, operator, second_num = problem
    
    if operator not in ['+', '-']:
        return "Error: Operator must be '+' or '-'."
    
    if not first_num.isdigit() or not second_num.isdigit():
        return 'Error: Numbers must only contain digits.'
    
    if len(first_num) > 4 or len(second_num) > 4:
        return 'Error: Numbers cannot be more than four digits.'

    return None  

def arithmetic_operations(first_num, second_num, operator):
    return int(first_num) + int(second_num) if operator == '+' else int(first_num) - int(second_num)

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line, second_line, dashes_line, answers_line = [], [], [], []

    for problem in problems:
        error = validate_problem(problem.split())
        if error:
            return error 

        first_num, operator, second_num = problem.split()
        answer = arithmetic_operations(first_num, second_num, operator)

        longest_num = max(len(first_num), len(second_num))
        width = longest_num + 2

        first_line.append(first_num.rjust(width))
        second_line.append(f'{operator} {second_num.rjust(longest_num)}')
        dashes_line.append('-' * width)
        if show_answers:
            answers_line.append(str(answer).rjust(width))

    arranged_problems = '\n'.join([
        '    '.join(first_line),
        '    '.join(second_line),
        '    '.join(dashes_line)
    ])
    
    if show_answers:
        arranged_problems += f'\n{"    ".join(answers_line)}'

    return arranged_problems

print(arithmetic_arranger(["32 + 8", "3801 - 3800", "9999 + 9999", "523 - 49"], True))
