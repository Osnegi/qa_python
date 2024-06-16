from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_name_more_than_40(self):
        collector = BooksCollector()
        collector.add_new_book('Очень длинное название книжки-мартышки-малышки')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_name_zero_symbols(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_name_in_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_book_in_books_genre_and_genre_in_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.books_genre.get('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_set_book_genre_book_not_in_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert (not collector.books_genre.get('Гордость и предубеждение и зомби') == 'Ужасы') and (len(collector.get_books_genre()) == 1)

    def test_set_book_genre_genre_not_in_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Про любовь')
        assert not collector.books_genre.get('Гордость и предубеждение и зомби') == 'Про любовь'

    def test_get_book_genre_name_in_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_book_genre_name_not_in_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert (not collector.get_book_genre('Просто зомби') == 'Ужасы') and (len(collector.get_books_genre()) == 1)

    def test_get_books_with_specific_genre_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Просто зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Просто кот')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Просто зомби', 'Детективы')
        collector.set_book_genre('Просто кот', 'Комедии')
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2

    def test_get_books_with_specific_genre_zero_books(self):
        collector = BooksCollector()
        collector.add_new_book('Просто зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Просто кот')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Просто зомби', 'Детективы')
        collector.set_book_genre('Просто кот', 'Комедии')
        assert len(collector.get_books_with_specific_genre('Фантастика')) == 0

    def test_get_books_with_specific_genre_zero_books(self):
        collector = BooksCollector()
        collector.add_new_book('Просто зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Просто кот')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Просто зомби', 'Детективы')
        collector.set_book_genre('Просто кот', 'Комедии')
        assert len(collector.get_books_with_specific_genre('Про любовь')) == 0

    def test_get_books_genre_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Просто зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Просто зомби', 'Детективы')
        assert collector.get_books_genre() == {'Просто зомби':'Детективы',
                                              'Гордость и предубеждение и зомби':'Ужасы'}

    def test_get_books_for_children_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Просто зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Просто кот')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Мультфильмы')
        collector.set_book_genre('Просто зомби', 'Детективы')
        collector.set_book_genre('Просто кот', 'Комедии')
        assert len(collector.get_books_for_children()) == 2

    def test_get_books_for_children_zero_books(self):
        collector = BooksCollector()
        collector.add_new_book('Просто зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Просто зомби', 'Детективы')
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_name_in_books_genre_and_not_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Просто зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Просто зомби', 'Детективы')
        collector.add_book_in_favorites('Просто зомби')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_name_not_in_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Просто зомби')
        collector.set_book_genre('Просто зомби', 'Детективы')
        collector.add_book_in_favorites('Просто кот')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_name_in_books_genre_and_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Просто зомби')
        collector.set_book_genre('Просто зомби', 'Детективы')
        collector.add_book_in_favorites('Просто зомби')
        collector.add_book_in_favorites('Просто зомби')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_name_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Просто зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Просто зомби', 'Детективы')
        collector.add_book_in_favorites('Просто зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Просто зомби')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_name_not_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Просто зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Просто зомби', 'Детективы')
        collector.add_book_in_favorites('Просто зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Просто кот')
        assert len(collector.get_list_of_favorites_books()) == 2
