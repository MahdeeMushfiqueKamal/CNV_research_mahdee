# CNV_research_mahdee

## Copy Number Variation Estimation

### For Reference:

#### 1st step:

`wgsim -d 300 -N 7700000 -1 101 -2 101 reference.fa frag1_ref.fastq frag2_ref.fastq`

wgsim: This is the command to execute the WGSIM tool.
- -d 300: This parameter sets the base error rate to 0.3% (or 0.003) per base, representing the sequencing error rate.
- -N 7700000: This parameter sets the total number of read pairs to be simulated. In this case, it is set to 7,700,000 read pairs.
- -1 101: This parameter specifies the length of the first mate in the read pair. In this case, it is set to 101 bases.
- -2 101: This parameter specifies the length of the second mate in the read pair. Again, it is set to 101 bases.
- reference.fasta: This is the input file containing the reference genome in FASTA format.
- frag1_ref.fastq: This is the output file where the simulated reads for the first mate will be written in FASTQ format.
- frag2_ref.fastq: This is the output file where the simulated reads for the second mate will be written in FASTQ format.

#### 2nd Step:

`./bowtie2-build reference.fa bias`
This command creates an index of the reference genome (reference.fa) using Bowtie 2. The index will be stored in files with the prefix "bias" for future alignment.

`./bowtie2 -p 4 -k 15 --no-mixed -x bias -1 frag1_ref.fastq -2 frag2_ref.fastq -S biasOut.sam`

This command performs the alignment of paired-end reads (frag1_ref.fastq and frag2_ref.fastq) to the reference genome index ("bias") using Bowtie 2. Here's a breakdown of the options used:

- -p 4: Specifies the number of CPU threads to use (in this case, 4 threads).
- -k 15: Sets the maximum number of alignments to report per read (up to 15 alignments).
- --no-mixed: Disables reporting of alignments involving both mates from the same read.
- -x bias: Specifies the prefix of the Bowtie 2 index to use for alignment.
- -1 frag1_ref.fastq: Specifies the file containing the first mate (read 1) of the paired-end reads.
- -2 frag2_ref.fastq: Specifies the file containing the second mate (read 2) of the paired-end reads.
- -S biasOut.sam: Specifies the output file where the aligned reads will be stored in SAM format.

#### 3rd Step
`g++ -o bowtie2convert bowtie2convert.cpp` - compiling the C++ source code file "bowtie2convert.cpp" into an executable named "bowtie2convert 

`./bowtie2convert biasOut.sam reference.fa 300` - todo: what does this program do?
