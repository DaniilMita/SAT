Un fișier .cnf în format DIMACS conține:
Linii de comentariu (opțional) — încep cu c
Linia de problemă — începe cu p cnf
Clauzele — una pe linie, fiecare terminată cu 0

```dimacs
c Formula: (x1 ∨ x2) ∧ (¬x2 ∨ ¬x3)
p cnf 3 2
1 2 0
-2 -3 0

