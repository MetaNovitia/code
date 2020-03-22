from os import system, listdir, mkdir

def cpp_checker(root, diff):
	pwd = f'{root}/work-folder'
	i_dir = f'{pwd}/data/input'
	o_dir = f'{pwd}/data/output'
	res_dir = f'{pwd}/data/result'
	try: mkdir(res_dir)
	except: pass
	system(f'rm -rf {res_dir}/*')
	inputs = sorted(listdir(i_dir))
	outputs = sorted(listdir(o_dir))

	system(f'g++-9 -std=c++11 {pwd}/code/code.cpp -o {pwd}/code/code')

	for ind in range(len(inputs)):
		i = inputs[ind]
		print(f'{ind}: {i}')
		system(f'{pwd}/code/code < {i_dir}/{i} > {res_dir}/{i}')
		if diff: 
			o = outputs[ind]
			system(f'diff {res_dir}/{i} {o_dir}/{o}')

def py_checker(root, diff):
	pwd = f'{root}/work-folder'
	i_dir = f'{pwd}/data/input'
	o_dir = f'{pwd}/data/output'
	res_dir = f'{pwd}/data/result'
	system(f'rm -rf {res_dir}/*')
	try: mkdir(res_dir)
	except: pass
	inputs = sorted(listdir(i_dir))
	outputs = sorted(listdir(o_dir))
	for ind in range(len(inputs)):
		i = inputs[ind]
		print(f'{ind}: {i}')
		system(f'python3 {pwd}/code/code.py < {i_dir}/{i} > {res_dir}/{i}')
		if diff: 
			o = outputs[ind]
			system(f'diff {res_dir}/{i} {o_dir}/{o}')