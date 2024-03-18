from latex_utils import generate_latex_table

# Пример исходных данных
data = [["one", "two", "three"], [1, 2, 3]]

# Вызов функции и сохранение в файл
latex_code = generate_latex_table(data)
with open("hw_2/artifacts/table_example.tex", "w") as file:
    file.write(latex_code)
