from django.shortcuts import render,get_object_or_404
from .models import *
from django.views.decorators.http import require_POST
from django.conf import settings



def index(request):
    profiles=Profile.objects.all()
    if request.method=='POST':
        form=IcecreamForms(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data['name']
            description=form.cleaned_data['description']
            # slug=slugify(nam)
            slug=slugify(translit(name,'ru',reversed=True))
            photo=form.cleaned_data['photo']
            file=form.cleaned_data['file']
            Icecream.objects.get_or_create(name=name,
                                              defaults={
                                                  'description':description,
                                                  'slug':slug,
                                                  'photo':photo,
                                                  'file':file
                                                  })
            context={'success':True}
            return render(request,'mains/index.html',context=context)
    else:
        form=IcecreamForms
    
    context={
        'title':'text',
        'profiles':profiles,
        'form':form,
    }
    return render(request,'mains/index.html',context=context)

# def detail_card(request,id):
#     profile=get_object_or_404(Profile,id=id)
#     context={
#         'profile':profile
#     }
#     return render(request,'mains/profile_detail.html',context=context)


# from .models import MenuItem
from django.core.mail import EmailMessage
from .forms import *

# def menu_view(request):
#     menu_items = MenuItem.objects.all()
#     return render(request, 'mains/three_menu.html', {'menu_items': menu_items})

def first_form(request):
    if request.method=='POST':
        form=EmailForms(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            comment=form.cleaned_data.get('comment','')
            file=form.cleaned_data['file']
            image=form.cleaned_data['image']
            
            subject=name
            message=f'{name}\nTo: {email}\\n{comment}\nФото:{image}\nФайл{file}'
            email_message=EmailMessage(subject,message,settings.EMAIL_HOST_USER,[email])
            email_message.attach(file.name,file.read(),file.content_type)
            email_message.attach(image.name,image.read(),image.content_type)
            email_message.send()
            context={'success':True}
            return render(request, 'mains/mail_form.html', context)
    else:
        form=EmailForms
        
    context={'form':form}
    return render(request, 'mains/mail_form.html', context)


def post(request):
    post_all=Post.objects.all()
    context={
        'post_all':post_all
        }
    return render(request,'mains/post.html',context=context)



def post_detail(request, slug):
    post = get_object_or_404(Post,status=Post.Status.PUBLISHED,slug=slug)
 # Список активных комментариев к этому посту
    comments = post.comments.filter(active=True)
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        print(comment,'ПЕРВОЕ')
        print(comment.post,'ВТОРОЕ')
        # Назначить пост комментарию
        comment.post = post
        # Сохранить комментарий в базе данных
        comment.save()
 # Форма для комментирования пользователями
    # form = CommentForm()
    context={
        'post': post,
        'comments': comments,
        'form': form
        }
    return render(request,'mains/post_detail.html',context=context)

# # @require_POST
# def post_comment(request, slug):
#     post = get_object_or_404(Post,
#     slug=slug,
#     status=Post.Status.PUBLISHED)
#     comment = None
#     # Комментарий был отправлен
#     form = CommentForm(data=request.POST)
#     if form.is_valid():
#         # Создать объект класса Comment, не сохраняя его в базе данных
#         comment = form.save(commit=False)
#         print(comment,'ПЕРВОЕ')
#         print(comment.post,'ВТОРОЕ')
#         # Назначить пост комментарию
#         comment.post = post
#         # Сохранить комментарий в базе данных
#         comment.save()
#         return render(request, 'mains/post_detail.html',
#                       {'post': post,
#                       'form': form,
#                       'comment': comment})

# def create_icecream_objects():
#     icecream_db = [
#     {
#     'name': 'Золотое мороженое',
#     'description': ('Шарики таитянского ванильного мороженого, шоколад '
#                     '"Amedei Porcelana" и груда экзотических фруктов.'
#                     'Всё это покрыто золотой фольгой, '
#                     'её тоже полагается съесть.'),
#     },
#     {   
#     'name': 'Готическое мороженое',
#     'description': ('Чёрное мороженое в чёрном вафельном рожке для '
#                     'true black goths. Состав: сливочное мороженое, '
#                     'миндаль, активированный уголь, чернота, мрак, отрицание.'),
#     },
#     {
#     'name': 'Мороженое паста карбонара',
#     'description': ('Порция макарон под тёмным соусом. '
#                     'Паста — из ванильного мороженого, '
#                     'продавленного через пресс с дырочками, '
#                     'соус — ликёр с орехами. Buon appetito!'),
#     },
#     {
#     'name': 'Фруктово-ягодное мороженое ГОСТ 119-52',
#     'description': ('Сырьё: сливки, пахта, фрукты и ягоды в свежем виде, '
#                     'яичный порошок из куриных яиц, патока карамельная. '
#                     'Общее количество микробов в 1 мл мороженого: '
#                     'не более 250 тыс.'),
#     },
#     {
#     'name': 'Люминесцентное мороженое',
#     'description': ('Сливочное мороженое с белками, активированными кальцием. '
#                     'Светится, если облизнуть. '
#                     'Можно подавать в тыкве на Хэллоуин '
#                     'или кормить собаку Баскервилей.'),
#     },
#     {
#     'name': 'Жареное мороженое',
#     'description': ('Шарики мороженого обваливают яйце и в панировке, '
#                     'сильно замораживают и быстро обжаривают '
#                     'в растительном масле. Едят быстро.'),
#     },
#     {
#     'name': 'Томатное мороженое',
#     'description': ('Сливки, помидоры, чеснок, лавровый лист, '
#                     'молотый перец. Если растает — '
#                     'можно подавать к обеду как первое блюдо.'),
#     },
# ]


#     for icecream_data in icecream_db:
#         Icecream.objects.get_or_create(
#             name=icecream_data['name'],
#             defaults={'description': icecream_data['description']}
#         )
        
# def icecream_list(request):
#     create_icecream_objects()
#     icecreams = Icecream.objects.all()
#     return render(request, 'icecream_list.html', {'icecreams': icecreams})
