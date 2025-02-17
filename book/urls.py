from django.urls import path, re_path

from book import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# 6 路由组件
from rest_framework import routers
# router = routers.DefaultRouter()
# router.register('book', views.BookView, basename='book')
# router.register('publisher', views.PublisherViewSet, basename='publisher')
# router.register('author', views.AuthorViewSet, basename='author')

urlpatterns = [
    # 1 APIView
    path('books/', views.BookView.as_view()),
    # path('books/<int:pk>/', views.BookDetailView.as_view()),

    # 2 GenericAPIView
    # path('books/', views.BookView.as_view()),
    # path('books/<int:pk>/', views.BookDetailView.as_view()),
    # path('authors/', views.AuthorView.as_view()),
    # path('authors/<int:pk>/', views.AuthorDetailView.as_view()),

    # 3 MinIn混合类
    # path('books/', views.BookView.as_view()),
    # path('books/<int:pk>/', views.BookDetailView.as_view()),

    # 4 MinIn混合类的再封装继续简化接口
    # path('books/', views.BookView.as_view()),
    # path('books/<int:pk>/', views.BookDetailView.as_view()),
    # path('authors/', views.AuthorView.as_view()),
    # path('authors/<int:pk>/', views.AuthorDetailView.as_view()),

    # 5 ViewSet 修改路由分发机制
    # path('books/', views.BookView.as_view({'get': 'list', 'post': 'create'})),
    # re_path('books/(?P<pk>\d+)/', views.BookView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # 6 ModelViewSet 修改路由分发机制
    # path('books/', views.BookView.as_view({'get': 'list', 'post': 'create'})),
    # re_path('books/(?P<pk>\d+)/', views.BookView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # path('publisher/', views.PublisherViewSet.as_view({'get': 'list', 'post': 'create'})),
    # re_path('publisher/(?P<pk>\d+)/', views.PublisherViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # path('author/', views.AuthorViewSet.as_view({'get': 'list', 'post': 'create'})),
    # re_path('author/(?P<pk>\d+)/', views.AuthorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),


    # token jwt
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

# 6 路由组件# 路由工具
# urlpatterns += router.urls
