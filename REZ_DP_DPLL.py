import random
import time
import sys
import platform

if platform.system()=="Windows":
    import psutil
else:
    import resource

from itertools import combinations
sys.setrecursionlimit(100000)

def generate_random_cnf(num_vars, num_clauses, clause_size):
    clauses=[]
    for _ in range(num_clauses):
        clause=set()
        while len(clause)<clause_size:
             var=random.randint(1,num_vars)
             sign=random.choice([-1,1])
             clause.add(sign*var)
        clauses.append(list(clause))
    return clauses
  
def memory_usage_kb():
    if platform.system()=="Windows":
       process=psutil.Process()
       return process.memory_info().rss//1024
    else:
       usage=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
       if sys.platform=='darwin':
            usage //= 1024
       return usage
      
def simplify(formula,lit):
    new_formula=[]
    for clause in formula:
      if lit in clause:
        continue
      new_clause=[l for l in caluse if l != -lit]
      new_formula.append(new_clause)
   return new_formula

def dpll(formula,assignment=None):
   if assignment is None:
       assignment=[]
   if not formula:
       return True
   if any(len(clause)==0 for clause in formula):
       return False
   unit_caluses = [c[0] for c in formula if len(c) == 1]
   while unit_clauses:
      lit = unit_clauses.pop()
      formula = simplify(formula, lit)
      assignment.append(lit)
      if any(len(c) == 0 for c in formula):
          return False
      unit_clauses = [c[0] for c in formula if len(c) == 1]
   for clause in formula:
        for lit in clause:
            return dpll(simplify(formula, lit), assignment + [lit]) or \
                   dpll(simplify(formula, -lit), assignment + [-lit])
    return False

def solve_dpll(formula, num_vars):
    return dpll(formula)

def solve_dp(formula, num_vars):
    clauses = [set(c) for c in formula]
    for var in range(1, num_vars + 1):
        pos = [c for c in clauses if var in c]
        neg = [c for c in clauses if -var in c]
        rest = [c for c in clauses if var not in c and -var not in c]
        new_clauses = []
        for c1 in pos:
            for c2 in neg:
                resolvent = (c1 | c2) - {var, -var}
                if not resolvent:
                    return False
                new_clauses.append(resolvent)
        clauses = rest + new_clauses
    return True

def resolve_clauses(c1, c2):
    for lit in c1:
        if -lit in c2:
            resolvent = set(c1).union(c2)
            resolvent.discard(lit)
            resolvent.discard(-lit)
            return list(resolvent)
    return None

def solve_resolution(formula, num_vars):
    clauses = set(tuple(sorted(c)) for c in formula)
    new = set()
    seen = set()
    while True:
        changed = False
        for c1 in clauses:
            for c2 in clauses:
                if c1 >= c2 or (c1, c2) in seen:
                    continue
                seen.add((c1, c2))
                res = resolve_clauses(c1, c2)
                if res is not None:
                    if not res:
                        return False
                    t_res = tuple(sorted(res))
                    if t_res not in clauses and t_res not in new:
                        new.add(t_res)
                        changed = True
        if not changed:
            return True
        clauses |= new
        new.clear()

def run_all_solvers(num_vars, num_clauses, clause_size):
    print(f"\n--- Test: {num_vars} vars, {num_clauses} clauses, {clause_size}-SAT ---")
    formula = generate_random_cnf(num_vars, num_clauses, clause_size)

    for name, solver in [('Resolution', solve_resolution),
                         ('DP',solve_dp),
                         ('DPLL', solve_dpll)]:
        try:
            start = time.time()
            result = solver(formula, num_vars)
            duration = int((time.time() - start) * 1000)
            mem = memory_usage_kb()
            print(f"{name}: {'SAT' if result else 'UNSAT'}, Time={duration}ms, Mem={mem}KB")
        except Exception as e:
            print(f"{name}: FAILED ({str(e)})")

if __name__ == "__main__":
    #Exemplu 
    #run_all_solvers(num_vars=170, num_clauses=170, clause_size=2)
  
    #Exemplu pentru fișiere în format DIMACS 
    #run_all_solvers(cnf_file="exemplu.cnf")

