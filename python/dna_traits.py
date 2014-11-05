"""
A library for parsing and querying 23andme genomes.
"""

import _dna_traits

class Nucleotide:
    """A single nucleotide."""
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return self._value

    def __repr__(self):
        return "Nucleotide(%s)" % self._value

    def __len__(self):
        if self._value in ["-"]:
            return 0
        else:
            return 1

    def __eq__(self, o):
        return self._value == o._value

    def complement(self):
        """Returns the complement of this nucleotide."""
        compl = {"A": "T",
                 "C": "G",
                 "G": "C",
                 "T": "A",
                 "D": "D",
                 "I": "I",
                 "-": "-"}
        return Nucleotide(compl[self._value])

    def __invert__(self):
        return self.complement()

class SNP:
    """A single-nucleotide polymorphism."""

    def __init__(self, genotype, rsid, orientation):
        self._genotype = genotype
        self._rsid = rsid
        self._orientation = orientation

    def _genostr(self):
        return "".join(map(str, self._genotype))

    @property
    def orientation(self):
        """Returns orientation as either -1 or +1."""
        return self._orientation

    def __len__(self):
        return sum(map(len, self._genotype))

    def __getitem__(self, index):
        return self._genotype[index]

    @property
    def rsid(self):
        """Returns this SNP's RSID."""
        return self._rsid

    def count(self, nucleotide):
        """Returns number of given nucleotide in this SNP."""
        return self._genostr().count(nucleotide.upper())

    def complement(self):
        """Returns this SNP's complement."""
        genotype = map(lambda n: n.complement(), self._genotype)
        return SNP(genotype, self._rsid, self._orientation)

    def positive(self):
        """Returns SNP with positive orientation."""
        if self.orientation < 0:
            return self.complement()
        else:
            return self

    def negative(self):
        """Returns SNP with negative orientation."""
        if self.orientation > 0:
            return self.complement()
        else:
            return self

    def __eq__(self, snp):
        return str(self.positive()) == str(snp.positive())

    def __invert__(self):
        return self.complement()

    @property
    def genotype(self):
        """Returns a list of zero, one or two Nucleotides."""
        return self._genotype

    def __str__(self):
        return self._genostr()

    def __repr__(self):
        return "SNP(rsid=%s, genotype=%s, orientation=%s)" % (
                    self._rsid, self._genostr(), self._orientation)


class GenomeIterator:
    def __init__(self, genome):
        self._genome = genome
        self._rsid = 0

    def __iter__(self):
        return self

    def next(self):
        while self._rsid not in self._genome:
            self._rsid += 1
            # NOTE: This is *wrong*, we need to check if self._rsid >= max
            # rsid in genome
            if self._rsid >= len(self._genome):
                raise StopIteration()

        rsid = self._rsid
        self._rsid += 1
        return self._genome[rsid]

class Genome:
    """A genome consisting of SNPs."""

    def __init__(self, genome, orientation):
        self._genome = genome
        self._orientation = orientation

    def _rsid(self, rsid):
        if isinstance(rsid, int):
            return "rs%d" % rsid
        elif isinstance(rsid, str) and rsid.startswith("rs"):
            return rsid
        else:
            raise ValueError("Invalid RSID: %s" % rsid)

    def __iter__(self):
        return GenomeIterator(self)

    @property
    def ychromo(self):
        """True if genome contains a Y-chromosome."""
        return self._genome.ychromo()

    @property
    def male(self):
        """True if genome contains a Y-chromosome."""
        return self.ychromo

    @property
    def female(self):
        """False if genome contains a Y-chromosome."""
        return not self.male

    @property
    def orientation(self):
        """Returns this Genome's orientation as an integer of either -1 or
        +1."""
        return self._orientation

    def __getitem__(self, rsid):
        """Returns SNP with given RSID.  If RSID is not present, return an
        empty SNP."""
        try:
            rsid = self._rsid(rsid)
            geno = map(Nucleotide, self._genome[rsid])
            return SNP(geno, rsid, self._orientation)
        except KeyError:
            return SNP([], rsid, self._orientation)

    def snp(self, rsid):
        """Returns SNP with given RSID."""
        return self.__getitem__(rsid)

    def __str__(self):
        return "Genome"

    def __contains__(self, rsid):
        try:
            self._genome[self._rsid(rsid)]
            return True
        except KeyError:
            return False

    def __repr__(self):
        return "Genome(len=%d, ychromo=%s, orientation=%s)" % (
                len(self), self.ychromo, self.orientation)

    def __getattr__(self, rsid):
        # Query with genome.rs28357092
        if isinstance(rsid, str) and rsid.startswith("rs"):
            return self.__getitem__(rsid)
        raise AttributeError("Unknown attribute %s" % rsid)

    def __len__(self):
        """Returns number of SNPs in this genome."""
        return len(self._genome)

    def match(self, criteria):
        """Match list of (RSID, BasePair) with genome. BasePair should be a
        string with positive orientation.

        Example:
            all(match(genome, [("rs4778241", "CC"), ("rs1291832", "GG")]))
        """
        return (str(genome[rsid]) == pair for rsid, pair in criteria)


def parse(filename, orientation=+1):
    """Parses a 23andme file and returns a Genome."""
    return Genome(_dna_traits.parse(filename), orientation)