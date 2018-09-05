class ExecuteTool(object):
    """docstring for ExecuteTool."""
    def __init__(self, tool,filepath):
        super(ExecuteTool, self).__init__()
        self.tool = tool
        self.filepath = filepath
    print ("Starting ", tool ," genome analysis..."
    if(tool=="Virulence Finder"):
        print '\nStarting Virulence Finder Data Analysis...\n\n\n'
        os.system("./PhiSpy.py -i " + input_genome_dir + " -o " + output_analysis_dir + " -t 0")
        print '\Virulence Finder Data Analysis finished...\n\n\n'
