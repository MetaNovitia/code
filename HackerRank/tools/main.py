import new, sys, submit

if __name__ == "__main__":
	cmd = [""]
	while cmd[0]!="end":
		try: 
			print("----------------------------------------------------")
			cmd = input("command: ").split()
			if   cmd[0]=="new": new.main(cmd[1])
			elif cmd[0]=="open": new.open_dir(cmd[1])
			elif cmd[0]=="submit": submit.main()
			# elif cmd[0]=="save": 

		except: print(f"ERR: {sys.exc_info()[0]} {sys.exc_info()[1]} line: {sys.exc_info()[2].tb_lineno}")


