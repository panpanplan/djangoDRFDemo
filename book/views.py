import json

from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from book.models import Book, Publisher, Author

# -------------------------------------------------------------------------基于APIView的接口实现--------------------------1

# 基础序列化器，低耦合，手动创建
# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     price = serializers.IntegerField()
#     date = serializers.DateTimeField(source='pub_date')
#
#     def create(self, validated_data):
#         book = Book.objects.create(**validated_data)
#         return BookSerializer(book).data
#
#     def update(self, instance, validated_data):
#         Book.objects.filter(pk=instance.pk).update(**validated_data)
#         book = Book.objects.get(pk=instance.pk)
#         return BookSerializer(book).data

# 升级序列化器，自动实现上面基础版本，强耦合了，自动创建
# class BookSerializer(serializers.ModelSerializer):
#     date = serializers.DateTimeField(source='pub_date')
#     class Meta:
#         model = Book
#         # fields = '__all__'
#         exclude = ['pub_date']


# class BookView(APIView):
#
#     # 查所有
#     def get(self, request):
#         print(request.user)
#         print(request.query_params)
#         books = Book.objects.all()
#         # 序列化多个对象
#         serializer = BookSerializer(instance=books, many=True)
#         return Response(serializer.data)
#
#     # 增加
#     def post(self, request):
#         # 反序列化
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             result = serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class BookDetailView(APIView):
#     # 查一条
#     def get(self, request, pk):
#         book = Book.objects.get(pk=pk)
#         # 序列化一个对象
#         serializer = BookSerializer(instance=book)
#         if serializer.is_valid():
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     # 更新
#     def put(self, request, pk):
#         book = Book.objects.get(pk=pk)
#         serializer = BookSerializer(instance=book, data=request.data)
#         if serializer.is_valid():
#             # 更新数据
#             # Book.objects.filter(pk=pk).update(**serializer.validated_data)
#             # serializer.instance = Book.objects.get(pk=pk)
#             result = serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     # 删除
#     def delete(self, request, pk):
#         book = Book.objects.get(pk=pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# -------------------------------------------------------------------------基于APIView的接口实现--------------------------1




# -------------------------------------------------------------------基于GenericAPIView的接口实现--------------------------2
# GenericAPIView 提取常用变量，方便增加别的表格接口
# from rest_framework.generics import GenericAPIView

# class BookSerializer(serializers.ModelSerializer):
#     date = serializers.DateTimeField(source='pub_date')
#     class Meta:
#         model = Book
#         # fields = '__all__'
#         exclude = ['pub_date']

