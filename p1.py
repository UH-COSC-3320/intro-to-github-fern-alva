
def clean(s):
	result = ''
	for ch in s:
		if ch.isalpha():
			result += ch
	return result.upper()

def main():
	try:
		while True:
			line = input()
			line = line.strip()
			out = clean(line)
			if out:
				print(out)
			else:
				print()
	except EOFError:
		pass

if __name__ == '__main__':
	main()

