def generate_latex_table(table):
    num_columns = len(table[0])
    table_header = (
        "\\begin{tabular}{" + " | ".join(["c"] * num_columns) + "}\n\\hline\n"
    )
    table_body = ""
    for row in table:
        table_body += " & ".join(map(str, row)) + " \\\\\n\\hline\n"
    table_footer = "\\end{tabular}\n"

    result = table_header + table_body + table_footer
    return result


def add_image_to_latex(
    img_path, img_cap="cap", img_label="label", width="0.8\\textwidth"
):
    print(img_path, img_cap, img_label, width)
    return f"""\\begin{{figure}}[h]
    \\centering
    \\includegraphics[width={width}]{{{img_path}}}
    \\caption{{{img_cap}}}
    \\label{{{img_label}}}
\\end{{figure}}
"""


def generate_complete_latex_document(table, img_path, img_cap="cap", img_label="label"):
    document_class = "\\documentclass{article}\n"
    packages = "\\usepackage[utf8]{inputenc}\n\\usepackage{graphicx}\n"
    begin_document = "\\begin{document}\n"
    end_document = "\\end{document}\n"
    table_latex = generate_latex_table(table)
    image_latex = add_image_to_latex(img_path, img_cap, img_label)
    complete_document = (
        document_class
        + packages
        + begin_document
        + table_latex
        + image_latex
        + end_document
    )

    return complete_document
