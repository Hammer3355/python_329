# Создаем таблицу MarvelCharacters в базе данных marvel

# CREATE TABLE MarvelCharacters(
#     page_id INTEGER,
#     name TEXT,
#     urlslug TEXT,
#     identify TEXT,
#     ALIGN TEXT,
#     EYE TEXT,
#     HAIR TEXT,
#     SEX TEXT,
#     GSM TEXT,
#     ALIVE TEXT,
#     APPEARANCES INTEGER,
#     FIRST_APPEARANCES TEXT,
#     Year
# )

# Создаем новую таблицу MarvelCharacters_new с дополнительным полем уникального id записи
# "id INTEGER PRIMARY KEY AUTOINCREMENT".

# CREATE TABLE MarvelCharacters_new (
#     id INTEGER PRIMARY KEY AUTOINCREMENT
#     page_id           INTEGER,
#     name              TEXT,
#     urlslug           TEXT,
#     identify          TEXT,
#     ALIGN             TEXT,
#     EYE               TEXT,
#     HAIR              TEXT,
#     SEX               TEXT,
#     GSM               TEXT,
#     ALIVE             TEXT,
#     APPEARANCES       INTEGER,
#     FIRST_APPEARANCES TEXT,
#     Year
# );
#
# Перенос данных из MarvelCharacters в MarvelCharacters_new
# INSERT INTO MarvelCharacters_new(
#      page_id,
#      name,
#      urlslug,
#      identify,
#      ALIGN,
#      EYE,
#      HAIR,
#      SEX,
#      GSM,
#      ALIVE,
#      APPEARANCES,
#      FIRST_APPEARANCE,
#      Year
# )
# SELECT
#     page_id,
#     name,
#     urlslug,
#     identify,
#     ALIGN,
#     EYE,
#     HAIR,
#     SEX,
#     GSM,
#     ALIVE,
#     APPEARANCES,
#     FIRST_APPEARANCE,
#     Year
# FROM MarvelCharacters;

# Удаление таблицы MarvelCharacters
# DROP TABLE MarvelCharacters;

# Переименование таблицы MarvelCharacters_new в MarvelCharacters
# ALTER TABLE MarvelCharacters_new
# RENAME TO MarvelCharacters;

# Создание таблиц для уникальных значений
# CREATE TABLE Sex (
#   sex_id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT UNIQUE
# );
#
# CREATE TABLE EyeColor (
#   eye_id INTEGER PRIMARY KEY AUTOINCREMENT,
#   color TEXT UNIQUE
# );
#
# CREATE TABLE HairColor (
#   hair_id INTEGER PRIMARY KEY AUTOINCREMENT,
#   color TEXT UNIQUE
# );
#
# CREATE TABLE Alignment (
#   align_id INTEGER PRIMARY KEY AUTOINCREMENT,
#   name TEXT UNIQUE
# );
#
# CREATE TABLE LivingStatus (
#   status_id INTEGER PRIMARY KEY AUTOINCREMENT,
#   status TEXT UNIQUE
# );
#
# CREATE TABLE Identity (
#   identity_id INTEGER PRIMARY KEY AUTOINCREMENT,
#   identity TEXT UNIQUE
# );
#
# Запрос на заполнение таблиц уникальными значениями из таблицы MarvelCharacters:
# INSERT INTO Sex (name)
# SELECT DISTINCT SEX FROM MarvelCharacters;
#
# INSERT INTO EyeColor (color)
# SELECT DISTINCT EYE FROM MarvelCharacters;
#
# INSERT INTO HairColor (color)
# SELECT DISTINCT HAIR FROM MarvelCharacters;
#
# INSERT INTO Alignment (name)
# SELECT DISTINCT ALIGN FROM MarvelCharacters;
#
# INSERT INTO LivingStatus (status)
# SELECT DISTINCT ALIVE FROM MarvelCharacters;
#
# INSERT INTO Identity (identity)
# SELECT DISTINCT identify FROM MarvelCharacters;
#
# Создание таблицы с внешними ключами
# CREATE TABLE MarvelCharacters_New (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     page_id INTEGER,
#     name TEXT,
#     urlslug TEXT,
#     identity_id INTEGER,
#     align_id INTEGER,
#     eye_id INTEGER,
#     hair_id INTEGER,
#     sex_id INTEGER,
#     status_id INTEGER,
#     APPEARANCES INTEGER,
#     FIRST_APPEARANCE TEXT,
#     Year INTEGER,
#     FOREIGN KEY (identity_id) REFERENCES Identity(id),
#     FOREIGN KEY (align_id) REFERENCES Alignment(id),
#     FOREIGN KEY (eye_id) REFERENCES EyeColor(id),
#     FOREIGN KEY (hair_id) REFERENCES HairColor(id),
#     FOREIGN KEY (sex_id) REFERENCES Sex(id),
#     FOREIGN KEY (status_id) REFERENCES LivingStatus(id)
# );
