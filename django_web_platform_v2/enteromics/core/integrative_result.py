import os
#from process_result import
import pandas
import csv
from os import listdir
from os.path import isfile, join


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


def filter_results(organism_name,filepath_v,filepath_r):
    vir=ResultFile(virulence_column,filepath_v)
    res=ResultFile(resistance_column,filepath_r)
    row_data=[organism_name,get_columns(vir.filepath,vir.column),get_columns(res.filepath,res.column)]
    return row_data




class IntegrativeResult(object):
    """object used to """
    def __init__(self, vir_path,resistance_path):
        self.vir_path = vir_path
        self.res_path = resistance_path

    def start(self,filename,path):
        data = []
        data.append(filter_results(filename,self.vir_path,self.res_path))
        df = pandas.DataFrame(data,columns=["Organism","Virulence factors","Resistance Genes"])
        print("writing and saving file...")
        df.to_csv(path+'integrative_analysis.csv')



##################### PROCESS PIPELINE #############################
mypath="genomas"
virulence_column="Virulence factor"
resistance_column="Best_Hit_ARO"
