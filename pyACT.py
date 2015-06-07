#imports are declared here
import sys
import msvcrt as m

def calculate(englishraw, mathraw, readingraw, scienceraw, writingraw):
	#Correction factors: English=-2, math=+1, reading=+2, science==1.5
	engcorrectfactor = -2
	engscaled = round((englishraw * 36 / 75) + engcorrectfactor)
	matcorrectfactor = 1
	matscaled = round((mathraw * 36 / 60) + matcorrectfactor)
	redcorrectfactor = 2
	redscaled = round((readingraw * 36 / 40) + redcorrectfactor)
	scicorrectfactor = 1.5
	sciscaled = round((scienceraw * 36 / 40) + scicorrectfactor)

	#specific case correction
	if engscaled < 1:
		engscaled = 1

	#debugging
	print('\nEnglish score: ' + str(engscaled))
	print('Mathematics score: ' + str(matscaled))
	print('Reading score: ' + str(redscaled))
	print('Science score: ' + str(sciscaled))

	engfinal = getwriting(engscaled, writingraw)
	print('Composite english scaled score: ' + str(engfinal))
	composite = (engfinal + matscaled + redscaled + sciscaled) / 4

	return composite

def getwriting(englishraw, writingraw):
	table = {}
	purestring = """1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 
					2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 11, 
					2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 
					3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 
					4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 13, 
					5, 6, 7, 7, 8, 9, 10, 11, 12, 13, 14, 
					5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
					6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 
					7, 8, 9, 10, 11, 12, 13, 13, 14, 15, 16, 
					8, 9, 9, 10, 11, 12, 13, 14, 15, 16, 17, 
					8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 
					9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
					10, 11, 12, 13, 14, 14, 15, 16, 17, 18, 19, 
					10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
					11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 
					12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 21, 
					13, 14, 15, 16, 16, 17, 18, 19, 20, 21, 22, 
					13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 
					14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 
					15, 16, 17, 18, 19, 20, 21, 21, 22, 23, 24, 
					16, 17, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
					16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 
					17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 
					18, 19, 20, 21, 22, 23, 23, 24, 25, 26, 27, 
					18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 
					19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 
					20, 21, 22, 23, 24, 25, 26, 27, 28, 28, 29, 
					21, 22, 23, 24, 24, 25, 26, 27, 28, 29, 30, 
					21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 
					22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 
					23, 24, 25, 26, 27, 28, 29, 30, 30, 31, 32, 
					24, 25, 25, 26, 27, 28, 29, 30, 31, 32, 33, 
					24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 
					25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 
					26, 27, 28, 29, 30, 31, 31, 32, 33, 34, 35, 
					26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36"""
	puredata = purestring.split(', ')
	#List english score then writing score to create composite english score
	#Encode with english score from 1-36 and essay from range 2-12
	for english in range(1,37):
		for essay in range(2,13):
			# +1 appended to compensate for starting on 0 in array
			placehold = ((english-1)*11)
			table[(english, essay)] = puredata[placehold+(essay-2)]
	return int(table[englishraw, writingraw])

def numbererror():
	print('Not a number')
	sys.exit()

def main():
	print('\nACT calculator')
	warning = """Warning: Correction factor for scaled scores varies based on several factors. It is an estimate cited from McGraw-Hill's estimation for average scores. This is not an official scoring method."""
	print('\n' + warning + '\n')
	
	try:
		eng = mode=int(raw_input('Enter amount of correct english answers out of 75 questions:'))
	except ValueError:
		numbererror()

	try:
		mat = mode=int(raw_input('Enter amount of correct mathematics answers out of 60 questions:'))
	except ValueError:
		numbererror()

	try:
		red = node=int(raw_input('Enter amount of correct reading answers out of 40 questions:'))
	except ValueError:
		numbererror()

	try:
		sci = mode=int(raw_input('Enter amount of correct science reasoning answers out of 40 questions:'))
	except ValueError:
		numbererror()

	try:
		wri = mode=int(raw_input('Enter writing score out of 12 points:'))
	except ValueError:
		numbererror()

	if eng < 0 or eng > 75:
		print('English score is out of parameters')
	elif mat < 0 or mat > 60:
		print('Math score is out of parameters')
	elif red < 0 or red > 40:
		print('Reading score is out of parameters')
	elif sci < 0 or sci > 40:
		print('Science score is out of parameters')
	elif wri < 2 or wri > 12:
		print('Writing score is out of parameters')
	else:
		finalscore = calculate(eng, mat, red, sci, wri)
		print('\nPure composite score: ' + str(finalscore))
		simplescore = round(finalscore, 0)
		print('Actual composite score: ' + str(simplescore))
		print('\nPress any key to restart the program and press ESC to exit')
		userinput = m.getch()
		if userinput == chr(27).encode():
			sys.exit()
		else:
			main()

if __name__ == "__main__":
	main()