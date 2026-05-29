def calculer_ttc(prix_ht: float) -> float:
    return prix_ht * 1.20

prix_ttc = calculer_ttc(100)
print(f"Prix TTC: {prix_ttc}")
