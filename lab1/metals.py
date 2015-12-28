alkaline_earth_metals = [["berylium", 4], ["magnesium", 12], ["calcium", 20], ["strontium", 38], ["barium", 56], ["radium", 88]]

M_m = max( x[1] for x in alkaline_earth_metals )
print(M_m)

alkaline_earth_metals.sort(key=lambda metal:metal[1])
print(alkaline_earth_metals)

D_m = {x[0]:x[1] for x in alkaline_earth_metals}
print(D_m)

noble_gas = {"helium":2, "neon":10, "argon":18, "krypton":36, "xenon":54, "radon":86}
print(noble_gas)

tot = {**D_m, **noble_gas}
print(tot)

final = sorted(tot.items())
print(final)

