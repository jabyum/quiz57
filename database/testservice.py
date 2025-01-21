from database import get_db
from database.models import *

# функция добавления вопроса

def add_question_db(main_question, v1,v2, correct_answer, level,
                    v3=None, v4=None):
    with next(get_db()) as db:
        new_question = Question(main_question=main_question,
                                v1=v1, v2=v2, v3=v3, v4=v4,
                                correct_answer=correct_answer,
                                level=level)
        db.add(new_question)
        db.commit()
        return True

