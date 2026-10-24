import json

l, lp, g = 500, [], {} # (limit, list of primes, groups)

for n in range(2, l+1): 
  c = 1
  for i in lp: c *= 0 if n % i == 0 else 1
  if c: lp.append(n)

for i in range(len(lp)-1):
  d = lp[i+1]- lp[i] # (difference between primes)
  p = f"{lp[i+1]}, {lp[i]}" # (pair of primes)
  if d in g.keys(): g[d].append(p)
  else: g[d] = [p]

with open("groupings.json", "w") as f: # (file)
  json.dump(g, f, indent= 2)

# time to complete -> 29:45.83
# date and time of official completion -> 2026-10-24 18:45:22.763185
# 17 lines of code
# 333 characters


''' AI's model code (this is for comparison)

import json

lim, ps, gps = 100, [], {}
for n in range(2, lim + 1):
  if all(n % p for p in ps): ps.append(n)
for i in range(len(ps) - 1):
  d, a = ps[i + 1], ps[i]
  gps.setdefault(d - a, []).append(f"{d}, {a}")
with open("groupings.json", "w") as f: json.dump(gps, f, indent=2)

# 9 lines of code
# 279 characters

'''