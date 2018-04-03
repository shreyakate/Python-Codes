def ReverseVowels(s):
	vowels = ['a','e','i','o','u']
	l,r= 0, len(s)-1
	while l < r:
		if s[l] not in vowels and s[r] not in vowels:
			l +=1
			r -= 1
		elif s[l] not in vowels:
			l += 1
		elif s[r] not in vowels:
			r -= 1
		else:
			s = s[:l]+s[r]+s[l+1:r]+s[l]+s[r+1:]
			l += 1
			r -= 1
	return s


print ReverseVowels("I am very much hotter")