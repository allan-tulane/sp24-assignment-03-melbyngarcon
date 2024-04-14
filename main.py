
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
  if not S:
      return len(T)
  if not T:
      return len(S)
  if S[0] == T[0]:
      return MED(S[1:], T[1:])  # No cost if characters are the same
  else:
      insert_cost = 1 + MED(S, T[1:])  # Insertion
      delete_cost = 1 + MED(S[1:], T)  # Deletion
      substitute_cost = 1 + MED(S[1:], T[1:])  # Substitution
      return min(insert_cost, delete_cost, substitute_cost)


def fast_MED(S, T, memo={}):
  if (S, T) in memo:
    return memo[(S, T)]
  if not S:
    return len(T)
  if not T:
    return len(S)
  if S[0] == T[0]:
    memo[(S, T)] = fast_MED(S[1:], T[1:], memo)
  else:
    insert_cost = 1 + fast_MED(S, T[1:], memo)
    delete_cost = 1 + fast_MED(S[1:], T, memo)
    substitute_cost = 1 + fast_MED(S[1:], T[1:], memo)
    memo[(S, T)] = min(insert_cost, delete_cost, substitute_cost)
  return memo[(S, T)]
def fast_align_MED(S, T, MED={}):
      if (S, T) in MED:
          return MED[(S, T)][1], MED[(S, T)][2]  # Return only the alignment parts

      if not S:
          alignment = ("-" * len(T), T)
          MED[(S, T)] = (len(T), *alignment)
          return alignment

      if not T:
          alignment = (S, "-" * len(S))
          MED[(S, T)] = (len(S), *alignment)
          return alignment

      if S[0] == T[0]:
          align_S, align_T = fast_align_MED(S[1:], T[1:], MED)
          alignment = (S[0] + align_S, T[0] + align_T)
          MED[(S, T)] = (MED[(S[1:], T[1:])][0], *alignment)
          return alignment

      else:
          insert_align_S, insert_align_T = "-" + fast_align_MED(S, T[1:], MED)[0], T[0] + fast_align_MED(S, T[1:], MED)[1]
          insert_cost = 1 + MED.get((S, T[1:]), (float('inf'), None, None))[0]

          delete_align_S, delete_align_T = S[0] + fast_align_MED(S[1:], T, MED)[0], "-" + fast_align_MED(S[1:], T, MED)[1]
          delete_cost = 1 + MED.get((S[1:], T), (float('inf'), None, None))[0]

          substitute_align_S, substitute_align_T = S[0] + fast_align_MED(S[1:], T[1:], MED)[0], T[0] + fast_align_MED(S[1:], T[1:], MED)[1]
          substitute_cost = 1 + MED.get((S[1:], T[1:]), (float('inf'), None, None))[0]

          costs = [
              (insert_cost, insert_align_S, insert_align_T),
              (delete_cost, delete_align_S, delete_align_T),
              (substitute_cost, substitute_align_S, substitute_align_T)
          ]

          best = min(costs, key=lambda x: x[0])
          MED[(S, T)] = (best[0], best[1], best[2])
          return best[1], best[2]
for S, T in test_cases:
  result = fast_MED(S, T)
  print(f"Minimum Edit Distance between '{S}' and '{T}': {result}")

