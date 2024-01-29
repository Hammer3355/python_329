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