import sys, getopt
import datetime
import os
def main(argv):
	dateFile = ''
	nameOfScript = ''
	try:
		opts, args = getopt.getopt(argv,"hd:n:",["dateFile=","nameOfScript="])
	except getopt.GetoptError:
		print 'createWorkoutScript.py -d <dataFile> -n <nameOfScript>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'createWorkoutScript.py -d <dataFile> -n <nameOfScript>'
			sys.exit()
		elif opt in ("-d", "--dateFile"):
			dateFile = arg
		elif opt in ("-n", "--nameOfScript"):
			nameOfScript = arg
	print 'dateFile file is "', dateFile
	print 'nameOfScript will be "', nameOfScript
	
    #get arguments from cmd
	datafileWithPYExtension, file_extension = os.path.splitext(nameOfScript)
	datafileWithPYExtension+=".py"
	lines = [line.rstrip('\n') for line in open(dateFile,"r+")]
	additionalScriptFile = open(datafileWithPYExtension,"w+") 
	additionalScriptFile.truncate(0)
	#CreateDate
	todayDate = str( (datetime.datetime.today()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d"))
	print("Starting Workout AT" +str(todayDate))
	#write packages
	import subprocess
	additionalScriptFile.write("""import subprocess
import datetime
import sys
""")
	#write date to file
	additionalScriptFile.write("""dateOfStart="%(todayDate)s"
""" %locals())
	#write function
	additionalScriptFile.write("""def getWorkout(argument):
	switcher = {
	""")
	#write "switch"
	for workoutNumber,workout in enumerate(lines):
		additionalScriptFile.write("""    %(workoutNumber)i : "%(workout)s",
	""" % locals())
	additionalScriptFile.write("""}
	return switcher.get(argument,"nothing")
""")
	#calculate current workout day
	additionalScriptFile.write("""workout = getWorkout((datetime.datetime.strptime(dateOfStart, '%Y-%m-%d').date() - datetime.datetime.today().date()).days)
print("Workout -> " + str(workout))
""")
	additionalScriptFile.write("""if workout is "nothing":
	print("zwrocilo nothing, blad")
	sys.exit()
""")
	additionalScriptFile.write("""p = subprocess.Popen(["vlc",workout])
""")

	additionalScriptFile.close();
if __name__ == "__main__":
   main(sys.argv[1:])

