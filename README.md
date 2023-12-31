# CNV_research_mahdee

## Copy Number Variation Estimation

### For Reference:

#### 1st step:

**Calculating number of read pairs (N):**
- lineCount =  `cat [testfileName].fa | wc -l``
- readCount =  lineCount * 50 *30 / 202
- `50`: Each DNA sequence (read) is assumed to be 50 base pairs long, 
- `30`: 30X coverage, 
- `202`: Length of the DNA Fragment

`wgsim -d 300 -N 7700000 -1 101 -2 101 reference.fa frag1_ref.fastq frag2_ref.fastq`

wgsim: This is the command to execute the WGSIM tool.
- -d 300: This parameter sets the base error rate to 0.3% (or 0.003) per base, representing the sequencing error rate.
- -N 7700000: This parameter sets the total number of read pairs to be simulated. In this case, it is set to 7,700,000 read pairs.
- -1 101: This parameter specifies the length of the first mate in the read pair. In this case, it is set to 101 bases.
- -2 101: This parameter specifies the length of the second mate in the read pair. Again, it is set to 101 bases.
- reference.fasta: This is the input file containing the reference genome in FASTA format.
- frag1_ref.fastq: This is the output file where the simulated reads for the first mate will be written in FASTQ format.
- frag2_ref.fastq: This is the output file where the simulated reads for the second mate will be written in FASTQ format.

time to run appx: *1m*

#### 2nd Step:

`bowtie2-build reference.fa bias`
This command creates an index of the reference genome (reference.fa) using Bowtie 2. The index will be stored in files with the prefix "bias" for future alignment.

time to run appx: *1m*

`bowtie2 -p 4 -k 15 --no-mixed -x bias -1 frag1_ref.fastq -2 frag2_ref.fastq -S biasOut.sam`

This command performs the alignment of paired-end reads (frag1_ref.fastq and frag2_ref.fastq) to the reference genome index ("bias") using Bowtie 2. Here's a breakdown of the options used:

- -p 4: Specifies the number of CPU threads to use (in this case, 4 threads).
- -k 15: Sets the maximum number of alignments to report per read (up to 15 alignments).
- --no-mixed: Disables reporting of alignments involving both mates from the same read.
- -x bias: Specifies the prefix of the Bowtie 2 index to use for alignment.
- -1 frag1_ref.fastq: Specifies the file containing the first mate (read 1) of the paired-end reads.
- -2 frag2_ref.fastq: Specifies the file containing the second mate (read 2) of the paired-end reads.
- -S biasOut.sam: Specifies the output file where the aligned reads will be stored in SAM format.

time to run appx: *45m*


`g++ -o bowtie2convert bowtie2convert.cpp` - compiling the C++ source code file "bowtie2convert.cpp" into an executable named "bowtie2convert 

`./bowtie2convert biasOut.sam reference.fa 300` 
- todo: what does this program do? 300 or 500?

Output Files: 
- `counts.txt` (0 51304566 1873599.999999)
- `stat.txt` (7700001 49248 101 300)
- `unmapped.txt`
- `linking.sam`
- `myout.sam`
- `singletons.sam`

time to run appx: *1m30s*

Does this command modify the `reference.fa`? - NO

#### 3rd Step

`g++ -w -o cgal_perPositionMapping cgal_perPositionMapping.cpp`

`./cgal_perPositionMapping reference.fa` 

Required Files: 
1. `myout.sam` - 'Can't open map file' error if missing. 
2. `stat.txt` - No error message but segmentation fault if missing. 

- todo: is this command even right? What does it do? 

Output: 
- `gcValue.txt`
- `info1.txt`
- `infoOutput1.txt`
- `out.txt`
- `readsInPerPositionGenome.txt`

time to run appx: *15m* - user-time: *11m*


- todo: what files to get for analysis from this 3 steps?


### For simulated testfiles:

#### 1st step:
- todo: what are these [testfileName]s?
lineCount =  `cmd: cat [testfileName].fa | wc -l`
readCount =  lineCount * 50 *30/202
`wgsim -d 300 -N readCount -1 101 -2 101 test.fasta frag1Copy_test.fastq frag2Copy_test.fastq`


#### 2nd step
`bowtie2-build reference.fa bias`
`bowtie2 -p 4 -k 15 --no-mixed -x bias -1 frag1Copy_test.fastq -2 frag2Copy_test.fastq -S biasOut.sam`
`./bowtie2convert biasOut.sam reference.fa 500`

#### 3rd step
`./cgal_perPositionMapping reference.fa` 

#### 4th Step

Installing `DNAcopy` - https://bioconductor.org/packages/release/bioc/html/DNAcopy.html

`Rscript segmentation_cbs.R` todo: configure variables.

