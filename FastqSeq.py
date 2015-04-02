# -*- coding: utf-8 -*-

"""
@package    Sekator
@brief      Contain a class to model a fastq sequence and an iterator function to read fastq files
@copyright  [GNU General Public License v2](http://www.gnu.org/licenses/gpl-2.0.html)
@author     Adrien Leger - 2014
* <adrien.leger@gmail.com>
* <adrien.leger@inserm.fr>
* <adrien.leger@univ-nantes.fr>
* [Github](https://github.com/a-slide)
* [Atlantic Gene Therapies - INSERM 1089] (http://www.atlantic-gene-therapies.fr/)
"""

# Third party imports
import numpy as np

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class FastqSeq (object):
    """
    Simple Representation of a fastq file. The object support slicing and addition operations
    The quality score is a numpy array to facilitate further data manipulation
    Only works with illumina 1.8+ Phred 33 quality encoding
    """
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    #~~~~~~~FUNDAMENTAL METHODS~~~~~~~#

    def __init__ (self, name, seq, qual, descr=""):
        """
        @param name Name of the sequence (without spaces)
        @param seq DNA sequence string
        @param qual string of quality encoded in illumina 1.8+ phred +33, or ndarray of int or
        list of int
        @param descr Facultative description
        """

        self.name = name
        self.seq = seq
        self.descr = descr

        if type(qual) == str:
            self.qual = np.array([ord(x)-33 for x in qual])
            print ("Str type")

        elif type(qual) == np.ndarray:
            self.qual = qual
            print ("ndarray type")

        elif type(qual) == list:
            self.qual = np.array(qual)
            print ("list type")

        else:
            raise TypeError("qual is not a valid type : str, numpy.ndarray or list of int")

        assert len(self.seq) == len(self.qual), "Sequence length and quality string length are not equal."

    def __repr__(self):
        return "<Instance of {} from {} >".format(self.__class__.__name__, self.__module__)

    def __str__(self):
        if len(self) > 20:
            return "{} : {}...{}  {}...{}".format(self.name, self.seq[:10], self.seq[-10:], self.qual[:10], self.qual[-10:])
        else:
            return "{} : {}  {}".format(self.name, self.seq, self.qual)

    #~~~~~~~PROPERTIES~~~~~~~#

    @property
    def qualstr(self ):
        """Compute the quality string from the numpy int array """
        qualstr_phred = ""
        for i in self.qual:
            qualstr_phred += str(unichr(i+33))
        return qualstr_phred

    @property
    def fastqstr(self):
        """Return string formated as a fastq sequence"""
        if self.descr:
            return "@{} {}\n{}\n+\n{}\n".format(self.name, self.descr, self.seq, self.qualstr)
        else:
            return "@{}\n{}\n+\n{}\n".format(self.name, self.seq, self.qualstr)


    #~~~~~~~MAGIC METHODS~~~~~~~#

    def __len__ (self):
        """Support for len method"""
        return len(self.seq)

    def __getitem__( self, item ):
        """Support for slicing operator"""
        return FastqSeq(name = self.name, seq = self.seq[ item ], qual = self.qual[ item ])

    def __add__(self, other):
        """Support for concatenation of fastqSeq objects = + operator"""
        return FastqSeq(
            name = "{}_{}".format(self.name, other.name),
            seq = self.seq+other.seq,
            qual = np.concatenate((self.qual, other.qual)),
            descr = self.descr+other.descr)
