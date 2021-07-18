from rest_framework import serializers
from order_books.models import Book
class bookSerializer(serializers.Serializer):
    class Meta:
        title = serializers.CharField(max_length=200)
        quantity = serializers.IntegerField(default=0)
        price = serializers.IntegerField(default=0)

class bookSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'quantity', 'price')
