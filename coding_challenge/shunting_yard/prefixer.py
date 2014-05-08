import re
num_pattern = re.compile('[0-9]+')
op_pattern = re.compile('[*+-/]')
paren_pattern = re.compile('[()]')

# PRECEDENCE = {
#     '+': 1,
#     '-': 1,
#     '/': 2,
#     '*': 2
# }

def precedence(operator):
    if operator in ['+', '-']:
        return 1
    if operator in ['*', '/']:
        return 2

def parse(user_input):
    tokens = user_input.split()
    return tokens

def create_out_queue(user_input):
    tokens = parse(user_input)

    out_queue = []
    op_stack = []

    while tokens:
        token = tokens.pop(0)
        if num_pattern.match(token):
            out_queue.append(token)
        elif op_pattern.match(token):
            if not op_stack or precedence(op_stack[-1]) < precedence(token):
                op_stack.append(token)
            elif precedence(op_stack[-1]) >= precedence(token):
                to_queue = op_stack.pop()
                out_queue.append(to_queue)
                op_stack.append(token)
            else: 
                print "WHAT IS THIS.", token
        else:
            print "Unexpected token %r" %token
    # output to reverse polish notation/RPN
    while op_stack:
        operator = op_stack.pop()
        out_queue.append(operator)
    print out_queue
    return out_queue

# recursively traverse out_queue
# def out_string(queue):
    # if len(queue) == 3: # base case
    #     operator = queue[2]
    #     arg1 = queue[0]
    #     arg2 = queue[1]
    #     return '(' + arg1 + ' ' + arg2 + ' ' + operator + ')'

    # elif num_pattern.match(queue[-1]): # number
    #     return queue[-1]

    # operator = queue[-1]
    # exp = out_string(queue[:-1])
    # print 'operator', operator
    # print exp
    # return '(' + exp + operator + ')'

def queue_to_postfix(queue):

    if not queue:
        return ''

    if len(queue) == 3: # base case
        operator = queue[2]
        arg1 = queue[0]
        arg2 = queue[1]
        return '(' + arg1 + ' ' + arg2 + ' ' + operator + ')'

    out = '('
    first = queue.pop(0)
    while not op_pattern.match(first):
        out += first + ' '
        first = queue.pop(0)
    # operator found
    out += first + ')'
    return '(' + out + queue_to_postfix(queue) + ')'

def infix_to_postfix(user_input):
    out_queue = create_out_queue(user_input)
    return queue_to_postfix(out_queue)