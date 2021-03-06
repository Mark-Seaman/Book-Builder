# Design Pattern - Django Data Views

Build generic views to do all of the CRUD operations


### Django View Classes

Django defines a number of general purpose view classes.
Each of these classes define the common behavoir for views.

Each view can be implmented in its simplest form with just
a few lines of code.  Then the view can be customized as
much as needed.

* TemplateView
* ListView
* DetailView
* CreateView
* UpdateView
* DeleteView


### SuperHero Example

Here is a very simple example that shows little customization.


### Define Python class
Superhero (name, identity, image)

hero/models.py

    class Superhero(models.Model):
        name = models.CharField(max_length=20)
        identity = models.CharField(max_length=20)
        image = models.CharField(max_length=20)
        
        def __str__(self):
            return self.name
            
        def get_absolute_url(self): 
            return reverse('home', args=[str(self.id)])


### TemplateView

templates/hero_detail.html

    <h1>{{ title }}</h1>
    <p>
        Hero Name: {{ hero.name }}
    </p>
    <p>
        Secret Identify: {{ hero.identity }}
    </p>
    <p>
        SHIELD Number: {{ hero.pk }}
    </p>
    
    
hero/views.py
    
    from django.views.generic import TemplateView

    class HeroView(TemplateView):
        template_name = "hero_detail.html"

        def get_context_data(self, **kwargs):
            heroes = Superhero.objects.get(pk=1)
            return {'hero': hero}

hero/urls.py

    from django.urls import path
    from .views import HeroView

    urlpatterns = [
        path('', HeroView.as_view(), name='home'),
        path('<str:identity>', HeroView.as_view(), name='hero_detail'),
    ]

 
### ListView
* Create a table or divs that show a list of records
* Each hero should have a link that goes to the details page

templates/hero_list.html

    {% extends 'page_theme.html' %}


    {% block main %}

        <h1>Heroes Gallery</h1>

        {% for hero in heroes %}

            <h2>Hero - {{ hero.name }}</h2>
            <p>
                This page shows my favorite hero.
            </p>
            <p>
                Secret ID: {{ hero.identity }}
            </p>
            <img width="300" src="/static/images/{{ hero.name }}.jpg" alt="{{ hero.identity }}">

        {% endfor %}

    {% endblock main %}

    
hero/views.py
    
    from django.views.generic import ListView
    from .models import Superhero

    class HeroListView(ListView):
        template_name = "hero_list.html"
        model = Superhero


hero/urls.py

    from django.urls import path
    from hero.views import HeroView

    urlpatterns = [
        path('', HeroListView.as_view(), name='hero_list'),        
    ]


### DetailView
* Display all info from the Database record
* Show the image as a thumbnail with a link to the large image
* Add a button to Edit the record

templates/hero_detail.html

    <a href="/">Hero List</a>
    <h1>{{ title }}</h1>
    <p>
        Hero Name: {{ hero.name }}
    </p>
    <p>
        Secret Identify: {{ hero.identity }}
    </p>
    <p>
        SHIELD Number: {{ hero.pk }}
    </p>
    
    
hero/views.py
    
    from django.views.generic import DetailView

    class HeroView(DetailView):
        template_name = "hero_detail.html"
        model = Superhero
        

hero/urls.py

    from django.urls import path
    from .views import HeroDetailView

    urlpatterns = [
        path('<int:pk>', HeroDetailView.as_view(), name='hero_detail'),        
    ]


### CreateView
* Create new records with a view
* You can cheat by loading the image file into a directory
* Add the image as a URL pointing to this file

templates/hero_add.html

    {% extends 'page_theme.html' %}

    {% block content %}

        <h1>New Hero</h1>

        <form action="" method="post">{% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Save">
        </form>

    {% endblock content %}
  
    
hero/views.py

    from django.views.generic.edit import CreateView
    from .models import Superhero
    
    class HeroAddView(CreateView):
        template_name = "hero_add.html"
        model = Superhero
        fields = '__all__'


hero/urls.py

    from django.urls import path
    from .views import HeroAddView

    urlpatterns = [
        path('<int:pk>', HeroAddView.as_view(), name='hero_add'),        
    ]



### UpdateView
* Make sure that you can edit the records
* Make sure that the page is redirected after save


templates/hero_edit.html

    {% extends 'page_theme.html' %}

    {% block content %}

        <h1>Edit Hero</h1>

        <form action="" method="post">{% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Save">
        </form>

    {% endblock content %}
  
    
hero/views.py

    from django.views.generic.edit import CreateView
    from .models import Superhero
    
    class HeroEditView(CreateView):
        template_name = "hero_edit.html"
        model = Superhero
        fields = '__all__'


hero/urls.py

    from django.urls import path
    from .views import HeroAddView, HeroEditView

    urlpatterns = [
        path('<int:pk>',  HeroAddView.as_view(),    name='hero_add'),        
        path('<int:pk>/', HeroUpdateView.as_view(), name='hero_edit'),
    ]


### DeleteView
* Delete the records after confirmation
* Go to the list after a delete

templates/hero_delete.html

    {% extends 'page_theme.html' %}

    {% block content %}

        <h1>Delete Hero?</h1>

        <form action="" method="post">{% csrf_token %}
            <p>Are you sure you want to delete "{{ hero.name }}"?</p>
            <input type="submit" value="Confirm">
        </form>

    {% endblock content %}

    
hero/views.py

    from django.urls import reverse_lazy 
    from django.views.generic.edit import DeleteView
    from .models import Superhero
    
    class HeroDeleteView(DeleteView):
        template_name = "hero_delete.html"
        model = Superhero
        success_url = reverse_lazy('hero_list')
        

hero/urls.py

    from django.urls import path
    from .views import HeroAddView, HeroDetailView, HeroEditView, HeroListView, HeroUpdateView

    urlpatterns = [
        path('',          HeroListView.as_view(),   name='hero_list'),
        path('add',       HeroAddView.as_view(),    name='hero_add'),        
        path('<int:pk>',  HeroDetailView.as_view(), name='hero_detail'),
        path('<int:pk>/', HeroUpdateView.as_view(), name='hero_edit'),
        path('<int:pk>/delete', HeroDeleteView.as_view(), name='hero_delete'),
    ]
