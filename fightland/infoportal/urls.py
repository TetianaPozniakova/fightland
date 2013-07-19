from django.conf.urls.defaults import *
from infoportal.views import *
from infoportal.models import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    (r'^$', main_page),

    (r'^aikido/$', aikido),
    (r'^kudo/$', kudo),
    (r'^arashi_karate/$', arashi_karate),
    (r'^boks/$', boks),
    (r'^enshin_karate/$', enshin_karate),
    (r'^djiudjitsu/$', djiudjitsu),
    (r'^dzyudo/$', dzyudo),
    (r'^kempo/$', kempo),
    (r'^kiokushin/$', kiokushin),
    (r'^kiokushin_karate/$', kiokushin_karate),
    (r'^mma/$', mma),
    (r'^sambo/$', sambo),
    (r'^taiskiy_boks/$', taiskiy_boks),
    (r'^taekvondo/$', taekvondo),
    (r'^ushu_sanda/$', ushu_sanda),
    (r'^shidokan_karate/$', shidokan_karate),

    # Static pages
    (r'^contacts/$', direct_to_template,
        {'template': 'contacts_page.html'}),
    (r'^links/$', direct_to_template,
        {'template': 'links_page.html'}),

    )