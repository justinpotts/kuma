from django.conf.urls import url

from . import feeds
from . import views


urlpatterns = [
    url(r'^$',
        views.HomeView.as_view(),
        name='demos'),

    url(r'^devderby/?$',
        views.devderby_landing,
        name='demos_devderby_landing'),
    url(r'^devderby/(?P<year>\d\d\d\d)/(?P<month>[\w]+)/?$',
        views.DevDerbyByDate.as_view(),
        name='demos_devderby_by_date'),
    url(r'^devderby/tag/(?P<tag>[^/]+)/?$',
        views.DevDerbyTagView.as_view(),
        name='demos_devderby_tag'),

    url(r'^terms',
        views.terms,
        name='demos_terms'),

    url(r'^submit',
        views.submit,
        name='demos_submit'),

    url(r'^detail/(?P<slug>[^/]+)/?$',
        views.detail,
        name='demos_detail'),
    url(r'^detail/(?P<slug>[^/]+)/like$',
        views.like,
        name='demos_like'),
    url(r'^detail/(?P<slug>[^/]+)/unlike$',
        views.unlike,
        name='demos_unlike'),
    url(r'^detail/(?P<slug>[^/]+)/flag$',
        views.flag,
        name='demos_flag'),
    url(r'^detail/(?P<slug>[^/]+)/download$',
        views.download,
        name='demos_download'),
    url(r'^detail/(?P<slug>[^/]+)/launch$',
        views.launch,
        name='demos_launch'),
    url(r'^detail/(?P<slug>[^/]+)/edit$',
        views.edit,
        name='demos_edit'),
    url(r'^detail/(?P<slug>[^/]+)/delete$',
        views.delete,
        name='demos_delete'),
    url(r'^detail/(?P<slug>[^/]+)/hide$',
        views.hideshow,
        {'hide': True},
        name='demos_hide'),
    url(r'^detail/(?P<slug>[^/]+)/show$',
        views.hideshow,
        {'hide': False},
        name='demos_show'),

    url(r'^search/?$',
        views.SearchView.as_view(),
        name="demos_search"),
    url(r'^all/?$',
        views.AllView.as_view(),
        name='demos_all'),
    url(r'^tag/(?P<tag>[^/]+)/?$',
        views.TagView.as_view(),
        name='demos_tag'),
    url(r'^profile/(?P<username>[^/]+)/?$',
        views.profile_detail,
        name="demos_profile_detail"),

    url(r'feeds/(?P<format>[^/]+)/all/',
        feeds.RecentSubmissionsFeed(),
        name="demos_feed_recent"),
    url(r'feeds/(?P<format>[^/]+)/featured/',
        feeds.FeaturedSubmissionsFeed(),
        name="demos_feed_featured"),
    url(r'feeds/(?P<format>[^/]+)/search/?$',
        feeds.SearchSubmissionsFeed(),
        name="demos_feed_search"),
    url(r'feeds/(?P<format>[^/]+)/tag/(?P<tag>[^/]+)/?$',
        feeds.TagSubmissionsFeed(),
        name="demos_feed_tag"),
    url(r'feeds/(?P<format>[^/]+)/profile/(?P<username>[^/]+)/?$',
        feeds.ProfileSubmissionsFeed(),
        name="demos_feed_profile"),

]
