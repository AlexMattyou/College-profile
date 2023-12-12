def backChain(base, goal):
    if goal in base.facts:
        return True
    for rule in base.rules:
        if goal in rule.con:
            if all(backChain(base, ante) for ante in rule.ante):
                return True
    return False
class Rule:
    def __init__(self, ante, con):
        self.ante = ante
        self.con = con
class RuleBase:
    def __init__(self, rules, facts):
        self.rules = rules
        self.facts = facts

rules = [Rule(['Rainy'], 'Carry Umbrella'), Rule(['Sunny'], 'Wear Sunglasses')]
facts = ['Rainy']
base = RuleBase(rules, facts)

print(backChain(base, 'Carry Umbrella'))
print(backChain(base, 'Wear Sunglasses'))

