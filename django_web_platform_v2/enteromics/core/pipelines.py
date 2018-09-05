
class AutomatizedTool(object):
    """docstring for ExecuteTool."""
    def __init__(self, tool,filepath):
        super(ExecuteTool, self).__init__()
        self.tool = tool
        self.filepath = filepath

    def start(self):
        print ("Selected ", tool ," for genome analysis..."
        if(self.tool == 'Virulence Finder'):
            print '\nStarting Virulence Finder Data Analysis...\n\n\n'
            os.system("perl /home/icaro/virulence_finder/virulencefinder.pl -d database/ -i "+ self.filepath + "-o out_virulence" + "-s virulence_ent -k 85.00")
            print '\nVirulence Finder Data Analysis finished...\n\n\n'
