import tools, sys
from time import time

if __name__ == "__main__":

	cmd = [" "]
	tools.loadCache()
	while len(cmd):
		try: 
			if   cmd[0]=="new": tools.new(cmd[1])
			elif cmd[0]=="open": tools.open_dir(cmd[1])
			# elif cmd[0]=="login": tools.site["checker"].main()
			# elif cmd[0]=="save": 
			# 	if len(cmd)<2: cmd.append("py")
			# 	if len(cmd)<3: cmd.append(str(int(time()))+"-Save")
			# 	tools.site["checker"].save(cmd[2],cmd[1])
			elif cmd[0]=="clear": tools.copyTemplates()
			elif cmd[0]=="help": 
				print(
					"new [link]\nopen [link]\nlogin\nsave (ext) (fname)\n" + 
					"clear\nhelp")

		except: print(f"ERR: {sys.exc_info()[0]} {sys.exc_info()[1]} line: {sys.exc_info()[2].tb_lineno}")
		tools.saveCache()
		print("----------------------------------------------------")
		cmd = input("command: ").split()

