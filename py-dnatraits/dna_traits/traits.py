# -*- encoding: utf-8 -*-

"""
Used to infer some traits.

Use with caution, this code may contain errors!

Copyright (C) 2014 Christian Stigen Larsen
Distributed under the GPL v3 or later. See COPYING.
"""

from dna_traits.match import unphased_match
from dna_traits.util import make_report


def _assert_european(genome):
    """If ethnicity is set, make sure it's European."""
    if genome.ethnicity not in [None, "european"]:
        raise ValueError("Only applicable to Europeans")

def bitter_taste(genome):
    "Bitter taste perception."
    return unphased_match(genome.rs713598, {
        "CC": "Probably can't taste certain bitter flavours",
        "CG": "Can taste bitter flavours that others can't",
        "GG": "Can taste bitter flavours that others can't",
        None: "Unable to determine"})

def alcohol_flush_reaction(genome):
    "Alcohol flush reaction."
    return unphased_match(genome.rs671, {
        "AA": "Extreme reaction (no copies of the ALDH2 gene)",
        "AG": "Moderate reaction (one copy of the ALDH2 gene)",
        "GG": "Little to no reaction (two copies of the ALDH2 gene)",
        None: "Unable to determine"})

def earwax_type(genome):
    "Earwax type."
    return unphased_match(genome.rs17822931, {
        "CC": "Wet earwax (sticky, honey-colored)",
        "CT": "Wet earwax (sticky, honey-colored)",
        "TT": "Dry earwax (flaky, pale)",
        None: "Unable to determine"})

def eye_color(genome):
    "Eye color."
    _assert_european(genome)
    return unphased_match(genome.rs12913832, {
        "AA": "Brown eyes, although 14% have green and 1% have blue",
        "AG": "Most likely brown or green, but 7% have blue",
        "GG": "Most likely blue, but 30% have green and 1% brown",
        None: "Unable to determine"})

def lactose_intolerance(genome):
    "Lactose intolerance."
    return unphased_match(genome.rs4988235, {
        "AA": "Likely lactose tolerant",
        "AG": "Likely lactose tolerant",
        "GG": "Likely lactose intolerant",
        None: "Unable to determine"})

def malaria_resistance(genome):
    "Malaria resistance (Duffy antigen)."
    return unphased_match(genome.rs2814778, {
        "CC": "Likely resistant to P. vivax",
        "CT": "Likely to have some resistance to P. vivax",
        "TT": "Likely not resistant to P. vivax",
        None: "Unable to determine"})

def male_pattern_baldness(genome):
    """Male pattern baldness.

    Studies:
        http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Search&db=PubMed&term=18849991
        http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Search&db=PubMed&term=15902657
        http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Search&db=PubMed&term=18849994
    """
    raise NotImplementedError()

    # X-chromosome: rs6625163, A->G is risk mutation (OR 1.17)
    # rs6113491, A->C is risk mutation (AA has OR 1.77)
    # TODO: Attempt to match ORs

def norovirus_resistance(genome):
    """Norovirus resistance (most common strain)."""
    return unphased_match(genome.rs601338, {
        "AA": "Resistant to most common strain",
        "AG": "Likely not resistant to most common strain",
        "GG": "Likely not resistant to most common strain",
        None: "Unable to determine"})

def muscle_performance(genome):
    """Muscle performance."""
    return unphased_match(genome.rs1815739, {
        "CC": "Likely sprinter, perhaps endurance athlete (two copies)",
        "CT": "Likely sprinter, perhaps endurance athlete (one copy)",
        "TT": "Unlikely sprinter, but likely endurance athlete (no copies)",
        None: "Unable to determine"})

def smoking_behaviour(genome):
    """Smoking behaviour."""
    _assert_european(genome)
    return unphased_match(genome.rs1051730, {
        "AA": "Likely to smoke more than average",
        "AG": "Likely to smoke a little bit more than average",
        "GG": "Likely to smoke typical amount of cigarettes per day",
        None: "Unable to determine"})

def red_hair(genome):
    """Hair color; odds for red hair."""
    return unphased_match(genome.rs1805007, {
        "CC": "Typical odds for red hair",
        "CT": "Substantially increased odds for red hair",
        "TT": "Greatly increased odds for red hair",
        None: "Unable to determine"})

def blond_vs_brown_hair(genome):
    """Hair color; blond versus brown."""
    return unphased_match(genome.rs1667394, {
        "CC": "Greatly decreased odds of having blond hair vs. brown",
        "CT": "Decreased odds of having blond hair vs. brown",
        "TT": "Typical odds of having blond hair vs. brown hair",
        None: "Unable to determine"})

