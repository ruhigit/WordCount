import sys
def count_words(ip,op):
	##Open the files
		with open(ip,'r') as inputfile:
			with open(op,'w') as outputfile:
				
				##read input file each line at a time
				for line in inputfile:
					count=len(line.split())	##split on whitespace
					output=str(count)	##convert to string
					outputfile.write(output+"\n")##write to output file
					
			outputfile.closed
			
		inputfile.closed
	
def main():
	##print len(sys.argv) 
	##check number of arguments
	if len(sys.argv)<2:
		print ("Provide input and output file names as parameters")
		
	else: 
		##print "Input file:",sys.argv[1]
		##print "Output file:",sys.argv[2]
		count_words(sys.argv[1],sys.argv[2])
		
		
	return
if __name__=="__main__":
	main()
