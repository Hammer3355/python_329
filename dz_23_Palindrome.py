import json
from dataclasses import dataclass


@dataclass
class Palindrome:
    word: str
    meaning: str

    def is_palindrome(self) -> bool:
        """
        Проверяет, является ли слово палиндромом.

        Returns:
            bool: True, если слово является палиндромом, иначе False.
        """
        clean_word = "".join(filter(str.isalpha, self.word.lower()))
        return clean_word == clean_word[::-1]

    @classmethod
    def from_json(cls, json_data: list) -> list:
        """
        Создает список экземпляров класса Palindrome из JSON-данных.

        Args:
            json_data (list): JSON-данные в виде списка словарей.

        Returns:
            list: Список экземпляров класса Palindrome.
        """
        palindromes = []
        for data in json_data:
            palindrome = cls(data["word"], data["meaning"])
            palindromes.append(palindrome)
        return palindromes


def main() -> None:
    """
    Основная функция программы.
    """
    with open("palindromes.json", encoding="utf-8") as file:
        data = json.load(file)

    palindromes = Palindrome.from_json(data)

    palindrome_count = 0
    non_palindrome_count = 0
    palindrome_words = []
    non_palindrome_words = []

    for palindrome in palindromes:
        if palindrome.is_palindrome():
            palindrome_count += 1
            palindrome_words.append(palindrome.word)
        else:
            non_palindrome_count += 1
            non_palindrome_words.append(palindrome.word)

    print(f"Количество палиндромов: {palindrome_count}")
    print(f"Количество непалиндромов: {non_palindrome_count}")
    print("Слова-палиндромы:")
    for word in palindrome_words:
        print(word)
    print("Непалиндромные слова:")
    for word in non_palindrome_words:
        print(word)


if __name__ == "__main__":
    main()
