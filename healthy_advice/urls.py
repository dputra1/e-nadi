from django.urls import path
from healthy_advice.views import healthy_advice, get_all_comment, delete_comment, edit_comment, detail_article
urlpatterns = [
    path('', healthy_advice, name="healthy-advice"),
    path('get_all_comment', get_all_comment, name='get-all-comment'),
    path('delete/<int:id>', delete_comment, name='delete-comment'),
    path('edit/<int:id>', edit_comment, name='edit-comment'),
    path('details/<int:id>', detail_article, name='detail-article')
]