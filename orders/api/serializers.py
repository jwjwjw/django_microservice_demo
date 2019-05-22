from rest_framework import serializers

from .models import Order

# TODO: write here your model serializers

class OrderSerializer(serializers.ModelSerializer):

	class Meta:
		model = Order
		fields = "__all__"
