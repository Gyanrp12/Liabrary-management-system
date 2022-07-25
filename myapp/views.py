from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookSerializer, UserSerializer, LoginSerializer, BookviewSerializer, BookissuedSerializer,IssuedSerializer
from .models import User, Book, IssuedBook
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .permission import LibrarianPermissions, UserPermissions
from datetime import date,timedelta
import json

# Create your views here.
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            user = User.objects.filter(email=user.email).first()
            serializer = UserSerializer(user)
            data = {
                "token": token,
                "user": serializer.data
            }
            return Response(data)
        else:
            return Response({"msg": "Invalid credentials"})


class BookaddView(APIView):
    serializer_class = BookSerializer

    permission_classes = [LibrarianPermissions]

    def post(self, request):
        try:
            user = User.objects.filter(email=request.user).first()
            # if user.user_type == 'librarian':
            serializer = BookSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            # id = serializer.data.get('author')
            serializer.save(author=request.user)
            return Response(serializer.data)
            # else:
            #     return Response({"msg": "Invalid credentials"})
        except:
            return Response({"msg": "Permission Denied"})


class BookView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        book_id = request.data.get('id')
        if book_id is not None:
            book = Book.objects.get(id=book_id)
            serializer = BookviewSerializer(book)
            return Response(serializer.data)
        book = Book.objects.all()
        serializer = BookviewSerializer(book, many=True)
        return Response(serializer.data)


class BookcrudView(APIView):
    permission_classes = [LibrarianPermissions]

    def put(self, request, pk):
        # # book_id = request.data.get(pk)
        # user = User.objects.filter(email=request.user).first()
        bookdetails = Book.objects.get(id=pk)
        serializer = BookSerializer(
            bookdetails, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "update book"})

    def delete(self, request):
        try:
            book_id = request.data.get('id')
            bookdetails = Book.objects.get(id=book_id)
            bookdetails.delete()
            return Response({"msg": "book deleted"})
        except:
            return Response({"msg": "Book not found"})


class BookissuedView(APIView):
    permission_classes = [UserPermissions]

    def post(self, request):
        serializer = BookissuedSerializer(data=request.data)
        email = request.user
        user = User.objects.get(email=email)
        serializer.is_valid(raise_exception=True)
        serializer.save(student_id=request.user)
        return Response(serializer.data)


class IssuedbookView(APIView):
    permission_classes = [UserPermissions]

    def get(self, request):
        user = User.objects.filter(email=request.user).first()
        print("++++++++++++++++++++++++", user.id)
        details = []
        if user is not None:
             books = IssuedBook.objects.filter(student_id=user.id)
            
            # for i in books:
            #     print("*******************",books)
            #     print("*******************",date.today())
            #     days = (date.today()-i.issued_date)
            #     d=days.days
            #     fine=0
            #     if d > 7:
            #         day = d - 7
            #         fine = day * 10
            #         total = fine + i.book.price
            #         serializer = IssuedSerializer(books,many=True)
            #         return Response({'total':total,"data":serializer.data})
            #     else:
            #         # book = IssuedBook.objects.filter(student_id=user.id)
                    
            #         fine = i.book.price

            #         # for l in book:
            #         i=0
            #         t=(books[i].book,books[i].issued_date,books[i].expiry_date,fine)
            #         # print("================================",t)
            #         list(t)
            #         i=i+1
            #         details.append(t)
            # print("================================",details)
        serializer = IssuedSerializer(books, many=True)
        return Response({"data":serializer.data})
                 
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
            # print("-------------------------",books)
            # days = books.expiry_date - books.issued_date
            # fine = days.days*10
            # if days > 0:
            #     print(fine)
            # else:
            #     print('000000')

            # bo = Book.objects.filter(book=books)
            # print(bo)
            # print("=========================",serializer.data.get('username'))

            # for i in books:

            #     days = datetime.date.today() - i.expiry_date
            #     print("******///////////////",days)
            #     d=days.days

            #     fine=0
            #     if d > 0:
            #         fine = 'Rs'+days.days

            #     print("++++++++++++++++books+++++++++++++++++++",i.book.id)

            #     booklist =list(Book.objects.filter(id=i.book.id))
            #     print("++++++++++++++++ booklist +++++++++++++++++++",booklist)
            #     # print("++++++++++++++++ booklist22 +++++++++++++++++++",booklist[i].price)
            #     i=0
            #     for l in booklist:

            #         # print('__________________l_________________________',l.author)
            #         reponse = Response
            #         t=(l[i].name, l[i].author, l[i].price ,fine)
            #         print("____________________ t _____________",booklist[i].name)
            #         i=i+1
            #         details.append(t)
            #         print("2525252525252525",details)
            #         serializer = IssuedSerializer(details, many=True)
            #         # print("---------------------------",serializer.data)
            #     return Response({"msg":serializer.data})
            # else:
            #     return Response({"msg":"invalid"})




















     # if i.expiry_date < date.today():
                #     print("++++++++++++++++++++++++++++++++++",i.expiry_date)
                #     fine = 0
                #     book = Book.objects.id(id=i.id)
                #     serializer = IssuedSerializer(book)
                #     print("++++++++++++++++",serializer.data)
                #     return Response({'ser':serializer.data,"fine":fine})
                # else:
                #     days = i.expiry_date - date.today()
                #     day = days.days 
                #     total = day * 5
                #     print("++++++++++++++++++++++++++++++++",total)
                #     # print("+++++++++++++++++++++",charge)
                #     # return Response({'charge':total})