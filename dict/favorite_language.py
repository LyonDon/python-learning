favorite_language={
	'jen': 'python',
	'sarah': 'C',
	'edword': 'Ruby',
	'Phil': 'python',
}
invested_p=['jen','sarah','dell','jack']
for person in invested_p:
	if person in favorite_language.keys():
		print('thanks '+person.title())
	else:
		print(person.title()+' please come to have a investment')
		pass
	pass