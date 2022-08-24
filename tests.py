from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    def test_set_book_rating_to_exciting_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем новую книгу и выставляем ей рейтинг 3
        name = 'Гордость и предубеждение и зомби'
        rating = 3
        collector.add_new_book(name)
        collector.set_book_rating(name, rating)

        assert collector.books_rating[name] == 3

    def test_get_book_rating(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем новую книгу и выставляем ей рейтинг 10
        name = 'Война и мир и любовь'
        rating = 10
        collector.add_new_book(name)
        collector.set_book_rating(name, rating)

        assert collector.books_rating[name] == rating
        assert list(collector.books_rating.keys())[0] == name

    def test_get_books_with_specific_rating(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем новую книгу и выставляем ей рейтинг 100
        name = 'Война и мир и любовь'
        rating = 10
        collector.add_new_book(name)
        collector.set_book_rating(name, rating)

        assert len(collector.get_books_with_specific_rating(rating)) == 1

    def test_get_books_rating(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги и выставляем им рейтинг
        name1 = 'Сказки Пушкина'
        rating1 = 9
        name2 = 'Русские народные сказки'

        collector.add_new_book(name1)
        collector.set_book_rating(name1, rating1)

        collector.add_new_book(name2)

        assert len(collector.get_books_rating()) == 2

    def test_add_book_in_favorites(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу и выставляем ей рейтинг 10
        name = 'Сказки Пушкина'
        rating = 10

        collector.add_new_book(name)
        collector.set_book_rating(name, rating)

        collector.add_book_in_favorites(name)

        assert len(collector.favorites) > 0
        assert name in collector.favorites

    def test_delete_book_from_favorites(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу и выставляем ей рейтинг 10
        name = 'Сказки Пушкина'
        rating = 10

        collector.add_new_book(name)
        collector.set_book_rating(name, rating)

        # Добавлеяем книгу в favorites
        collector.add_book_in_favorites(name)

        collector.favorites.remove(name)

        assert len(collector.favorites) == 0
        assert name not in collector.favorites

    def test_get_list_of_favorites_books(self):
        # Cоздаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # Добавляем книгу
        name = 'Сказки Пушкина'
        collector.add_new_book(name)

        # Добавлеяем книгу в favorites
        collector.add_book_in_favorites(name)

        assert len(collector.get_list_of_favorites_books()) == 1
        assert name in collector.get_list_of_favorites_books()
