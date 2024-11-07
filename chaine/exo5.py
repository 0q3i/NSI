def concatener_inverser(l1,l2):
     if l1 is None:
          return l2
     else:
          return concatener_inverser(concatener_inverser(l1.suivante,l1),l2)