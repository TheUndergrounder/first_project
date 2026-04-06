from dotenv import load_dotenv
import os

load_dotenv()
author = os.getenv('AUTHOR')

def print_author():
	print(f'Автор: {author}')
print('hello from repo')
print_author()
