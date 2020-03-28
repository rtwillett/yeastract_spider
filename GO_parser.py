import pandas as pd
import numpy as np
from itertools import chain

def GO_parse(df, go_param):

    df1 = df.loc[:, [go_param, "proteinname"]]
    cols = df1.columns.difference([go_param])
    go_lists = df1[go_param].str.split(":")

    long_df =  (df1.loc[df1.index.repeat(go_lists.str.len()), cols]
         .assign(go_IC=list(chain.from_iterable(go_lists.tolist()))))

    return long_df

df_GO = pd.read_csv("gene_data_GO.csv")

bioproc = df_GO.loc[:, ["proteinname", "go_BioProc"]]
bioproc_long = GO_parse(bioproc, "go_BioProc")

cellcomp = df_GO.loc[:, ["proteinname", "go_CellComp"]]
cellcomp_long = GO_parse(cellcomp, "go_CellComp")

molfunc = df_GO.loc[:, ["proteinname", "go_MolFunc"]]
molfunc = GO_parse(cellcomp, "go_MolFunc")

bioproc_long.to_csv(r"/Users/willettr/NYCDSA/scrapy/yeastract/bioproc.csv", index=None, header=True)
cellcomp_long.to_csv(r"/Users/willettr/NYCDSA/scrapy/yeastract/cellcomp.csv", index=None, header=True)
molfunc_long.to_csv(r"/Users/willettr/NYCDSA/scrapy/yeastract/molfunc.csv", index=None, header=True)
