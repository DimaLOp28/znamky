znamky = [1, 2, 3, 4, 5]

for i in range(5):
    znamka = int(input(f"Zadej {i+1}. známku (1-5): "))
    znamky.append(znamka)
 
print("Všechny známky:", znamky)
 
prumer = sum(znamky) / len(znamky)
print("Průměr všech známek je:", round(prumer, 2))