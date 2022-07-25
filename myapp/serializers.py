from .models import User, Book, IssuedBook
from rest_framework import serializers
import random
from datetime import date, timedelta


class UserSerializer(serializers.ModelSerializer):

    # For hide the password
    password = serializers.CharField(
        style={'input_type': 'password'},
        min_length=6,
        max_length=68,
        write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password',
                  'first_name', 'last_name', 'phone', 'user_type']

    # password hassing

    def create(self, validated_data):

        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            user_type=validated_data['user_type'],
        )
        user.set_password(validated_data['password'])

        # chars = "abcdefghijklmnop"
        # for i in range(0,8):
        #     password  = random.choice(chars)
        # user.set_password(password),

        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'description', 'price']


class ShowuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name']


class BookviewSerializer(serializers.ModelSerializer):
    author = ShowuserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'description', 'price', 'author']

    # def create(self, validated_data):
    #     book = Book(
    #     name=validated_data['name'],
    #     description=validated_data['description'],
    #     price=validated_data['price'],
    #     )
    #     book.save()
    #     return book


class Books(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'price']


class BookissuedSerializer(serializers.ModelSerializer):
    # student_id = UserSerializer(read_only = True)
    # book = Books(read_only = True)
    class Meta:
        model = IssuedBook
        fields = ['book', 'issued_date', 'expiry_date']


# class IssuedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = IssuedBook
#         fields = ['issued_date', 'student_id']


class IssuedSerializer(serializers.ModelSerializer):

    fine = serializers.SerializerMethodField('get_fine')

    class Meta:
        model = IssuedBook
        fields = ['book', 'issued_date', 'expiry_date', 'fine']

    def get_fine(self, obj):
        print( '______________________________________________________________________', obj.student_id)
        book = IssuedBook.objects.filter(student_id=obj.student_id)
        for i in book:
            print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",i)
        days = (date.today()-i.issued_date)
        d=days.days
        fine=0
        if d > 7:
            day = d - 7
            fine = day * 10
            print("************************************",i.book.price)
            total = int(i.book.price) + fine
            
            return total

        else:
            return fine