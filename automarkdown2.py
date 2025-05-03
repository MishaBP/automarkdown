import sys
import argparse
import datetime 
import os 
import markdown
import dos2unix

filename = "tempfile.txt"

current_dir = os.getcwd() # Current Working Directory(CWD,shell)
# code
code = ""
#current date 
taday_date = datetime.date.today()

# Parser 
parser = argparse.ArgumentParser(description="Programm for generation markdown files")
# Аргументы
parser.add_argument('name', type=str, help='Имя файла')
parser.add_argument('--tags', type=str,nargs='+', help='тегги')
parser.add_argument('--text', type=str,nargs='+', help='описание')
parser.add_argument('--language', type=str,nargs='+', help='описание')
parser.add_argument('-v', '--verbose', action='store_true', help='Подробный вывод')

# Распарсим аргументы
args = parser.parse_args()

formatted_tags ="\n".join(args.tags)
formatted_language = ''.join(args.language)
formatted_text = ' '.join(args.text)
# формирование строки
def make_md_str() -> str:
    return (f'---\n'		
		f'создал заметку: {taday_date}\n'
		f'tags  \n'
		f'{formatted_tags} \n'
		f' {formatted_text} \n'
		f'\n'
		f'```{formatted_language}\n'
		f'{code}\n'
		f'```\n')
md_text = make_md_str()
#print(md_text)

with open(filename, 'w', encoding='utf-8') as file:
    file.writelines(md_text)

dos2unix.convert_file(filename,'test3.md')