# SAT Solver 

Acest proiect implementează și compară trei algoritmi clasici de satisfiabilitate propozițională (SAT):

- **Rezoluție (Resolution)**
- **Davis–Putnam (DP)**
- **Davis–Putnam–Logemann–Loveland (DPLL)**

## 📌 Descriere

Codul generează formule SAT aleatoare în formă normală conjunctivă (CNF) și evaluează performanța fiecărui algoritm în termeni de:
- **Rezultat** (`SAT` sau `UNSAT`)
- **Timp de execuție** (în milisecunde)
- **Memorie utilizată** (în kilobytes)

Este compatibil cu platforme Windows, Linux și macOS.

## ⚙️ Conținut

- `generate_random_cnf(...)` — generează formule CNF aleatoare.
- `solve_resolution(...)` — implementează metoda de rezoluție.
- `solve_dp(...)` — implementează algoritmul Davis–Putnam.
- `solve_dpll(...)` — implementează DPLL cu propagare a literalilor unitari.
- `run_all_solvers(...)` — rulează toți algoritmii pe aceeași formulă și afișează statistici.

## ✅ Exemplu rulare

```zsh
python sat_solver.py
