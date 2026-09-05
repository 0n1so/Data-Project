def calculate_lye(oils, superfat=0.05):
    total_naoh = sum(weight * sap for weight, sap in oils.values())
    total_naoh *= (1 - superfat)
    return round(total_naoh, 2)

oils = {
    "оливкова": (300, 0.134),
    "кокосова": (200, 0.178),
    "касторова": (50, 0.128)
}

print(calculate_lye(oils, superfat=0.05))
