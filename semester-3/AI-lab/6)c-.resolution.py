from itertools import combinations
def resolve(c1, c2):
    res = []
    for p in c1:
        if 'not ' + p in c2:
            res.append([x for x in c1 if x != p] + [x for x in c2 if x != 'not ' + p])
    for p in c2:
        if 'not ' + p in c1:
            res.append([x for x in c1 if x != 'not ' + p] + [x for x in c2 if x != p])
    return res
def resolution(kb, ng):
    clauses = kb + [ng]
    while True:
        new_clauses = []
        for c1, c2 in combinations(clauses, 2):
            resolvents = resolve(c1, c2)
            if [] in resolvents:
                return True
            new_clauses += resolvents
        if len(new_clauses) == 0 or any(nc in clauses for nc in new_clauses):
            return False
        clauses += new_clauses

kb1 = [["A"], ["not A", "B"], ["not B", "C"]]
ng1 = ["not C"]
print(resolution(kb1, ng1))

kb2 = [["A"], ["not A", "B"], ["B", "C"]]
ng2 = ["not C"]
print(resolution(kb2, ng2))

kb3 = [["A"], ["not A", "B"], ["not B", "C"], ["C"]]
ng3 = ["not C"]
print(resolution(kb3, ng3))

