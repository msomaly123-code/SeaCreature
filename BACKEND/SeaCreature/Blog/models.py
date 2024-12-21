from django.db import models
from django.contrib.auth.models import User

class SeaCreature(models.Model):
    """
    Represents a marine sea creature.
    """
    name = models.CharField(max_length=100, unique=True)
    scientific_name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='sea_creatures/')
    habitat = models.CharField(max_length=200)
    diet = models.CharField(max_length=200)
    size = models.DecimalField(max_digits=5, decimal_places=2, help_text="Size in meters")
    conservation_status = models.CharField(
        max_length=50,
        choices=[
            ('LC', 'Least Concern'),
            ('NT', 'Near Threatened'),
            ('VU', 'Vulnerable'),
            ('EN', 'Endangered'),
            ('CR', 'Critically Endangered'),
            ('EW', 'Extinct in the Wild'),
            ('EX', 'Extinct')
        ],
        default='LC'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    """
    Represents a blog post about sea creatures.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    sea_creature = models.ForeignKey(SeaCreature, on_delete=models.CASCADE, related_name='blog_posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    """
    Represents a comment on a blog post.
    """
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.blog_post.title}"
