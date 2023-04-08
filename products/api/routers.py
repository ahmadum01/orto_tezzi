from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register("product", views.ProductViewSet, "product")

urls = router.urls
