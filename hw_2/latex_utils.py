def generate_latex_table(matrix):
    num_columns = len(matrix[0])
    document_class = "\\documentclass{article}\n"
    packages = "\\usepackage[utf8]{inputenc}\n"
    begin_document = "\\begin{document}\n"
    end_document = "\\end{document}"

    table_header = "\\begin{tabular}{" + "|c" * num_columns + "|}\n\hline\n"
    table_body = ""
    for row in matrix:
        table_body += " & ".join(map(str, row)) + " \\\\\n\hline\n"
    table_footer = "\\end{tabular}"

    complete_document = (
        document_class
        + packages
        + begin_document
        + table_header
        + table_body
        + table_footer
        + end_document
    )

    return complete_document
