def repeatedSubstringPattern(str):
	if not str:
		return False
	ss = (str+str)[1:-1]
	return ss.find(str)!=-1
	
