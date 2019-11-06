from django.contrib import admin
from django.urls import path, include # new
from ser import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('req/',views.req,name="req "),
    path('shop/',views.shop,name="shop "),
    path('email/',views.serv_mail,name="email"),
    path('list/',views.MyView,name="list"),
    path('show/',views.Myreqview,name="show"),
    path('gmail/',views.shopmail,name="gmail"),
    path('',include('signin.urls')),
    path('',include('notice.urls')),
    path('residents/',views.residents,name="residents"),
    path('category3/<category>', views.CategoryListView.as_view(), name='category-list'),
    path('add_item/',views.add_item,name='add_item'),
    path('category5/<category>', views.ServiceListView.as_view(), name='serv_view'),
    path('category6/<category>', views.ShopListView.as_view(), name='shop_view'),
    # path('category6/<category>',views.validate_user,name='shop_name')
   
    
]