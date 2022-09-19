from experta import *

all_skills = {
    "Опыт преподавания",
    "Грамотная речь",
    "Пользователь ПК",
    "Умение вести клиента",
    "Высшее образование",
    "Знание английского",
    "Знание SQL",
    "Знание Python",
    "Знание C/C++"
    "Знание Java",
    "Знание ООП",
    "Опыт в написании нейросетей",
    "Знание статистики",
    "Умение работать в коллективе",
    "Вождение автомобиля"
}


job_score = {
    "Programming teacher": 0,
    "MO engeneer": 0,
    "Data Scientist": 0,
    "Сourier Yandex food": 0,
    "Junior Java developer": 0,
    "Database Administrator": 0,
    "Sales Manager": 0
}


class EnterInfo(Fact):
    pass


class Rules(KnowledgeEngine):

    @Rule(EnterInfo(skill="Опыт преподавания"))
    def programming_expirience(self):
        job_score["Programming teacher"] += 1

    @Rule(EnterInfo(skill="Грамотная речь"))
    def right_speech(self):
        job_score["Programming teacher"] += 1

    @Rule(EnterInfo(skill="Пользователь ПК"))
    def user_pk(self):
        job_score["Programming teacher"] += 1

    @Rule(EnterInfo(skill="Умение вести клиента"))
    def client_skill(self):
        job_score["Sales Manager"] += 1
        job_score["Сourier Yandex food"] += 1

    @Rule(EnterInfo(skill="Высшее образование"))
    def master_degree(self):
        job_score["Programming teacher"] += 1
        job_score["Data Scientist"] += 1
        job_score["MO engeneer"] += 1
        job_score["Database Administrator"] += 1
        job_score["Junior Java developer"] += 1

    @Rule(EnterInfo(skill="Знание английского"))
    def know_english(self):
        job_score["Programming teacher"] += 1
        job_score["Data Scientist"] += 1
        job_score["MO engeneer"] += 1
        job_score["Database Administrator"] += 1
        job_score["Junior Java developer"] += 1

    @Rule(EnterInfo(skill="Знание SQL"))
    def know_sql(self):
        job_score["Database Administrator"] += 1

    @Rule(EnterInfo(skill="Знание Python"))
    def know_python(self):
        job_score["Data Scientist"] += 1
        job_score["MO engeneer"] += 1


    @Rule(EnterInfo(skill="Знание C/C++"))
    def know_cplus(self):
        job_score["Data Scientist"] += 1


    @Rule(EnterInfo(skill="Знание Java"))
    def know_java(self):
        job_score["Junior Java developer"] += 1

    @Rule(EnterInfo(skill="Знание ООП"))
    def know_oop(self):
        job_score["Junior Java developer"] += 1
        job_score["Programming teacher"] += 1
        job_score["Data Scientist"] += 1
        job_score["MO engeneer"] += 1
        job_score["Database Administrator"] += 1

    @Rule(EnterInfo(skill="Опыт в написании нейросетей"))
    def know_neyro(self):
        job_score["Data Scientist"] += 1
        job_score["MO engeneer"] += 1

    @Rule(EnterInfo(skill="Знание статистики"))
    def know_static(self):
        job_score["Data Scientist"] += 1
        job_score["MO engeneer"] += 1

    @Rule(EnterInfo(skill="Умение работать в коллективе"))
    def can_work_in_staff(self):
        job_score["Сourier Yandex food"] += 1
        job_score["Sales Manager"] += 1

    @Rule(EnterInfo(skill="Вождение автомобиля"))
    def got_car(self):
        job_score["Сourier Yandex food"] += 1
        job_score["Sales Manager"] += 1
        job_score["Junior Java developer"] += 1
        job_score["Programming teacher"] += 1
        job_score["Data Scientist"] += 1
        job_score["MO engeneer"] += 1
        job_score["Database Administrator"] += 1


def check_skills(user_skills):

    rules = Rules()
    rules.reset()

    data = {}

    rules.declare(EnterInfo(skill=user_skills["skill1"][0]))
    rules.declare(EnterInfo(skill=user_skills["skill2"][0]))
    rules.declare(EnterInfo(skill=user_skills["skill3"][0]))
    rules.declare(EnterInfo(skill=user_skills["skill4"][0]))
    rules.declare(EnterInfo(skill=user_skills["skill5"][0]))
    rules.declare(EnterInfo(skill=user_skills["skill6"][0]))
    rules.declare(EnterInfo(skill=user_skills["skill7"][0]))
    rules.declare(EnterInfo(skill=user_skills["skill8"][0]))
    rules.declare(EnterInfo(skill=user_skills["skill9"][0]))
    rules.declare(EnterInfo(skill=user_skills["skill10"][0]))
    rules.declare(EnterInfo(skill=user_skills["skill11"][0]))
    rules.declare(EnterInfo(skill=user_skills["skill12"][0]))
    rules.declare(EnterInfo(skill=user_skills["skill13"][0]))
    rules.declare(EnterInfo(skill=user_skills["skill14"][0]))
    rules.run()

    return job_score