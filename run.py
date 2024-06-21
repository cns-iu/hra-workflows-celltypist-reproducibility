import scanpy as sc
import celltypist
import pandas

file = "HBM444.DXLZ.643.h5ad"
use_ensembl_lookup = True

adata = sc.read(file)
adata.X = adata.layers["spliced_unspliced_sum"]
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)

if use_ensembl_lookup:
    lookup = pandas.read_csv("ensemble-lookup.csv")
    gene_names_by_ensembl = {}
    for item in lookup.itertuples(index=False):
        gene_names_by_ensembl[item.ensemble] = item.gene_name

    def get_new_name(name):
        key = name.split(".", 1)[0]
        return gene_names_by_ensembl.get(key, name)

    adata.var_names = adata.var_names.map(get_new_name)
else:
    adata = adata[:, ~adata.var.hugo_symbol.isna().values].copy()
    adata.var_names = list(adata.var.hugo_symbol.values)

adata.var_names_make_unique()
celltypist.annotate(
    adata, "Human_Lung_Atlas.pkl", majority_voting=True
).predicted_labels[["predicted_labels", "majority_voting"]].to_csv(
    f"{file.replace('h5ad', 'csv')}", header=True, index=True
)
