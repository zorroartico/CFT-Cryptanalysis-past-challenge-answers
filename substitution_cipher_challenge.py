ciphertext = 'ogrk hg tl`n srbszizrzig aiphgu mg ycahzylluf vllu fg ahcoogneg pceinc is ngzdluag'


wlist = {
		'key1': {'o':'l'},
		'key2': {'z':'t'},
		'key3': {'r':'u'},
		'key4': {'g':'e'},
		'key5': {'t':'z'},
		}

def decrypt():
	translated = ''
	for letter in ciphertext:
		if letter == 'o':
			letter = wlist['key1'].get('o')
			translated = translated + letter
		elif letter == 'z':
			letter = wlist['key2'].get('z')
			translated = translated + letter
		elif letter == 'r':
			letter = wlist['key3'].get('r')
			translated = translated + letter
		elif letter == 'g':
			letter = wlist['key4'].get('g')
			translated = translated + letter
		elif letter == 't':
			letter = wlist['key5'].get('t')
			translated = translated + letter
		else:
			translated += letter
			
	print(translated)
	
decrypt()

# Original statement: ogrk hg tl`n srbszizrzig aiphgu mg ycahzylluf vllu fg ahcoogneg pceinc is ngzdluag
# Hint they gave me: leuk he zo`n subst...
# First decrypt: leuk he zl`n substitutie aipheu me ycahtylluf vllu fe ahcllenee pceinc is netdluae

# Seems like l=o or vice versa, same for u=r. Then it becomes, leuk he zo'n susbstitutie (a=c)ipher me yachtyoord voor de challenge pagina is net(d=f)orce

# Second decrypt: netforce is the password.


