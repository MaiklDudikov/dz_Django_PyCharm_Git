from django.shortcuts import render


def favorite_song(request):
    context = {
        'song_line': "We are the champions, my friends",
        'song_title': "Queen, We are the champions"
    }
    return render(request, 'framework_04/song.html', context)


def song_in_language(request, lang):
    translations = {
        'en': "We are the champions, my friends",
        'fr': "Nous sommes les champions, mes amis",
        'de': "Wir sind die Champions, meine Freunde",
        'es': "Somos los campeones, mis amigos",
    }
    song_line = translations.get(lang, translations['en'])
    context = {'song_line': song_line, 'song_title': "Queen, We are the champions"}
    return render(request, 'framework_04/song.html', context)
