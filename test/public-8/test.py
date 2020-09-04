import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import cartesianproduct
import pickle


answer = frozenset(cartesianproduct([{1},{2},{3,4,5}]))
print(answer)
with open('output', 'wb') as f:
  pickle.dump(answer, f)
