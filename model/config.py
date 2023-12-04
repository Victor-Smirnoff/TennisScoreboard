

class Settings:
    """
    Класс для валидации данных для подключения к БД MySQL
    """
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_USER: str = "root"
    DB_PASS: str = "KUku1212_b2zZ"
    DB_NAME: str = "tennis"

    @property
    def DATA_BASE_URL(self):
        """
        Метод возвращает строку с данными для подключения к БД MySQL.
        Эти данные передаются в метод create_engine при создании объекта движка engine
        :return: str
        """
        # "mysql+pymysql://root:KUku1212_b2zZ@localhost:3306/tennis"
        return f"mysql+pymysql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

settings = Settings()