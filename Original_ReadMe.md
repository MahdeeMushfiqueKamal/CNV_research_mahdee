Copy Number Variation Estimation
--------------------------------

For Reference:

1st step:
---------
### For read generation for both normal & abnormal

wgsim -d 300 -N 7700000 -1 101 -2 101 reference.fasta frag1_ref.fastq frag2_ref.fastq 

genome size 51304650*30/202

reference read = 7700000 

genomesize cmd: cat reference.fa | wc -l

--> multiply line number * 50 --> *30/202

2nd step
--------
./bowtie2-build reference.fa bias
./bowtie2 -p 4 -k 15 --no-mixed -x bias -1 frag1_ref.fastq -2 frag2_ref.fastq -S biasOut.sam
./bowtie2convert biasOut.sam reference.fa 500 
./bowtie2convert biasOut.sam reference.fa 300  # should be 300?  

3rd step
--------
./cgal_perposition* reference.fa




For simulated testfiles:
-----------------------
1st step:
---------
### For read generation for both normal & abnormal
lineCount =  cmd: cat [testfileName].fa | wc -l

readCount--> lineCount * 50 *30/202

wgsim -d 300 -N readCount -1 101 -2 101 test.fasta frag1Copy_test.fastq frag2Copy_test.fastq


2nd step
--------
bowtie2-build reference.fa bias
bowtie2 -p 4 -k 15 --no-mixed -x bias -1 frag1Copy_test.fastq -2 frag2Copy_test.fastq -S biasOut.sam
./bowtie2convert biasOut.sam reference.fa 500

3rd step
--------
./cgal_perposition* reference.fa

4 Step
--------
Segmentation.R + small region delete 
Rscript segmentation_cbs.R

5 Step
------
segments_fasta_in_contigs.py

6th Step
---------
bowtie2-build reference_G1S1_segmented.fa segmented
bowtie2 -p 2 -k 15 --no-mixed -x segmented -1 frag_1_G1S1.fastq -2 frag_2_G1S1.fastq -S segmentedOut.sam
./bowtie2convert segmentedOut.sam reference_G1S1_segmented.fa 500


7th Step
--------
./cgal_dependent reference_G1S1_segmented.fa






Running Cmds:
G1S1:
wgsim -d 300 -N 8389299 -1 101 -2 101 reference.fa frag1_G1S1.fastq frag2_G2S2.fastq


Printing lines:
head -n 10 [filename]

Compiling files:
g++ cgal_dependent.cpp -lm -o cgal_dependent



