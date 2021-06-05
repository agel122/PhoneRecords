from django.urls import path
from .views import (
    PhoneBookListView,
    PhoneBookDetailView,
    PhoneBookCreateView,
    PhoneBookUpdateView,
    PhoneBookDeleteView,
    PhoneBookListViewSel,
    select_group,
)

urlpatterns = [
    path('', PhoneBookListView.as_view(), name='records_list'),
    path('records/<int:pk>/', PhoneBookDetailView.as_view(), name='records_detail'),
    path('records/new/', PhoneBookCreateView.as_view(), name='records_new'),
    path('records/<int:pk>/edit/', PhoneBookUpdateView.as_view(), name='records_edit'),
    path('records/<int:pk>/delete/', PhoneBookDeleteView.as_view(), name='records_delete'),
    path('records/select/', select_group, name='records_select'),
    path('records/groupselect', PhoneBookListViewSel.as_view(), name='selected_group'),
]
