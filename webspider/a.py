def FinStr(matchfile):
	f=open(matchfile)
	for line in f:
		if line.startswitch("username"):
			print line
	f.close()
