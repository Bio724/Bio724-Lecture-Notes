#!/usr/bin/env python

import argparse

import pandas as pd
from matplotlib import pyplot as plt

import vcf

def qual_and_depth(infile):
    data = {"Chrom":[], "Coord":[], "Qual":[],"Depth":[]}
    rdr = rdr = vcf.Reader(infile)
    for rec in rdr:
        data["Chrom"].append(rec.CHROM)
        data["Coord"].append(rec.POS)
        data["Qual"].append(rec.QUAL)
        data["Depth"].append(rec.INFO["DP"])        
    return pd.DataFrame(data)

def plot_depth(dfdepth):
    



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get quality and depth info at variable sites from a VCF file')
    parser.add_argument("infile", type=argparse.FileType('r'), help="input VCF file (or stdin)")
    parser.add_argument("outfile", type=argparse.FileType('w'), help="output CSV file (or stdout)")
    args = parser.parse_args()

    df = qual_and_depth(args.infile)
    try:
        df.to_csv(args.outfile, index=False)
    except BrokenPipeError:  # avoids error message when piping to less
        pass