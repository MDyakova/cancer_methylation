# cancer_methylation

# check syntactic errors
flake8_nb --notebook-cell-format '{nb_path}:code_cell#{code_cell_count}' FILE_NAME
black data_preparation.ipynb