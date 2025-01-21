from database import get_db
from database.models import *

# функция добавления юзера
def add_user_db(name, phone_number):
    # создаем сессию (первый вариант, устаревший)
    db = next(get_db())
    # создать объект нового пользователя
    new_user = User(username=name, phone_number=phone_number)
    # добавляем объект в бд
    db.add(new_user)
    # сохраняем изменения
    db.commit()
# получение всех юзеров
def get_all_user_db():
    # второй вариант создания сессии (актуальный)
    with next(get_db()) as db:
        all_users = db.query(User).all()
        return all_users
# получение информации об конкретном юзере
def get_exact_user_db(id):
    with next(get_db()) as db:
        exact_user = db.query(User).filter_by(id=id).one()
        # если мы смогли поместить информацию в переменную
        if exact_user:
            # мы передаем её
            return exact_user
        return "Юзер не найден"
# функция сохранения ответа






