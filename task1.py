def read(file_name):
	with open(file_name, 'r') as file :
		text = file.read()

	word = text.split()

	print(word)


read("sample.txt")
