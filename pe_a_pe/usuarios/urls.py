from django.urls import path, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register("adress", api.AdressViewSet)
router.register("measurements", api.MeasurementsViewSet)
router.register("usuario", api.UsuarioViewSet)

urlpatterns = (
    path("", include(router.urls)),
    path(
        "usuarios/adress/", views.AdressListView.as_view(), name="usuarios_adress_list"
    ),
    path(
        "usuarios/adress/create/",
        views.AdressCreateView.as_view(),
        name="usuarios_adress_create",
    ),
    path(
        "usuarios/adress/detail/<int:pk>/",
        views.AdressDetailView.as_view(),
        name="usuarios_adress_detail",
    ),
    path(
        "usuarios/adress/update/<int:pk>/",
        views.AdressUpdateView.as_view(),
        name="usuarios_adress_update",
    ),
    path(
        "usuarios/adress/delete/<int:pk>/",
        views.AdressDeleteView.as_view(),
        name="usuarios_adress_delete",
    ),
    path(
        "usuarios/measurements/",
        views.MeasurementsListView.as_view(),
        name="usuarios_measurements_list",
    ),
    path(
        "usuarios/measurements/create/",
        views.MeasurementsCreateView.as_view(),
        name="usuarios_measurements_create",
    ),
    path(
        "usuarios/measurements/detail/<int:pk>/",
        views.MeasurementsDetailView.as_view(),
        name="usuarios_measurements_detail",
    ),
    path(
        "usuarios/measurements/update/<int:pk>/",
        views.MeasurementsUpdateView.as_view(),
        name="usuarios_measurements_update",
    ),
    path(
        "usuarios/measurements/delete/<int:pk>/",
        views.MeasurementsDeleteView.as_view(),
        name="usuarios_measurements_delete",
    ),
    path(
        "usuarios/usuario/",
        views.UsuarioListView.as_view(),
        name="usuarios_usuario_list",
    ),
    path(
        "usuarios/usuario/create/",
        views.UsuarioCreateView.as_view(),
        name="usuarios_usuario_create",
    ),
    path(
        "usuarios/usuario/detail/<int:pk>/",
        views.UsuarioDetailView.as_view(),
        name="usuarios_usuario_detail",
    ),
    path(
        "usuarios/usuario/update/<int:pk>/",
        views.UsuarioUpdateView.as_view(),
        name="usuarios_usuario_update",
    ),
    path(
        "usuarios/usuario/delete/<int:pk>/",
        views.UsuarioDeleteView.as_view(),
        name="usuarios_usuario_delete",
    ),
)
