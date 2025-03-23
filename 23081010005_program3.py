from sympy import symbols, And, Or, Not 

# Definisi proposisi
P, Q = symbols('P Q')

# Kombinasi logika proposisi
ekspresi_and = And(P, Q)  # Cuaca panas DAN saya menyalakan kipas angin
ekspresi_or = Or(P, Q)    # Cuaca panas ATAU saya menyalakan kipas angin
ekspresi_not = Not(P)     # Cuaca TIDAK panas

# Evaluasi ekspresi
print("Cuaca panas DAN saya menyalakan kipas angin:", ekspresi_and.subs({P: True, Q: True}))
print("Cuaca panas ATAU saya menyalakan kipas angin:", ekspresi_or.subs({P: True, Q: False}))
print("Cuaca TIDAK panas:", ekspresi_not.subs(P, True))
