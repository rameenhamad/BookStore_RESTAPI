from rest_framework import serializers
from .models import Book
from datetime import date


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than zero."
            )
        return value
        
    def validate_isbn(self, value):
        if len(value) != 13:
            raise serializers.ValidationError(
                "ISBN must contain exactly 13 digits."
            )
        return value

    def validate_published_date(self, value):
        if value > date.today():
            raise serializers.ValidationError(
                "Published date cannot be in the future."
            )
        return value