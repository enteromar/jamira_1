#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)
# test if there is at least one argument: if not, return an error
if (length(args)==0) {
	stop("At least one argument must be supplied (input file).n", call.=FALSE)
} else if (length(args)==1) {
	# retrieving data from params
	prophage_file="prophage_tbl.txt"
	prophage_result_dir=args[1]
	filtered_result_filename="prophage_tbl_filtered.txt"
	#opening file
	dataset <- read.delim(paste(prophage_result_dir,prophage_file, sep=""))
	#filtering by prophage gene like final status
	filtered = dataset[dataset$Final_status=='1',]
	#writing file
	print(paste("output saved at ",prophage_result_dir,filtered_result_filename,"...",sep=""))
	write.table(filtered, paste(prophage_result_dir,filtered_result_filename, sep=""), sep="\t")
}