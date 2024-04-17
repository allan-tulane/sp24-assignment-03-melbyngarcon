
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
  # TODO - modify to account for insertions, deletions and substitutions
  if (S == ""):
      return(len(T))
  elif (T == ""):
      return(len(S))
  else:
      if (S[0] == T[0]):
          return(MED(S[1:], T[1:]))
      else:
          return(1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[1:], T[1:])))


def fast_MED(S, T, MED_cache={}):
  if (S, T) in MED_cache:
      return MED_cache[(S, T)]
  else:
      if (S == ""):
          return(len(T))
      elif (T == ""):
          return(len(S))
      else:
          if (S[0] == T[0]):
              MED_cache[(S, T)] = fast_MED(S[1:], T[1:], MED_cache)
          else:
              MED_cache[(S, T)] = 1 + min(fast_MED(S, T[1:], MED_cache), fast_MED(S[1:], T, MED_cache), fast_MED(S[1:], T[1:], MED_cache))
          return(MED_cache[(S, T)])


def helper(S, T, MED_cache={}):
  if (S, T) in MED_cache:
      return MED_cache[(S, T)]
  else:
      if (S == ""):
          return(len(T), T[len(S):])
      elif (T == ""):
          diff = len(S) - len(T)
          return(len(S), "-" * diff)
      else:
          if (S[0] == T[0]):
              new = (helper(S[1:], T[1:], MED_cache))
              MED_cache[(S, T)] = (new[0], T[0] + new[1])
          else:
              insert = ((helper(S, T[1:], MED_cache)))
              delete = ((helper(S[1:], T, MED_cache)))
              sub = ((helper(S[1:], T[1:], MED_cache)))
              best = min(insert[0], delete[0], sub[0])
              if best == sub[0]:
                  new = (1 + sub[0], T[0] + sub[1])
              elif best == delete[0]:
                  new = (1 + delete[0],  "-" + delete[1])
              else:
                  new = (1 + insert[0], T[0] + insert[1])
              MED_cache[(S, T)] = new
          return(MED_cache[(S, T)])

def fast_align_MED(S, T):
  return (helper(T, S)[1], helper(S, T)[1])


def test_MED():
  for S, T in test_cases:
      assert fast_MED(S, T) == MED(S, T)

def test_align():
  for i in range(len(test_cases)):
      S, T = test_cases[i]
      align_S, align_T = fast_align_MED(S, T)
      assert (align_S == alignments[i][0] and align_T == alignments[i][1])

test_MED()
test_align()