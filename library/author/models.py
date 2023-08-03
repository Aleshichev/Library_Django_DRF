from django.db import models


class Author(models.Model):
    """
    This class represents an Author.
    """

    name = models.CharField(blank=True, max_length=20)
    surname = models.CharField(blank=True, max_length=20)
    patronymic = models.CharField(blank=True, max_length=20)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        """
        Magic method is redefined to show all information about Author.
        """
        return f"id: {self.pk} --- {self.name} {self.surname} {self.patronymic} ---"

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Author object.
        """
        return f"Author(id={self.pk})"

    @staticmethod
    def get_by_id(author_id):
        """
        :param author_id: SERIAL: the id of a Author to be found in the DB
        :return: author object or None if a user with such ID does not exist
        """
        try:
            return Author.objects.get(pk=author_id)
        except Author.DoesNotExist:
            return None

    @staticmethod
    def delete_by_id(author_id):
        """
        :param author_id: an id of a author to be deleted
        :type author_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        try:
            author = Author.objects.get(pk=author_id)
            author.delete()
            return True
        except Author.DoesNotExist:
            return False

    @staticmethod
    def create(name, surname, patronymic):
        """
        """
        if (
            name
            and len(name) <= 20
            and surname
            and len(surname) <= 20
            and patronymic
            and len(patronymic) <= 20
        ):
            author = Author(name=name, surname=surname, patronymic=patronymic)
            author.save()
            return author

    def to_dict(self):
        """
        :return: author id, author name, author surname, author patronymic

        """
        return self.__dict__()

    def update(self, name=None, surname=None, patronymic=None):
        """
        Updates author in the database with the specified parameters.
        """

        if name and len(name) <= 20:
            self.name = name
        if surname and len(surname) <= 20:
            self.surname = surname
        if patronymic and len(patronymic) <= 20:
            self.patronymic = patronymic
        self.save()

    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all authors
        """
        return Author.objects.all()
