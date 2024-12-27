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
        ("Дыши", "Мультфильмы"),
        ("Прачечная, стирающая печали", "Комедии"),
        ("1794 Никлас Натт-о-Даг", "Детективы")
    ])
    def test_set_book_genre_valid_genres(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] == genre

    @pytest.mark.parametrize("book_name, genre", [
        ("1794 Никлас Натт-о-Даг", "Нераспространенный жанр"),
        ("Большое волшебство", "Роман"),
        ("Вампир понарошку", "Графический роман"),
        ("Хорошо быть тихоней", "Драма"),
        ("Когда бог был кроликом", "Современная зарубежная литература")
    ])
    def test_set_book_genre_invalid_cases(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        if book_name in collector.books_genre:
            assert collector.books_genre[book_name] != genre
            assert collector.books_genre[book_name] == ""
        else:
            assert book_name not in collector.books_genre

    def test_set_book_genre_success(self, collector):
        collector.add_new_book("Резьба по живому")
        collector.set_book_genre("Резьба по живому", "Ужасы")
        assert collector.books_genre["Резьба по живому"] == "Ужасы"


    def test_set_book_genre_nonexistent_book(self, collector):
        collector.set_book_genre("Несуществующая книга", "Фантастика")
        assert "Несуществующая книга" not in collector.books_genre


    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book("Последнее желание")
        collector.set_book_genre("Последнее желание", "Нераспространенный жанр")
        assert collector.books_genre["Последнее желание"] == ""


    def test_get_book_genre_existing(self, collector):
        collector.add_new_book("Резьба по живому")
        collector.set_book_genre("Резьба по живому", "Ужасы")
        assert collector.get_book_genre("Резьба по живому") == "Ужасы"


    def test_get_book_genre_nonexistent(self, collector):
        assert collector.get_book_genre("Несуществующая книга") is None


    @pytest.mark.parametrize("genre, expected_books", [
        ("Фантастика", ["Последнее желание"]),
        ("Ужасы", ["Резьба по живому"]),
        ("Детективы", ["1794 Никлас Натт-о-Даг"]),  # Обновлённое название детектива
        ("Мультфильмы", ["Дыши"]),
        ("Комедии", ["Прачечная, стирающая печали"])
    ])
    def test_get_books_with_specific_genre(self, collector, genre, expected_books):
        if genre == "Фантастика":
            collector.add_new_book("Последнее желание")
            collector.set_book_genre("Последнее желание", "Фантастика")
        if genre == "Ужасы":
            collector.add_new_book("Резьба по живому")
            collector.set_book_genre("Резьба по живому", "Ужасы")
        if genre == "Детективы":
            collector.add_new_book("1794 Никлас Натт-о-Даг")  # Обновлённое название детектива
            collector.set_book_genre("1794 Никлас Натт-о-Даг", "Детективы")
        if genre == "Мультфильмы":
            collector.add_new_book("Дыши")
            collector.set_book_genre("Дыши", "Мультфильмы")
        if genre == "Комедии":
            collector.add_new_book("Прачечная, стирающая печали")
            collector.set_book_genre("Прачечная, стирающая печали", "Комедии")
        books_with_genre = collector.get_books_with_specific_genre(genre)
        assert books_with_genre == expected_books

    def test_get_books_with_specific_genre_no_matches(self, collector):
        collector.add_new_book("Резьба по живому")
        collector.set_book_genre("Резьба по живому", "Ужасы")
        collector.add_new_book("Прачечная, стирающая печали")
        collector.set_book_genre("Прачечная, стирающая печали", "Комедии")
        books_with_non_existent_genre = collector.get_books_with_specific_genre("Фантастика")
        assert books_with_non_existent_genre == []


    def test_get_books_genre(self, collector):
        collector.add_new_book("Последнее желание")
        collector.add_new_book("Прачечная, стирающая печали")
        collector.set_book_genre("Последнее желание", "Фантастика")
        collector.set_book_genre("Прачечная, стирающая печали", "Комедии")
        expected = {
            "Последнее желание": "Фантастика",
            "Прачечная, стирающая печали": "Комедии"
        }
        assert collector.get_books_genre() == expected


    def test_get_books_for_children_with_favorites(self, collector):
        books = [
            ("Последнее желание", "Фантастика"),
            ("Резьба по живому", "Ужасы"),
            ("Дыши", "Мультфильмы"),
            ("Прачечная, стирающая печали", "Комедии")
        ]
        for book, genre in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
            collector.add_book_in_favorites(book)

        books_for_children = collector.get_books_for_children()
        assert books_for_children == ["Последнее желание", "Дыши", "Прачечная, стирающая печали"]

    def test_get_books_for_children_no_books(self, collector):
        books_for_children = collector.get_books_for_children()
        assert books_for_children == []


    def test_add_book_in_favorites_success(self, collector):
        collector.add_new_book("Резьба по живому")
        collector.set_book_genre("Резьба по живому", "Ужасы")
        collector.add_book_in_favorites("Резьба по живому")
        assert "Резьба по живому" in collector.favorites

    def test_add_book_in_favorites_nonexistent_book(self, collector):
        collector.add_book_in_favorites("Несуществующая книга")
        assert "Несуществующая книга" not in collector.favorites

    def test_add_book_in_favorites_duplicate(self, collector):
        collector.add_new_book("Резьба по живому")
        collector.set_book_genre("Резьба по живому", "Ужасы")
        collector.add_book_in_favorites("Резьба по живому")
        collector.add_book_in_favorites("Резьба по живому")
        assert collector.favorites.count("Резьба по живому") == 1

    def test_delete_book_from_favorites_success(self, collector):
        collector.add_new_book("Резьба по живому")
        collector.set_book_genre("Резьба по живому", "Ужасы")
        collector.add_book_in_favorites("Резьба по живому")
        collector.delete_book_from_favorites("Резьба по живому")
        assert "Резьба по живому" not in collector.favorites

    def test_delete_book_from_favorites_not_in_favorites(self, collector):
        collector.add_new_book("Резьба по живому")
        collector.set_book_genre("Резьба по живому", "Ужасы")
        collector.delete_book_from_favorites("Резьба по живому")
        assert "Резьба по живому" not in collector.favorites

    def test_get_list_of_favorites_books(self, collector):
        books = [
            ("Последнее желание", "Фантастика"),
            ("Резьба по живому", "Ужасы"),
            ("Дыши", "Мультфильмы"),
            ("Прачечная, стирающая печали", "Комедии"),
            ("1794 Никлас Натт-о-Даг", "Детективы")
        ]
        for book, genre in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
            collector.add_book_in_favorites(book)

        favorites = collector.get_list_of_favorites_books()
        expected_favorites = [
            "Последнее желание",
            "Резьба по живому",
            "Дыши",
            "Прачечная, стирающая печали",
            "1794 Никлас Натт-о-Даг"
        ]
        assert favorites == expected_favorites

    def test_get_list_of_favorites_books_empty(self, collector):
        favorites = collector.get_list_of_favorites_books()
        assert favorites == []
