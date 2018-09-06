import os
class AutomatizedTool(object):
    """docstring for ExecuteTool."""
    def __init__(self, tool,filepath):
        #super(AutomatizedTool, self).__init__()
        self.tool = tool
        self.filepath = filepath

    def start(self):
        print ("Selected ", self.tool ," for genome analysis...")
        if(self.tool == 'Virulence Finder'):
            print ('\nStarting Virulence Finder Data Analysis...\n\n\n')
            command = "perl /home/icaro/virulence_finder/virulencefinder.pl -d /home/icaro/virulence_finder/database/ -i " + self.filepath + " -o out_virulence -s virulence_ent -k 85.00"
            print(command)
            os.system(command)
            print ('\nVirulence Finder Data Analysis finished...\n\n\n')
        if(self.tool == 'RGI'):
            print ('\nStarting RGI Data Analysis...\n\n\n')
            command = "rgi main -i "+ self.filepath + " -o resistance_out/ -t contig -n 4 -a BLAST"
            print(command)
            os.system(command)
            print ('\nRGI Data Analysis finished...\n\n\n')
