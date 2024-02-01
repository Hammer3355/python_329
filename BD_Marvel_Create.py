Создаем таблицу MarvelCharacters в базе данных marvel

CREATE TABLE MarvelCharacters (
    page_id INTEGER,
    name TEXT,
    urlslug TEXT,
    identify TEXT,
    ALIGN TEXT,
    EYE TEXT,
    HAIR TEXT,
    SEX TEXT,
    GSM TEXT,
    ALIVE TEXT,
    APPEARANCES INTEGER,
    FIRST_APPEARANCE TEXT,
    Year INTEGER
);

Создаем новую таблицу MarvelCharacters_new с дополнительным полем уникального id записи
"id INTEGER PRIMARY KEY AUTOINCREMENT".

CREATE TABLE MarvelCharacters_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    page_id           INTEGER,
    name              TEXT,
    urlslug           TEXT,
    identify          TEXT,
    ALIGN             TEXT,
    EYE               TEXT,
    HAIR              TEXT,
    SEX               TEXT,
    GSM               TEXT,
    ALIVE             TEXT,
    APPEARANCES       INTEGER,
    FIRST_APPEARANCE TEXT,
    Year
);

Перенос данных из MarvelCharacters в MarvelCharacters_new
INSERT INTO MarvelCharacters_new(
     page_id,
     name,
     urlslug,
     identify,
     ALIGN,
     EYE,
     HAIR,
     SEX,
     GSM,
     ALIVE,
     APPEARANCES,
     FIRST_APPEARANCE,
     Year
)
SELECT
    page_id,
    name,
    urlslug,
    identify,
    ALIGN,
    EYE,
    HAIR,
    SEX,
    GSM,
    ALIVE,
    APPEARANCES,
    FIRST_APPEARANCE,
    Year
FROM MarvelCharacters;

Удаление таблицы MarvelCharacters
DROP TABLE MarvelCharacters;

Переименование таблицы MarvelCharacters_new в MarvelCharacters
ALTER TABLE MarvelCharacters_new
RENAME TO MarvelCharacters;

Создание таблиц для уникальных значений
CREATE TABLE  Alignment (
 align_id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT UNIQUE
);
CREATE TABLE  EyeColor (
 eye_id INTEGER PRIMARY KEY AUTOINCREMENT,
 color TEXT UNIQUE
);
CREATE TABLE  HairColor (
 hair_id INTEGER PRIMARY KEY AUTOINCREMENT,
 color TEXT UNIQUE
);
CREATE TABLE  Identity (
 identity_id INTEGER PRIMARY KEY AUTOINCREMENT,
 identity TEXT UNIQUE
);
CREATE TABLE  LivingStatus (
 status_id INTEGER PRIMARY KEY AUTOINCREMENT,
 status TEXT UNIQUE
);
CREATE TABLE  Sex (
 sex_id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT UNIQUE
);

Запрос на заполнение таблиц уникальными значениями из таблицы MarvelCharacters:
INSERT INTO Alignment (name)
SELECT DISTINCT ALIGN FROM MarvelCharacters;

INSERT INTO EyeColor (color)
SELECT DISTINCT EYE FROM MarvelCharacters;

INSERT INTO HairColor (color)
SELECT DISTINCT HAIR FROM MarvelCharacters;

INSERT INTO Identity (identity)
SELECT DISTINCT identify FROM MarvelCharacters;

INSERT INTO LivingStatus (status)
SELECT DISTINCT ALIVE FROM MarvelCharacters;

INSERT INTO Sex (name)
SELECT DISTINCT SEX FROM MarvelCharacters;

Создание таблицы с внешними ключами
CREATE TABLE MarvelCharacters_new (
id INTEGER PRIMARY KEY AUTOINCREMENT,
page_id INTEGER,
name TEXT,
urlslug TEXT,
identity_id INTEGER,
align_id INTEGER,
eye_id INTEGER,
hair_id INTEGER,
sex_id INTEGER,
status_id INTEGER,
APPEARANCES INTEGER,
FIRST_APPEARANCE TEXT,
Year INTEGER,
FOREIGN KEY (identity_id) REFERENCES Identity (identity_id),
FOREIGN KEY (align_id) REFERENCES Alignment (align_id),
FOREIGN KEY (eye_id) REFERENCES EyeColor (eye_id),
FOREIGN KEY (hair_id) REFERENCES HairColor (hair_id),
FOREIGN KEY (sex_id) REFERENCES Sex (sex_id)
FOREIGN KEY (status_id) REFERENCES LivingStatus (status_id)
);

Наполнение новой таблицы данными
INSERT INTO MarvelCharacters_New (page_id, name, urlslug, identity_id, align_id, eye_id, hair_id, sex_id, status_id, APPEARANCES, FIRST_APPEARANCE, Year)
SELECT mc.page_id, mc.name, mc.urlslug, id.identity_id, al.align_id, ec.eye_id, hc.hair_id, s.sex_id, ls.status_id, mc.APPEARANCES, mc.FIRST_APPEARANCE, mc.Year
FROM MarvelCharacters AS mc
JOIN Identity AS id ON mc.identify = id.identity
JOIN Alignment AS al ON mc.ALIGN = al.name
JOIN EyeColor AS ec ON mc.EYE = ec.color
JOIN HairColor AS hc ON mc.HAIR = hc.color
JOIN Sex AS s ON mc.SEX = s.name
JOIN LivingStatus AS ls ON mc.ALIVE = ls.status;

Удаление старой таблицы
DROP TABLE MarvelCharacters;

Переименование тоблицы
ALTER TABLE MarvelCharacters_new RENAME TO MarvelCharacters;