from django.core.exceptions import ValidationError


def validate_numbers(value):

    if value.isdigit():
        raise ValidationError("숫자만 입력하지 말아주세요! 조금이라도 오늘의 기분을 써보아요!", code="number_error")
