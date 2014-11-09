/*
 * Copyright (C) 2014 Christian Stigen Larsen
 * Distributed under the GPL v3 or later. See COPYING.
 */

#include <iostream>
#include <unistd.h>
#include "dnatraits.hpp"

/**
 * Has blue eye color? gs237 criteria http://snpedia.com/index.php/Gs237/criteria
 * For more info, see http://snpedia.com/index.php/Eye_color
 */
static bool gs237(const Genome& genome)
{
  return genome[ 4778241] ==  CC
      && genome[12913832] ==  GG
      && genome[ 7495174] ==  AA
      && genome[ 8028689] ==  TT
      && genome[ 7183877] ==  CC
      && genome[ 1800401] == ~CC;
}

static std::string skin_color_1426654(const Genome& genome)
{
  auto gt = genome[1426654];

  if ( gt == AA )
    return "Probably light-skinned, European ancestry";

  if ( gt == GA || gt == AG )
    return "Mixed African/European ancestry possible";

  if ( gt == GG )
    return "Probably darker-skinned, Asian or African ancestry";

  return "Unknown";
}

void summary(const Genome& genome)
{
  using namespace std;

  cout
    << "SUMMARY" << endl << endl

    << "  Gender:     " << (genome.ychromo? "Male" : "Female")
    << " (" << (genome.ychromo? "has" : "no") << " Y-chromosome)" << endl

    << "  Blue eyes?  " << (gs237(genome)? "Yes" : "No")
    << " (gs237)" << endl

    << "  Skin color: " << skin_color_1426654(genome)
    << " (rs1426654)" << endl

    << endl;
}

int main(int argc, char** argv)
{
  using namespace std;

  try {
    for ( auto n=1; n<argc; ++n ) {
      auto file = argv[n];
      cout << "Reading " << file << " ... ";
      cout.flush();

      Genome genome(1000000);
      parse_file(file, genome);

      cout << "done" << endl; cout.flush();
      cout << "Read " << genome.snp.size() << " unique SNPs" << endl << endl;

#ifdef DEBUG
      cout << "Size of Genotype: " << sizeof(Genotype) << endl
           << "Size of RSID: " << sizeof(RSID) << endl
           << endl;
#endif

      cout << "Example SNPs in this genome:" << endl << endl
           << "  " << format(genome, 7495174) << endl
           << "  " << format(genome, 1805007) << endl
           << "  " << format(genome, 1800401) << endl
           << "  " << format(genome, 28357092) << endl
           << "  " << format(genome, 12087250) << endl
           << endl;

      summary(genome);

      cout << "Developer info:" << endl
           << "  sizeof(Chromosome) = " << sizeof(Chromosome) << endl
           << "  sizeof(Genotype) = " << sizeof(Genotype) << endl
           << "  sizeof(Nucleotide) = " << sizeof(Nucleotide) << endl
           << "  sizeof(Position) = " << sizeof(Position) << endl
           << "  sizeof(RSID) = " << sizeof(RSID) << endl
           << "  sizeof(SNP) = " << sizeof(SNP) << endl
           << "  load factor = " << genome.snp.load_factor() << endl;
    }

    return 0;
  } catch ( const exception& e) {
    cout << endl
         << "Error: " << e.what() << endl;
    return 1;
  }
}
