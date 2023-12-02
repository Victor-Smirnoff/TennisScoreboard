from re import fullmatch


class NewMatchPostHandler:
    """
    Класс для обработки поступающих данных на странице '/new-match'
    Проверяет что записи Имя игрока 1 и Имя игрока 2 не пустые
    Что Имя игрока 1 и Имя игрока 2 не равны друг другу
    А также что имя состоит только из букв

    Если с полученными данными всё ок, то:
    1. Проверяет существование игроков в таблице Players. Если игрока с таким именем не существует, создаём
    2. Создаём экземпляр класса Match (содержащий айди игроков и текущий счёт) и кладём в коллекцию текущих матчей
    (существующую только в памяти приложения, либо в key-value storage).
    Ключом коллекции является UUID, значением - экземпляр класса Match.
    3. Редирект на страницу /match-score?uuid=$match_id
    """
    CURRENT_MATCHES = {} # коллекция текущих матчей

    def __call__(self, player_1_name, player_2_name):
        """
        Метод для вызова объекта класса NewMatchPostHandler
        :param player_1_name: имя игрока 1
        :param player_2_name: имя игрока 2
        :return: возвращаем HTML страницу
        """


    def is_correct_player_name(self, player_name: str) -> bool:
        """
        Метод проверяет имя игрока на коррекность
        :param player_name: имя игрока
        :return: bool True - если имя корректное, False - имя не корректное
        """
        return True if fullmatch(r"^[a-zA-Zа-яА-ЯёЁ ]+$", player_name) else False


# test_obj = NewMatchPostHandler()
# print(test_obj.is_correct_player_name(""))
# print(test_obj.is_correct_player_name("_"))
# print(test_obj.is_correct_player_name("123124"))
# print(test_obj.is_correct_player_name("паса2"))
# print(test_obj.is_correct_player_name("паса2Vasa"))
# print(test_obj.is_correct_player_name("2Vasa"))
# print(test_obj.is_correct_player_name("Vasa 531"))
#
# print(test_obj.is_correct_player_name("Vasa"))
# print(test_obj.is_correct_player_name("vasa"))
# print(test_obj.is_correct_player_name("Васа"))
# print(test_obj.is_correct_player_name("паса"))
# print(test_obj.is_correct_player_name("паса васа"))
# print(test_obj.is_correct_player_name("паса васа тык"))