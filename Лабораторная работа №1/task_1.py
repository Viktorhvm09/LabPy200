# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Chair:
    def __init__(self, color: str, height: int | float):
        """Инициализация стула

        :param color: Цвет стула.
        :param height: Высота стула.

        Примеры:
        >>> chair = Chair('Белый', 45) # инициализация экземпляра класса
        >>> chair = Chair('Белый', 54) # Неверная инициализация класса
        """
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
        if not isinstance(height, (int, float)):
            raise TypeError("Высота стула должна быть типа int или float")
        if float(48) < height < float(22):
            raise ValueError("Высота стула от 22 до 48")
        self.color = color
        self.height = height

    def set_color(self, color: str) -> None:
        """
        Изменение цвета стула.

        :param color: Задаваемый цвет.

        Пример:
        >>> chair = Chair('Белый', 45)
        >>> chair.set_color('Черный')
        """
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
        self.color = color

    def set_height(self, height: int | float) -> None:
            """
            Изменение высоты стула.

            :param height: Задаваемая высота.

            Пример:
            >>> chair = Chair('Белый', 45)
            >>> chair.set_height(30)
            """
            if not isinstance(height, (int, float)):
                raise TypeError("Значение должен быть типа int или float")
            if float(48) < height < float(22):
                raise ValueError("Высота стула от 22 до 48")
            self.height = height


class Table:
    def __init__(self, color: str | None, width: int | float, lenght: int | float):
        """Инициализация стола

        :param color: Цвет стола.
        :param width: Ширина стола.
        :param lenght: Длина стола.

        Примеры:
        >>> table = Table('Белый', 80, 120) # инициализация экземпляра класса
        >>> table = Table('Белый', 80, '120') # Неверная инициализация класса
        Traceback (most recent call last):
        ...
        TypeError: Ширина и длина стола должен быть типа int или float
        """

        if not (isinstance(width, (int, float)) and isinstance(lenght, (int, float))):
            raise TypeError("Ширина и длина стола должен быть типа int или float")
        if width < float(60):
            raise ValueError("Слишком узкий стол. Рекомендуется от 60 см")
        if lenght < float(40):
            raise ValueError("Слишком короткий стол. Рекомендуется от 40 см")

        self.color = None
        self.init_color(color)
        self.width = width
        self.lenght = lenght

    def init_color(self, color: str) -> None:
        """
        Инициализация цвета стола.

        :param color: Задаваемый цвет.

        Пример:
        >>> table = Table(color=None, width=60, lenght=50)
        >>> table.init_color('Черный')
        """
        if not isinstance(color, str|None):
            raise TypeError("Цвет должен быть типа str")
        self.color = color

    def quadratic(self) -> bool:
        """
        Проверка является ли стол квадратным.

        :return:  Является ли стол квадратным

        >>> table = Table(None, 60, 60)
        >>> table.quadratic()
        True
        """
        if self.width == self.lenght:
            return True
        else:
            return False

class PhoneBook:
    def __init__(self, name: None, phone: None):
        """"
        Инициализация записей телефонной книге.

        :param name: Имя абонента.
        :param phone: Телефон абонента.
        """
        self.name = None
        self.phone = None
        self.record(name, phone)

    def record(self, name: str, phone: int)-> None:
        """
        Инициализирование атрибутов объекта.
        :param name: Имя.
        :param phone: Телефон

        >>> first = PhoneBook('Max', 89998887766)
        """
        if not isinstance(name, str):
            raise TypeError("Имя должен быть типа str")
        self.name = name
        if not isinstance(phone, int):
            raise TypeError("Телефон должен быть типа int")
        if 12 < len(str(phone)) < 11:
            raise ValueError("Телефон должен быть от 11 до 12 символов")
        self.phone = phone

    def clean(self):
        """
        Очистка записи

        >>> first = PhoneBook('Max', 89998887766)
        >>> first.clean()
        """
        self.name = None
        self.phone = None

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
