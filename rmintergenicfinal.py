import sys
import pandas as pd

filename1 = sys.argv[1]
filename2 = sys.argv[2]

def rmintergenic(vcf_file, out_file):
    with open(vcf_file) as f:                
        lines = [next(f) for l in range(19)] 

    with open(vcf_file) as f:
        for line in f:
            if line[:6] == '#CHROM':
                vcf_header = line.strip().split('\t')
                vcf_header[0] = vcf_header[0][0:]
                break

    gen_df = pd.read_csv(vcf_file, sep='\t', comment='#', header=None, names=vcf_header)
    gen_dffixtemp1 = gen_df[gen_df.applymap(lambda x: False if 'ANN=A|intergenic' in str(x) else True)].dropna()
    gen_dffixtemp2 = gen_dffixtemp1[gen_df.applymap(lambda x: False if 'ANN=G|intergenic' in str(x) else True)].dropna()
    gen_dffixtemp3 = gen_dffixtemp2[gen_df.applymap(lambda x: False if 'ANN=C|intergenic' in str(x) else True)].dropna()
    gen_dffix = gen_dffixtemp3[gen_df.applymap(lambda x: False if 'ANN=T|intergenic' in str(x) else True)].dropna()

    output_VCF = out_file

    with open(output_VCF, 'w') as vcf:
        vcf.write("".join(lines))             
    gen_dffix.to_csv(output_VCF, sep="\t", mode='a', index=False)

rmintergenic(filename1,filename2)

