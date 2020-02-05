# LFMM_G2E
Using Latent Factor Mixed Models (LFMM) for Genotype to Environment (G2E) association analysis

[LFMM tutorial](http://membres-timc.imag.fr/Olivier.Francois/lfmm/index.htm).
# Input
- ## Input data: *lfmm*
  Convert *VCF* file to *lfmm* file using **vcf2lfmm**
- ## Input data: *env*
  Convert environmental *matrix* file to *env* file using **write.env**
- ## Input parameter: *K*
  1. Convert *VCF* file to *geno* file using **vcf2geno**
  1. Run **snmf** with the *geno* file
  1. plot the **snmf** result to find the best *K*

# Output


![](my_plot.png)
