import numpy as np


class Matrix_3_1:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы отличаются по размерам.")
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix_3_1(result)

    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы отличаются по размерам.")
        result = [
            [self.data[i][j] * other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix_3_1(result)

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError(
                "Матрицы отличаются по размерам. Количество столбцов в первой мрице должно сопадать с количеством строк во второй матрице."
            )
        result = [
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ]
        return Matrix_3_1(result)

    def __str__(self):
        matrix_3_1_str = ""
        for row in self.data:
            row_str = " ".join(f"{elem:3}" for elem in row)
            matrix_3_1_str += f"|{row_str} |\n"
        return matrix_3_1_str


import numpy as np


class Matrix_3_2:
    def __init__(self, data):
        self._data = np.array(data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = np.array(value)

    def rows(self):
        return self._data.shape[0]

    def cols(self):
        return self._data.shape[1]

    def __add__(self, other):
        if self._data.shape != other._data.shape:
            raise ValueError("Матрицы отличаются по размерам.")
        return Matrix_3_2(self._data + other._data)

    def __sub__(self, other):
        if self._data.shape != other._data.shape:
            raise ValueError("Матрицы отличаются по размерам.")
        return Matrix_3_2(self._data - other._data)

    def __mul__(self, other):
        if isinstance(other, Matrix_3_2):
            if self._data.shape != other._data.shape:
                raise ValueError("Матрицы отличаются по размерам.")
            return Matrix_3_2(self._data * other._data)
        else:
            return Matrix_3_2(self._data * other)

    def __matmul__(self, other):
        if self.cols() != other.rows():
            raise ValueError(
                "Матрицы отличаются по размерам. Количество столбцов в первой мрице должно сопадать с количеством строк во второй матрице."
            )
        return Matrix_3_2(self._data @ other._data)

    def __str__(self):
        return "\n".join(
            [
                "| "
                + " ".join(
                    f"{int(item):3}" if item.is_integer() else f"{item:3.2f}"
                    for item in row
                )
                + " |"
                for row in self._data
            ]
        )

    def save_matrix_to_txt(self, file_path):
        with open(file_path, "w") as file:
            file.write(self.__str__())
