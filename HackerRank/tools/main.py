import new, sys, submit
from time import time

if __name__ == "__main__":
	cmd = [" "]
	while len(cmd):
		try: 
			print("----------------------------------------------------")
			if   cmd[0]=="new": new.main(cmd[1])
			elif cmd[0]=="open": new.open_dir(cmd[1])
			elif cmd[0]=="login": submit.main()
			elif cmd[0]=="save": 
				if len(cmd)<2: cmd.append("py")
				if len(cmd)<3: cmd.append(str(int(time()))+"-Save")
				submit.save(cmd[2],cmd[1])

		except: print(f"ERR: {sys.exc_info()[0]} {sys.exc_info()[1]} line: {sys.exc_info()[2].tb_lineno}")
		cmd = input("command: ").split()

