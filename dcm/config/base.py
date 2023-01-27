import os
import sys
import locale


# 현재 운영 체제
CURRENT_OS = os.getenv('OS')
# 기본 언어 설정
APPLICATION_DEFAULT_LANGUAGE = 'ko_KR'

# 현재 시스템 언어, 인코딩
try:
    locale_language, locale_encoding = locale.getdefaultlocale()
except :
    locale_language = APPLICATION_DEFAULT_LANGUAGE



def _get_locale_language():
    """
    """
    return



def _translate_language(src_lang) -> str:
    """
    # @TODO 언어에 따른 번역 필요.
    @param src_lang:
    @return:
    """

    return ""
