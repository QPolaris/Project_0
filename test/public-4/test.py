import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import cuberoot
import pickle


answer = cuberoot(-125)
print(answer)
with open('output', 'wb') as f:
  pickle.dump(answer, f)
