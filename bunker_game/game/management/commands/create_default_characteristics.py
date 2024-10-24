from typing import Any

from django.apps import apps
from django.core.management import BaseCommand
from django.db import transaction


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args: Any, **options: Any) -> None:
        diseases = [
            "Алкоголизм",
            "Аллергия На Животных",
            "Ангина",
            "Анорексия",
            "Астма",
            "Аутизм",
            "Авитаминоз",
            "Бессонница",
            "Бесплодность",
            "Биполярное расстройство",
            "Болезнь Альцгеймера",
            "Ветрянка",
            "ВИЧ",
            "Гастрит",
            "Гайморит",
            "Гемофилия",
            "Гепатит B",
            "Глаукома",
            "Глухота",
            "Грыжа",
            "Дальтонизм",
            "Депрессия",
            "Диарея",
            "ДЦП",
            "Заикание",
            "Желтуха",
            "Кариес",
            "Косоглазие",
            "Ожирение",
            "Медвежья болезнь (непроизвольное выделение мочи)",
            "Межпозвоночная грыжа",
            "Мигрень",
            "Мочекаменная болезнь",
            "Наркомания",
            "Недержание мочи",
            "Ожирение",
            "Остеохондроз",
            "Отит (воспаление уха)",
            "Паранойя",
            "Пневмония",
            "Плоскостопие",
            "Поражение сердечной мышцы",
            "Простуда",
            "Псориаз",
            "Психопатия",
            "Птичий грипп",
            "Рак",
            "Сахарный диабет",
            "Сифилис",
            "Синдром Дауна",
            "Синдром Туретта",
            "Слепота",
            "СПИД",
            "Травма глаза",
            "Туберкулёз",
            "Умственная недостаточность",
            "Цинга",
            "Цистит (воспаление мочевого пузыря)",
            "Цирроз печени",
            "Шизофрения",
            "Эпилепсия",
            "Язва желудка",
            "Ячмень",
            "Полностью здоров",
            "Легкое Ожирение",
        ]

        professions = {
            "Биолог": "Может выращивать растения для медицинских целей",
            "Винодел": "",
            "Повар": "",
            "Хирург": "",
            "Программист": "",
            "Хакер": "Может взломать защиту другого бункера",
            "Матрос": "",
            "Биохимик": "",
            "Таксист": "",
            "Кассир": "",
            "Художник": "",
            "Предприниматель": "",
            "Режиссёр": "",
            "Писатель": "",
            "Психолог": "Может вылечить фобию любого игрока",
            "Продавец оружия": "В багаж добавлен разряженный пистолет",
            "Депутат": "",
            "Полицейский": "",
            "Физик": "",
            "Педиатр": "",
            "Банкир": "",
            "Экономист": "",
            "Инженер-химик": "",
            "Инженер": "",
            "Агент ФБР": "",
            "Охранник": "",
            "Пилот": "Может управлять любым воздушным транспортом",
            "Кинолог": "Может дрессировать собак для поиска ресурсов",
            "Грузчик": "",
            "Бухгалтер": "",
            "Военный": "Может использовать оружие в бою",
            "Гробовщик": "",
            "Священник": "Может снизить стресс игроков",
            "Акушер": "",
            "Военный летчик": "Может управлять любым воздушным транспортом",
            "Нейрохирург": "",
            "Садовод": "Может выращивать еду в экстремальных условиях",
            "Слесарь": "",
            "Плотник": "Может строить защитные сооружения",
            "Фермер": "",
            "Сексолог": "Может сменить ориентацию игрока на гетеросексуальность",
            "Гид": "",
            "Президент": "",
            "Сварщик": "Может ремонтировать технику",
            "Военный врач": "Может лечить раны и болезни",
            "Дипломат": "Может сделать враждебный бункер дружелюбным",
            "Стриптизёр": "",
            "Спецназовец": "Может вести боевые операции",
            "Учитель": "",
            "Продавец одежды": "",
            "Флорист": "Может выращивать растения для медицинских целей",
            "Уролог": "",
            "Венеролог": "",
            "Учёный": "",
            "Кондитер": "",
            "Продюсер": "",
            "Певец": "Может поднять настроение группы",
            "Музыкант": "",
            "Диспетчер": "",
            "Водитель автобуса": "Может управлять большими транспортными средствами",
            "Тату-мастер": "",
            "Порно-звезда": "",
            "Вебкам-модель": "",
            "Надзиратель": "",
            "Судья": "",
            "Адвокат": "",
            "Дворник": "",
        }

        phobias = [
            "Арахнофобия - боязнь пауков",
            "Клаустрофобия - боязнь закрытых пространств и помещений",
            "Отсутствует",
            "Авиафобия - боязнь полетов",
            "Акрофобия - боязнь высоты",
            "Агорафобия - боязнь открытых мест и пространств",
            "Некрофобия - боязнь трупов и похоронных принадлежностей",
            "Гемофобия - боязнь крови",
            "Мизофобия - боязнь заразиться инфекционным заболеванием",
            "Герпетофобия - боязнь рептилий",
            "Канцерофобия - боязнь заболевания раком",
            "Айлурофобия - боязнь кошек",
            "Кинофобия - боязнь собак",
            "Спермофобия - боязнь микробов",
            "Пирофобия - боязнь огня и пожаров",
            "Танатофобия - боязнь смерти",
            "Гидрофобия - боязнь воды",
            "Гипнофобия - боязнь заснуть",
            "Теофобия - боязнь бога",
            "Филофобия - боязнь влюбиться",
            "Эротофобия - боязнь секса",
            "Аграфобия - боязнь больших открытых пространств",
            "Аутофобия - страх одиночества",
            "Ахлуофобия - боязнь темноты",
            "Бронтофобия - боязнь грома",
            "Децидофобия - боязнь принимать решения",
            "Зоофобия - боязнь животных",
            "Инсектофобия - боязнь насекомых",
            "Трипанофобия - боязнь уколов",
            "Токсикофобия - боязнь отравления",
            "Айхмофобия - боязнь острых предметов",
            "Ангинофобия - боязнь сердечного приступа",
            "Клаустрофобия - боязнь замкнутых пространств",
            "Агамофобия - боязнь брака",
            "Копрофобия - боязнь фекалий",
            "Коулрофобия - боязнь клоунов",
            "Криптофобия - боязнь скрытых угроз",
            "Лалофобия - боязнь говорить",
            "Лифтофобия - боязнь лифтов",
            "Мирмекофобия - боязнь муравьев",
            "Маниофобия - боязнь психических заболеваний",
            "Неофобия - боязнь нового",
            "Нозокомефобия - боязнь больниц",
            "Орнитофобия - боязнь птиц",
            "Панофобия - боязнь всего",
            "Педиофобия - боязнь кукол",
            "Танатофобия - боязнь смерти",
            "Скабиофобия - боязнь чесотки",
            "Теофобия - боязнь божественного наказания",
            "Фазмофобия - боязнь призраков",
            "Гомофобия - боязнь проявления гомосексуальности",
            "Херофобия - боязнь веселья",
            "Гаптофобия - боязнь прикосновений",
            "Хирофобия - боязнь хирургов или операций",
            "Топофобия - боязнь быть одному в помещении",
            "Фотофобия - боязнь света",
            "Хроматофобия - боязнь какого-либо цвета",
            "Анемофобия - боязнь ветра",
            "Филофобия - боязнь эмоциональной привязанности",
            "Агорафобия - боязнь толпы",
            "Венерофобия - боязнь венерических заболеваний",
            "Акрофобия - страх высоты",
            "Геронтофобия — страх старости",
            "Электрофобия — боязнь электричества",
        ]

        hobbies = [
            "Рисование",
            "Писательство",
            "Программирование",
            "Вышивание",
            "Танцы",
            "Интересуется светскими новостями",
            "Астрология",
            "Картография",
            "Биология",
            "Физика",
            "Математика",
            "Делать украшения из бисера",
            "Делать мозаики",
            "Бег",
            "Азартные игры",
            "Стенд-ап",
            "Изготовлять куклы",
            "Плетение корзин из веток",
            "Животноводство",
            "Выращивание растений",
            "Занимается ювелирством",
            "Коллекционирует монеты",
            "Коллекционирует сушеных насекомых",
            "Готовка",
            "Альпинизм",
            "Теннис",
            "Баскетбол",
            "Волейбол",
            "Верховая езда",
            "Стрельба из лука",
            "Стрельба из оружия",
            "Увлекается иностранными языками",
            "Разрабатывание сайтов",
            "Лепит горшки и посуду из глины",
            "Разводить животных",
            "Разыгрывать всех подряд",
            "Плаванье",
            "Спорт",
            "Автомобили",
            "Ароматерапия",
            "Астрономия",
            "Аэробика",
            "Аэрография",
            "Бадминтон",
            "Батут",
            "Бильярд",
            "Блоггерство",
            "Бодиарт",
            "Боевые искусства",
            "Боулинг",
            "Велосипед",
            "Видеомонтаж",
            "Вязание",
            "Гербарий",
            "Головоломки",
            "Гольф",
            "Горные лыжи",
            "Граффити",
            "Дайвинг",
            "Дартс",
            "Декупаж",
            "Дерево (выжигание и резьба)",
            "Дизайн интерьера",
            "Дизайн одежды",
            "Животные (разведение и уход)",
            "Жонглирование",
            "Игра на музыкальных инструментах",
            "Игрушки и куклы",
            "Игры на компьютерах и приставках",
            "Изделия из металла и кузнечное дело",
            "Икебана",
            "Йога",
            "Исторические реконструкции",
            "Каллиграфия",
            "Картинг и квадроциклы",
            "Квест-комнаты",
            "Кладоискательство и археология",
            "Коллекционирование",
            "Компьютерная графика",
            "Посещение концертов",
            "Лазертаг",
            "Лепка",
            "Верховая езда на лошадях",
        ]

        characters = [
            "Авантюризм",
            "Безотказность",
            "Безынициативность",
            "Благоразумность",
            "Боязливость",
            "Буйность",
            "Весёлость",
            "Властность",
            "Внимательность",
            "Внушаемость",
            "Ворчливость",
            "Гостеприимность",
            "Грубость",
            "Деликатность",
            "Добродушие",
            "Доброта",
            "Доверчивость",
            "Жадность",
            "Жестокость",
            "Жизнерадостность",
            "Истеричность",
            "Конфликтность",
            "Лицемерие",
            "Любезность",
            "Надёжность",
            "Невозмутимость",
            "Нежность",
            "Ненадёжность",
            "Неравнодушие",
            "Неусидчивость",
            "Обидчивость",
            "Осторожность",
            "Пофигизм",
            "Предприимчивость",
            "Равнодушие",
            "Расчётливость",
            "Самовлюбленность",
            "Самостоятельность",
            "Сдержанность",
            "Скандальность",
            "Слабохарактерность",
            "Собранность",
            "Терпеливость",
            "Тревожность",
            "Трусость",
            "Усидчивость",
            "Флегматичность",
            "Харизматичность",
            "Храбрость",
            "Эгоизм",
            "Вальяжность",
            "Плаксивость",
            "Смелость",
            "Открытость",
            "Замкнутость",
            "Благородство",
            "Болтливость",
            "Героизм",
            "Коварство",
            "Любопытство",
            "Недотрога",
            "Пунктуальность",
            "Скромность",
            "Упрямство",
            "Наглость",
            "Щедрость",
            "Душнила",
        ]

        additional_info = [
            "Работал вожатым в летнем лагере",
            "Ведёт личный дневник с подростковых лет",
            "Убеждён в существовании инопланетян",
            "Верит в существование потусторонних существ",
            "Обладает отличной физической подготовкой",
            "Выиграл в лотерею крупную сумму денег",
            "Победил в марафоне на 42 километра",
            "Знает наизусть все стихотворения Пушкина",
            "Владеет четырьмя иностранными языками",
            "Выступал в театре на главных ролях",
            "Имеет два высших образования, одно из них техническое",
            "Считает, что у него экстрасенсорные способности",
            "Коллекционирует мягкие игрушки с детства",
            "Может оказать квалифицированную первую помощь",
            "Ненавидит вкус кофе и никогда его не пьёт",
            "Презирает современную поп-музыку",
            "Не переносит алкоголь даже в малых дозах",
            "Обладает феноменальной памятью, помнит даты и цифры",
            "Ограбил банк и остался безнаказанным",
            "Пережил три покушения на свою жизнь",
            "Побывал в 18 странах за последние три года",
            "Покорил вершину Эвереста в одиночку",
            "По первому образованию врач-терапевт",
            "Лично участвовал в проектировании этого бункера",
            "Проходил курсы по самообороне и владеет боевыми искусствами",
            "Заканчивал кулинарные курсы, умеет готовить как шеф-повар",
            "Проходил курсы профессионального массажа",
            "Учился на парикмахера и подстригает всех друзей",
            "Проходил курсы психологии и хорошо разбирается в людях",
            "Отсидел срок в тюрьме за мошенничество",
            "Спас тонущего человека, рискуя собственной жизнью",
            "Страдает морской болезнью, поэтому избегает поездок на воде",
            "Уверен, что живёт в компьютерной симуляции",
            "Убеждён, что эта катастрофа — дело рук рептилоидов",
            "Занимается животноводством и разводит редкие породы коров",
            "Увлекается охотой на крупную дичь",
            "Мастерски вскрывает замки без ключа",
            "Умеет жонглировать пятью предметами одновременно",
            "Ориентируется по звёздам лучше, чем по карте",
            "Свободно владеет высшей математикой, решает задачи в уме",
            "Чемпион по покеру среди друзей",
            "Умеет находить общий язык с любыми животными",
            "Хорошо ориентируется в любых условиях — хоть в лесу, хоть в городе",
            "Читал все книги о выживании на необитаемом острове",
            "Является убеждённым вегетарианцем уже много лет",
            "Мастер спорта по боксу, имеет множество наград",
            "Может продать всё что угодно — от машины до ручки",
            "Контактировал с инопланетянами и твёрдо верит в это",
            "Приютил 40 кошек и любит каждую из них",
            "Зависим от алкоголя, хотя старается бросить",
            "Делает зарядку каждое утро, не пропускает ни дня",
            "Строго придерживается принципов правильного питания",
            "Часто ходит по дому без одежды — чувствует себя так свободнее",
            "Превосходно готовит вино из любых фруктов",
            "Легко готовит консервы, как профессиональный повар",
            "Однажды спас котёнка из горящего дома",
            "Прячется от полиции за мошенничество",
            "Бегает от закона, скрываясь под чужим именем",
            "Панически боится облысеть и покупает дорогие шампуни",
            "Снимает тик-токи на любую тему и обожает быть в центре внимания",
            "Проиграл свой дом на ставках, но не теряет надежды",
            "До сих пор девственник и не стыдится этого",
            "Никогда не врёт, даже когда это доставляет проблемы",
            "Любит подсматривать за людьми и наблюдать за их поведением",
            "Знает больше анекдотов, чем любой человек, которого вы встретите",
            "Обожает обсуждать политику и всегда в теме",
        ]

        baggages = [
            "Беспроводная колонка",
            "Будильник",
            "Бутылка шампанского",
            "Гаечный ключ",
            "Газовая горелка",
            "Гитара",
            "Грудной ребёнок",
            "Губная гармошка",
            "Дедовское ружьё",
            "Десять одноразовых медицинских масок",
            "Дневник выжившего",
            "Дублёнка",
            "Зажигалка",
            "Карманные часы",
            "Карта местности",
            "Кассеты с фильмами",
            "Книга по социологии",
            "Компас",
            "Консервы",
            "Коробка с боеприпасами",
            "Коробок спичек",
            "Косметическое зеркало",
            "Ледоруб и трос",
            "Лейка",
            "Лук и стрелы",
            "Молоток и гвозди",
            "Музыкальная шкатулка",
            "Набор для шитья",
            "Набор инструментов",
            "Набор кухонных инструментов",
            "Настольные игры",
            "Немецкая овчарка",
            "Ноутбук",
            "Открывалка",
            "Пачка сигарет",
            "Персидский кот",
            "Пневматический пистолет",
            "Презервативы",
            "Противогаз",
            "Пустая коробка",
            "Радио",
            "Рулоны туалетной бумаги",
            "Семена капусты",
            "Семена картофеля",
            "Семена моркови",
            "Семена пшеницы",
            "Сотовый телефон",
            "Стерильные одноразовые шприцы",
            "Стопка журналов для взрослых",
            "Телевизор",
            "Топор и верёвка",
            "Три респираторные маски",
            "Флейта",
            "Фонарик и запасные батарейки",
            "Фотоаппарат",
            "Четыре рации",
            "Две пары трусов",
            "Аптечка",
            "Миллион долларов",
            "Чемодан с крышками от бутылок",
            "Коллекция порно журналов",
            "Видеомагнитофон и кассеты",
            "Караоке",
            "Десять пакетов",
            "Комнатный цветок",
            "Десять айфонов",
            "Пробирка с вирусом",
            "Винтажная статуэтка",
            "Мороженое",
            "Деревянная палка",
            "Селфи-палка",
            "Пульт от телевизора",
            "Крем от загара",
            "Чертеж бункера",
            "Банка с огурцами",
            "Мыло",
            "Верёвка",
            "Корм для животных",
            "Гриль",
            "Штатив",
            "Бочка с вином",
            "Удобрения",
            "Подгузники",
            "Тест на беременность",
            "Блок сигарет",
            "Генератор",
            "Беруши",
            "Маска для сна",
            "Пижама",
            "Накладной нос",
            "Фара от автомобиля",
            "Спички",
            "Набор сух пайков",
            "Бочка чистой воды",
            "Коллекция настольных игр",
            "Нож",
            "Набор инструментов",
            "Самогонный аппарат",
            "Надувной матрац",
            "Ортопедическая подушка",
            "Надувной бассейн с шариками",
            "Набор для вышивания",
            "Набор таблеток первой необходимости",
            "Компас",
            "Кофейный аппарат",
        ]

        characteristics = {
            "Disease": diseases,
            "Profession": professions,
            "Phobia": phobias,
            "Hobby": hobbies,
            "Character": characters,
            "AdditionalInfo": additional_info,
            "Baggage": baggages,
        }

        for model_type, values in characteristics.items():
            model = apps.get_model("game", model_type)
            if type(values) is list:
                for name in values:
                    if model_type in frozenset(
                        ["Phobia", "Hobby", "Baggage", "Disease"],
                    ):
                        model.objects.filter(is_generated=False).get_or_create(
                            name=name,
                        )
                    else:
                        model.objects.get_or_create(name=name)
            elif type(values) is dict:
                for name, skill in values.items():
                    model.objects.get_or_create(
                        name=name,
                        is_generated=False,
                        additional_skill=skill,
                    )
            model_name = model._meta.verbose_name_plural.capitalize()  # noqa: SLF001
            self.stdout.write(self.style.SUCCESS(f"... {model_name} созданы ..."))