def pain_sensitivity(genome):
    """Pain sensitivity."""
    return unphased_match(genome.rs6269, {
        "AA": "Increased sensitivity to pain",
        "AG": "Typical sensitivity to pain",
        "GG": "Less sensitive to pain",
        None: "Unable to determine"})

def caffeine_metabolism(genome):
    """Caffeine metabolism."""
    _assert_european(genome)
    return unphased_match(genome.rs762551, {
        "AA": "Fast metabolizer",
        "AC": "Slow metabolizer",
        "CC": "Slow metabolizer",
        None: "Unable to determine"})

def heroin_addiction(genome):
    """Heroin addiction."""
    _assert_european(genome)
    return unphased_match(genome.rs1799971, {
        "AA": "Typical odds of addiction",
        "AG": "Higher odds of addiction",
        "GG": "Higher odds of addiction",
        None: "Unable to determine"})

def hair_curl(genome):
    _assert_european(genome)
    return unphased_match(genome.rs17646946, {
        "AA": "Straighter hair on average",
        "AG": "Straighter hair on average",
        "GG": "Slightly curlier hair on average"})

def hiv_aids_resistance(genome):
    """Resistance to HIV/AIDS."""
    return unphased_match(genome.i3003626, {
        "DD": "Some resistance to most common strain of HIV",
        "DI": "Not resistant, but may have slower disease progression",
        "II": "Not resistant"})

def aspargus_detection(genome):
    """Aspargus metabolite detection."""
    _assert_european(genome)
    return unphased_match(genome.rs4481887, {
        "AA": "Higher odds of smelling aspargus in urine",
        "AG": "Medium odds of smelling aspargus in urine",
        "GG": "Typical odds of smelling aspargus in urine",
        None: "Unable to determine"})

def adiponectin_levels(genome):
    """Adiponectin levels."""
    if genome.ethnicity == "asian":
        r = unphased_match(genome.rs1851665, {
            "AA": "Slightly lower, which may be bad (rs1851665)\n",
            "AG": "Typical (rs1851665)\n",
            "GG": "Slightly higher, which is good (rs1851665)\n",
            None: "Unable to determine for rs1851665\n"})

        r += unphased_match(genome.rs7193788, {
            "AA": "Slightly higher, which is good (rs7193788)",
            "AG": "Typical (rs7193788)",
            "GG": "Slightly lower, which may be bad (rs7193788)",
            None: "Unable to determine for rs7193788"})
        return r

    elif genome.ethnicity in [None, "european"]:
        return unphased_match(genome.rs6444175, {
            "AA": "Lower, which may be bad",
            "AG": "Slightly lower, which may be bad",
            "GG": "Typical levels",
            None: "Unable to determine"})

def biological_age(genome):
    """Biological aging (telomere length indication)."""
    _assert_european(genome)
    age = []

    age.append(unphased_match(genome.rs10936599, {
        "TT": 7.82,
        "CT": 3.91,
        "CC": 0,
        None: 0}))

    age.append(unphased_match(genome.rs2736100, {
        "AA": 3.14,
        "AC": 0,
        "CC": -3.14,
        None: 0}))

    age.append(unphased_match(genome.rs9420907, {
        "AA": 0,
        "AC": -2.76,
        "CC": -5.52,
        None: 0}))

    age.append(unphased_match(genome.rs755017, {
        "AA": 0,
        "AG": -2.47,
        "GG": -4.94,
        None: 0}))


    age.append(unphased_match(genome.rs11100479, {
        "CC": 5.98,
        "CT": -2.99,
        "TT": 0,
        None: 0}))

    age.append(unphased_match(genome.rs10165485, {
        "TT": 0,
        "CT": -2.23,
        "CC": -4.46,
        None: 0}))

    avg = sum(age)/len(age)
    if avg > 0:
        s1 = "older"
    elif avg < 1:
        s1 = "younger"
    else:
        s1 = ""
    return "Average %.1f years %s than actual age\n(From %.1f to %.1f years)" % (
            avg, s1, min(age), max(age))

def traits_report(genome):
    """Infer traits from genome."""
    return make_report(genome, [
        adiponectin_levels,
        alcohol_flush_reaction,
        aspargus_detection,
        biological_age,
        bitter_taste,
        blond_vs_brown_hair,
        caffeine_metabolism,
        earwax_type,
        eye_color,
        hair_curl,
        heroin_addiction,
        hiv_aids_resistance,
        lactose_intolerance,
        malaria_resistance,
        male_pattern_baldness,
        muscle_performance,
        norovirus_resistance,
        pain_sensitivity,
        red_hair,
        smoking_behaviour,
    ])
