from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('pages:homepage'),
        ),
        name='registration',
    ),
    path('birthday/', include('birthday.urls')),
]

handler404 = 'core.views.page_not_found'
handler400 = 'core.views.bad_request'
handler403 = 'core.views.response_forbidden'

if settings.DEBUG:
    import debug_toolbar
    # Добавить к списку urlpatterns список адресов из приложения debug_toolbar:
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)),]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
