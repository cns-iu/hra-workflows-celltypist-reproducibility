# hra-workflows-celltypist-reproducibility

- Original [code](./original.py) by Chuan
- Original [ensemble-lookup.csv](https://github.com/hubmapconsortium/hra-workflows/blob/main/containers/celltypist/context/ensemble-lookup.csv)

### Reproducing Chuan's result
Running the code provided by Chuan gives the exact same results as reported in his [google doc](https://docs.google.com/document/d/1L_mt9ayVe7JOx5IxMLWVTso5iYxVD11meGNY3VOhBTg/edit). 59,814 matching predictions and 41,141 different.

### Cause of difference
In the original code the `adata.var.hugo_symbol` is used as the gene_name. This property is not available in datasets from other sources such as CellXGene and GTeX. Instead we use a [lookup table](./ensemble-lookup.csv) to translate ensembl identifiers to gene names. See [normalize_var_names](https://github.com/hubmapconsortium/hra-workflows/blob/main/containers/celltypist/context/main.py#L87) for the logic.

After applying this change to the original code in [run.py](./run.py) and rerunning the tool, the results matches the output of hra-workflows-runner **exactly**.
