import asyncio
import calendar as cal
from datetime import datetime, timedelta

import flet as ft


def main(page: ft.Page):
  # Базовые настройки страницы
  page.title = "Совет обучающихся"
  page.bgcolor = "#F8F8F8"
  page.fonts = {"MainFont": "fonts/ofont_ru_FindSans_Pro.ttf"}

  page.theme = ft.Theme(
      font_family="MainFont",
      text_theme=ft.TextTheme(
          display_large=ft.TextStyle(
              font_family="MainFont",
              color="#13233D",
          ),
          display_medium=ft.TextStyle(
              font_family="MainFont",
              color="#13233D",
          ),
          display_small=ft.TextStyle(
              font_family="MainFont",
              color="#13233D",
          ),
          headline_large=ft.TextStyle(
              font_family="MainFont",
              color="#13233D",
          ),
          headline_medium=ft.TextStyle(
              font_family="MainFont",
              color="#13233D",
          ),
          headline_small=ft.TextStyle(
              font_family="MainFont",
              color="#13233D",
          ),
          title_large=ft.TextStyle(
              font_family="MainFont",
              color="#13233D",
          ),
          title_medium=ft.TextStyle(
              font_family="MainFont",
              color="#13233D",
          ),
          title_small=ft.TextStyle(
              font_family="MainFont",
              color="#13233D",
          ),
          label_large=ft.TextStyle(
              font_family="MainFont",
              color="#13233D",
          ),
          label_medium=ft.TextStyle(
              font_family="MainFont",
              color="#13233D",
          ),
          label_small=ft.TextStyle(
              font_family="MainFont",
              color="#13233D",
          ),
          body_large=ft.TextStyle(
              font_family="MainFont",
              color="#13233D",
          ),
          body_medium=ft.TextStyle(
              font_family="MainFont",
              color="#13233D",
          ),
          body_small=ft.TextStyle(
              font_family="MainFont",
              color="#13233D",
          ),
      ),
  )

  # Основной контейнер, в который динамически загружаются экраны приложения
  content = ft.Container(expand=True)

  # Виджет часов для отображения текущего времени в реальном времени
  clock = ft.Text(
      "00:00",
      size=300,
      weight=ft.FontWeight.BOLD,
      color="#13233D",
  )

  # Состояние приложения: отслеживание текущей активной вкладки
  active_page = "home"

  # Хранилища данных в памяти (в будущем могут быть заменены на SQLite)
  calendar_data = {}

  # Глобальный список мероприятий
  events_data = [
      {
          "title": "День спорта",
          "date": "20.09.2026",
          "direction": "Спорт",
          "description": "Спортивное мероприятие для учащихся школы.",
          "photo": None,
      },
      {
          "title": "День волонтёра",
          "date": "24.09.2026",
          "direction": "Волонтёрство",
          "description": "Общее волонтёрское мероприятие Совета обучающихся.",
          "photo": None,
      },
      {
          "title": "Научный квиз",
          "date": "28.09.2026",
          "direction": "Наука и учёба",
          "description": "Интеллектуальная игра для участников школы.",
          "photo": None,
      },
      {
          "title": "Творческий вечер",
          "date": "02.10.2026",
          "direction": "Творчество",
          "description": "Вечер творческих выступлений учащихся.",
          "photo": None,
      },
  ]

  # ==========================================
  # 1. ГЛАВНАЯ СТРАНИЦА
  # ==========================================
  def home(e):
    nonlocal active_page
    active_page = "home"

    # Формируем интерфейс главного экрана
    content.content = ft.Column(
        controls=[
            # Часы
            ft.Container(
                height=450,
                margin=ft.Margin(
                    top=120,
                    right=0,
                    bottom=0,
                    left=0,
                ),
                alignment=ft.Alignment(0, 0),
                content=clock,
            ),
            # Карточки
            ft.Container(
                margin=ft.Margin(
                    top=80,
                    right=35,
                    bottom=0,
                    left=35,
                ),
                content=ft.Row(
                    controls=[
                        # Информационный блок: Ближайшие мероприятия
                        ft.Container(
                            expand=True,
                            height=250,
                            bgcolor="#F8F8F8",
                            padding=50,
                            border_radius=60,
                            border=ft.Border.all(1, "#13233D"),
                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        "Ближайшие мероприятия",
                                        size=20,
                                        color="#13233D",
                                    ),
                                    ft.Text(
                                        "Пока мероприятий нет",
                                        color="#13233D",
                                    ),
                                ]
                            ),
                        ),
                        # Информационный блок: Ближайшие дни рождения
                        ft.Container(
                            width=550,
                            height=250,
                            bgcolor="#F8F8F8",
                            padding=50,
                            border_radius=60,
                            border=ft.Border.all(1, "#13233D"),
                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        "Ближайшие дни рождения",
                                        size=20,
                                        color="#13233D",
                                    ),
                                    ft.Text(
                                        "Пока дней рождений нет",
                                        color="#13233D",
                                    ),
                                ]
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=40,
                ),
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )

    page.update()

  # ==========================================
  # 2. СТРАНИЦА УЧАСТНИКОВ
  # ==========================================
  def members(e):
    nonlocal active_page
    active_page = "members"

    # Создаём временные данные только один раз
    if not hasattr(members, "members_data"):
      members.members_data = [
          {
              "name": "Иван Иванов",
              "photo": "assets/members/member1.jpg",
              "points": 250,
              "class": "10А",
              "birthday": "15.04.2008",
              "hobbies": "Фотография, спорт",
              "qualities": "Ответственный, активный",
              "history": [],
          },
          {
              "name": "Алексей Петров",
              "photo": "assets/members/member1.jpg",
              "points": 210,
              "class": "10Б",
              "birthday": "22.06.2008",
              "hobbies": "Музыка, рисование",
              "qualities": "Общительный, инициативный",
              "history": [],
          },
          {
              "name": "Максим Смирнов",
              "photo": "assets/members/member1.jpg",
              "points": 180,
              "class": "9А",
              "birthday": "03.09.2008",
              "hobbies": "Чтение, спорт",
              "qualities": "Внимательный, спокойный",
              "history": [],
          },
          {
              "name": "Дмитрий Кузнецов",
              "photo": "assets/members/member1.jpg",
              "points": 160,
              "class": "11А",
              "birthday": "11.01.2008",
              "hobbies": "Футбол",
              "qualities": "Активный, доброжелательный",
              "history": [],
          },
          {
              "name": "Артём Попов",
              "photo": "assets/members/member1.jpg",
              "points": 150,
              "class": "10А",
              "birthday": "19.02.2008",
              "hobbies": "Танцы",
              "qualities": "Творческий, ответственный",
              "history": [],
          },
          {
              "name": "Кирилл Васильев",
              "photo": "assets/members/member1.jpg",
              "points": 140,
              "class": "9Б",
              "birthday": "27.03.2008",
              "hobbies": "Волейбол",
              "qualities": "Командный, активный",
              "history": [],
          },
          {
              "name": "Роман Новиков",
              "photo": "assets/members/member1.jpg",
              "points": 130,
              "class": "10Б",
              "birthday": "05.05.2008",
              "hobbies": "Компьютеры",
              "qualities": "Усидчивый, внимательный",
              "history": [],
          },
          {
              "name": "Егор Морозов",
              "photo": "assets/members/member1.jpg",
              "points": 120,
              "class": "9А",
              "birthday": "16.06.2008",
              "hobbies": "Баскетбол",
              "qualities": "Энергичный, общительный",
              "history": [],
          },
          {
              "name": "Михаил Волков",
              "photo": "assets/members/member1.jpg",
              "points": 110,
              "class": "11Б",
              "birthday": "29.07.2008",
              "hobbies": "Музыка",
              "qualities": "Спокойный, ответственный",
              "history": [],
          },
          {
              "name": "Никита Фёдоров",
              "photo": "assets/members/member1.jpg",
              "points": 100,
              "class": "10А",
              "birthday": "08.08.2008",
              "hobbies": "Фотография",
              "qualities": "Творческий, активный",
              "history": [],
          },
          {
              "name": "Даниил Орлов",
              "photo": "assets/members/member1.jpg",
              "points": 90,
              "class": "9Б",
              "birthday": "14.09.2008",
              "hobbies": "Игры",
              "qualities": "Командный, дружелюбный",
              "history": [],
          },
          {
              "name": "Илья Андреев",
              "photo": "assets/members/member1.jpg",
              "points": 80,
              "class": "10Б",
              "birthday": "21.10.2008",
              "hobbies": "Рисование",
              "qualities": "Креативный, внимательный",
              "history": [],
          },
          {
              "name": "Матвей Захаров",
              "photo": "assets/members/member1.jpg",
              "points": 70,
              "class": "11А",
              "birthday": "04.11.2008",
              "hobbies": "Бег",
              "qualities": "Целеустремлённый, активный",
              "history": [],
          },
          {
              "name": "Александр Павлов",
              "photo": "assets/members/member1.jpg",
              "points": 60,
              "class": "9А",
              "birthday": "12.12.2008",
              "hobbies": "Кино",
              "qualities": "Спокойный, добрый",
              "history": [],
          },
          {
              "name": "Тимофей Семёнов",
              "photo": "assets/members/member1.jpg",
              "points": 50,
              "class": "10А",
              "birthday": "18.01.2008",
              "hobbies": "Настольные игры",
              "qualities": "Внимательный, общительный",
              "history": [],
          },
          {
              "name": "Владислав Беляев",
              "photo": "assets/members/member1.jpg",
              "points": 40,
              "class": "10Б",
              "birthday": "25.02.2008",
              "hobbies": "Спорт",
              "qualities": "Активный, дружелюбный",
              "history": [],
          },
      ]

    members_data = members.members_data

    # Отрисовка списка
    def render_members():

      sorted_members = sorted(
          members_data,
          key=lambda member: member["points"],
          reverse=True,
      )

      top_members = sorted_members[:3]
      other_members = sorted_members[3:]

      # Открытие профиля
      def open_member(member):

        # ---------------------------------
        # ОТОБРАЖЕНИЕ ДАННЫХ
        # ---------------------------------

        name_view = ft.Text(
            member["name"],
            size=24,
            weight=ft.FontWeight.W_700,
            color="#13233D",
            text_align=ft.TextAlign.CENTER,
        )

        class_view = ft.Text(
            member["class"],
            size=24,
            weight=ft.FontWeight.W_700,
            color="#13233D",
            text_align=ft.TextAlign.CENTER,
        )

        birthday_view = ft.Text(
            member["birthday"],
            size=18,
            color="#13233D",
            text_align=ft.TextAlign.CENTER,
        )

        hobbies_view = ft.Text(
            f"Хобби: {member['hobbies']}",
            size=18,
            color="#13233D",
            text_align=ft.TextAlign.CENTER,
        )

        qualities_view = ft.Text(
            f"Качества: {member['qualities']}",
            size=18,
            color="#13233D",
            text_align=ft.TextAlign.CENTER,
        )

        # ---------------------------------
        # ПОЛЯ РЕДАКТИРОВАНИЯ
        # ---------------------------------

        name_field = ft.TextField(
            value=member["name"],
            width=400,
            text_align=ft.TextAlign.CENTER,
            border=ft.InputBorder.NONE,
            visible=False,
        )

        class_field = ft.TextField(
            value=member["class"],
            width=120,
            text_align=ft.TextAlign.CENTER,
            border=ft.InputBorder.NONE,
            visible=False,
        )

        birthday_field = ft.TextField(
            value=member["birthday"],
            width=300,
            text_align=ft.TextAlign.CENTER,
            border=ft.InputBorder.NONE,
            visible=False,
        )

        hobbies_field = ft.TextField(
            value=member["hobbies"],
            width=400,
            text_align=ft.TextAlign.CENTER,
            border=ft.InputBorder.NONE,
            visible=False,
        )

        qualities_field = ft.TextField(
            value=member["qualities"],
            width=400,
            text_align=ft.TextAlign.CENTER,
            border=ft.InputBorder.NONE,
            visible=False,
        )

        # ---------------------------------
        # БАЛЛЫ
        # ---------------------------------

        score_text = ft.Text(
            f"{member['points']}б",
            size=24,
            weight=ft.FontWeight.W_700,
            color="#13233D",
            text_align=ft.TextAlign.CENTER,
        )

        # ---------------------------------
        # НАЧИСЛЕНИЕ
        # ---------------------------------

        points_field = ft.TextField(
            label="Баллы",
            width=100,
            value="10",
            text_align=ft.TextAlign.CENTER,
        )

        activity_field = ft.TextField(
            label="Активность",
            width=320,
            text_align=ft.TextAlign.CENTER,
        )

        # ---------------------------------
        # ИСТОРИЯ
        # ---------------------------------

        history_column = ft.Column(
            controls=[
                ft.Text(
                    item,
                    size=16,
                    color="#13233D",
                    text_align=ft.TextAlign.CENTER,
                )
                for item in member["history"]
            ],
            spacing=6,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        # ---------------------------------
        # РЕДАКТИРОВАНИЕ
        # ---------------------------------

        editing = False

        def toggle_edit(e):
          nonlocal editing

          if not editing:
            editing = True

            name_view.visible = False
            class_view.visible = False
            birthday_view.visible = False
            hobbies_view.visible = False
            qualities_view.visible = False

            name_field.visible = True
            class_field.visible = True
            birthday_field.visible = True
            hobbies_field.visible = True
            qualities_field.visible = True

            edit_button.icon = ft.Icons.CHECK

          else:
            editing = False

            member["name"] = name_field.value
            member["class"] = class_field.value
            member["birthday"] = birthday_field.value
            member["hobbies"] = hobbies_field.value
            member["qualities"] = qualities_field.value

            name_view.value = member["name"]
            class_view.value = member["class"]
            birthday_view.value = member["birthday"]
            hobbies_view.value = f"Хобби: {member['hobbies']}"
            qualities_view.value = f"Качества: {member['qualities']}"

            name_view.visible = True
            class_view.visible = True
            birthday_view.visible = True
            hobbies_view.visible = True
            qualities_view.visible = True

            name_field.visible = False
            class_field.visible = False
            birthday_field.visible = False
            hobbies_field.visible = False
            qualities_field.visible = False

            edit_button.icon = ft.Icons.EDIT

          page.update()

        # ---------------------------------
        # НАЧИСЛЕНИЕ БАЛЛОВ
        # ---------------------------------

        def add_points(e):

          try:
            points = int(points_field.value)
          except (ValueError, TypeError):
            return

          activity = activity_field.value.strip()

          if points <= 0 or not activity:
            return

          member["points"] += points

          member["history"].append(f"+{points} — {activity}")

          score_text.value = f"{member['points']}б"

          history_column.controls.append(
              ft.Text(
                  f"+{points} — {activity}",
                  size=16,
                  color="#13233D",
                  text_align=ft.TextAlign.CENTER,
              )
          )

          activity_field.value = ""
          points_field.value = "10"

          page.update()

        # ---------------------------------
        # ЗАКРЫТИЕ
        # ---------------------------------

        def close_profile(e):

          if profile_overlay in page.overlay:
            page.overlay.remove(profile_overlay)

          page.update()
          render_members()

        # ---------------------------------
        # КНОПКИ
        # ---------------------------------

        edit_button = ft.IconButton(
            icon=ft.Icons.EDIT,
            tooltip="Редактировать",
            icon_color="#13233D",
            on_click=toggle_edit,
        )

        close_button = ft.IconButton(
            icon=ft.Icons.CLOSE,
            tooltip="Закрыть",
            icon_color="#13233D",
            on_click=close_profile,
        )

        # ---------------------------------
        # ИМЯ + КЛАСС
        # ---------------------------------

        name_class_row = ft.Row(
            controls=[
                name_view,
                class_view,
                name_field,
                class_field,
            ],
            spacing=10,
            tight=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

        # ---------------------------------
        # ХОББИ
        # ---------------------------------

        hobbies_row = ft.Container(
            width=820,
            alignment=ft.Alignment(0, 0),
            content=hobbies_view,
        )

        # ---------------------------------
        # КАЧЕСТВА
        # ---------------------------------

        qualities_row = ft.Container(
            width=820,
            alignment=ft.Alignment(0, 0),
            content=qualities_view,
        )

        # ---------------------------------
        # ПРОФИЛЬ
        # ---------------------------------

        profile_content = ft.Container(
            width=900,
            height=850,
            bgcolor="#FFFFFF",
            border_radius=20,
            padding=30,
            alignment=ft.Alignment(0, 0),
            content=ft.Column(
                controls=[
                    # Верхняя панель
                    ft.Row(
                        controls=[
                            close_button,
                            ft.Container(
                                expand=True,
                            ),
                            edit_button,
                        ],
                        width=820,
                    ),
                    # Фото
                    ft.Container(
                        width=760,
                        height=250,
                        alignment=ft.Alignment(0, 0),
                        content=ft.Image(
                            src=member["photo"],
                            width=700,
                            height=250,
                            fit=ft.BoxFit.CONTAIN,
                        ),
                    ),
                    # Имя + класс
                    name_class_row,
                    # Дата рождения
                    birthday_view,
                    # Поле даты
                    birthday_field,
                    # Баллы
                    ft.Container(
                        width=820,
                        alignment=ft.Alignment(0, 0),
                        content=score_text,
                    ),
                    # Хобби
                    hobbies_row,
                    # Поле хобби
                    hobbies_field,
                    # Качества
                    qualities_row,
                    # Поле качеств
                    qualities_field,
                    # Начисление
                    ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    points_field,
                                    activity_field,
                                ],
                                spacing=20,
                                tight=True,
                                alignment=ft.MainAxisAlignment.CENTER,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            ft.Button(
                                "Начислить",
                                on_click=add_points,
                            ),
                        ],
                        spacing=18,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    # История
                    history_column,
                ],
                spacing=18,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO,
            ),
        )

        # Прозрачный слой
        profile_overlay = ft.Container(
            expand=True,
            alignment=ft.Alignment(0, 0),
            content=profile_content,
        )

        page.overlay.append(profile_overlay)
        page.update()

      # ---------------------------------
      # ТОП-3
      # ---------------------------------

      def top_member_card(member):
        return ft.Container(
            width=300,
            height=360,
            margin=ft.Margin(
                left=-20,
                right=-20,
                top=20,
                bottom=30,
            ),
            padding=0,
            on_click=lambda e, member=member: open_member(member),
            content=ft.Column(
                controls=[
                    ft.Image(
                        src=member["photo"],
                        width=300,
                        height=300,
                        fit=ft.BoxFit.CONTAIN,
                    ),
                    ft.Container(
                        height=60,
                        alignment=ft.Alignment(0, -4),
                        content=ft.Text(
                            str(member["points"]),
                            size=24,
                            weight=ft.FontWeight.W_700,
                            color="#13233D",
                            text_align=ft.TextAlign.CENTER,
                        ),
                    ),
                ],
                spacing=0,
            ),
        )

      # ---------------------------------
      # ОБЫЧНАЯ КАРТОЧКА
      # ---------------------------------

      def member_card(member):
        return ft.Container(
            width=320,
            height=390,
            margin=ft.Margin(
                left=-15,
                right=-15,
                top=-100,
                bottom=0,
            ),
            padding=0,
            on_click=lambda e, member=member: open_member(member),
            content=ft.Image(
                src=member["photo"],
                width=320,
                height=390,
                fit=ft.BoxFit.CONTAIN,
            ),
        )

      # Карточки
      top_cards = [top_member_card(member) for member in top_members]

      cards = [member_card(member) for member in other_members]

      # Ряды по 4
      member_rows = []

      for i in range(0, len(cards), 4):
        member_rows.append(
            ft.Row(
                controls=cards[i : i + 4],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=0,
            )
        )

      # Страница участников
      content.content = ft.Column(
          controls=[
              ft.Row(
                  controls=top_cards,
                  alignment=ft.MainAxisAlignment.CENTER,
                  spacing=0,
              ),
              *member_rows,
          ],
          expand=True,
          scroll=ft.ScrollMode.AUTO,
          horizontal_alignment=ft.CrossAxisAlignment.CENTER,
          spacing=0,
      )

      page.update()

    render_members()

  # ==========================================
  # 3. СТРАНИЦА ПОСЕЩАЕМОСТИ
  # ==========================================
  def attendance(e):
    nonlocal active_page
    active_page = "attendance"

    participants = [
        {"name": "Иванов Иван Иванович", "class": "11-А"},
        {"name": "Петрова Анна Сергеевна", "class": "11-Б"},
        {"name": "Волков Кирилл", "class": "11-В"},
        {"name": "Смирнов Артём Дмитриевич", "class": "10-А"},
        {"name": "Попова Софья Андреевна", "class": "10-А"},
        {"name": "Сидоров Максим Андреевич", "class": "10-Б"},
        {"name": "Васильева Елизавета", "class": "10-В"},
        {"name": "Кузнецова Мария", "class": "9-А"},
        {"name": "Морозов Даниил", "class": "9-Б"},
        {"name": "Фёдорова Алиса", "class": "9-А"},
        {"name": "Участник 8-А", "class": "8-А"},
        {"name": "Участник 8-Б", "class": "8-Б"},
        {"name": "Участник 7-А", "class": "7-А"},
        {"name": "Участник 7-Б", "class": "7-Б"},
        {"name": "Участник 6-А", "class": "6-А"},
        {"name": "Участник 6-Б", "class": "6-Б"},
        {"name": "Участник 5-А", "class": "5-А"},
        {"name": "Участник 5-Б", "class": "5-Б"},
    ]

    # Сортировка списка по параллелям классов (от 5 до 11)
    participants = sorted(
        participants,
        key=lambda person: (
            int(person["class"].split("-")[0]),
            person["class"],
            person["name"],
        ),
    )

    meetings = {
        "13.09.2026": {
            "description": (
                "Подготовка к мероприятию, распределение обязанностей и планы"
                " на месяц."
            )
        },
        "20.09.2026": {
            "description": (
                "Обсуждение предстоящего мероприятия и распределение задач"
                " между участниками."
            )
        },
        "27.09.2026": {
            "description": (
                "Подведение итогов месяца и обсуждение новых предложений."
            )
        },
    }

    attendance_data = {}
    for date in meetings:
      attendance_data[date] = {}
      for person in participants:
        attendance_data[date][person["name"]] = ""

    def open_meeting(date):
      dialog = ft.AlertDialog(
          modal=True,
          title=ft.Text(f"Заседание {date}"),
          content=ft.Column(
              controls=[
                  ft.Text("Дата:", weight=ft.FontWeight.BOLD),
                  ft.Text(date),
                  ft.Divider(),
                  ft.Text("Что обсуждали:", weight=ft.FontWeight.BOLD),
                  ft.Text(meetings[date]["description"]),
              ],
              tight=True,
          ),
          actions=[
              ft.TextButton(
                  "Изменить информацию", on_click=lambda e: edit_meeting(date)
              ),
              ft.TextButton(
                  "Удалить заседание",
                  on_click=lambda e: confirm_delete_meeting(date),
              ),
              ft.TextButton("Закрыть", on_click=lambda e: page.pop_dialog()),
          ],
      )
      page.show_dialog(dialog)

    def edit_meeting(date):
      page.pop_dialog()
      description_field = ft.TextField(
          label="Что обсуждали?",
          value=meetings[date]["description"],
          multiline=True,
          min_lines=4,
          max_lines=8,
      )

      def save_changes(e):
        meetings[date]["description"] = (
            description_field.value or "Информация отсутствует."
        )
        page.pop_dialog()
        render_page()

      dialog = ft.AlertDialog(
          modal=True,
          title=ft.Text(f"Изменить заседание {date}"),
          content=description_field,
          actions=[
              ft.TextButton("Отмена", on_click=lambda e: page.pop_dialog()),
              ft.TextButton("Сохранить", on_click=save_changes),
          ],
      )
      page.show_dialog(dialog)

    def confirm_delete_meeting(date):
      page.pop_dialog()
      dialog = ft.AlertDialog(
          modal=True,
          title=ft.Text("Удалить заседание?"),
          content=ft.Text(
              f"Удалить заседание {date}?\n\nБудет удалена дата, описание и вся"
              " посещаемость за это заседание."
          ),
          actions=[
              ft.TextButton("Отмена", on_click=lambda e: page.pop_dialog()),
              ft.TextButton(
                  "Удалить", on_click=lambda e: delete_meeting(date)
              ),
          ],
      )
      page.show_dialog(dialog)

    def delete_meeting(date):
      if date in meetings:
        del meetings[date]
      if date in attendance_data:
        del attendance_data[date]
      page.pop_dialog()
      render_page()

    # Циклическое изменение статуса посещения ("", "+", "-", "x")
    def change_status(person, date):
      current_status = attendance_data[date][person]
      if current_status == "":
        new_status = "+"
      elif current_status == "+":
        new_status = "-"
      elif current_status == "-":
        new_status = "x"
      else:
        new_status = "+"

      attendance_data[date][person] = new_status
      render_page()

    def attendance_button(person, date):
      current_status = attendance_data[date][person]
      if current_status == "+":
        bgcolor, color = ft.Colors.GREEN, ft.Colors.WHITE
      elif current_status == "-":
        bgcolor, color = ft.Colors.RED, ft.Colors.WHITE
      elif current_status == "x":
        bgcolor, color = ft.Colors.ORANGE, ft.Colors.WHITE
      else:
        bgcolor, color = None, ft.Colors.BLACK

      return ft.TextButton(
          current_status or "—",
          width=50,
          height=40,
          style=ft.ButtonStyle(
              color=color,
              bgcolor=bgcolor,
              padding=0,
              alignment=ft.Alignment.CENTER,
          ),
          on_click=lambda e: change_status(person, date),
      )

    def add_meeting():
      selected_date = {"value": None}
      description_field = ft.TextField(
          label="Что обсуждали?", multiline=True, min_lines=3, max_lines=6
      )

      def on_date_selected(e):
        selected_date["value"] = e.control.value

      date_picker = ft.DatePicker(on_change=on_date_selected)

      def save_meeting(e):
        chosen_date = selected_date["value"]
        if chosen_date is None:
          return

        chosen_date = chosen_date + timedelta(hours=12)
        date_text = chosen_date.strftime("%d.%m.%Y")

        if date_text in meetings:
          return

        meetings[date_text] = {
            "description": (
                description_field.value or "Информация отсутствует."
            )
        }
        attendance_data[date_text] = {}
        for person in participants:
          attendance_data[date_text][person["name"]] = ""

        page.pop_dialog()
        render_page()

      dialog = ft.AlertDialog(
          modal=True,
          title=ft.Text("Добавить заседание"),
          content=ft.Column(
              controls=[
                  ft.Button(
                      "Выбрать дату",
                      icon=ft.Icons.CALENDAR_MONTH,
                      on_click=lambda e: page.show_dialog(date_picker),
                  ),
                  description_field,
              ],
              tight=True,
          ),
          actions=[
              ft.TextButton("Отмена", on_click=lambda e: page.pop_dialog()),
              ft.TextButton("Добавить", on_click=save_meeting),
          ],
      )
      page.show_dialog(dialog)

    # Отрисовка интерактивной таблицы посещаемости с фиксированной левой частью
    def render_page():
      participant_column_width = 250
      class_column_width = 80
      date_column_width = 130
      row_height = 55

      left_width = participant_column_width + class_column_width
      right_width = len(meetings) * date_column_width
      table_height = (len(participants) + 1) * row_height
      border = ft.Border.all(1, ft.Colors.OUTLINE)

      # Левая колонка (ФИО и класс)
      left_rows = [
          ft.Row(
              controls=[
                  ft.Container(
                      width=participant_column_width,
                      height=row_height,
                      alignment=ft.Alignment.CENTER,
                      border=border,
                      content=ft.Text("Участник", weight=ft.FontWeight.BOLD),
                  ),
                  ft.Container(
                      width=class_column_width,
                      height=row_height,
                      alignment=ft.Alignment.CENTER,
                      border=border,
                      content=ft.Text("Класс", weight=ft.FontWeight.BOLD),
                  ),
              ],
              spacing=0,
          )
      ]
      for person in participants:
        left_rows.append(
            ft.Row(
                controls=[
                    ft.Container(
                        width=participant_column_width,
                        height=row_height,
                        alignment=ft.Alignment.CENTER,
                        border=border,
                        content=ft.Text(
                            person["name"],
                            size=15,
                            text_align=ft.TextAlign.CENTER,
                        ),
                    ),
                    ft.Container(
                        width=class_column_width,
                        height=row_height,
                        alignment=ft.Alignment.CENTER,
                        border=border,
                        content=ft.Text(
                            person["class"],
                            size=15,
                            text_align=ft.TextAlign.CENTER,
                        ),
                    ),
                ],
                spacing=0,
            )
        )
      left_column = ft.Column(controls=left_rows, spacing=0, tight=True)

      # Правая колонка (даты и сетка статусов посещаемости)
      right_rows = []
      date_header = []
      for date in meetings:
        date_header.append(
            ft.Container(
                width=date_column_width,
                height=row_height,
                alignment=ft.Alignment.CENTER,
                border=border,
                content=ft.TextButton(
                    content=date,
                    width=date_column_width,
                    height=row_height,
                    style=ft.ButtonStyle(
                        padding=0, alignment=ft.Alignment.CENTER
                    ),
                    on_click=lambda e, d=date: open_meeting(d),
                ),
            )
        )
      right_rows.append(ft.Row(controls=date_header, spacing=0, tight=True))

      for person in participants:
        row_cells = []
        for date in meetings:
          row_cells.append(
              ft.Container(
                  width=date_column_width,
                  height=row_height,
                  alignment=ft.Alignment.CENTER,
                  border=border,
                  content=attendance_button(person["name"], date),
              )
          )
        right_rows.append(ft.Row(controls=row_cells, spacing=0, tight=True))

      right_column = ft.Column(controls=right_rows, spacing=0, tight=True)

      # Логика горизонтального скролла таблицы с помощью правой кнопки мыши (GestureDetector)
      drag_state = {"last_x": None}

      def right_pan_start(e):
        if e.global_position is not None:
          drag_state["last_x"] = e.global_position.x

      def right_pan_update(e):
        if e.global_position is None:
          return
        current_x = e.global_position.x
        last_x = drag_state["last_x"]
        if last_x is None:
          drag_state["last_x"] = current_x
          return
        delta_x = current_x - last_x
        drag_state["last_x"] = current_x
        current_left = right_drag.left or 0
        new_left = current_left + delta_x
        viewport_width = page.width - left_width
        if viewport_width < 0:
          viewport_width = 0
        min_left = min(0, viewport_width - right_width - 110)
        if new_left > 0:
          new_left = 0
        if new_left < min_left:
          new_left = min_left
        right_drag.left = new_left
        right_drag.update()

      def right_pan_end(e):
        drag_state["last_x"] = None

      right_drag = ft.GestureDetector(
          width=right_width,
          height=table_height,
          left=0,
          top=0,
          mouse_cursor=ft.MouseCursor.MOVE,
          drag_interval=10,
          on_right_pan_start=right_pan_start,
          on_right_pan_update=right_pan_update,
          on_right_pan_end=right_pan_end,
          content=right_column,
      )

      right_viewport = ft.Stack(
          expand=True,
          height=table_height,
          clip_behavior=ft.ClipBehavior.HARD_EDGE,
          controls=[right_drag],
      )

      table = ft.Row(
          controls=[
              ft.Container(width=left_width, content=left_column),
              ft.Container(
                  expand=True, height=table_height, content=right_viewport
              ),
          ],
          spacing=0,
          vertical_alignment=ft.CrossAxisAlignment.START,
      )

      content.content = ft.Column(
          controls=[
              ft.Row(
                  controls=[
                      ft.Text(
                          "Посещаемость", size=30, weight=ft.FontWeight.BOLD
                      ),
                      ft.Container(expand=True),
                      ft.Button(
                          "Добавить заседание",
                          icon=ft.Icons.ADD,
                          on_click=lambda e: add_meeting(),
                      ),
                  ]
              ),
              ft.Divider(),
              ft.Container(expand=True, content=table),
          ],
          expand=True,
          scroll=ft.ScrollMode.AUTO,
      )
      page.update()

    render_page()

  # ==========================================
  # 4. СТРАНИЦА КАЛЕНДАРЯ
  # ==========================================
  def calendar(e):
    nonlocal active_page
    active_page = "calendar"

    calendar_date = datetime.now()

    def build_calendar():
      nonlocal calendar_date
      year = calendar_date.year
      month = calendar_date.month

      month_days = cal.monthcalendar(year, month)
      month_name = calendar_date.strftime("%B %Y")

      week_days = ft.Row(
          controls=[
              ft.Text("Пн", expand=True, text_align=ft.TextAlign.CENTER),
              ft.Text("Вт", expand=True, text_align=ft.TextAlign.CENTER),
              ft.Text("Ср", expand=True, text_align=ft.TextAlign.CENTER),
              ft.Text("Чт", expand=True, text_align=ft.TextAlign.CENTER),
              ft.Text("Пт", expand=True, text_align=ft.TextAlign.CENTER),
              ft.Text("Сб", expand=True, text_align=ft.TextAlign.CENTER),
              ft.Text("Вс", expand=True, text_align=ft.TextAlign.CENTER),
          ],
          spacing=0,
      )

      def previous_month(e):
        nonlocal calendar_date
        if calendar_date.month == 1:
          calendar_date = calendar_date.replace(
              year=calendar_date.year - 1, month=12
          )
        else:
          calendar_date = calendar_date.replace(month=calendar_date.month - 1)
        build_calendar()

      def next_month(e):
        nonlocal calendar_date
        if calendar_date.month == 12:
          calendar_date = calendar_date.replace(
              year=calendar_date.year + 1, month=1
          )
        else:
          calendar_date = calendar_date.replace(month=calendar_date.month + 1)
        build_calendar()

      def create_event(e):
        selected_event_date = None
        event_field = ft.TextField(label="Название мероприятия")
        date_text = ft.Text("Дата не выбрана")
        photo_container = ft.Container()

        def date_changed(e):
          nonlocal selected_event_date
          selected_event_date = e.control.value
          if selected_event_date:
            selected_event_date = selected_event_date + timedelta(days=1)
            date_text.value = selected_event_date.strftime("%d.%m.%Y")
            page.update()

        date_picker = ft.DatePicker(
            entry_mode=ft.DatePickerEntryMode.CALENDAR_ONLY,
            value=calendar_date,
            current_date=calendar_date,
            on_change=date_changed,
        )

        def open_date_picker(e):
          page.show_dialog(date_picker)

        file_picker = ft.FilePicker()

        async def pick_photo(e):
          files = await file_picker.pick_files(
              allow_multiple=False, allowed_extensions=["jpg", "jpeg", "png"]
          )
          if files:
            photo_container.content = ft.Image(
                src=files[0].path, width=300, height=200
            )
            page.update()

        def save_new_event(e):
          nonlocal calendar_date
          if selected_event_date is None:
            return

          selected_date_str = selected_event_date.strftime("%d.%m.%Y")
          calendar_data[selected_date_str] = {
              "event": event_field.value,
              "photo": (
                  photo_container.content.src
                  if photo_container.content
                  else None
              ),
          }
          calendar_date = selected_event_date
          dialog.open = False
          page.update()
          build_calendar()

        dialog = ft.AlertDialog(
            title=ft.Text("Новое мероприятие"),
            content=ft.Column(
                controls=[
                    ft.TextButton(
                        content=ft.Text("Выбрать дату"),
                        on_click=open_date_picker,
                    ),
                    date_text,
                    event_field,
                    ft.Text("Фото"),
                    ft.TextButton(
                        content=ft.Text("Добавить фото"), on_click=pick_photo
                    ),
                    photo_container,
                    ft.TextButton(
                        content=ft.Text("Создать"), on_click=save_new_event
                    ),
                ],
                spacing=10,
                tight=True,
            ),
        )
        page.overlay.append(dialog)
        dialog.open = True
        page.update()

      def open_date(day):
        selected_date_str = (
            f"{day:02d}.{calendar_date.month:02d}.{calendar_date.year}"
        )
        saved_data = calendar_data.get(selected_date_str)

        if saved_data is None:

          def close_empty_dialog(e):
            dialog.open = False
            page.update()

          dialog = ft.AlertDialog(
              title=ft.Text(f"Дата: {selected_date_str}"),
              content=ft.Text("На эту дату мероприятий нет."),
              actions=[ft.TextButton("Закрыть", on_click=close_empty_dialog)],
          )
        else:
          controls = []
          if saved_data.get("event"):
            controls.append(
                ft.Text(
                    saved_data["event"],
                    size=20,
                    text_align=ft.TextAlign.CENTER,
                )
            )
          if saved_data.get("photo"):
            controls.append(
                ft.Image(src=saved_data["photo"], width=300, height=200)
            )

          def delete_event(e):
            def confirm_delete(e):
              del calendar_data[selected_date_str]
              confirm_dialog.open = False
              dialog.open = False
              page.update()
              build_calendar()

            confirm_dialog = ft.AlertDialog(
                title=ft.Text("Удалить мероприятие?"),
                content=ft.Text("Это действие нельзя отменить."),
                actions=[
                    ft.TextButton(
                        content=ft.Text("Отмена"),
                        on_click=lambda e: (
                            setattr(confirm_dialog, "open", False),
                            page.update(),
                        ),
                    ),
                    ft.TextButton(
                        content=ft.Text("Удалить"), on_click=confirm_delete
                    ),
                ],
            )
            page.overlay.append(confirm_dialog)
            confirm_dialog.open = True
            page.update()

          dialog = ft.AlertDialog(
              title=ft.Text(f"Дата: {selected_date_str}"),
              content=ft.Column(
                  controls=controls,
                  spacing=10,
                  tight=True,
                  horizontal_alignment=ft.CrossAxisAlignment.CENTER,
              ),
              actions=[
                  ft.TextButton(
                      content=ft.Text("Закрыть"),
                      on_click=lambda e: (
                          setattr(dialog, "open", False),
                          page.update(),
                      ),
                  ),
                  ft.TextButton(
                      content=ft.Text("Удалить"), on_click=delete_event
                  ),
              ],
          )

        page.show_dialog(dialog)

      calendar_rows = []
      for week in month_days:
        row = ft.Row(controls=[], expand=True, spacing=0)
        for day in week:
          if day == 0:
            cell = ft.Container(
                expand=True, border=ft.Border.all(1, "#E5E7EB")
            )
          else:
            selected_date_str = (
                f"{day:02d}.{calendar_date.month:02d}.{calendar_date.year}"
            )
            saved_data = calendar_data.get(selected_date_str)
            cell_controls = [
                ft.Container(
                    content=ft.Text(
                        str(day), size=16, text_align=ft.TextAlign.CENTER
                    ),
                    width=130,
                    height=22,
                )
            ]
            if saved_data is not None:
              if saved_data.get("event"):
                cell_controls.append(
                    ft.Container(
                        content=ft.Text(
                            saved_data["event"],
                            size=13,
                            text_align=ft.TextAlign.CENTER,
                            max_lines=1,
                            overflow=ft.TextOverflow.ELLIPSIS,
                        ),
                        width=130,
                        height=20,
                    )
                )
              if saved_data.get("photo"):
                cell_controls.append(
                    ft.Container(
                        content=ft.Image(
                            src=saved_data["photo"], width=80, height=50
                        ),
                        width=80,
                        height=50,
                    )
                )

            cell = ft.Container(
                content=ft.Column(
                    controls=cell_controls,
                    spacing=2,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                expand=True,
                padding=ft.Padding.only(top=5, left=5, right=5),
                border=ft.Border.all(1, "#E5E7EB"),
                on_click=lambda e, d=day: open_date(d),
            )
          row.controls.append(cell)
        calendar_rows.append(row)

      content.content = ft.Column(
          expand=True,
          spacing=0,
          controls=[
              ft.Row(
                  controls=[
                      ft.Container(expand=True),
                      ft.IconButton(icon=ft.Icons.ADD, on_click=create_event),
                  ]
              ),
              ft.Row(
                  controls=[
                      ft.IconButton(
                          icon=ft.Icons.CHEVRON_LEFT, on_click=previous_month
                      ),
                      ft.Text(month_name, size=25),
                      ft.IconButton(
                          icon=ft.Icons.CHEVRON_RIGHT, on_click=next_month
                      ),
                  ],
                  alignment=ft.MainAxisAlignment.CENTER,
              ),
              week_days,
              *calendar_rows,
          ],
      )
      page.update()

    build_calendar()

  # ==========================================
  # 5. СТРАНИЦА МЕРОПРИЯТИЙ
  # ==========================================
  def events(e):
    nonlocal active_page
    active_page = "events"

    def open_event(event):
      controls = []
      if event.get("photo"):
        controls.append(
            ft.Image(
                src=event["photo"],
                width=400,
                height=220,
                fit=ft.BoxFit.COVER,
            )
        )
      controls.append(ft.Text(f"Дата: {event['date']}"))
      controls.append(ft.Text(f"Направление: {event['direction']}"))
      controls.append(ft.Divider())
      controls.append(ft.Text(event["description"]))

      dialog = ft.AlertDialog(
          modal=True,
          title=ft.Text(
              event["title"], size=22, weight=ft.FontWeight.BOLD
          ),
          content=ft.Column(
              controls=controls, tight=True, scroll=ft.ScrollMode.AUTO
          ),
          actions=[
              ft.TextButton(
                  "Изменить", on_click=lambda e: edit_event(event)
              ),
              ft.TextButton(
                  "Удалить", on_click=lambda e: confirm_delete_event(event)
              ),
              ft.TextButton("Закрыть", on_click=lambda e: page.pop_dialog()),
          ],
      )
      page.show_dialog(dialog)

    def edit_event(event):
      page.pop_dialog()
      selected_date = {
          "value": datetime.strptime(event["date"], "%d.%m.%Y")
      }
      selected_photo = {"value": event.get("photo")}

      title_field = ft.TextField(
          label="Название мероприятия", value=event["title"]
      )
      direction_field = ft.TextField(
          label="Направление", value=event["direction"]
      )
      description_field = ft.TextField(
          label="Описание",
          value=event["description"],
          multiline=True,
          min_lines=3,
          max_lines=6,
      )
      date_text = ft.Text(selected_date["value"].strftime("%d.%m.%Y"))

      def on_date_selected(e):
        selected_date["value"] = e.control.value
        if selected_date["value"]:
          selected_date["value"] = selected_date["value"] + timedelta(
              hours=12
          )
          date_text.value = selected_date["value"].strftime("%d.%m.%Y")
          page.update()

      date_picker = ft.DatePicker(
          value=selected_date["value"],
          current_date=selected_date["value"],
          on_change=on_date_selected,
      )
      photo_container = ft.Container()

      if selected_photo["value"]:
        photo_container.content = ft.Image(
            src=selected_photo["value"],
            width=300,
            height=180,
            fit=ft.BoxFit.COVER,
        )

      file_picker = ft.FilePicker()

      async def pick_photo(e):
        files = await file_picker.pick_files(
            allow_multiple=False, allowed_extensions=["jpg", "jpeg", "png"]
        )
        if files:
          selected_photo["value"] = files[0].path
          photo_container.content = ft.Image(
              src=files[0].path, width=300, height=180, fit=ft.BoxFit.COVER
          )
          page.update()

      def save_changes(e):
        event["title"] = title_field.value or "Без названия"
        event["date"] = selected_date["value"].strftime("%d.%m.%Y")
        event["direction"] = direction_field.value or "Без направления"
        event["description"] = (
            description_field.value or "Описание отсутствует."
        )
        event["photo"] = selected_photo["value"]
        page.pop_dialog()
        render_events()

      dialog = ft.AlertDialog(
          modal=True,
          title=ft.Text("Изменить мероприятие"),
          content=ft.Column(
              controls=[
                  title_field,
                  direction_field,
                  description_field,
                  ft.Row(
                      controls=[
                          ft.Button(
                              "Выбрать дату",
                              icon=ft.Icons.CALENDAR_MONTH,
                              on_click=lambda e: page.show_dialog(
                                  date_picker
                              ),
                          ),
                          date_text,
                      ],
                      spacing=10,
                  ),
                  ft.Button(
                      "Изменить фото", icon=ft.Icons.IMAGE, on_click=pick_photo
                  ),
                  photo_container,
              ],
              tight=True,
              scroll=ft.ScrollMode.AUTO,
          ),
          actions=[
              ft.TextButton("Отмена", on_click=lambda e: page.pop_dialog()),
              ft.TextButton("Сохранить", on_click=save_changes),
          ],
      )
      page.show_dialog(dialog)

    def confirm_delete_event(event):
      def delete_event(e):
        events_data.remove(event)
        page.pop_dialog()
        render_events()

      dialog = ft.AlertDialog(
          modal=True,
          title=ft.Text("Удалить мероприятие?"),
          content=ft.Text(f"Удалить «{event['title']}»?"),
          actions=[
              ft.TextButton("Отмена", on_click=lambda e: page.pop_dialog()),
              ft.TextButton("Удалить", on_click=delete_event),
          ],
      )
      page.show_dialog(dialog)

    def add_event(e):
      selected_date = {"value": None}
      selected_photo = {"value": None}

      title_field = ft.TextField(label="Название мероприятия")
      direction_field = ft.TextField(label="Направление")
      description_field = ft.TextField(
          label="Описание", multiline=True, min_lines=3, max_lines=6
      )
      date_text = ft.Text("Дата не выбрана")

      def on_date_selected(e):
        selected_date["value"] = e.control.value
        if selected_date["value"]:
          selected_date["value"] = selected_date["value"] + timedelta(
              hours=12
          )
          date_text.value = selected_date["value"].strftime("%d.%m.%Y")
          page.update()

      date_picker = ft.DatePicker(on_change=on_date_selected)
      photo_container = ft.Container()
      file_picker = ft.FilePicker()

      async def pick_photo(e):
        files = await file_picker.pick_files(
            allow_multiple=False, allowed_extensions=["jpg", "jpeg", "png"]
        )
        if files:
          selected_photo["value"] = files[0].path
          photo_container.content = ft.Image(
              src=files[0].path, width=300, height=180, fit=ft.BoxFit.COVER
          )
          page.update()

      def save_new_event(e):
        if selected_date["value"] is None:
          return

        new_event = {
            "title": title_field.value or "Без названия",
            "date": selected_date["value"].strftime("%d.%m.%Y"),
            "direction": direction_field.value or "Без направления",
            "description": description_field.value or "Описание отсутствует.",
            "photo": selected_photo["value"],
        }
        events_data.append(new_event)
        page.pop_dialog()
        render_events()

      dialog = ft.AlertDialog(
          modal=True,
          title=ft.Text("Новое мероприятие"),
          content=ft.Column(
              controls=[
                  title_field,
                  direction_field,
                  description_field,
                  ft.Row(
                      controls=[
                          ft.Button(
                              "Выбрать дату",
                              icon=ft.Icons.CALENDAR_MONTH,
                              on_click=lambda e: page.show_dialog(
                                  date_picker
                              ),
                          ),
                          date_text,
                      ],
                      spacing=10,
                  ),
                  ft.Button(
                      "Добавить фото", icon=ft.Icons.IMAGE, on_click=pick_photo
                  ),
                  photo_container,
              ],
              tight=True,
              scroll=ft.ScrollMode.AUTO,
          ),
          actions=[
              ft.TextButton("Отмена", on_click=lambda e: page.pop_dialog()),
              ft.TextButton("Создать", on_click=save_new_event),
          ],
      )
      page.show_dialog(dialog)

    def render_events():
      events_grid = ft.GridView(
          expand=True,
          max_extent=320,
          spacing=20,
          run_spacing=20,
          padding=10,
      )

      for event in events_data:
        if event.get("photo"):
          image = ft.Image(
              src=event["photo"], width=300, height=170, fit=ft.BoxFit.COVER
          )
        else:
          image = ft.Container(
              width=300,
              height=170,
              alignment=ft.Alignment.CENTER,
              content=ft.Icon(ft.Icons.EVENT, size=60),
          )

        card = ft.Container(
            width=300,
            border=ft.Border.all(1, "#E5E7EB"),
            border_radius=12,
            on_click=lambda e, item=event: open_event(item),
            content=ft.Column(
                controls=[
                    image,
                    ft.Container(
                        padding=15,
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    event["title"],
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Text(event["date"], size=14),
                                ft.Text(event["direction"], size=14),
                                ft.Text(
                                    event["description"],
                                    size=13,
                                    max_lines=2,
                                    overflow=ft.TextOverflow.ELLIPSIS,
                                ),
                            ],
                            spacing=7,
                        ),
                    ),
                ],
                spacing=0,
            ),
        )
        events_grid.controls.append(card)

      content.content = ft.Column(
          controls=[
              ft.Row(
                  controls=[
                      ft.Text(
                          "Мероприятия", size=30, weight=ft.FontWeight.BOLD
                      ),
                      ft.Container(expand=True),
                      ft.IconButton(
                          icon=ft.Icons.ADD,
                          on_click=add_event,
                          tooltip="Добавить мероприятие",
                      ),
                  ],
              ),
              ft.Divider(),
              events_grid,
          ],
          expand=True,
      )
      page.update()

    render_events()

  # Фоновая задача для автоматического обновления часов каждую секунду
  async def update_clock():
    while True:
      try:
        clock.value = datetime.now().strftime("%H:%M")
        page.update()
      except RuntimeError:
        break
      await asyncio.sleep(1)

  # Инициализация боковой навигационной панели и главного каркаса приложения
  page.add(
      ft.Row(
          controls=[
              ft.Container(
                  width=200,
                  bgcolor="#F8F8F8",
                  padding=ft.Padding(
                      left=40,
                      right=0,
                      top=0,
                      bottom=0,
                  ),
                  content=ft.Column(
                      controls=[
                          ft.IconButton(
                              icon=ft.Image(
                                  src="assets/icons/home.svg",
                                  width=150,
                                  height=150,
                              ),
                              width=150,
                              height=150,
                              on_click=home,
                          ),
                          ft.IconButton(
                              icon=ft.Image(
                                  src="assets/icons/members.svg",
                                  width=150,
                                  height=150,
                              ),
                              width=150,
                              height=150,
                              on_click=members,
                          ),
                          ft.IconButton(
                              icon=ft.Image(
                                  src="assets/icons/attendance.svg",
                                  width=150,
                                  height=150,
                              ),
                              width=150,
                              height=150,
                              on_click=attendance,
                          ),
                          ft.IconButton(
                              icon=ft.Image(
                                  src="assets/icons/calendar.svg",
                                  width=150,
                                  height=150,
                              ),
                              width=150,
                              height=150,
                              on_click=calendar,
                          ),
                          ft.IconButton(
                              icon=ft.Image(
                                  src="assets/icons/events.svg",
                                  width=150,
                                  height=150,
                              ),
                              width=150,
                              height=150,
                              on_click=events,
                          ),
                      ],
                      alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                      horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                  ),
              ),
              content,
          ],
          expand=True,
      )
  )

  # Запуск приложения с открытия главной страницы и старта часов
  home(None)
  page.run_task(update_clock)


ft.run(main)