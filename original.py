file = 'HBM444.DXLZ.643.h5ad'
adata = sc.read(file)
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
adata = adata[:, ~adata.var.hugo_symbol.isna().values].copy()
adata.var_names = list(adata.var.hugo_symbol.values)
adata.var_names_make_unique()
celltypist.annotate(adata, 'Human_Lung_Atlas.pkl', majority_voting = True).predicted_labels[['predicted_labels', 'majority_voting']].to_csv(f"{file.replace('h5ad', 'csv')}", header = True, index = True) 
