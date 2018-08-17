import string 
s = string.ascii_lowercase[:]
s = awefgrhtjyukiluouikyujtyhtrgdrsfdc
d = {}
for i in s:
	if i not in d:
		d[i] = 1
	else:
		d[i] += 1
print(d)

d_reverse = {}
for k in d:
	if d[k] not in d_reverse:
		d_reverse[d[k]] = []
		d_reverse[d[k]].append(k)
	else:
		d_reverse[d[k]].append(k)
print(d)