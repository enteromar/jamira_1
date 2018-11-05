import os
class AutomatizedTool(object):
    """docstring for ExecuteTool."""
    def __init__(self, tool,filepath):
        #super(AutomatizedTool, self).__init__()
        self.tool = tool
        self.filepath = filepath

    def start(self):
        print ("Selected ", self.tool ," for genome analysis...")
<<<<<<< HEAD
        #print ("path: ", self.filepath)
        if(self.tool == 'VirulenceFinder'):
            print ('\nStarting Virulence Finder Data Analysis...\n\n\n')
            #command = "perl /home/icaro/virulence_finder/virulencefinder.pl -d /home/icaro/virulence_finder/database/ -i " + self.filepath + " -o results/out_virulence -s virulence_ent -k 85.00"
=======
        fullpath=self.filepath.rsplit("/",1)[0] # get the analysis path
        if(self.tool == 'VirulenceFinder'):
            print ('\nStarting Virulence Finder Data Analysis...\n\n\n')
            command = "cd "+ fullpath + " ; perl /home/icaro/virulence_finder/virulencefinder.pl -d /home/icaro/virulence_finder/database/ -i " + self.filepath + " -o out_virulence -s virulence_ent -k 85.00"
>>>>>>> 882bbffb87e5e2e0c0a425f3bbe90ceabbbe7e99
            #print(command)
            os.system(command)
            print ('\nVirulence Finder Data Analysis finished...\n\n\n')
        if(self.tool == 'RGI'):
            print ('\nStarting RGI Data Analysis...\n\n\n')
            command = "cd "+ fullpath + " ; mkdir out_resistance/ ; rgi main -i "+ self.filepath + " -o out_resistance/out_resistance -t contig -n 4 -a BLAST"
            #print(command)
            os.system(command)
            print ('\nRGI Data Analysis finished...\n\n\n')
        if(self.tool == 'PhySpy'):
            print ('\nStarting Physpy Data Analysis...\n\n\n')
