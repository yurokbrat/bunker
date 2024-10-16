from rest_framework.routers import SimpleRouter

from bunker_game.users.views import UserViewSet

app_name = "users"

router = SimpleRouter()

router.register("users", UserViewSet)

urlpatterns = router.urls
