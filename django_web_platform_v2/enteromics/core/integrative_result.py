import os
import pandas
import csv

class ResultFile(object):
    """object used to encapsulate the file and his specific column to be processed and filtered"""
    def __init__(self, column,filepath):
        #super(AutomatizedTool, self).__init__()
        self.column = column
        self.filepath = filepath


def get_columns(filepath,column):
    df = pandas.read_csv(filepath, sep='\t')
    annotated_genes = df[column].tolist()

    #join list in a string separated by ';'
    annotated_genes = '; '.join(annotated_genes)
    print("\n\nannotated_genes:",annotated_genes,"\n\n")
    return annotated_genes


#virulence and resitance paths and columns
filepath_v="C:/Users/icaromsc/Documents/django/jamira/django_web_platform_v2/enteromics/out_virulence/results_tab.txt"
virulence_column="Virulence factor"
filepath_r="C:/Users/icaromsc/Documents/django/jamira/django_web_platform_v2/enteromics/media/analysis_requests/001/out_resistance/out_resistance.txt"
resistance_column="Best_Hit_ARO"

vir=ResultFile(virulence_column,filepath_v)
res=ResultFile(resistance_column,filepath_r)
#results = [vir,res]

print("filtering columns of results...")

#list to represent the organism and his genomic elements
row_data=['E_hirae_DMW-1',get_columns(vir.filepath,vir.column),get_columns(res.filepath,res.column)]

#for result in results:
    #df = pandas.read_csv(result.filepath, sep='\t')
    #print(df,"\n\n")
    #annotated_genes = df[result.column].tolist()
    #print(annotated_genes,"\n\n")
    #raw_data.append(get_columns(result.filepath,result.column))
print(row_data)

print("saving results to dataset...")
#create and save integrative result dataset
data = [row_data]
df = pandas.DataFrame(data,columns=["Organism",virulence_column,"Resistance Genes"])
print("writing and saving file...")
df.to_csv('output.csv')
