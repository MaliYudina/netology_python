import requests

LANG_OUT = 'ru'
KEY = 'XXXXXXXXXXXXXXXX'
LANGS = {
    'de': 'assets/DE.txt',
    'es': 'assets/ES.txt',
    'fr': 'assets/FR.txt',
}


def translate_it(text, lang_in, lang_out):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    params = {
        'key': KEY,
        'lang': '{}-{}'.format(lang_in, lang_out),
        'text': text,
    }
    response = requests.get(url, params=params)
    # print(response.status_code)
    return ' '.join(response.json().get('text', []))


def write_results(file_in, file_out, lang_in, lang_out):
    with open(file_in) as in_file, open(file_out, 'w') as out_file:
        result = translate_it(in_file.read(), lang_in, lang_out)
        out_file.write(result)


def main():
    for lang, file_path in LANGS.items():
        write_results(
            file_in=file_path,
            file_out='{}-{}.txt'.format(lang, LANG_OUT),
            lang_in=lang,
            lang_out=LANG_OUT,
        )


if __name__ == '__main__':
    main()