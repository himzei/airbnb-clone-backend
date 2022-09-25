from django.utils import timezone
from rest_framework import serializers
from .models import Booking


class CreateRoomBookingSerializer(serializers.ModelSerializer):

    check_in = serializers.DateField()
    check_out = serializers.DateField()

    class Meta:
        model = Booking
        fields = ("check_in", "check_out", "guests")

    def validate_check_in(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("지난 날짜는 체크인 설정이 안됩니다.")
        return value

    def validate_check_out(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("지난 날짜는 체크아웃 설정이 안됩니다.")
        return value

    def validate(self, data):
        if data["check_out"] <= data["check_in"]:
            raise serializers.ValidationError("체크인 날짜는 체크아웃 날짜보다 앞서야 함니다.")
        if Booking.objects.filter(
            check_in__lte=data["check_out"],
            check_out__gte=data["check_in"]
        ).exists():
            raise serializers.ValidationError("해당 날짜에는 이미 예약이 되어 있습니다.")

        return data


class PublicBookingSerializer(serializers.ModelSerializer):

    class Meta:

        model = Booking
        fields = ("pk", "check_in", "check_out", "experience_time", "guests")
