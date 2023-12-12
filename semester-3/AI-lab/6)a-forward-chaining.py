facts = [["insect", "bee"], ["can fly", "bee"], ["mammal", "elephant"]]
isChanged = True

def assertFact(fact):
    global facts
    global isChanged
    if not fact in facts:
        facts += [fact]
        isChanged = True

while isChanged:
    isChanged = False
    for A1 in facts:
        if A1[0] == "insect":
            assertFact(["animal", A1[1]])
        if A1[0] == "insect" and ["can fly", A1[1]] in facts:
            assertFact(["flying_animal", A1[1]])
        if A1[0] == "flying_animal":
            assertFact(["bird", A1[1]])

print(facts)

