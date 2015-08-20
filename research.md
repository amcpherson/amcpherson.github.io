---
layout: page
title: Research
---

# Research Interests

## Summary

My research focuses on the development new methods and algorithms for facilitating novel analyses of sequencing data, primarily with application to understanding cancer development.
I am interested in the design of combinatorial algorithms, and creating efficient implementations that may be used with real world sized datasets.
I am also interested in probabilistic modeling of sequence data, and the development of efficient inference and learning algorithms.

 *** 

## Cancer Genomics

### Discovery and Characterization of Genome Rearrangements

High throughput sequencing promises the ability to comprehensively detect novel sequences in DNA samples.
However, these new technologies come with an additional computational burden.
Experiments produce a large number of sequences (reads), and the length of each sequence is short.
Short read lengths prevent unambiguous assignment of some reads to a single genomic loci.

A significant portion of my PhD work involved development of algorithms for predicting gene fusions and genomic rearrangements, accounting for read mapping ambiguity.

* [deFuse](http://dx.doi.org/10.1371/journal.pcbi.1001138) for predicting gene fusions from RNA-Seq,
* [nFuse](http://dx.doi.org/10.1101/gr.136572.111) for predicting gene fusions and associated rearrangements from RNA-Seq and WGS,
* deStruct for predicing breakpoints from WGS.

deStruct has been used to profile rearrangements in
[prostate tumours](http://dx.doi.org/10.1038/ng.3315),
[breast cancer derived xenografts](http://dx.doi.org/10.1038/nature13952), and
[lymphomas](http://dx.doi.org/10.1182/blood-2013-10-535443).
deFuse has been used by collaborators to identify fusions in
[lymphoid cancers](http://dx.doi.org/10.1038/nature09754),
[high-grade endometrial stromal sarcoma](http://dx.doi.org/10.1073/pnas.1115528109), and
[prostate cancer](http://dx.doi.org/10.1002/path.3987).

Further work is required to allow prediction of somatic rearrangements involving highly repetitive genomic elements such as LINEs, and may require adoption of a non-linear representation of the genome.
Furthermore, current tools for breakpoint prediction perform well for near clean breakpoints produced by Non-Homologous End Joining based repair, but are unable to identify breakpoints with significant non-template inserted sequence or significant breakpoint homology.

### Complex Genomic Rearrangements

Collections of related genomic breakpoints are frequently an indicator of a specific mutational mechanisms.
Breakage-fusion-bridge, chromothripsis, chromoplexy, and somatic transposon insertion each leave a specific signature in the breakpoint profile of a tumor.
Using [nFuse](http://dx.doi.org/10.1101/gr.136572.111), we have been able to identify both 
[chromoplexy](http://dx.doi.org/10.1186/s13059-014-0426-y) and
[chromothripsis](http://dx.doi.org/10.1002/gcc.21999)
in prostate tumours, and provide examples of its effects on the transcriptome.

### Tumor Evolution and Metastasis

Active mutational processes produce genomically distinct populations of tumor cells (_clones_) related by descent to a common ancestor.
Genomic diversity results in differential fitness with respect to the ability metastasize and to survive therapies, the immune system and competition with other clones.
Researchers are now using bulk targeted deep sequencing to infer clonal prevalence of specific mutations, and thereby understand a mutations timing and relative importance.

We developed 
[CITUP](http://dx.doi.org/10.1093/bioinformatics/btv003)
to reconstruct the mutation content of tumor clones and the phylogenetic relationships between those clones given deep sequencing data.
We applied CITUP to CLL and ALL datasets.
CITUP is aimed at cancers with near diploid copy number profiles.
Further algorithmic work is required to handle the significantly more difficult problem of phylogenetic reconstruction for genomically unstable tumors.

## Algorithm Development

### Genome Graph Algorithms

Breakpoint detection in WGS (with deStruct or similar tools) provides predictions of adjacency between contiguous DNA sequences.
Typically full reconstruction of chromosomes is neither possible nor necessary.
Genome graphs are an important tool for modeling the structure of the genome, as they succinctly capture unexpected adjacencies between genomic segments.
We leveraged genome graphs when developing
[nFuse](http://dx.doi.org/10.1101/gr.136572.111),
which required fast implementations of algorithms working with large genome graphs.
With
[ReMixT](http://link.springer.com/chapter/10.1007/978-3-319-16706-0_25),
we challenged the use of HMMs as the standard modeling technique for copy number data, and show that use of genome graphs and a novel combinatorial inference algorithm, can improve prediction of clone specific copy number.


