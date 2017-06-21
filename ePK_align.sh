#!/bin/bash

# align to profile hmm
hmmalign --trim --outformat selex PKinase.hmm ePKs_named.fasta > ePKs_named_hmmalign.selex

# convert to fasta format
python selex2fasta.py ePKs_named_hmmalign.selex ePKs_named_hmmalign.fasta

# trimAl
trimal -in ePKs_named_hmmalign.fasta -out ePKs_named_hmmalign_trim.fasta -automated1

# SATe
python run_sate.py sate_config.txt

# raxml
raxmlHPC-PTHREADS-AVX -T 16 -f a -p 12345 -s ePKs_sate/ePKs_sate.marker001.ePKs_named_hmmalign_trim.aln -x 12345 -# autoMRE -m PROTGAMMAAUTO -n ePKtree
