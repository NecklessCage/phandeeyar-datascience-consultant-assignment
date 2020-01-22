import re

myan = re.compile(
        r'(?:(?<!္)([\U00010000-\U0010ffffက-ဪဿ၊-၏]|[၀-၉]+|[^က-၏\U00010000-\U0010ffff]+)(?![ှျ]?[့္်]))',
        re.UNICODE)

def syllable_break(text):
    return [syl.strip() for syl in myan.sub(r'𝕊\1', text).strip('𝕊').split('𝕊')]
