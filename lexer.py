KEYWORDS=["auto","break","case","char","const","continue","default","do","double","else","enum","extern","float","for","goto","if","int","long","register","return","short","signed","sizeof","static","struct","switch","typedef","union","unsigned","void","volatile","while"]
UnGetch= 'ungetch'
GLOB="0123456789abcdefghijklmnoqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ;,.()[]}{\"=+-*/!<_>&|$” \\ \n" + ""
digit='0123456789'
punctuation = "}{)(][;,."
letter='abcdefghijklmnoqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
space='\n\t '
symboltable = []

STATES={
	'start_state':[
		('int',digit,None),
		('lower_than','<',None),
		('grater_than','>',None),
		('assign','=',None),
		('not','!',None),
		('id',letter+'_',None),
		('sub','-',None),
		('start_state',space,None),
		('comment', '/' , None),
		('punctuation', punctuation, None),
		('str', "”", None)
	],
	#punctuation
	'punctuation' : [
		('punctuation', punctuation, 'punctuation'),
		('start_state', space, 'punctuation'),
		('comment', '/', 'punctuation'),
		('assign', '=', 'punctuation'),
		('id', letter + '_', 'punctuation'),
		('int', digit, 'punctuation'),
		('start_state', '\n', 'punctuation')
	],
	#id
	'id':[
		('id',letter+digit+'_',None),
		('start_state',space,'id'),
		('assign', '=', 'id'),
		('lower_than', '<', 'id'),
		('grater_than', '>', 'id'),
		# ('assign', '=', 'int'),
		('plus', '+', 'id'),
		('punctuation', punctuation, 'id'),
	],
#	#comment
	'comment': [
		('comment', '/', None),
		('start_state', '\\', None),
		('multiline', '*', None),
		('start_state', '\n', None),
	],
	# 'commente':[
	# 	('start_state', 'n', 'comment'),
	# 	('comment', '')
	# ],
	'multiline' : [
		('e_multiline', '*', None),
		# ('multiline',, None),
		('e_multiline', '*', None)
	],
	'e_multiline' : [
		('start_state', '/', None),
		('multiline', '*', None)
	],
	#string
	'str': [
		('start_state', "”" ,'str'),
		# ('str', GLOB + !GLOB, 'str'),
		('punctuation', punctuation, 'str')
	],
	#relop
	'lower_than':[
		('le','=',None),
		('int',digit,'lower_than'),
		('id',letter+'_','lower_than'),
		('start_state',space,None),
	],
	'grater_than':[
		('ge','=',None),
		('int',digit,'grater_than'),
		('id',letter+'_','grater_than'),
		('start_state',space,None),
	],
	'assign':[
		('equal','=',None),
		('int',digit,'assign'),
		('id',letter+'_','assign'),
		('start_state',space,'assign'),
		# ('')
		('str', "”" ,'assign'),
		('assign2', '-', UnGetch)
	],
	'assign2':[
		('start_state', space, None),
		('int', digit, None)
	],
	'not':[
		('not_equal','=',None),
		('int',digit,'not'),
		('id',letter+'_','not'),	
		('start_state',space,None),
	],
	'le':[
		('int',digit,'lower_and_equal'),
		('id',letter+'_','lower_and_equal'),
		('start_state',space,None),

	],
	'ge':[
		('int',digit,'grater_and_equal'),
		('id',letter+'_','grater_and_equal'),
		('start_state',space,None),

	],
	'equal':[
		('int',digit,'equal'),
		('id',letter+'_','equal'),
		('start_state',space,None),
	],
	'not_equal':[
		('int',digit,'not_equal'),
		('id',letter+'_','not_equal'),
		('start_state',space,None),
	],
#	#number abcdefghijklmnoqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ([{}\"=+-*/!<>&|
#int
	'int':[
		('int',digit,None),
		('pre_real','.',None),
		('pre_sci1','eE',None),
		('start_state',space,'int'),
		('lower_than', '<', 'int'),
		('grater_than', '>', 'int'),
		('assign', '=', 'int'),
		('punctuation', punctuation, 'int')
		# ('semi_colon',';','int'),
		# ('comma',';','int'),
		# ('parentheses_close',')','int'),
		# ('bract_close',']','int'),
	],
	'pre_real':[
		('real',digit,None),
		('punctuation', punctuation, UnGetch),
		#('start_state',space,None),
	],
	'real':[
		('real',digit,None),
		('pre_sci1','eE',None),		
		('start_state',space,'real'),
		('lower_than', '<', 'real'),
		('grater_than', '>', 'real'),
		('assign', '=', 'real'),
		('punctuation', punctuation, None),
	],
	'pre_sci1':[
		('pre_sci2','+-',None),
		('sci',digit,None),
		('start_state',space,None),
	],
	'pre_sci2':[
		('sci',digit,None),
		('start_state',space,None),
	],
	'sci':[
		('sci',digit,None),
		('start_state',space,'sci'),
		('lower_than', '<', 'sci'),
		('grater_than', '>', 'sci'),
		('assign', '=', 'sci'),
		('punctuation', punctuation, 'sci')
	],
	#operation
	'sub':[
		('int',digit,'sub'),
		('id',letter+'_','sub'),
		('start_state',space, 'sub'),
		('subsub', '-', None)
	],
	'plus': [
		('int', digit, 'plus'),
		('id', letter + '_', 'plus'),
		('start_state', space, 'plus'),
		('plusplus', '+' , UnGetch),

	],
	'subsub': [
		('start_state',space,'subsub')
	],
	'plusplus': [
		('start_state', space, 'plusplus'),
		('punctuation', punctuation, None)
		# ('start')
	],
}

