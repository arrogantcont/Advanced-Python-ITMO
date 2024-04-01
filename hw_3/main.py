from matrix import Matrix_3_1, Matrix_3_2


def generate_matrix_data(seed, size=(10, 10), low=0, high=10):
    import random

    random.seed(seed)
    return [
        [random.randint(low, high - 1) for _ in range(size[1])] for _ in range(size[0])
    ]


def main_3_1(save_dir):
    matrix_a = Matrix_3_1(generate_matrix_data(0))
    matrix_b = Matrix_3_1(generate_matrix_data(1))

    add_res = matrix_a + matrix_b
    mult_res = matrix_a * matrix_b
    mat_mul_res = matrix_a @ matrix_b

    with open(f"{save_dir}/matrix+.txt", "w") as f:
        f.write(str(add_res))

    with open(f"{save_dir}/matrix*.txt", "w") as f:
        f.write(str(mult_res))

    with open(f"{save_dir}/matrix@.txt", "w") as f:
        f.write(str(mat_mul_res))


def check_getters_setters():
    print("Проверка геттеров и сеттеров из задания 3.2 \n")

    matrix = Matrix_3_2([[67, 676], [6767676, 76767676]])
    print("Исходные данные:")
    print(str(matrix.data))
    print("\nЧисло строк:")
    print(str(matrix.rows()))
    print("\nЧисло строк:")
    print(str(matrix.cols()))
    matrix.data = [0, 0]
    print("\nОбновили матрицу через сеттер:")
    print(str(matrix.data))


def main_3_2(save_dir):
    matrix_a = Matrix_3_2(generate_matrix_data(0))
    matrix_b = Matrix_3_2(generate_matrix_data(0))

    mat_mul_res = matrix_a @ matrix_b
    add_res = matrix_a + matrix_b
    sub_res = matrix_a - matrix_b
    mult_res = matrix_a * matrix_b

    operations = ["+", "-", "*", "@"]
    results = [add_res, sub_res, mult_res, mat_mul_res]
    filenames = [f"matrix{op}.txt" for op in operations]

    for filename, result in zip(filenames, results):
        with open(f"{save_dir}/{filename}", "w") as f:
            f.write(str(result))

    check_getters_setters()


if __name__ == "__main__":
    main_3_1(save_dir="hw_3/artifacts/3.1")
    main_3_2(save_dir="hw_3/artifacts/3.2")
