import pickle

def load(data):
  '''
  data is dict with filename keys 
  '''
  for el in data.keys():
    with open(el+'.pickle', 'rb') as f:
      data[el].extend(pickle.load(f))

def save(el, data):
  name = ''
  if isinstance(el, str):
    name = el.lower()
  else:
    name = el.__class__.__name__.lower()
  with open(name+'s.pickle', 'wb') as f:
    pickle.dump(data[name+'s'], f)