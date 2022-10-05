from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from .serializers import BookSerializer

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class BookViewset(viewsets.ModelViewSet):
    serializer_class =BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializer(instance)
        return Response(serializer.data)






def first(request):
    books=Book.objects.all()
    return render(request,'first_temp.html',{'data':books})

class Another(View):
    #book=Book.objects.all()
    #book=Book.objects.filer(is_published=True)
    book=Book.objects.get(id=1)
    s=f'We have {book.title} book \n'

    def get(self,request):
        return HttpResponse(self.s)
