from app.database import News, Role, InterestingTheme
from app.database.base import SessionLocal

import pandas as pd
import numpy as np


stakeholder_keywords = [
    "развитие",
    "эффективность",
    "эффективный",
    "рост",
    "спрос",
    "прибыль",
    "клиент",
    "потребитель",
    "настроение",
    "будущий",
    "будущее",
    "перспектива",
    "перспективный",
    "актив",
    "устойчивый",
    "снижение",
    "повышение",
    "мера",
    "поддержка",
]

bookkeeper_keywords = [
    "закон",
    "акт",
    "нормативный",
    "законопроект",
    "законодательство",
    "правило",
    "изменение",
    "требование",
    "норматив",
    "норма",
    "статья",
    "договор",
    "ставка",
    "принят",
    "принять",
    "рассмотрен",
    "закрепить",
    "изменить",
    "изменение",
    "изменён",
    "изменен",
    "госдума",
    "дума",
    "регулятор",
]


def restore_list(text):
    """
    Преобразование полей 'text_prepared' 'text_prepared2' 'title_prepared' 'title_prepared2'
    обратно в списки после сохранения в csv и загрузки
    """
    return eval(text)


def create_roles_and_themes():
    with SessionLocal() as session:
        stakeholder_role = Role(name="Владелец бизнеса", code=1)
        bookkeeper_role = Role(name="Бухгалтер", code=2)
        session.add_all((stakeholder_role, bookkeeper_role))
        session.commit()
        session.refresh(stakeholder_role)
        session.refresh(bookkeeper_role)
        session.add_all(InterestingTheme(name=name) for name in set(stakeholder_keywords + bookkeeper_keywords))
        session.commit()
        keywords = {keyword.name: keyword for keyword in session.query(InterestingTheme).all()}
        stakeholder_role.interesting_themes = [keywords[keyword] for keyword in set(stakeholder_keywords)]
        bookkeeper_role.interesting_themes = [keywords[keyword] for keyword in set(bookkeeper_keywords)]
        session.add(stakeholder_role)
        session.add(bookkeeper_role)
        session.commit()


def create_news(filename):
    df = pd.read_csv(filename, index_col=0)
    df["text_prepared"] = df["text_prepared2"].apply(restore_list)
    df["title_prepared"] = df["title_prepared2"].apply(restore_list)
    df["date"] = pd.to_datetime(df["date"]).dt.date
    df = df[["url", "title", "text", "date", "url_preview", "text_prepared", "title_prepared"]]
    print("Df prepared, filling database...")
    with SessionLocal() as session:
        for chunk in np.array_split(df, 10):
            session.add_all([News(**row) for _, row in chunk.iterrows()])
            session.commit()
            print("Created chunk")
    


def fill_database(filename):
    create_roles_and_themes()
    create_news(filename)