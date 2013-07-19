# coding=utf-8

fightlist = {
    "boks" : "",
    "aikido" : "Айкидо",
    "arashi_karate" : "",

    "enshin_karate" : "",
    "djiudjitsu" : "",
    "dzyudo" : "",
    "kempo" : "",
    "kiokushin" : "",
    "kiokushin_karate" : "",
    "kudo" : "Кюдо",
    "mma" : "",
    "sambo" : "",
    "taiskiy_boks" : "",
    "taekvondo" : "",
    "ushu_sanda" : "",
    "shidokan_karate" : "",
}

wiki_renderer = "http://ru.wikipedia.org/w/index.php?action=render&title="

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, RequestContext
from django.shortcuts import render_to_response, get_object_or_404, render
from infoportal.models import *
from easy_news.models import News
from urllib2 import *
from django.utils.encoding import iri_to_uri

def main_page(request):
    return render_to_response('main_page.html', RequestContext(request))

def video_list(request):
    latest_video = Video.objects.all().order_by('-date')
    return render(request, "video_gallery.html", {"latest_video":latest_video})

def getWikiPage(url):
    opener = build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    infile = opener.open(url)
    return infile.read()

def aikido(request):
    if fightlist["aikido"] != "":
        url = wiki_renderer + iri_to_uri(fightlist["aikido"])
    else:
        raise Http404(u'Page is not linked to the Wikipedia article.')
    return render(request, "aikido.html", {"page" : getWikiPage(url)})

def arashi_karate(request):
    if fightlist["arashi_karate"] != "":
        url = wiki_renderer + iri_to_uri(fightlist["arashi_karate"])
    else:
        raise Http404(u'Page is not linked to the Wikipedia article.')
    return render(request, "arashi_karate.html", {"page" : getWikiPage(url)})

def boks(request):
    if fightlist["boks"] != "":
        url = wiki_renderer + iri_to_uri(fightlist["boks"])
    else:
        raise Http404(u'Page is not linked to the Wikipedia article.')
    return render(request, "boks.html", {"page" : getWikiPage(url)})

def enshin_karate(request):
    if fightlist["enshin_karate"] != "":
        url = wiki_renderer + iri_to_uri(fightlist["enshin_karate"])
    else:
        raise Http404(u'Page is not linked to the Wikipedia article.')
    return render(request, "enshin_karate.html", {"page" : getWikiPage(url)})

def djiudjitsu(request):
    if fightlist["djiudjitsu"] != "":
        url = wiki_renderer + iri_to_uri(fightlist["djiudjitsu"])
    else:
        raise Http404(u'Page is not linked to the Wikipedia article.')
    return render(request, "djiudjitsu.html", {"page" : getWikiPage(url)})

def dzyudo(request):
    if fightlist["dzyudo"] != "":
        url = wiki_renderer + iri_to_uri(fightlist["dzyudo"])
    else:
        raise Http404(u'Page is not linked to the Wikipedia article.')
    return render(request, "dzyudo.html", {"page" : getWikiPage(url)})

def kempo(request):
    if fightlist["kempo"] != "":
        url = wiki_renderer + iri_to_uri(fightlist["kempo"])
    else:
        raise Http404(u'Page is not linked to the Wikipedia article.')
    return render(request, "kempo.html", {"page" : getWikiPage(url)})

def kiokushin(request):
    if fightlist["kiokushin"] != "":
        url = wiki_renderer + iri_to_uri(fightlist["kiokushin"])
    else:
        raise Http404(u'Page is not linked to the Wikipedia article.')
    return render(request, "kiokushin.html", {"page" : getWikiPage(url)})

def kudo(request):
    if fightlist["kudo"] != "":
        url = wiki_renderer + iri_to_uri(fightlist["kudo"])
    else:
        raise Http404(u'Page is not linked to the Wikipedia article.')
    return render(request, "kudo.html", {"page" : getWikiPage(url)})

def kiokushin_karate(request):
    if fightlist["kiokushin_karate"] != "":
        url = wiki_renderer + iri_to_uri(fightlist["kiokushin_karate"])
    else:
        raise Http404(u'Page is not linked to the Wikipedia article.')
    return render(request, "kiokushin_karate.html", {"page" : getWikiPage(url)})

def mma(request):
    if fightlist["mma"] != "":
        url = wiki_renderer + iri_to_uri(fightlist["mma"])
    else:
        raise Http404(u'Page is not linked to the Wikipedia article.')
    return render(request, "mma.html", {"page" : getWikiPage(url)})

def sambo(request):
    if fightlist["sambo"] != "":
        url = wiki_renderer + iri_to_uri(fightlist["sambo"])
    else:
        raise Http404(u'Page is not linked to the Wikipedia article.')
    return render(request, "sambo.html", {"page" : getWikiPage(url)})

def taiskiy_boks(request):
    if fightlist["taiskiy_boks"] != "":
        url = wiki_renderer + iri_to_uri(fightlist["taiskiy_boks"])
    else:
        raise Http404(u'Page is not linked to the Wikipedia article.')
    return render(request, "taiskiy_boks.html", {"page" : getWikiPage(url)})

def taekvondo(request):
    if fightlist["taekvondo"] != "":
        url = wiki_renderer + iri_to_uri(fightlist["taekvondo"])
    else:
        raise Http404(u'Page is not linked to the Wikipedia article.')
    return render(request, "taekvondo.html", {"page" : getWikiPage(url)})

def ushu_sanda(request):
    if fightlist["ushu_sanda"] != "":
        url = wiki_renderer + iri_to_uri(fightlist["ushu_sanda"])
    else:
        raise Http404(u'Page is not linked to the Wikipedia article.')
    return render(request, "ushu_sanda.html", {"page" : getWikiPage(url)})

def shidokan_karate(request):
    if fightlist["shidokan_karate"] != "":
        url = wiki_renderer + iri_to_uri(fightlist["shidokan_karate"])
    else:
        raise Http404(u'Page is not linked to the Wikipedia article.')
    return render(request, "shidokan_karate.html", {"page" : getWikiPage(url)})