import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import is_leapday
import pickle


answer = is_leapday("Feb 29, 2008 3:00:00pm")
print(answer)
with open('output', 'wb') as f:
  pickle.dump(answer, f)