# inp='int _number_One1 = 8889 //نشانه پایانی فراموش شده ودر این فاز پروژه مهم نیست  ;'
# inp='char myS[]=”sampleکلمه ٪٪٪Sample”;'
# inp='//condition'
# inp='if(_number_One1 >900)$'
# inp='/*some \
# comment*/'
# inp='_number_One1++; } \
inp="""int _number_One1 = 8889 //نشانه پایانی فراموش شده ودر این فاز پروژه مهم نیست  ;
char myS[]=”sampleکلمه ٪٪٪Sample”;
//condition
if(_number_One1 >900)
{
کاراکترفارسی یا ناشناخته در زبان سی در جای نامناسب که گاهی فاصله بین آنهاست
/*some
comment*/
_number_One1++;
}
double abcd=-45.4e22 ;$"""
current_state='start_state'
token=[]
output = []
#print(s)
for c in inp:
	token+=c
	if GLOB.find(c) != -1 or current_state == 'comment' or current_state == 'multiline' or current_state == 'e_multiline' or current_state == 'str': # check kone k asn has tu dayere loqat ya na
		if c == '$':
			tt = ''.join(token[0:len(token) -1])
			output.append(current_state + '\t' + ''.join(tt))
		else:
			for t in STATES[current_state]: 
				if c in t[1]: # mitune in state bashe ya na
					current_state=t[0]
					if t[2] is UnGetch: # vase unget kardane
						output.pop()
						output.append('ungetch')
						output.append(current_state +'\t'+''.join(token))
						token = [token[len(token) -1]]
						token =[]
					elif t[2] is not None:
						tt = ''.join(token[0:len(token) -1])
						if (t[2] == 'str' and current_state == 'start_state'):
							tt = ''.join(token)
						if t[2] == 'id':
							if tt in KEYWORDS:# fqt idie k mitune keyword bashe
								output.append('keyword' + '\t'+''.join(tt))
							else:
								output.append(t[2] + '\t'+''.join(tt))
								for s in symboltable:
									if s == ''.join(tt):
										output.append('false')
								if output[len(output) -1] != 'false': #akhari
									symboltable.append(''.join(tt))
									output.append('true')
						# elif t[2] == 'str':
						# 	pass
							tt = ''.join(token[0:len(token) -1])
						else: # agar id nabud mese halate adi append kon
							output.append(t[2] + '\t'+''.join(tt))
						# token = []
						if token[len(token) -1] == ' ':
							token = []
						else:
							token= [token[len(token) -1]]
					# token+=c
					if current_state == 'start_state':
						token = ''
					break
	else:
		# print('error\n')
		# output.append()
		if current_state != 'start_state':
			output.append(current_state + '\t' + ''.join(token[0: len(token) -1]))
			token = []
			current_state = 'start_state'
		output.append('error')
		
for c in output: 
	print(''.join(c) + '\n');


print('\n\n**********symbol table**********\n\n')
for i in symboltable:
	print(i + '\n')
# s = '\n'
# if s in '\n':
# 	print('yess')
