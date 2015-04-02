# -*- coding: utf-8 -*-

"""
@package    Sekator
@brief      Contain an iterator function to read fastq files and return FastqSeq objects
@copyright  [GNU General Public License v2](http://www.gnu.org/licenses/gpl-2.0.html)
@author     Adrien Leger - 2014
* <adrien.leger@gmail.com>
* <adrien.leger@inserm.fr>
* <adrien.leger@univ-nantes.fr>
* [Github](https://github.com/a-slide)
* [Atlantic Gene Therapies - INSERM 1089] (http://www.atlantic-gene-therapies.fr/)
"""

# Standard library imports
from gzip import open as gopen

# Local imports
from FastqSeq import FastqSeq

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# FUNCTIONS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def FastqReader (fastq_file):
    """ Simple fastq reader returning a generator over a fastq file """
    try:

        # Open the file depending of the compression status
        fastq = gopen(fastq_file, "rb") if fastq_file[-2:] == "gz" else open(fastq_file, "rb")
        i=0

        # Iterate on the file until the end
        while True:

            # Extract informations from the fastq file
            name, seq, sep, qual= next(fastq), next(fastq), next(fastq), next(fastq)

            # Try to generate a valid FastqSeq object
            try:
                yield FastqSeq(
                name = name.rstrip()[1:].split()[0],
                seq = seq.rstrip(),
                qual = qual.rstrip())

                i+=1

            except AssertionError as E:
                print(E)
                print ("Skipping the sequence")

    except IOError as E:
        print(E)
        print ("Error while reading {} file".format(fastq_file))
        exit()

    except StopIteration:
        raise StopIteration("\t{} sequences parsed".format(i))
