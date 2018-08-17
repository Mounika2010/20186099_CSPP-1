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
