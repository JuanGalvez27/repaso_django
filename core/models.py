from django.db import models

class Author(models.Model):
    name = models.CharField(
        max_length=30,
        help_text = "Name of the author",
        null = False,
        blank = False
    )
    last_name = models.CharField(
        max_length=30,
        help_text = "Last name of the author",
        null = False,
        blank = False
    )
    nationality = models.CharField(max_length=30)
    email = models.EmailField(
        null=False,
        blank = False,
        unique = True
    )
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

class EntryBlog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="entry_blog")
    content = models.TextField()
     

