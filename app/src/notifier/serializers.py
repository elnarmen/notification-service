from rest_framework import serializers
from django.utils import timezone
from .models import Client, Mailing, Message


class ClientSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()  # noqa A003

    class Meta:
        model = Client
        fields = ['id', 'phone_number', 'operator_code', 'tag', 'timezone']


class MessageSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()  # noqa A003
    client = ClientSerializer()

    class Meta:
        model = Message
        fields = ['dispatch_at', 'status', 'mailing', 'client']


class MailingSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()  # noqa A003

    class Meta:
        model = Mailing
        fields = [
            'id',
            'content',
            'start_at',
            'end_at',
            'operator_code',
            'client_tag',
        ]

    def to_representation(self, instance):
        if self.context.get('include_messages', False):
            self.fields['messages'] = MessageSerializer(many=True, read_only=True)
        return super().to_representation(instance)

    def validate(self, data):
        if data['start_at'] >= data['end_at']:
            raise serializers.ValidationError(
                'Время начала рассылки должно быть позже её окончания.',
            )
        if data['end_at'] <= timezone.now():
            raise serializers.ValidationError('Время окончания рассылки уже прошло.')
        return super().validate(data)
