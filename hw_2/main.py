import argparse
from gfdreyur_latex_utils import generate_complete_latex_document
import json


def parse_table(table):
    try:
        table_type = json.loads(table)
        if isinstance(table_type, list) and all(
            isinstance(row, list) for row in table_type
        ):
            return table_type
        raise ValueError
    except ValueError:
        raise argparse.ArgumentTypeError(
            "Таблица должна быть задана как список списков (матрица)"
        )


parser = argparse.ArgumentParser(
    description="Сгенерировать .tex документ с таблицей и картинкой"
)
parser.add_argument(
    "--table",
    type=parse_table,
    default=[[1, 2, 3], [1, 2, 3]],
    help="Таблица в виде списка из списов [[1, 2, 3], [1, 2, 3]]",
)
parser.add_argument(
    "--img-path",
    type=str,
    default="hw_2/artifacts/image.png",
    help="Путь к картинке",
)
parser.add_argument("--img-cap", type=str, default="cap", help="Подпись картинки")
parser.add_argument(
    "--img-label",
    type=str,
    default="label",
    help="Название картинки",
)

args = parser.parse_args()

table = args.table
img_path = args.img_path
img_cap = args.img_cap
img_label = args.img_label

latex_document = generate_complete_latex_document(table, img_path, img_cap, img_label)

# Write the LaTeX document to a file
output_path = "artifacts/document.tex"
with open(output_path, "w") as file:
    file.write(latex_document)

print(f"LaTeX докумет сохранен в  {output_path}")
