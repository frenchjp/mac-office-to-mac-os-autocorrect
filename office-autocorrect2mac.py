# Microsoft Mac Office 2011 AutoCorrect To Mac OS X Keyboard Replace
# By Jim French
# http://www.frenchjim.com/
# https://www.linkedin.com/in/frenchjp
infilename = raw_input("Enter Microsoft Office input text file name: ")
try:
	infile = open(infilename,"r")
except:
	print 'File cannot be opened:',infilename
	exit()
outfilename = raw_input("Enter Mac keyboard output plist file name: ")
try:
	outfile = open(outfilename,"w")
except:
	print 'File cannot be opened:',outfilename
	exit()
outfile.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
outfile.write("<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">\n")
outfile.write("<plist version=\"1.0\">\n")
outfile.write("<array>\n")
while True:
	fromstring = infile.readline().strip().replace('&', '&amp;')
	tostring = infile.readline().strip().replace('&', '&amp;')
	# Break from while if fromstring is none and empty or blank
	if not fromstring:
		break
	# Don't write entry if it is not alphanumeric
	#if not fromstring.isalnum() or not tostring.isalnum():
	#	continue
	# show results
	print fromstring + " > " + tostring
	# write autocorrect entry to plist file
	outfile.write("	<dict>\n")
	outfile.write("		<key>phrase</key>\n")
	outfile.write("		<string>" + tostring + "</string>\n")
	outfile.write("		<key>shortcut</key>\n")
	outfile.write("		<string>" + fromstring + "</string>\n")
	outfile.write("	</dict>\n")
# ending tags
outfile.write("</array>\n")
outfile.write("</plist>\n")
# close the files
outfile.close()
infile.close()