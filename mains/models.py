from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.utils.text import slugify
from transliterate import translit
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager
from taggit.models import Tag



#Создаю модельку OneToMany
class Product(models.Model):
    name=models.CharField(max_length=255)
    created=models.DateTimeField(auto_now_add=True)
    # publish=models.DateTimeField(default=(timezone.now()+timedelta(hours=6)))
    # updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering='-name',
        verbose_name='Продукт'
        verbose_name_plural='Продукты'

    def __str__(self):
        return self.name
        

class Category(models.Model):
    name=models.CharField(max_length=255)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
    
    def __str__(self):
        return self.name

#создаю модельку OneToOne
class User(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural='Пользователи'

    def __str__(self):
        return self.name

class Profile(models.Model):
    name=models.CharField(max_length=255)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name='Профиль'
        verbose_name_plural='Профили'

    def __str__(self):
        return self.name


#ManyToMany
class Students(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()

    class Meta:
        verbose_name='Студент'
        verbose_name_plural='Студенты'

    def __str__(self):
        return self.name

class Courses(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    students=models.ManyToManyField(Students,related_name='courses')

    class Meta:
        verbose_name='Курс'
        verbose_name_plural='Курсы'

    def __str__(self):
        return self.title


class Icecream(models.Model):
    name=models.CharField(max_length=255,verbose_name='Имя')
    description=models.CharField(max_length=255,verbose_name='описание')
    photo=models.ImageField(upload_to='photoForm',null=True)
    file=models.FileField(upload_to='fileForm',null=True)
    slug=models.SlugField(max_length=255,)
    
    class Meta:
        verbose_name='Мороженное'
        verbose_name_plural='Мороженное'
        # indexes = [models.Index(fields=['description']),]

    def __str__(self):
        return self.name 

@receiver(post_migrate)
def seed_data(sender,**kwargs):
    
    icecream_db = [
            {
                'name': 'Золотое мороженое',
                'description': ('Шарики таитянского ванильного мороженого, шоколад '
                                '"Amedei Porcelana" и груда экзотических фруктов.'
                                'Всё это покрыто золотой фольгой, '
                                'её тоже полагается съесть.'),
        },
        {
        'name': 'Готическое мороженое',
        'description': ('Чёрное мороженое в чёрном вафельном рожке для '
                        'true black goths. Состав: сливочное мороженое, '
                        'миндаль, активированный уголь, чернота, мрак, отрицание.'),
        },
        {
        'name': 'Мороженое паста карбонара',
        'description': ('Порция макарон под тёмным соусом. '
                        'Паста — из ванильного мороженого, '
                        'продавленного через пресс с дырочками, '
                        'соус — ликёр с орехами. Buon appetito!'),
        },
        {
        'name': 'Фруктово-ягодное мороженое ГОСТ 119-52',
        'description': ('Сырьё: сливки, пахта, фрукты и ягоды в свежем виде, '
                        'яичный порошок из куриных яиц, патока карамельная. '
                        'Общее количество микробов в 1 мл мороженого: '
                        'не более 250 тыс.'),
        },
        {
        'name': 'Люминесцентное мороженое',
        'description': ('Сливочное мороженое с белками, активированными кальцием. '
                        'Светится, если облизнуть. '
                        'Можно подавать в тыкве на Хэллоуин '
                        'или кормить собаку Баскервилей.'),
        },
        {
        'name': 'Жареное мороженое',
        'description': ('Шарики мороженого обваливают яйце и в панировке, '
                        'сильно замораживают и быстро обжаривают '
                        'в растительном масле. Едят быстро.'),
        },
        {
        'name': 'Томатное мороженое',
        'description': ('Сливки, помидоры, чеснок, лавровый лист, '
                        'молотый перец. Если растает — '
                        'можно подавать к обеду как первое блюдо.'),
        },
    ]
    for icecream_data in icecream_db:
        icecream,created=Icecream.objects.update_or_create(name=icecream_data['name'],defaults=
                                                           {
                                                               'description':icecream_data['description'],
                                                               'slug':slugify(translit(icecream_data['name'],'ru',reversed=True
                                                                                       ))})
        # print(icecream,created)
        


class Post(models.Model):

    # status_choices={'DF': 'Draft',
    #                 'PB': 'Published'
    #                 }
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    tags=TaggableManager()
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,choices=Status.choices,default=Status.DRAFT)
    slug = models.SlugField(max_length=250,unique_for_date='publish')

    class Meta: 
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish']),]
        verbose_name='Пост'
        verbose_name_plural='Посты'
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail',args=[self.slug])

class Comments(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=255)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        verbose_name='Коментарий'
        verbose_name_plural='Коментарии'

    def __str__(self):
        return f'Comment by {self.name}'
    
    def get_absolute_url(self):
        return reverse('post_card',args=[self.slug])
    