# class BookView(GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     # 查所有
#     def get(self, request):
#         # books = self.get_queryset()
#         # # 序列化多个对象
#         # serializer = BookSerializer(instance=books, many=True)
#
#         # serializer = self.get_serializer_class()(instance=self.get_queryset(), many=True)
#
#         serializer = self.get_serializer(instance=self.get_queryset(), many=True)
#         return Response(serializer.data)
#
#     # 增加
#     def post(self, request):
#         # 反序列化
#         # serializer = BookSerializer(data=request.data)
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             result = serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class BookDetailView(GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get(self, request, pk):
#         serializer = self.get_serializer(instance=self.get_object(), many=False)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         serializer = self.get_serializer(instance=self.get_object(), data=request.data)
#         if serializer.is_valid():
#             result = serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         self.get_object().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = '__all__'
# class AuthorView(GenericAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#     def get(self, request):
#         serializer = self.get_serializer(instance=self.get_queryset(), many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             result = serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class AuthorDetailView(GenericAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#     def get(self, request, pk):
#         serializer = self.get_serializer(instance=self.get_object(), many=False)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         serializer = self.get_serializer(instance=self.get_object(), data=request.data)
#         if serializer.is_valid():
#             result = serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         self.get_object().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# -------------------------------------------------------------------基于GenericAPIView的接口实现--------------------------2








# -------------------------------------------------------------------基于MinIn混合类的接口实现-----------------------------3
# 使用MinIn混合类简化上面的接口
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
#
# class BookSerializer(serializers.ModelSerializer):
#     date = serializers.DateTimeField(source='pub_date')
#     class Meta:
#         model = Book
#         # fields = '__all__'
#         exclude = ['pub_date']
#
# class BookView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     # 查所有
#     def get(self, request):
#         return self.list(request)
#
#     # 增加
#     def post(self, request):
#         return self.create(request)
#
#
# class BookDetailView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin, GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get(self, request, pk):
#         return self.retrieve(request, pk)
#
#     def put(self, request, pk):
#         return self.update(request, pk)
#
#     def delete(self, request, pk):
#         return self.destroy(request, pk)
# -------------------------------------------------------------------基于MinIn混合类的接口实现-----------------------------3







# -------------------------------------------------------------------基于MinIn混合类的再封装接口实现------------------------4
# 使用MinIn混合类的再封装继续简化接口
# from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
# from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
#
# class BookSerializer(serializers.ModelSerializer):
#     date = serializers.DateTimeField(source='pub_date')
#     class Meta:
#         model = Book
#         # fields = '__all__'
#         exclude = ['pub_date']
#
# class BookView(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
#
# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = '__all__'
#
# class AuthorView(ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
# class AuthorDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
# -------------------------------------------------------------------基于MinIn混合类的再封装接口实现------------------------4





# -------------------------------------------------------------------基于ViewSet接口实现----------------------------------5
# 使用ViewSet, 合并 带参与不带参请求类
# 重新构建路由分发机制， 可自定义请求def 方法名 如 get 可改为 list或get_all...
'''
            # Bind methods to actions
            # This is the bit that's different to a standard view
            # {'get': 'list', 'post': 'create'}
            for method, action in actions.items():
                handler = getattr(self, action)
                setattr(self, method, handler)
'''
# from rest_framework.viewsets import ViewSet
#
# class BookSerializer(serializers.ModelSerializer):
#     date = serializers.DateTimeField(source='pub_date')
#     class Meta:
#         model = Book
#         # fields = '__all__'
#         exclude = ['pub_date']
#
# class BookView(ViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     # get
#     def list(self, request):
#         return Response("get")
#
#     # post
#     def create(self, request):
#         return self.create(request)
#
#     # get
#     def retrieve(self, request, pk=None):
#         return Response("get")
#
#     # put
#     def update(self, request, pk=None):
#         return self.update(request, pk)
#
#     # delete
#     def destroy(self, request, pk=None):
#         return self.destroy(request, pk)

# -------------------------------------------------------------------基于ViewSet接口实现----------------------------------5






# --------------------------------------------------------------基于ModelViewSet接口实现----------------------------------6
# 使用ModelViewSet, 合并 带参与不带参请求类，更新路由分发机制-> 使用同一个class实现带参与不带参url
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# class BookSerializer(serializers.ModelSerializer):
#     date = serializers.DateTimeField(source='pub_date')
#     class Meta:
#         model = Book
#         # fields = '__all__'
#         exclude = ['pub_date']

# class BookView(GenericViewSet,
#                ListModelMixin,      # 查询所有get
#                CreateModelMixin,    # 添加post
#                RetrieveModelMixin,  # 查询一条get
#                UpdateModelMixin,    # 更新put
#                DestroyModelMixin    # 删除delete
#                ):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# 合并继承类
# class BookView(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
# class PublisherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Publisher
#         fields = '__all__'
#
# class PublisherViewSet(ModelViewSet):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherSerializer
#
# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = '__all__'
#
# class AuthorViewSet(ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
# --------------------------------------------------------------基于ModelViewSet接口实现----------------------------------6






# 升级序列化器，自动实现上面基础版本，强耦合了，自动创建
class BookSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(source='pub_date')
    class Meta:
        model = Book
        # fields = '__all__'
        exclude = ['pub_date']

class BookView(APIView):
    # 认证设置
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    # 权限设置
    permission_classes = (IsAuthenticated,)

    # 查所有
    def get(self, request):
        print(request.user)
        print(request.query_params)
        books = Book.objects.all()
        # 序列化多个对象
        serializer = BookSerializer(instance=books, many=True)
        return Response(serializer.data)

    # 增加
    def post(self, request):
        # 反序列化
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
