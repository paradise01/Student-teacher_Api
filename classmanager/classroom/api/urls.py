from rest_framework.routers import DefaultRouter
from .views import ClassNoticeViewSet, ClassAssignmentViewSet

router = DefaultRouter()
router.register('classNotice', ClassNoticeViewSet)
router.register('classAssignment', ClassAssignmentViewSet)
urlpatterns = router.urls
