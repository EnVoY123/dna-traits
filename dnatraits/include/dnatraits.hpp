/*
 * Copyright (C) 2014, 2016 Christian Stigen Larsen
 * Distributed under the GPL v3 or later. See COPYING.
 */

#ifndef INC_DNATRAITS_H
#define INC_DNATRAITS_H

#include <cstdint>
#include <iostream>
#include <vector>
#include <string>

#include "export.hpp"

typedef std::uint32_t Position;
typedef std::uint32_t RSID;

enum Nucleotide {
  NONE, A, G, C, T, D, I
};

/*
 * CHR_MT denotes mitochondrial DNA
 */
enum Chromosome {
  NO_CHR=0,
  CHR1, CHR2, CHR3, CHR4, CHR5,
  CHR6, CHR7, CHR8, CHR9, CHR10,
  CHR11, CHR12, CHR13, CHR14, CHR15,
  CHR16, CHR17, CHR18, CHR19, CHR20,
  CHR21, CHR22, CHR_MT, CHR_X, CHR_Y
};

// We can get this down to a byte if we want to
#pragma pack(1)
struct DLL_PUBLIC Genotype {
  Nucleotide first : 3;
  Nucleotide second : 3;

  Genotype(const Nucleotide& a = NONE,
           const Nucleotide& b = NONE);

  friend Genotype operator~(const Genotype&);
  bool operator==(const Genotype& g) const;
  bool operator<(const Genotype& g) const;
};

// Some handy constants
extern DLL_PUBLIC const Genotype AA;
extern DLL_PUBLIC const Genotype AC;
extern DLL_PUBLIC const Genotype AG;
extern DLL_PUBLIC const Genotype AT;
extern DLL_PUBLIC const Genotype CA;
extern DLL_PUBLIC const Genotype CC;
extern DLL_PUBLIC const Genotype CG;
extern DLL_PUBLIC const Genotype CT;
extern DLL_PUBLIC const Genotype GA;
extern DLL_PUBLIC const Genotype GC;
extern DLL_PUBLIC const Genotype GG;
extern DLL_PUBLIC const Genotype GT;
extern DLL_PUBLIC const Genotype NN;
extern DLL_PUBLIC const Genotype TA;
extern DLL_PUBLIC const Genotype TC;
extern DLL_PUBLIC const Genotype TG;
extern DLL_PUBLIC const Genotype TT;

#pragma pack(1)
struct DLL_PUBLIC SNP {
  Chromosome chromosome : 5;
  Position position;
  Genotype genotype;

  SNP(const Chromosome& = NO_CHR,
      const Position& = 0,
      const Genotype& = NN);
  SNP(const SNP&);

  SNP& operator=(const SNP&);
  bool operator!=(const SNP&) const;
  bool operator<(const SNP&) const;
  bool operator<=(const SNP&) const;
  bool operator==(const Genotype&) const;
  bool operator==(const SNP&) const;
  bool operator>(const SNP&) const;
  bool operator>=(const SNP&) const;
};

extern DLL_PUBLIC const SNP NONE_SNP;

struct DLL_LOCAL GenomeIteratorImpl;

struct DLL_PUBLIC RsidSNP {
  RSID rsid;
  SNP snp;

  bool operator==(const RsidSNP& o) const
  {
    return rsid == o.rsid && snp == o.snp;
  }
};

struct DLL_PUBLIC GenomeIterator {
  // todo copy ctor, assignment op, dtor
  GenomeIterator(GenomeIteratorImpl*);
  ~GenomeIterator();
  GenomeIterator(const GenomeIterator&);
  GenomeIterator& operator=(const GenomeIterator&);
  GenomeIterator& operator++();
  bool operator==(const GenomeIterator&);
  bool operator!=(const GenomeIterator&);
  const RsidSNP operator*();
private:
  GenomeIteratorImpl* pimpl;
};

struct DLL_PUBLIC Genome {
  /*!
   * True if genome contains a Y-chromosome (with non-empty genotypes).
   */
  bool y_chromosome;

  /*!
   * Lowest RSID.
   */
  RSID first;

  /*!
   * Highest RSID.
   */
  RSID last;

  Genome(const size_t size);
  Genome(const Genome&);
  Genome& operator=(const Genome&);
  ~Genome();

  /*!
   * Access SNP. Throws on not found.
   */
  const SNP& operator[](const RSID& id) const;

  /*!
   * Checks if hash table contains given RSID.
   */
  bool has(const RSID& id) const;

  /*!
   * Add a SNP to the hash table.
   */
  void insert(const RSID& rsid, const SNP& snp);

  /*!
   * Underlying hash table's load factor. (For developer purposes)
   */
  double load_factor() const;

  /*!
   * Number of SNPs.
   */
  size_t size() const;

  /*!
   * Returns RSIDs that exist in both genomes.
   */
  std::vector<RSID> intersect_rsid(const Genome& genome) const;

  /*!
   * Returns RSID for SNPs that have the same genotype in both genomes.
   */
  std::vector<RSID> intersect_snp(const Genome& genome) const;

  /*!
   * Returns all RSIDs in this genome.
   */
  std::vector<RSID> rsids() const;

  /*!
   * Returns a copy of all SNPs.
   */
  std::vector<SNP> snps() const;

  bool operator==(const Genome&) const;
  bool operator!=(const Genome&) const;

  GenomeIterator begin() const;
  GenomeIterator end() const;

private:
  struct DLL_LOCAL GenomeImpl;
  GenomeImpl* pimpl;
};

Nucleotide complement(const Nucleotide& n);

/*!
 * Parse a 23andMe genome text file and put contents into genome.
 */
void parse_file(const std::string& filename, Genome&);

std::ostream& operator<<(std::ostream&, const Chromosome&);
std::ostream& operator<<(std::ostream&, const Genotype&);
std::ostream& operator<<(std::ostream&, const Nucleotide&);
std::ostream& operator<<(std::ostream&, const SNP&);

#endif
