import string
from django.core.exceptions import ValidationError


def contains_special_character(value):

    for text in value:
        if text in string.punctuation:  # punctuation 은 문자열에서 구두점들을 나타낸다
            return True

    return False


def valitaion_no_special_characters(value):
    if contains_special_character(value):
        raise ValidationError("특수문자가 포함되어 있습니다. 특수문자를 제외시켜 주세요.")
