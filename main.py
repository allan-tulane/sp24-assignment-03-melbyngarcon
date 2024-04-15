
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


  if not S:
    MED[(S, T)] = (len(T), "-" * len(T), T)
    return "-" * len(T), T
  if not T:
    MED[(S, T)] = (len(S), S, "-" * len(S))
    return S, "-" * len(S)

  # Handle the case where characters match
  if S[0] == T[0]:
    align_S, align_T = fast_align_MED(S[1:], T[1:], MED)
    alignment = (S[0] + align_S, T[0] + align_T)
    MED[(S, T)] = (MED[(S[1:], T[1:])][0], *alignment)
    return alignment

  # Handle the case where characters do not match
  else:
    insert_align_S, insert_align_T = fast_align_MED(S, T[1:], MED)
    delete_align_S, delete_align_T = fast_align_MED(S[1:], T, MED)
    substitute_align_S, substitute_align_T = fast_align_MED(S[1:], T[1:], MED)

    # Prepend ' ' (space) and '-' to S for insert
    insert_cost = 1 + MED[(S, T[1:])][0]
    insert_alignment = (" " + "-" + insert_align_S, T[0] + insert_align_T)

    # Prepend S[0] to S for delete, '-' to T for delete
    delete_cost = 1 + MED[(S[1:], T)][0]
    delete_alignment = (S[0] + delete_align_S, "-" + delete_align_T)

    # Align S[0] with T[0] directly for substitution
    substitute_cost = 1 + MED[(S[1:], T[1:])][0]
    substitute_alignment = (S[0] + substitute_align_S, T[0] + substitute_align_T)

    costs = [
        (insert_cost, insert_alignment[0], insert_alignment[1]),
        (delete_cost, delete_alignment[0], delete_alignment[1]),
        (substitute_cost, substitute_alignment[0], substitute_alignment[1])
    ]

    best = min(costs, key=lambda x: x[0])

    # Update MED dictionary to store alignments for all options
    MED[(S, T)] = (best[0], best[1], best[2], insert_alignment, delete_alignment, substitute_alignment)

    # Return the alignment of the chosen option
    return best[1], best[2]

def test_fast_align_MED():
  passed = True
  for i, (S, T) in enumerate(test_cases):
      expected_align_S, expected_align_T = alignments[i]
      align_S, align_T = fast_align_MED(S, T)

      # Checking if the function output matches the expected output
      if (align_S == expected_align_S) and (align_T == expected_align_T):
          print(f"Test case {i + 1} passed: ({S}, {T})")
      else:
          print(f"Test case {i + 1} failed: ({S}, {T})")
          print(f"  Expected: ({expected_align_S}, {expected_align_T})")
          print(f"  Received: ({align_S}, {align_T})")
          passed = False

  if passed:
      print("All tests passed!")
  else:
      print("Some tests failed. Check the output above for details.")

test_fast_align_MED()