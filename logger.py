from __future__ import print_function
import time
import os
import pprint
import csv



CIs = [] # {"timestamp:":int, "participant_name":"asdf", "CI":"incident descriptor"}
y = str(time.localtime().tm_year)
mo = str(time.localtime().tm_mon)
d = str(time.localtime().tm_mday)
h = str(time.localtime().tm_hour)
m = str(time.localtime().tm_min)
s = str(time.localtime().tm_sec)

helpScreen = "\n[commands]===========\n    + /exit := exits writes the csv and exits the app\n    + /reset := resets all data"
commands = ["/exit","/reset","/help"]

print("logging initiated at: ",str(h)+":"+str(m)+"."+str(s))
pName = raw_input("enter participant name: ")

os.system('cls')
startTime = time.time()

fileName = y+mo+d+"_"+h+m+"h"+"_"+pName

def writeCSV(data,filename):
	with open(filename+".csv","wb") as csvfile:
		fieldnames = data[0].keys()
		writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
		writer.writeheader()
		writer.writerows(data)

def main():
	global startTime
	global CIs
	global fileName
	while True:
		os.system('cls')
		# pprint.pprint(CIs)
		if (len(CIs)>0): print("\nLAST INCIDENT:",CIs[len(CIs)-1])
		CI = raw_input("critical incident: ")
		delta = time.time()-startTime

		if CI == commands[0]: # exit
			os.system('cls')
			print("writing csv data to: ",fileName+".csv")
			writeCSV(CIs,fileName)
			print("writing successful! Have a good day ;-)")
			print("Press [RETURN] to exit")
			raw_input()
			exit()	
		elif CI == commands[1]: # reset
			os.system('cls')
			print('reset data, are you sure? [Y/n]')
			response = raw_input()
			if (response == "Y") or (response == "y") or (response == "yes"):
				CIs = []
				print("Data reset!\nTimer still running with",time.time()-startTime,"total elapsed time.\nPress [ENTER] to continue")
				raw_input()
			
		elif CI == commands[2]: # help
			os.system('cls')
			print(helpScreen)
			CI = raw_input("critical incident: ")
		else:
			CIs.append({"timestamp":delta,"CI":CI})


main()