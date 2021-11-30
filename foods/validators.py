import string
from django.core.exceptions import ValidationError


def contains_special_character(value):

    for text in value:
        if text in string.punctuation:  # punctuation 은 문자열에서 구두점들을 나타낸다
            return True

    return False


class CustomPasswordValidator:
    def validate(self, password, user=None):

        if len(password) < 8 or not contains_special_character(password):
            raise ValidationError("현재 입력한 비밀번호가 8자 이하 이하이거나 특수문자를 포함 하지 않습니다")

    def get_help_text(self):
        return "8자 이상 혹은 특수문자를 포함시켜 주세요."


def valitaion_no_special_characters(value):
    if contains_special_character(value):
        raise ValidationError("특수문자가 포함되어 있습니다. 특수문자를 제외시켜 주세요.")
