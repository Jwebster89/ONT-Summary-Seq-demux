#!/usr/bin/env python3

import gzip, sys
import pandas as pd
from Bio import SeqIO

summary_file=sys.argv[1]
fastq_gzipped=sys.argv[2]

def get_fastq_headers(fastq_gzipped):
	IDS=[]
	with gzip.open(fastq_gzipped, "rt") as handle:
		for record in SeqIO.parse(handle, "fastq"):
			IDS.append(record.id)
	return(IDS)

def subset_sequencing_summary(summary_file,fastq_gzipped):
	df=pd.read_csv(summary_file, sep='\t')
	df2 = df[df['read_id'].isin(fastq_gzipped)]
	file_name=sys.argv[3]
	df2.to_csv(file_name, sep='\t', index=False)


def main():
	subset_sequencing_summary(summary_file, get_fastq_headers(fastq_gzipped))


if __name__ == "__main__":
	main()