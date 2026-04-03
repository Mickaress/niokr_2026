from django.core.management.base import BaseCommand
from django.db import transaction
from datetime import date, timedelta
from rest_framework.authtoken.models import Token
from api.models import User, UserProfile, EmployeeProfile, Company, Tag, Project, ProjectApplication


TEST_USERS = [
    {
        'external_id': 'test_customer',
        'full_name': 'Заказчиков Иван Иванович',
        'email': 'customer@test.ru',
        'phone': '+7 900 000 0001',
        'role': UserProfile.Role.CUSTOMER,
    },
    {
        'external_id': 'test_employee',
        'full_name': 'Сотрудников Пётр Петрович',
        'email': 'employee@test.ru',
        'phone': '+7 900 000 0002',
        'role': UserProfile.Role.EMPLOYEE,
    },
    {
        'external_id': 'test_admin',
        'full_name': 'Администраторов Сергей Сергеевич',
        'email': 'admin@test.ru',
        'phone': '+7 900 000 0003',
        'role': UserProfile.Role.ADMIN,
    },
]

TAGS = [
    'Байкальский институт БРИКС',
    'Институт авиамашиностроения и транспорта',
    'Институт архитектуры, строительства и дизайна',
    'Институт высоких технологий',
    'Институт заочно-вечернего обучения',
    'Институт информационных технологий и анализа данных',
    'Институт недропользования',
    'Институт "Сибирская школа геонаук (Siberian School of Geosciences)"',
    'Институт экономики, управления и права',
    'Институт энергетики',
]

COMPANIES = [
    {
        'name': 'ООО Технологии Будущего',
        'address': 'г. Москва, ул. Ленина, 10',
        'description': 'Компания занимается разработкой программного обеспечения для автоматизации бизнес-процессов.',
    },
]

PROJECT_TITLES = [
    'Цифровая платформа сопровождения студентов',
    'Сервис анализа образовательных метрик',
    'Система автоматизации документооборота',
    'Портал стажировок и практик',
    'Инструмент контроля проектной деятельности',
    'Единая база учебных кейсов',
    'Модуль оценки вовлеченности студентов',
    'Платформа мониторинга научных публикаций',
    'Сервис планирования учебной нагрузки',
    'Система подбора наставников и кураторов',
    'Портал управления лабораторными работами',
    'Инструмент аналитики карьерных траекторий',
    'Система учета достижений обучающихся',
    'Платформа организации проектных команд',
    'Сервис взаимодействия с индустриальными партнерами',
]


class Command(BaseCommand):
    help = 'Создаёт тестовых пользователей всех ролей и заполняет таблицы моковыми данными'

    @transaction.atomic
    def handle(self, *args, **options):
        # Теги
        tags = {}
        for tag_name in TAGS:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tags[tag_name] = tag
        self.stdout.write(f'Теги: создано/получено {len(tags)}')

        # Пользователи
        employee_profile = None
        customer_profile = None
        for data in TEST_USERS:
            role = data['role']
            user, created = User.objects.get_or_create(
                external_id=data['external_id'],
                defaults={
                    'full_name': data['full_name'],
                    'email': data['email'],
                    'phone': data['phone'],
                },
            )
            user.full_name = data['full_name']
            user.email = data['email']
            user.phone = data['phone']
            user.save(update_fields=['full_name', 'email', 'phone'])
            profile, _ = UserProfile.objects.get_or_create(user=user, defaults={'role': role})

            if role == UserProfile.Role.CUSTOMER:
                customer_profile = profile

            elif role == UserProfile.Role.EMPLOYEE:
                emp, _ = EmployeeProfile.objects.get_or_create(profile=profile, defaults={
                    'competencies': 'Коммуникация, работа в команде, критическое мышление, тайм-менеджмент, адаптивность',
                })
                emp.competencies = 'Коммуникация, работа в команде, критическое мышление, тайм-менеджмент, адаптивность'
                emp.save(update_fields=['competencies'])
                emp.tags.set([tags[TAGS[0]], tags[TAGS[3]], tags[TAGS[5]]])
                employee_profile = emp

            token, _ = Token.objects.get_or_create(user=user)
            status = 'создан' if created else 'уже существует'
            self.stdout.write(f'[{role}] {data["external_id"]} — {status} | Токен: {token.key}')

        # Компании (после создания customer_profile)
        companies = []
        for data in COMPANIES:
            company, _ = Company.objects.get_or_create(name=data['name'], defaults={
                'address': data['address'],
                'description': data['description'],
                'customer': customer_profile,
            })
            companies.append(company)
        self.stdout.write(f'Компании: создано/получено {len(companies)}')

        statuses = (
            [Project.Status.REVIEW] * 5 +
            [Project.Status.ACTIVE] * 5 +
            [Project.Status.ARCHIVED] * 5
        )
        projects_payload = []
        today = date.today()
        for i, (title, status) in enumerate(zip(PROJECT_TITLES, statuses), start=1):
            start_date = today + timedelta(days=i * 7)
            end_date = start_date + timedelta(days=180)
            first_tag = TAGS[(i - 1) % len(TAGS)]
            second_tag = TAGS[(i + 2) % len(TAGS)]
            projects_payload.append(
                {
                    'name': title,
                    'description': f'Тестовый проект "{title}" в статусе {status}.',
                    'date_start': start_date,
                    'date_end': end_date,
                    'status': status,
                    'tags': [first_tag, second_tag],
                    'views': i * 10,
                }
            )

        for i, data in enumerate(projects_payload):
            company = companies[i % len(companies)]
            project, created = Project.objects.get_or_create(
                name=data['name'],
                defaults={
                    'description': data['description'],
                    'date_start': data['date_start'],
                    'date_end': data['date_end'],
                    'status': data['status'],
                    'company': company,
                    'views': data['views'],
                },
            )
            project.tags.set([tags[t] for t in data['tags']])

            if employee_profile and not ProjectApplication.objects.filter(project=project, employee=employee_profile).exists():
                ProjectApplication.objects.create(project=project, employee=employee_profile)

        self.stdout.write(f'Проекты: создано/получено {len(projects_payload)}')
        self.stdout.write(self.style.SUCCESS('\nМоковые данные успешно загружены.'))
        self.stdout.write('\nВход: POST /api/login/ с телом {"external_id": "<external_id>"}')
