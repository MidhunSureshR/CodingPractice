def N(w, h):
    if h == 1:
        return w, 1000000000
    return w, h-1


def S(w, h):
    if h == 1000000000:
        return w, 1
    return w, h+1


def E(w, h):
    if w == 1000000000:
        return 1, h
    return w+1, h


def W(w, h):
    if w == 1:
        return 1000000000, h
    return w-1, h


def linearize(subproblem):
    last_paren = subproblem.rfind("(")

    if last_paren == -1:
        return subproblem

    count = int(subproblem[last_paren - 1])
    end_paren = last_paren + get_closing_index(subproblem[last_paren:])
    linear_problem = count * subproblem[last_paren+1:end_paren]
    subproblem = subproblem[0:last_paren-1] + linear_problem + subproblem[end_paren+1:])


def get_closing_index(subprogram):
    stack = [1]
    for i in range(1, len(subprogram)):
        if subprogram[i] == "(":
            stack.append(1)
        elif subprogram[i] == ")":
            stack.pop()
        if len(stack) == 0:
            return i
    return -1


def run_program(program):
    w, h = 1, 1
    for x in program:
        if x == "N":
            w, h = N(w, h)
        elif x == "W":
            w, h = W(w, h)
        elif x == "E":
            w, h = E(w, h)
        elif x == "S":
            w, h = S(w, h)
    return w, h


for x in range(int(input())):
    program = linearize(input())
    w, h = run_program(program)
    print(f'Case #{x+1}: {w} {h}')

