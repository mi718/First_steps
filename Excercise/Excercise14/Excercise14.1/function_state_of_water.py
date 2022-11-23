
def state(temperature):
    if temperature < 0:
        return "solid"
    elif 0 < temperature < 100:
        return "Liquid"
    elif temperature > 100:
        return "gas"
    else:
        return "wrong input!!!"