#Adiel Garcia Tavarez

from lwz_decode import decode

def encode(input):
	encoded_password = ''
	for char in input:
		encoded_password += str(int(char) + 3)
	return encoded_password

def main():
	password = ''
	while True:
		print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
		choice = int(input('Please enter an option: '))
		if choice == 1:
			password = encode(input('Please enter your password to encode: '))
		elif choice == 2:
			print(f'The encoded password is {password}, and the original password is {decode(password)}')
		elif choice == 3:
			break

if __name__ == '__main__':
	main()
