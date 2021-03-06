# pyFastq 0.1

**Simple python 2.7 libraries to parse fastq files and handle illumina 1.8+ fastq sequences**

**Creation : 2015/04/02**

**Last update : 2015/04/02**

## FastqReader
Parsing function that reads a fastq file and generates an iterator of FastqSeq object.
When the file is empty the generator raise a StopIteration exception indicating the number of valid sequence parsed. If a fastq sequence is invalid, this sequence is skipped.
Any part of the sequence name following a blank space will be removed

## FastqSeq : Simple object representing a Fastq sequence
FastqSeq is a simple python object class generating a object representing a Fastq sequence. The object is initialized with:

* A name for the sequence without @
* A DNA sequence as a string
* A quality score, as an **illumina 1.8+** encoded quality string, a numpy.ndarray of integers in **Phred +33** or python list of integers in **Phred +33**
* Eventually a short text description

The DNA sequence and the quality score must have the same size otherwise an assertion error is raised

After creation the object has the following fields:

* name = name of the sequence without @.
* seq = The DNA sequence of the fastq sequence store as a simple string.
* qual = An numpy integer ndarray representing the Phred Quality of bases (support all np.array methods)
* descr = A description of the fastq sequence.
* qualstr = A string of letters corresponding to the sequence quality in illumina 1.8+ Phred 33 encoding
* fastqstr = The field "descr" will be included in the output fastq sequence name after a space if present

The object support slicing([0:10]), concatenation(seq1+seq2) and the len method

## Authors and Contact

Adrien Leger - 2015

* <adrien.leger@gmail.com> - <adrien.leger@inserm.fr> - <adrien.leger@univ-nantes.fr>
* [Github](https://github.com/a-slide)
* [Atlantic Gene Therapies - INSERM 1089](http://www.atlantic-gene-therapies.fr/)
