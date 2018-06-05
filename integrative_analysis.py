import sys,os
#arguments
input_genome_dir=str(sys.argv[1])
output_analysis_dir=str(sys.argv[2])


print '\nStarting PhiSpy Data Analysis...\n\n\n'
os.system("./PhiSpy.py -i " + input_genome_dir + " -o " + output_analysis_dir + " -t 0")
print '\nPhiSpy Data Analysis finished...\n\n\n'


print 'calling R Script to filter prophage regions from PhiSpy...\n' 
os.system("Rscript --vanilla filter_dataset.R "+ output_analysis_dir)

#finished
print 'Thanks for using JAMIRA...\n'
