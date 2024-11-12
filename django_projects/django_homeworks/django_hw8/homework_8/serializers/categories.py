from rest_framework import serializers
from homework_8.models import Category


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


    @staticmethod
    def check_if_category_exists(name):
        if Category.objects.filter(name=name).exists():
            raise serializers.ValidationError(f"Category with name '{name}' already exists")

    def create(self, validated_data):
        self.check_if_category_exists(validated_data['name'])

        return super().create(validated_data)

    def update(self, instance, validated_data):
        self.check_if_category_exists(validated_data['name'])

        return super().update(instance, validated_data)