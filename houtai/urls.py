from django.urls import path
from houtai import views
urlpatterns = [
    #主页信息
    path('index/',views.to_index),
    path('one/',views.to_first),
    path('two/',views.to_seccond),
    path('three/',views.to_third),
    #登录、验证登录、注册模块
    path('tologin/',views.to_login),
    path("checklogin/",views.check_login),
    path("forregister/",views.to_register),#注册
    path("update/", views.update_register),#更新注册用户
    #个人信息管理
    path("showxinxi/", views.show_gerenxinxi),
    path("update_gerenxinxi/", views.update_gerenxinxi),
    path("xiugaimima/", views.to_xiugaimima),
    path("xiugaimima1/", views.to_xiugaimima1),
    path("xiugaimima2/", views.to_xiugaimima2),
    path("check_xiugaimima/", views.check_xiugaimima),
    path("deldenglu/", views.del_denglu),
    #二手房管理
    path("showbypage1/",views.show_all_bypage1),
    path("drop_ajax1/",views.drop_ajax1),
    path("update_ajax1/",views.update_ajax1),
    path("add_update_ajax1/",views.add_update_ajax1),
    #新房管理
    path("showbypage2/",views.show_all_bypage2),
    path("drop_ajax2/",views.drop_ajax2),
    path("update_ajax2/",views.update_ajax2),
    path("add_update_ajax2/",views.add_update_ajax2),
    #租房管理
    path("showbypage3/",views.show_all_bypage3),
    path("drop_ajax3/",views.drop_ajax3),
    path("update_ajax3/",views.update_ajax3),
    path("add_update_ajax3/",views.add_update_ajax3),
    #租赁管理
    path("showzulin/", views.show_zulin),
    path("drop_zulin/", views.drop_zulin),
    path("update_zulin/", views.update_zulin),
    path('zulin/', views.to_zulin),
    path("add_update_zulin/", views.add_update_zulin),
    #售卖管理
    path("showshoumai/", views.show_shoumai),
    path("drop_shoumai/", views.drop_shoumai),
    path("update_shoumai/", views.update_shoumai),
    path('shoumai/', views.to_shoumai),
    path("add_update_shoumai/", views.add_update_shoumai),
    #数据管理
    path("todata/",views.to_data),#展示数据管理页面
    path("bar_ajax/",views.bar_ajax),#传输数据
    # path("bar_ajax1/",views.bar_ajax1)#传输数据
    path("bar_ajax2/",views.bar_ajax2),#传输数据
    path("bar_ajax3/", views.bar_ajax3),  # 传输数据
    path("bar_ajax4/", views.bar_ajax4),  # 传输数据
    path("bar_ajax5/", views.bar_ajax5),  # 传输数据
    path("bar_ajax6/", views.bar_ajax6),  # 传输数据
    #查询
    ##################################
    path("searchxin/",views.search_xin),
    path("searcher/",views.search_er),
    path("searchzu/",views.search_zu),
    ################################
    #map
    path("showmap/",views.to_map)

]

