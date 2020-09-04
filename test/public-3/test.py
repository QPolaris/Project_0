import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import phonenumber
import pickle


answer = phonenumber('(123) 456-7890')
print(answer)
with open('output', 'wb') as f:
  pickle.dump(answer, f)
