from django.conf.urls.defaults import *

urlpatterns = patterns('bookstore.views',
    (r'^$', 'storefront'),
    (r'^readme$', 'readme'),    # use to preview readme.md
    (r'^robots.txt$', 'robots'),
    (r'^site/news/', 'site_news'),
    (r'^site/picks/', 'site_picks'),
    (r'^author/$', 'author_list'),
    (r'^author/(?P<author_link>[\w-]+)$', 'author_detail'),
    (r'^book/$', 'book_list'),
    (r'^book/(?P<book_link>[\w-]+)$', 'book_detail'),
    (r'^book/(?P<migrate_url>[^/]+)/(?P<book_link>[\w-]+)$', 'book_detail'), # migrate old urls
    (r'^coming-soon/$', 'coming_soon'),
    url(r'^signin/$', 'openid_login', name='openid-login'),
    url(r'^signin/complete/$', 'openid_complete', name='openid-complete'),
    (r'^signin/$', 'signin'),
    (r'^signout/$', 'signout'),
    (r'^purchase/book/(?P<pub_id>[^/]+)$', 'purchase_book'),
    (r'^download/book/(?P<pub_id>[^/]+)$', 'download_book'),
    (r'^download/review/(?P<key>[^/]+)/(?P<purchase_id>[^/]+)$', 'download_review'),
    (r'^download/$', 'download_pub'),
    (r'^user/(?P<user_id>[^/]*)$', 'user_detail'),
    (r'^user/purchases/$', 'purchase_listing'),
    (r'^user/purchases/(?P<purchase_id>[^/]+)/$', 'purchase_detail'),
    (r'^genre/$', 'genre_list'),
    (r'^genre/(?P<genre_link>[\w-]+)$', 'genre_detail'),
    (r'^paypal/ipn$', 'paypal_ipn'),
    (r'^staff/books/$', 'staff_allbooks'),
    (r'^staff/purchase/$', 'staff_purchase'),
    (r'^staff/purchase/(?P<purchase_id>[^/]+)/$', 'staff_purchase_detail'),
    (r'^staff/review/$', 'staff_review'),
    (r'^sitemap.xml$', 'sitemap'),
    (r'^(?P<migrate_url>page/)(?P<page_link>[\w-]+)$', 'site_page'),
    (r'^(?P<page_link>[\w-]+)$', 'site_page'),
)

from settings import DEBUG
if DEBUG:
    urlpatterns += patterns('bookstore.views',
        (r'^403/$', 'page_access_denied'),
        (r'^404/$', 'page_not_found'),
        (r'^500/$', 'page_server_error'),
    )