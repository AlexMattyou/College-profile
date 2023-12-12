def eval_formula(formula, model):
    if isinstance(formula, tuple):
        op, *operands = formula
        if op == 'not':
            return not eval_formula(operands[0], model)
        elif op == 'and':
            return all(eval_formula(opnd, model) for opnd in operands)
        elif op == 'or':
            return any(eval_formula(opnd, model) for opnd in operands)
        elif op == 'implies':
            return (not eval_formula(operands[0], model)) or eval_formula(operands[1], model)
        elif op == 'equiv':
            return eval_formula(operands[0], model) == eval_formula(operands[1], model)
    else:
        return model.get(formula, False)

def check_model(formula, model):
    return eval_formula(formula, model)

formula_1 = ('or', ('and', 'p', 'q'), ('not', 'r'))
model_1 = {'p': True, 'q': False, 'r': True}
result_1 = check_model(formula_1, model_1)
print(f"Example 1: Model satisfies the formula: {result_1}")

formula_2 = ('implies', ('and', 'p', ('not', 'q')), 'r')
model_2 = {'p': True, 'q': False, 'r': True}

result_2 = check_model(formula_2, model_2)
print(f"Example 2: Model satisfies the formula: {result_2}")


