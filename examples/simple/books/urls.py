from django.urls import path

from .views import (
    AddAuthorsToBookView,
    AuthorListView,
    AuthorListJSONView,
    AuthorListValuesView,
    AuthorListValuesWithCountsView,
    AuthorListWithCountsView,
    CreateAuthorsView,
    BookListView,
    BookListValuesView,
    BookListWithCountsView,
    PublisherIDsView,
    PublisherListView,
    UpdateBooksView,
    IndexView,
)

__all__ = ('urlpatterns',)


urlpatterns = [
    # Authors list
    path('authors/', AuthorListView.as_view(), name='books.authors'),

    # Authors list (more efficient)
    path('authors-values/',
        AuthorListValuesView.as_view(),
        name='books.authors_values'),

    # Authors list (with counts)
    path('authors-with-counts/',
        AuthorListWithCountsView.as_view(),
        name='books.authors_with_counts'),

    # Authors list (values with counts)
    path('authors-values-with-counts/',
        AuthorListValuesWithCountsView.as_view(),
        name='books.authors_values_with_counts'),

    # Authors list in JSON format
    path('authors-json/',
        AuthorListJSONView.as_view(),
        name='books.authors_json'),

    # Books list
    path('books/', BookListView.as_view(), name='books.books'),

    # Books list (with counts)
    path('books-with-counts/',
        BookListWithCountsView.as_view(),
        name='books.books_with_counts'),

    # Books list (more efficient)
    path('books-values/',
        view=BookListValuesView.as_view(),
        name='books.books_values'),

    # Publishers list
    path('publishers/',
        PublisherListView.as_view(),
        name='books.publishers'),

    # Publisher IDs
    path('publisher-ids/',
        PublisherIDsView.as_view(),
        name='books.publisher_ids'),

    # Create authors view
    path('create-authors/',
        CreateAuthorsView.as_view(),
        name='books.create_authors'),

    # Add authors to a book view
    path('add-authors-to-book/',
        AddAuthorsToBookView.as_view(),
        name='books.add_authors_to_book'),

    # Update books view
    path('update-books/',
        UpdateBooksView.as_view(),
        name='books.update_books'),

    # Index view
    path('', IndexView.as_view(), name='books.index'),
]
