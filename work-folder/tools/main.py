import tools, sys, os
from time import time
from config import help_string, root

if __name__ == "__main__":

	try: os.mkdir(f'{root}/work-folder/code')
	except: pass
	try: os.mkdir(f'{root}/work-folder/data')
	except: pass

	cmd = [" "]
	tools.loadCache()
	while len(cmd):
		option = cmd.pop(0)
		try: 
			if   option=="new"	: tools.new(cmd[0])
			elif option=="open"	: tools.open_dir(cmd[0])
			elif option=="login": tools.login()
			elif option=="save"	: tools.saveSolution(*cmd)
			elif option=="clear": tools.copyTemplates()
			elif option=="rm"	: tools.removeFile()
			elif option=="post"	: tools.post(*cmd)
			elif option=="check": tools.check(True, *cmd)
			elif option=="run"	: tools.check(False, *cmd)
			elif option=="help"	: print(help_string)

		except: print(
			f"ERR: {sys.exc_info()[0]} {sys.exc_info()[1]} "+
			f"line: {sys.exc_info()[2].tb_lineno}")

		print("----------------------------------------------------")
		tools.saveCache()
		cmd = input("command: ").split()
	
	if tools.site["checker"].driver!=None:
		tools.site["checker"].driver.quit()

	try: 
		f=open(geckodriver.log,'r')
		f.close()
		os.system("rm geckodriver.log")
	except: pass

