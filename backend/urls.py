from django.urls import re_path
import views

urlpatterns = [
	re_path('api/obtainFaceEmotionPrediction', views.obtainFaceEmotionPrediction),
    re_path('api/obtainMilitaryPrediction', views.obtainMilitaryPrediction)

]