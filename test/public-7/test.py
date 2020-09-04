import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import evalsum
import pickle


answer = evalsum("1+1.2-4.34343434000")
print(answer)
with open('output', 'wb') as f:
  pickle.dump(answer, f)
