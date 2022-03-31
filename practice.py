class IceCream:
    def __init__(self, flavor, num_sprinkles):
        self.flavor = flavor
        self.num_sprinkles = num_sprinkles


def sweetest_icecream(icelist):
    sweet = {"Chocolate": 10, "Vanilla": 5, "Strawberry": 20}
    max = value = 0
    for icecream in icelist:
        value = sweet[icecream.flavor] + icecream.num_sprinkles
        if value > max:
            max = value
    return max


ice1 = IceCream("Chocolate", 13)
ice2 = IceCream("Vanilla", 0)
ice3 = IceCream("Strawberry", 7)
ice1.age=7

print(sweetest_icecream([ice1, ice2, ice3]))
