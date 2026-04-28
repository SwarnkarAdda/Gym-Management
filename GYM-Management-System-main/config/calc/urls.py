from django.urls import path

from . import views

urlpatterns = [
    path("",views.login,name='login'),
    
    path('home/',views.Home,name="home"),

    path('NewMember/',views.NewMember,name="newMember"),

    path('NewTrainer/',views.NewTrainer,name="newTrainer"),

    path('MemberList/',views.MemberList,name="memberList"),

    path('TrainerList/',views.TrainerList,name="trainerList"),

    path('SearchedMem/',views.SearchedMem,name="searchedMem"),

    path('SearchedTra/',views.SearchedTra,name="searchedTra"),

    path('deleteMember/<int:id>/', views.delete_member, name='deleteMember'),

    path('deleteTrainer/<int:id>/', views.delete_trainer, name='deleteTrainer'),

    path('updateMember/<int:id>/', views.update_member, name='updateMember'),

    path('updateTrainer/<int:id>/', views.update_trainer, name='updateTrainer'),

    path('Successful/',views.Successful,name="successful"),

    path('Error/',views.Error,name="error"),

    path('about/',views.About,name="about"),

    path('contact/',views.Contact,name="contact"),
]
