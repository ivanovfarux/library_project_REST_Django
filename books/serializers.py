from jsonschema import ValidationError
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        # title faqat alfavitdan tashkil topgani haqida
        if title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitobni sarlavhasi harflardan iborat bo'lishi kerak!"
                }
            )
        # title va author DB da bor yo'qligini tekshiradi
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitob sarlavhasi va muallifi bir xil bo'lgan kitobni yuklay olmaysiz!"
                }
            )
        return data

    def validate_price(self, price):
        if price < 0 or price > 999999:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Narx noto'gri kiritilgan!"
                }
            )
        return price