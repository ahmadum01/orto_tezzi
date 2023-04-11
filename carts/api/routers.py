from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register("cart", views.PurchaseViewSet, "cart")

urls = router.urls
