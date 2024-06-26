# negation: 'not', '-', '~'
# logical disjunction: 'or'
# logical nor: 'nor'
# exclusive disjunction: 'xor', '!='
# logical conjunction: 'and'
# logical NAND: 'nand'
# material implication: '=>', 'implies'
# logical biconditional: '='
# bidirectional implication (<=>): '-(p!=q)'

from ttg import ttg

if __name__ == '__main__':
    # print(ttg.Truths(['p', 'q'], ['p and q', 'p or q', '(p or (~q)) => (~p)']))

    # table_val = ttg.Truths(['p', 'q'], ['(p and q) or (p and ~q)' ])
    # table_val = ttg.Truths(['p', 'q'], ['-(p!=~q)', 'p and ~q'])
    # table_val = ttg.Truths(['p', 'q'], ['p => (p or q)'])
    # table_val = ttg.Truths(['p', 'q'], ['~p or ~q', '~(p and q)'])
    # table_val = ttg.Truths(['p', 'q'], ['-(p!=-q)', '(p and -q)'])
    # table_val = ttg.Truths(['p', 'q'], ['(p and q) or (p and -q)'])
    # table_val = ttg.Truths(['p', 'q', 'r'], ['(p => q) and r'])
    table_val = ttg.Truths(['p', '-p'], ['p or -p'])
    # table_val = ttg.Truths(['p', 'q'], ['(-(p!=q)) and (p!=q)'])
    # table_val = ttg.Truths(['p', 'q'], ['(-(p!=q)) and (p!=q)'])
    print(table_val)
    print(table_val.valuation(3))
