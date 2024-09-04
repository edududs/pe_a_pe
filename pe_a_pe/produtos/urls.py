from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Produto", api.ProdutoViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("produtos/Produto/", views.ProdutoListView.as_view(), name="produtos_Produto_list"),
    path("produtos/Produto/create/", views.ProdutoCreateView.as_view(), name="produtos_Produto_create"),
    path("produtos/Produto/detail/<int:pk>/", views.ProdutoDetailView.as_view(), name="produtos_Produto_detail"),
    path("produtos/Produto/update/<int:pk>/", views.ProdutoUpdateView.as_view(), name="produtos_Produto_update"),
    path("produtos/Produto/delete/<int:pk>/", views.ProdutoDeleteView.as_view(), name="produtos_Produto_delete"),

)
