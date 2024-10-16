from rest_framework import routers

from bunker_game.room.views import RoomViewSet

router = routers.SimpleRouter()
router.register("rooms", RoomViewSet)

urlpatterns = router.urls
