
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S,T[1:]),MED(S[1:],T)))


def fast_MED(S, T, MED={}):
# Using the provided signature without modification

# Check if the result is already memoized
  if (S, T) in MED:
    return MED[(S, T)]

# Base cases
  if not S:
    MED[(S, T)] = len(T)
  elif not T:
    MED[(S, T)] = len(S)
  elif S[0] == T[0]:  # No edit needed for matching characters
    MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
  else:
    # Calculate costs for insert, delete, and substitute operations
    insert_cost = 1 + fast_MED(S, T[1:], MED)
    delete_cost = 1 + fast_MED(S[1:], T, MED)
    substitute_cost = 1 + fast_MED(S[1:], T[1:], MED)
    MED[(S, T)] = min(insert_cost, delete_cost, substitute_cost)

  return MED[(S, T)]

def fast_align_MED(S, T, MED={}):
# Check if the result is already memoized
  if (S, T) in MED:
    return MED[(S, T)]

# Correct base cases to ensure S and T are not empty
  if not S:
    MED[(S, T)] = (len(T), "-" * len(S), T)
    return MED[(S, T)]
  if not T:
    MED[(S, T)] = (len(S), S, "-" * len(T))
    return MED[(S, T)]

# Ensure we don't access S[0] or T[0] if S or T is empty (handled by base cases)
  if S[0] == T[0]:
    cost, alignS, alignT = fast_align_MED(S[1:], T[1:], MED)
    MED[(S, T)] = (cost, S[0] + alignS, T[0] + alignT)
  else:
    insert_cost, insert_alignS, insert_alignT = fast_align_MED(S, T[1:], MED)
    delete_cost, delete_alignS, delete_alignT = fast_align_MED(S[1:], T, MED)
    substitute_cost, substitute_alignS, substitute_alignT = fast_align_MED(S[1:], T[1:], MED)

    costs = [
        (insert_cost + 1, "-" + insert_alignS, T[0] + insert_alignT),
        (delete_cost + 1, S[0] + delete_alignS, "-" + delete_alignT),
        (substitute_cost + 1, S[0] + substitute_alignS, T[0] + substitute_alignT)
    ]

    MED[(S, T)] = min(costs, key=lambda x: x[0])

  return MED[(S, T)]
for S, T in test_cases:
  result = fast_MED(S, T)
  print(f"Minimum Edit Distance between '{S}' and '{T}': {result}")

for S, T in test_cases:
  cost, alignS, alignT = fast_align_MED(S, T)
  print(f"Cost: {cost}, Alignment for '{S}': {alignS}, Alignment for '{T}': {alignT}")