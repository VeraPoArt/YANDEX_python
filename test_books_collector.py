import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()



class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        # Добавляем две книги
        collector.add_new_book('Последнее желание')
        collector.add_new_book('Резьба по живому')

        # Проверяем, что добавилось именно две книги
        assert len(collector.get_books_genre()) == 2 #поправила тест, так как у нас он был с несуществующим методом

    # Тесты для add_new_book с валидными названиями
    @pytest.mark.parametrize("book_name", [
        "Последнее желание",
        "Резьба по живому",
        "Дыши",
        "Прачечная, стирающая печали",
        "1794 Никлас Натт-о-Даг"
    ])
    def test_add_new_book_valid_names(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre


    @pytest.mark.parametrize("book_name", [
        "",
        "1794 Цикл «Бельманская нуарная трилогия», №2 Никлас Натт-о-Даг",
        "A" * 41
    ])
    def test_add_new_book_invalid_names(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre

    def test_add_new_book_duplicate(self, collector):
        collector.add_new_book("Последнее желание")
        collector.add_new_book("Последнее желание")
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize("book_name, genre", [
        ("Последнее желание", "Фантастика"),
        ("Резьба по живому", "Ужасы"),
    ])
    def test_set_book_genre_success(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] == genre

    def test_set_book_genre_nonexistent_book(self, collector):
        collector.set_book_genre("Несуществующая книга", "Фантастика")
        assert "Несуществующая книга" not in collector.books_genre

    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book("Последнее желание")
        collector.set_book_genre("Последнее желание", "Нераспространенный жанр")
        assert collector.books_genre["Последнее желание"] == ""

    def test_get_book_genre_existing(self, collector):
        collector.add_new_book("Последнее желание")
        collector.set_book_genre("Последнее желание", "Фантастика")
        assert collector.get_book_genre("Последнее желание") == "Фантастика"

    def test_get_book_genre_nonexistent(self, collector):
        assert collector.get_book_genre("Несуществующая книга") is None

    @pytest.mark.parametrize("genre, expected_books", [
        ("Фантастика", ["Последнее желание"]),
        ("Ужасы", ["Резьба по живому"]),
    ])
    def test_get_books_with_specific_genre(self, collector, genre, expected_books):
        for book_name in expected_books:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, genre)
        assert collector.get_books_with_specific_genre(genre) == expected_books

    def test_get_books_with_specific_genre_no_matches(self, collector):
        assert collector.get_books_with_specific_genre("Фантастика") == []

    def test_get_books_genre(self, collector):
        collector.add_new_book("Последнее желание")
        collector.set_book_genre("Последнее желание", "Фантастика")
        expected = {"Последнее желание": "Фантастика"}
        assert collector.get_books_genre() == expected

    def test_get_books_for_children(self, collector):
        collector.add_new_book("Последнее желание")
        collector.set_book_genre("Последнее желание", "Фантастика")
        collector.add_new_book("Резьба по живому")
        collector.set_book_genre("Резьба по живому", "Ужасы")
        assert collector.get_books_for_children() == ["Последнее желание"]

    def test_add_book_in_favorites_success(self, collector):
        collector.add_new_book("Последнее желание")
        collector.add_book_in_favorites("Последнее желание")
        assert "Последнее желание" in collector.favorites

    def test_add_book_in_favorites_nonexistent_book(self, collector):
        collector.add_book_in_favorites("Несуществующая книга")
        assert "Несуществующая книга" not in collector.favorites

    def test_add_book_in_favorites_duplicate(self, collector):
        collector.add_new_book("Последнее желание")
        collector.add_book_in_favorites("Последнее желание")
        collector.add_book_in_favorites("Последнее желание")
        assert collector.favorites.count("Последнее желание") == 1

    def test_delete_book_from_favorites_success(self, collector):
        collector.add_new_book("Последнее желание")
        collector.add_book_in_favorites("Последнее желание")
        collector.delete_book_from_favorites("Последнее желание")
        assert "Последнее желание" not in collector.favorites

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book("Последнее желание")
        collector.add_book_in_favorites("Последнее желание")
        assert collector.get_list_of_favorites_books() == ["Последнее желание"]

    def test_get_list_of_favorites_books_empty(self, collector):
        assert collector.get_list_of_favorites_books() == []