from django.urls import path,include
from django.conf.urls import include, url   
from . import views
from django.conf.urls.static import static
from pro import settings
urlpatterns = [
            path("register", views.register, name="register"),
            path("index", views.index, name="index"),
            path('',views.index,name="index "),

            path('update',views.edit,name="update"),
            path('profile',views.profile,name="profile "),
            path('shop_ct',views.deliver_item,name="shop_ct"),
            path('service_ct',views.deliver_service,name="service_ct"),
            path('category/<category>', views.caretaker.as_view(), name='caretaker'),
            path('category2/<category>', views.caretaker2.as_view(), name='caretaker2'),
            path('display_items/',views.display_items,name='display_items'),
            path('category8/<category>', views.ItemListView.as_view(), name='detail_items'),
            

            url('', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
              
          

