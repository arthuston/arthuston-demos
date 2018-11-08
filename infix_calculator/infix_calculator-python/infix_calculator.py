"""
Convert an infix string arithmetic expression and calculate the value
using the precedence of the +, -, *, / and parentheses operators to return
the correct result.
"""

#####################################################
# operator precedence and binary arithmetic operation
#####################################################
OPERATORS = {
    '-': {'precedence': 0,
          'operation': lambda first, second: first - second},
    '+': {'precedence': 0,
          'operation': lambda first, second: first + second},
    '*': {'precedence': 1,
          'operation': lambda first, second: first * second},
    '/': {'precedence': 1,
          'operation': lambda first, second: first / second}
}

LEFT_PAREN = '('
RIGHT_PAREN = ')'


def is_operator(value):
    return value in OPERATORS


def operator_precedence(operator):
    return OPERATORS[operator]['precedence']


def apply_operator(operator, first, second):
    return OPERATORS[operator]['operation'](first, second)


#############################
# Convert expression to value
#############################

def is_digit(value):
    """
    Check if value is a numeric digit
    :param value: value
    :return: true if value is a numeric digit
    """
    return value in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def token_generator(expression):
    """
    Generator to get tokens from a string arithmetic expression
    :param expression: infix string expression
    :return: next token
    """
    i = 0
    while i < len(expression):
        char = expression[i]
        if is_operator(char) or char == LEFT_PAREN or char == RIGHT_PAREN:
            i += 1
            yield char
        elif is_digit(char):
            value = ord(char) - ord('0')
            i += 1
            while i < len(expression) and is_digit(expression[i]):
                value = value * 10 + ord(expression[i]) - ord('0')
                i += 1
            yield value
        else:
            raise ValueError('Unexpected character %s' % char)


def get_postfix_tokens(infix_tokens):
    """
    Get postfix tokens from infix tokens
    :param infix_tokens: infix tokens
    :return: postfix tokens
    """
    operator_stack = []
    postfix_tokens = []

    for token in infix_tokens:
        if is_operator(token):
            # pop stack and append to postfix tokens while peek(stack) is not LEFT_PAREN
            # and peek(stack) precedence >= operator precedence
            while len(operator_stack) > 0 and peek(operator_stack) != LEFT_PAREN and operator_precedence(
                    peek(operator_stack)) >= operator_precedence(token):
                postfix_tokens.append(operator_stack.pop())
            # push operator on stack
            operator_stack.append(token)
        elif token == LEFT_PAREN:
            operator_stack.append(token)
        elif token == RIGHT_PAREN:
            # pop stack and append to postfix tokens while peek(stack) != LEFT_PAREN
            while len(operator_stack) > 0 and peek(operator_stack) != LEFT_PAREN:
                postfix_tokens.append(operator_stack.pop())
            if len(operator_stack) == 0:
                raise ValueError('Missing left paren')
            # pop left paren
            operator_stack.pop()
        else:
            # immediately append value to postfix tokens
            postfix_tokens.append(token)

    # add remaining operator stack to postfix tokens
    while len(operator_stack) > 0:
        if operator_stack == '(':
            raise ValueError('Missing right paren')
        postfix_tokens.append(operator_stack.pop())
    return postfix_tokens


def peek(stack):
    """
    Peek the stack
    :param stack: the stack
    :return: top of the stack
    """
    return stack[len(stack) - 1]


def evaluate_postfix_tokens(postfix_tokens):
    """
    Calculate value using postfix tokens
    :param postfix_tokens: postfix tokens
    :return: arithmetic value
    """
    stack = []
    for token in postfix_tokens:
        if is_operator(token):
            op2 = stack.pop()
            op1 = stack.pop()
            result = apply_operator(token, op1, op2)
            stack.append(result)
        else:
            stack.append(token)
    return stack.pop()


def evaluate_infix_expression(infix_expression):
    """
    Evaluate an infix string arithmetic expression and return the result
    :param infix_expression: infix string arithmetic expression
    :return: integer result
    """
    infix_tokens = token_generator(infix_expression)
    postfix_tokens = get_postfix_tokens(infix_tokens)
    value = evaluate_postfix_tokens(postfix_tokens)
    return value


def test(expression, expected_result):
    result = evaluate_infix_expression(expression)
    print('%s = %s' % (expression, result))
    assert (result == expected_result)


if __name__ == '__main__':
    """
    Test the evaluate function.
    """
    test("1+2", 3)
    test("1*2*3*4*5", 120)
    test("34-5*100", -466)
    test("(34-5)*100", 2900)
    test("10-20*30+40/50", -589.2)
