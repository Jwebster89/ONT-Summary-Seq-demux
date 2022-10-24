# ONT-Summary-Seq-demux
A script to automate subsetting a summary_seq.txt file into separate barcode files based on multiplex data

## Introduction
Ever wanted to run something like [minion_qc](https://github.com/roblanf/minion_qc), but your sequencing summary file contains all your multiplexed data? ONT-Summary-Seq-demux.py will take demultiplexed fastq files and your original sequencing_summary.txt and spit out a new sequencing_summary file of just the reads in the supplied fastq.

## Usage
ONT-Summary-Seq-demux.py requires three inputs
- Your original sequencing_summary.txt
- Your fastq of interest (e.g. all fastq from one barcoded concatenated into one file), gzipped.
- An ouput file directory/name

`ONT-Summary-Seq-demux.py sequencing_summary.txt data/barcode01.cat.fastq.gz sequencing_summary.barcode01.txt`
