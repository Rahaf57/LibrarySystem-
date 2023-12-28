from django.db import models


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    publisher = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f" {self.publisher} - {self.location} "


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"  {self.first_name} - {self.last_name} "


class Language(models.Model):
    id = models.AutoField(primary_key=True)
    language = models.CharField(max_length=70)

    def __str__(self):
        return self.language


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    category_persion = models.CharField(max_length=100)

    def __str__(self):
        return f" {self.category}  "


class Section(models.Model):
    id = models.AutoField(primary_key=True)
    section = models.CharField(max_length=100)
    section_persion = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null= True)

    def __str__(self):
        return f" {self.section}  - {self.category} "


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    signatory = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=30, unique=True)
    peges = models.IntegerField(max_length=11)
    publication_year = models.IntegerField()
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null= True)
    description = models.TextField()
    edition = models.IntegerField()
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null= True)
    faculty = models.ForeignKey('user.faculty', on_delete=models.SET_NULL, null= True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null= True)


    def __str__(self):
        return f"{self.title} - {self.publication_year} - {self.language} -{self.author} -{self.faculty} " \
               f"{self.section} - {self.category} "


class eBook(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    extension = models.CharField(max_length=30)

    def __str__(self):
        return f" {self.book} - {self.extension}  "


class Copies(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"  {self.book}  -  {self.status} "


class Libraries(models.Model):
    id = models.AutoField(primary_key=True)
    faculty = models.ForeignKey('user.faculty', on_delete=models.SET_NULL, null= True)
    content = models.TextField()
    content_persian = models.TextField()
    privacy = models.TextField()
    privacy_persian = models.TextField()
    service = models.TextField()
    service_persian = models.TextField()
    email = models.EmailField(max_length=255)

    def __str__(self):
        return f" {self.faculty} - {self.email} "
