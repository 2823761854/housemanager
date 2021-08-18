from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from houtai.models import ershoufang, newfang, zufang, User, zulin, shoumai, Denglu
from django.db.models import Q


# Create your views here.
# 登录
def to_login(request):
    return render(request, 'login.html')


# 检查登录信息
def check_login(request):
    if request.method == 'POST':
        name = request.POST.get("username")
        pwd = request.POST.get("password")
        rs = User.objects.filter(username=name).filter(password=pwd)
        if rs.exists():
            # 登录成功
            re = Denglu()
            re.id = '1'
            re.username = name
            re.password = pwd
            re.save()
            return HttpResponseRedirect('/houtai/index/')
        else:
            return HttpResponseRedirect('/houtai/tologin/')


# 注册页面
def to_register(request):
    return render(request, 'register.html')


# 主页跳转
def to_index(request):
    return render(request, 'index.html')


# 二手房信息管理页面
def to_first(request):
    return render(request, 'ershoufang.html')


# 新房楼盘管理页面
def to_seccond(request):
    return render(request, 'xinfang.html')


# 租房管理页面
def to_third(request):
    return render(request, 'zufang.html')


#############################
# 注册管理
def update_register(request):
    if request.method == 'POST':
        re = User()
        re.username = request.POST.get('username')
        re.password = request.POST.get('password')
        re.save()
        return render(request, 'denglu.html')


#############################
# 个人信息管理
# 修改密码页面
def to_xiugaimima(request):
    return render(request, 'xiugaimima.html')


# 输入原始密码错误
def to_xiugaimima1(request):
    return render(request, 'xiugaimima1.html')


# 输入正确
def to_xiugaimima2(request):
    return render(request, 'xiugaimima2.html')


def show_gerenxinxi(request):
    rs = Denglu.objects.get(id='1')
    stu = User.objects.get(username=rs.username)
    data = {
        "stu": stu
    }
    return render(request, 'gerenxinxi.html', context=data)


#    path("update_gerenxinxi/", views.update_gerenxinxi),

def update_gerenxinxi(request):
    if request.method == 'POST':
        rs = Denglu.objects.get(id='1')
        stu = User.objects.get(username=rs.username)  # 登录名id
        stu.name = request.POST.get('name')  # 用户名
        stu.gender = request.POST.get('gender')
        stu.minzu = request.POST.get('minzu')
        stu.age = request.POST.get('age')
        stu.phone = request.POST.get('phone')
        stu.address = request.POST.get('address')
        stu.save()
        data = {
            "stu": stu
        }
    return render(request, 'gerenxinxi.html', context=data)


# 检查修改密码信息
def check_xiugaimima(request):
    if request.method == 'POST':
        pwd = request.POST.get("password")  # 原密码
        pwd2 = request.POST.get("password2")  # 新密码
        rs = Denglu.objects.filter(password=pwd)
        rs1 = User.objects.filter(password=pwd)
        if rs.exists():
            rs.update(password=pwd2)
            rs1.update(password=pwd2)
            return HttpResponseRedirect('/houtai/xiugaimima2/')
        else:
            return HttpResponseRedirect('/houtai/xiugaimima1/')


# 删除登录记录
def del_denglu(request):
    s = Denglu.objects.all()
    s.delete()
    return HttpResponseRedirect('/houtai/tologin/')


########################################
# 二手管理系统
# show展示所有信息
def show_all_bypage1(request):
    ershous = ershoufang.objects.all()
    lis = []
    # print(ershous)
    for ershou in ershous:
        data = dict()
        data['id'] = ershou.id
        data['title'] = ershou.title
        data['img'] = ershou.img
        data['info1'] = ershou.houseInfo1
        data['info2'] = ershou.houseInfo2
        data['info3'] = ershou.houseInfo3
        data['location'] = ershou.position1 + " " + ershou.position2 + " " + ershou.position3
        data['totalprice'] = ershou.totalPrice
        data['unitprice'] = ershou.unitPrice
        lis.append(data)
    # print(lis)
    page_index = request.GET.get('page')
    # 前台传来的一页显示多少条数据
    page_limit = request.GET.get('limit')
    # 分页器进行分配
    paginator = Paginator(lis, page_limit)
    # 前端传来页数的数据
    data = paginator.page(page_index)
    # 放在一个列表里：data列表
    ershou_info = [x for x in data]
    # students.count()总数据量，layui的table模块要接受的格式
    ershoufangs = {"code": 0, "msg": "", "count": ershous.count(), "data": ershou_info}
    return JsonResponse(ershoufangs)


# 二手房==》编辑
def update_ajax1(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        ershou = ershoufang.objects.get(pk=id)
        ershou.title = request.POST.get('title')
        ershou.houseInfo = request.POST.get('info')
        ershou.position1 = request.POST.get('location').split(" ")[0]
        ershou.position2 = request.POST.get('location').split(" ")[1]
        ershou.position3 = request.POST.get('location').split(" ")[2]
        ershou.img = ershou.img
        ershou.totalPrice = request.POST.get('totalprice')
        ershou.unitPrice = request.POST.get('unitprice')
    ershou.save()
    data = {
        'msg': "更新success！！！"
    }
    return JsonResponse(data)


# 二手房==》添加
def add_update_ajax1(request):
    if request.method == 'POST':
        ershou = ershoufang()
        ershou.title = request.POST.get('title')
        ershou.houseInfo = request.POST.get('info')
        ershou.position1 = request.POST.get('location').split(" ")[0]
        ershou.position2 = request.POST.get('location').split(" ")[1]
        ershou.totalPrice = request.POST.get('totalprice')
        ershou.unitPrice = request.POST.get('unitprice')
    ershou.save()
    data = {
        'msg': "添加success！！！"
    }
    return JsonResponse(data)


# 二手房==》删除
def drop_ajax1(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        ershou = ershoufang.objects.get(pk=id)
        ershou.delete()
        data = {
            'msg': "删除success！！！"
        }
        return JsonResponse(data)


# 新房信息管理
# 展示所有信息
def show_all_bypage2(request):
    xins = newfang.objects.all()
    lis = []
    # print(ershous)
    for xin in xins:
        data = dict()
        data['id'] = xin.id
        data['name'] = xin.name
        data['info'] = xin.houseinfo
        # data['img'] = xin.img
        data['location'] = xin.position1 + " " + xin.position2 + " " + xin.position3
        data['totalprice'] = xin.totalPrice
        data['unitprice'] = xin.unitPrice
        lis.append(data)
    # print(lis)
    page_index = request.GET.get('page')
    # 前台传来的一页显示多少条数据
    page_limit = request.GET.get('limit')
    # 分页器进行分配
    paginator = Paginator(lis, page_limit)
    # 前端传来页数的数据
    data = paginator.page(page_index)
    # 放在一个列表里：data列表
    xinfang_info = [x for x in data]
    # students.count()总数据量，layui的table模块要接受的格式
    xinfangs = {"code": 0, "msg": "", "count": xins.count(), "data": xinfang_info}
    return JsonResponse(xinfangs)


# 新房==》更新
def update_ajax2(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        xin = newfang.objects.get(pk=id)
        xin.name = request.POST.get('name')
        xin.houseinfo = request.POST.get('info')
        xin.position1 = request.POST.get('location').split(" ")[0]
        xin.position2 = request.POST.get('location').split(" ")[1]
        xin.position3 = request.POST.get('location').split(" ")[2]
        xin.totalPrice = request.POST.get('totalprice')
        xin.unitPrice = request.POST.get('unitprice')
    xin.save()
    data = {
        'msg': "更新success！！！"
    }
    return JsonResponse(data)


# 新房==》添加
def add_update_ajax2(request):
    if request.method == 'POST':
        xin = newfang()
        xin.name = request.POST.get('name')
        xin.houseinfo = request.POST.get('info')
        xin.position1 = request.POST.get('location').split(" ")[0]
        xin.position2 = request.POST.get('location').split(" ")[1]
        xin.position3 = request.POST.get('location').split(" ")[2]
        xin.totalPrice = request.POST.get('totalprice')
        xin.unitPrice = request.POST.get('unitprice')
    xin.save()
    data = {
        'msg': "添加success！！！"
    }
    return JsonResponse(data)


# 新房==》删除
def drop_ajax2(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        xin = newfang.objects.get(pk=id)
        xin.delete()
        data = {
            'msg': "删除success！！！"
        }
        return JsonResponse(data)


# 租房信息管理
# 展示所有信息
def show_all_bypage3(request):
    zus = zufang.objects.all()
    lis = []
    # print(ershous)
    for zu in zus:
        data = dict()
        data['id'] = zu.id
        data['title'] = zu.title
        data['size_room'] = zu.size_room
        data['area_room'] = zu.area_room
        data['num_room'] = zu.num_room
        data['location'] = zu.position1 + " " + zu.position2 + " " + zu.position3
        data['totalprice'] = zu.totalPrice
        lis.append(data)
    # print(lis)
    page_index = request.GET.get('page')
    # 前台传来的一页显示多少条数据
    page_limit = request.GET.get('limit')
    # 分页器进行分配
    paginator = Paginator(lis, page_limit)
    # 前端传来页数的数据
    data = paginator.page(page_index)
    # 放在一个列表里：data列表
    zufang_info = [x for x in data]
    # students.count()总数据量，layui的table模块要接受的格式
    zufangs = {"code": 0, "msg": "", "count": zus.count(), "data": zufang_info}
    return JsonResponse(zufangs)


# 租房==》更新
def update_ajax3(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        zu = zufang.objects.get(pk=id)
        zu.title = request.POST.get('title')
        zu.position1 = request.POST.get('location').split(" ")[0]
        zu.position2 = request.POST.get('location').split(" ")[1]
        zu.position3 = request.POST.get('location').split(" ")[2]
        zu.totalPrice = request.POST.get('totalprice')
        zu.size_room = request.POST.get('size_room')
        zu.area_room = request.POST.get('area_room')
        zu.num_room = request.POST.get('num_room')
        print(zu)
    zu.save()
    data = {
        'msg': "更新success！！！"
    }
    return JsonResponse(data)


# 租房===》添加
def add_update_ajax3(request):
    if request.method == 'POST':
        zu = zufang()
        zu.title = request.POST.get('title')
        zu.position1 = request.POST.get('location').split(" ")[0]
        zu.position2 = request.POST.get('location').split(" ")[1]
        zu.position3 = request.POST.get('location').split(" ")[2]
        zu.totalPrice = request.POST.get('totalprice')
        zu.size_room = request.POST.get('size_room')
        zu.area_room = request.POST.get('area_room')
        zu.num_room = request.POST.get('num_room')
        print(zu)
    zu.save()
    data = {
        'msg': "添加success！！！"
    }
    return JsonResponse(data)


# 租房==》删除
def drop_ajax3(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        zu = zufang.objects.get(pk=id)
        zu.delete()
        data = {
            'msg': "删除success！！！"
        }
        return JsonResponse(data)


###################################
# 数据可视化
def to_data(request):
    return render(request, 'showdata.html')


# 武汉市各区租房均价==》柱状图
def bar_ajax(request):
    zus = zufang.objects.all()  # 得到所有zufang信息
    area = ['黄陂', '洪山', '武昌', '江岸', '江汉', '汉阳',
            '硚口', '蔡甸', '东西湖', '东湖高新', '沌口开发区', '青山', '江夏', '新洲']
    price_dict = {}.fromkeys(area)
    num_dict = {}.fromkeys(area)
    for i in price_dict:
        price_dict[i] = 0
        num_dict[i] = 0

    for zu in zus:
        for a in area:
            if zu.position1 == a:
                price_dict[a] += zu.totalPrice
                num_dict[a] += 1
    for p in price_dict:
        if num_dict[p]!=0:
            price_dict[p] = price_dict[p] / num_dict[p]

    data = {
        'x': area,
        'y': [i for i in price_dict.values()]
    }
    # print(data['x'])
    # print(data['y'])
    # print(num_dict)
    return JsonResponse(data)



def bar_ajax2(request):
    xins = newfang.objects.all()  # 得到所有xinfang信息
    ershous = ershoufang.objects.all()  # 得到所有ershoufang信息
    area1 = ['黄陂', '洪山', '武昌', '江岸', '江汉', '汉阳', '硚口',
             '蔡甸', '东西湖', '东湖高新', '沌口开发区', '青山', '江夏', '新洲', '汉南']
    xin_dict1 = {}.fromkeys(area1)
    ershou_dict1 = {}.fromkeys(area1)
    num_dict1 = {}.fromkeys(area1)
    num_dict2 = {}.fromkeys(area1)
    # 初始化各区新房单价字典
    for i in xin_dict1:
        xin_dict1[i] = 0
        num_dict1[i] = 0

    # 初始化各区二手房单价字典
    for j in ershou_dict1:
        ershou_dict1[j] = 0
        num_dict2[j] = 0

    # 获取各区新房单价
    for xin in xins:
        for a in area1:
            if xin.position1 == a:
                if xin.unitPrice != "价格待定":
                    xin_dict1[a] += float(xin.unitPrice)
                    num_dict1[a] += 1
    # for p in xin_dict1:
    #     xin_dict1[p] = xin_dict1[p] / num_dict1[p]

    # 获取各区二手房单价
    for ershou in ershous:
        for a in area1:
            if ershou.position3 == a:
                ershou_dict1[a] += float(ershou.unitPrice)
                num_dict2[a] += 1
    for p, p1 in zip(xin_dict1, ershou_dict1):
        if num_dict1[p]!=0:
            xin_dict1[p] = xin_dict1[p] / num_dict1[p]
        if num_dict2[p1]!=0:
            ershou_dict1[p1] = ershou_dict1[p1] / num_dict2[p1]

    data = {
        'x': area1,
        'y1': [i for i in xin_dict1.values()],
        'y2': [j for j in ershou_dict1.values()]
    }

    return JsonResponse(data)


# 武汉市新房单价统计==》柱状图
def bar_ajax3(request):
    xins = newfang.objects.all()  # 得到所有xinfang信息
    area1 = ['黄陂', '洪山', '武昌', '江岸', '江汉', '汉阳', '硚口',
             '蔡甸', '东西湖', '东湖高新', '沌口开发区', '青山', '江夏', '新洲', '汉南']
    xin_dict1 = {}.fromkeys(area1)
    num_dict1 = {}.fromkeys(area1)
    # 初始化各区新房单价字典
    for i in xin_dict1:
        xin_dict1[i] = 0
        num_dict1[i] = 0
    # 获取各区新房单价
    for xin in xins:
        for a in area1:
            if xin.position1 == a:
                if xin.unitPrice != "价格待定":
                    xin_dict1[a] += float(xin.unitPrice)
                    num_dict1[a] += 1

    for p in xin_dict1:
        if num_dict1[p]!=0:
            xin_dict1[p] = xin_dict1[p] / num_dict1[p]

    data = {
        'x': area1,
        'y': [i for i in xin_dict1.values()]
    }
    # print(num_dict)
    return JsonResponse(data)

# 武汉市各区租房均价==》柱状图
def bar_ajax4(request):
    zus = newfang.objects.all()  #
    price_area = ['5k以下', '5k-10k', '10k-15k', '15k-20k', '20k-25k', '25k-30k', '30k以上']
    num = [0] * 7
    for zu in zus:
        if zu.unitPrice != "价格待定":
            tmp = int(zu.unitPrice)
            if tmp < 5000:
                num[0] += 1
            elif tmp < 10000:
                num[1] += 1
            elif tmp < 15000:
                num[2] += 1
            elif tmp < 20000:
                num[3] += 1
            elif tmp < 25000:
                num[4] += 1
            elif tmp < 30000:
                num[5] += 1
            else:
                num[6] += 1

    x = []
    for each in price_area:
        x.append(each)
    # print(list_temp)
    # print(len(list_temp))
    y = []
    for each in num:
        y.append(each)


    data = dict(zip(x,y))
    print(data)

    return JsonResponse(data)



#武汉市新房二手房售价对比
def bar_ajax5(request):
    xins = newfang.objects.all()  # 得到所有xinfang信息
    ershous = ershoufang.objects.all()#得到所有ershoufang信息
    area1 = ['黄陂', '洪山', '武昌', '江岸', '江汉', '汉阳','硚口',
             '蔡甸', '东西湖', '东湖高新', '沌口开发区', '青山', '江夏', '新洲', '汉南']
    xin_dict1 = {}.fromkeys(area1)
    ershou_dict1 = {}.fromkeys(area1)
    num_dict1 = {}.fromkeys(area1)
    num_dict2 = {}.fromkeys(area1)
    #初始化各区新房单价字典
    for i in xin_dict1:
        xin_dict1[i] = 0
        num_dict1[i] = 0

    #初始化各区二手房单价字典
    for j in ershou_dict1:
        ershou_dict1[j] = 0
        num_dict2[j] = 0

    #获取各区新房单价
    for xin in xins:
        for a in area1:
            if xin.position1 == a:
                if xin.unitPrice != "价格待定":
                    xin_dict1[a] += float(xin.unitPrice)
                    num_dict1[a] += 1

    #获取各区二手房单价
    for ershou in ershous:
        for a in area1:
            if ershou.position3 == a:
                ershou_dict1[a] += float(ershou.unitPrice)
                num_dict2[a] += 1

    for p,p1 in zip(xin_dict1,ershou_dict1):
        if num_dict1[p] != 0:
            xin_dict1[p] = int(xin_dict1[p] / num_dict1[p])
        if num_dict2[p1] != 0:
            ershou_dict1[p1] = int(ershou_dict1[p1] /num_dict2[p1])

    data = {
        'x': area1,
        'y1': [i for i in xin_dict1.values()],
        'y2': [j for j in ershou_dict1.values()]
    }
    # print(num_dict)
    return JsonResponse(data)


def bar_ajax6(request):
    xins = newfang.objects.all()  # 得到所有xinfang信息
    ershous = ershoufang.objects.all()#得到所有ershoufang信息
    zus = zufang.objects.all()  # 得到所有ershoufang信息
    area1 = ['黄陂', '洪山', '武昌', '江岸', '江汉', '汉阳','硚口',
             '蔡甸', '东西湖', '东湖高新', '沌口开发区', '青山', '江夏', '新洲', '汉南']

    xin_dict1 = {}.fromkeys(area1)
    ershou_dict1 = {}.fromkeys(area1)
    zu_dict1 = {}.fromkeys(area1)

    num_dict1 = {}.fromkeys(area1)
    num_dict2 = {}.fromkeys(area1)
    num_dict3 = {}.fromkeys(area1)
    #初始化各区新房单价字典
    for i in xin_dict1:
        xin_dict1[i] = 0
        num_dict1[i] = 0

    #初始化各区二手房单价字典
    for j in ershou_dict1:
        ershou_dict1[j] = 0
        num_dict2[j] = 0

    #初始化各区二手房单价字典
    for k in zu_dict1:
        zu_dict1[k] = 0
        num_dict3[k] = 0

    #获取各区新房单价
    for xin in xins:
        for a in area1:
            if xin.position1 == a:
                num_dict1[a] += 1


    #获取各区二手房单价
    for ershou in ershous:
        for a in area1:
            if ershou.position3 == a:
                num_dict2[a] += 1

    #获取各区二手房单价
    for zu in zus:
        for a in area1:
            if zu.position1 == a:
                num_dict3[a] += 1

    data = {
        'x': area1,
        'y1': [i for i in num_dict1.values()],
        'y2': [j for j in num_dict2.values()],
        'y3': [k for k in num_dict3.values()]
    }
    # print(num_dict)
    return JsonResponse(data)

########################################
# 租赁管理==求租管理
def to_zulin(request):
    return render(request, 'zulin.html')


def show_zulin(request):
    zulins = zulin.objects.all()
    lis = []

    for zl in zulins:
        data = dict()
        data['id'] = zl.id
        data['title'] = zl.title
        data['type'] = zl.type
        data['size_room'] = zl.size_room
        data['area_room'] = zl.area_room
        data['num_room'] = zl.num_room
        data['location'] = zl.position1
        # data['location'] = zl.position1+ " " + zl.position2+ " " + zl.position3
        data['totalPrice'] = zl.totalPrice
        lis.append(data)
    # print(lis)
    page_index = request.GET.get('page')
    # 前台传来的一页显示多少条数据
    page_limit = request.GET.get('limit')
    # 分页器进行分配
    paginator = Paginator(lis, page_limit)
    # 前端传来页数的数据
    data = paginator.page(page_index)
    # 放在一个列表里：data列表
    zulin_info = [x for x in data]
    # students.count()总数据量，layui的table模块要接受的格式
    zulinxinxi = {"code": 0, "msg": "", "count": zulins.count(), "data": zulin_info}
    return JsonResponse(zulinxinxi)


def update_zulin(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        zl = zulin.objects.get(pk=id)
        zl.title = request.POST.get('title')
        zl.type = request.POST.get('type')
        # data['info'] = zl.size_room+zl.area_room+zl.num_room
        zl.size_room = request.POST.get('size_room')
        zl.area_room = request.POST.get('area_room')
        zl.num_room = request.POST.get('num_room')
        zl.position1 = request.POST.get('location')
        # zl.position1 = request.POST.get('location').split(" ")[0]
        # zl.position2 = request.POST.get('location').split(" ")[1]
        # zl.position3 = request.POST.get('location').split(" ")[2]

        zl.totalPrice = request.POST.get('totalPrice')
    zl.save()
    data = {
        'msg': "success"
    }
    return JsonResponse(data)


def drop_zulin(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        zl = zulin.objects.get(pk=id)
        zl.delete()
        data = {
            'msg': "success"
        }
        return JsonResponse(data)


# 添加求租信息
def add_update_zulin(request):
    if request.method == 'POST':
        zl = zulin()
        zl.title = request.POST.get('title')
        zl.type = request.POST.get('type')
        zl.size_room = request.POST.get('size_room')
        zl.area_room = request.POST.get('area_room')
        zl.num_room = request.POST.get('num_room')
        zl.position1 = request.POST.get('location')
        zl.totalPrice = request.POST.get('totalPrice')
    zl.save()
    data = {
        'msg': "添加success！！！"
    }
    return JsonResponse(data)


########################################
# 售卖管理==求购管理
def to_shoumai(request):
    return render(request, 'shoumai.html')


def show_shoumai(request):
    shoumais = shoumai.objects.all()
    lis = []

    for zl in shoumais:
        data = dict()
        data['id'] = zl.id
        data['title'] = zl.title
        data['type'] = zl.type
        data['size_room'] = zl.size_room
        data['area_room'] = zl.area_room
        data['num_room'] = zl.num_room
        data['location'] = zl.position1
        data['totalPrice'] = zl.totalPrice
        lis.append(data)
    # print(lis)
    page_index = request.GET.get('page')
    # 前台传来的一页显示多少条数据
    page_limit = request.GET.get('limit')
    # 分页器进行分配
    paginator = Paginator(lis, page_limit)
    # 前端传来页数的数据
    data = paginator.page(page_index)
    # 放在一个列表里：data列表
    shoumai_info = [x for x in data]
    # students.count()总数据量，layui的table模块要接受的格式
    shoumaixinxi = {"code": 0, "msg": "", "count": shoumais.count(), "data": shoumai_info}
    return JsonResponse(shoumaixinxi)


def update_shoumai(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        zl = shoumai.objects.get(pk=id)
        zl.title = request.POST.get('title')
        zl.type = request.POST.get('type')
        # data['info'] = zl.size_room+zl.area_room+zl.num_room
        zl.size_room = request.POST.get('size_room')
        zl.area_room = request.POST.get('area_room')
        zl.num_room = request.POST.get('num_room')
        zl.position1 = request.POST.get('location')
        zl.totalPrice = request.POST.get('totalPrice')
    zl.save()
    data = {
        'msg': "success"
    }
    return JsonResponse(data)


def drop_shoumai(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        zl = shoumai.objects.get(pk=id)
        zl.delete()
        data = {
            'msg': "success"
        }
        return JsonResponse(data)


def add_update_shoumai(request):
    if request.method == 'POST':
        zl = shoumai()
        zl.title = request.POST.get('title')
        zl.type = request.POST.get('type')
        zl.size_room = request.POST.get('size_room')
        zl.area_room = request.POST.get('area_room')
        zl.num_room = request.POST.get('num_room')
        zl.position1 = request.POST.get('location')
        zl.totalPrice = request.POST.get('totalPrice')
    zl.save()
    data = {
        'msg': "添加success！！！"
    }
    return JsonResponse(data)


#############################
# 查询 position and area
def search_xin(request):
    a = request.GET.get('send_data')
    b = request.GET.get('price_data')
    if a!="" and b!= "":
        xins = newfang.objects.filter(Q(position1=a) & Q(position2=b))
    else:
        xins = newfang.objects.filter(Q(position1=a)|Q(position2=b))
    lis = []
    for xin in xins:
        data = dict()
        data['id'] = xin.id
        data['name'] = xin.name
        data['info'] = xin.houseinfo
        data['location'] = xin.position1 + " " + xin.position2 + " " + xin.position3
        data['totalprice'] = xin.totalPrice
        data['unitprice'] = xin.unitPrice
        lis.append(data)

    page_index = request.GET.get('page')
    # 前台传来的一页显示多少条数据
    page_limit = request.GET.get('limit')
    # 分页器进行分配
    paginator = Paginator(lis, page_limit)
    # 前端传来页数的数据
    data = paginator.page(page_index)
    # 放在一个列表里：data列表
    xinfang_info = [x for x in data]
    # students.count()总数据量，layui的table模块要接受的格式
    print(xinfang_info)
    xinfangs = {"code": 0, "msg": "", "count": xins.count(), "data": xinfang_info}
    return JsonResponse(xinfangs)


def search_er(request):
    a = request.GET.get('send_data')
    print(a)
    p1 = request.GET.get('price_data1')
    p2 = request.GET.get('price_data2')
    if a!="" and p1!="" and p2!="":#all query
        ershous = ershoufang.objects.filter(Q(position3=a)&Q(totalPrice__range=(p1,p2)))
    else:
        ershous = ershoufang.objects.filter(Q(position3=a) | Q(totalPrice__range=(p1, p2)))
    lis =[]
    for ershou in ershous:
        data = dict()
        data['id'] = ershou.id
        data['title'] = ershou.title
        data['img'] = ershou.img
        data['info1'] = ershou.houseInfo1
        data['info2'] = ershou.houseInfo2
        data['info3'] = ershou.houseInfo3
        data['location'] = ershou.position1 + " " + ershou.position2 + " " + ershou.position3
        data['totalprice'] = ershou.totalPrice
        data['unitprice'] = ershou.unitPrice
        lis.append(data)

    page_index = request.GET.get('page')
    # 前台传来的一页显示多少条数据
    page_limit = request.GET.get('limit')
    # 分页器进行分配
    paginator = Paginator(lis, page_limit)
    # 前端传来页数的数据
    data = paginator.page(page_index)
    # 放在一个列表里：data列表
    ershou_info = [x for x in data]
    # students.count()总数据量，layui的table模块要接受的格式
    ershoufangs = {"code": 0, "msg": "", "count": ershous.count(), "data": ershou_info}
    return JsonResponse(ershoufangs)


def search_zu(request):
    a = request.GET.get('send_data')
    p1 = request.GET.get('price_data1')
    p2 = request.GET.get('price_data2')
    # a1 = request.GET.get('area_data1')
    # a2= request.GET.get('area_data2')
    if a != "":  # all query
        zus = zufang.objects.filter(Q(position1=a) & Q(totalPrice__range=(p1, p2)))
    else:
        zus = zufang.objects.filter(Q(position1=a) & Q(totalPrice__range=(p1, p2)))
    lis = []
    for zu in zus:
        data = dict()
        data['id'] = zu.id
        data['title'] = zu.title
        data['size_room'] = zu.size_room
        data['area_room'] = zu.area_room
        data['num_room'] = zu.num_room
        data['location'] = zu.position1 + " " + zu.position2 + " " + zu.position3
        data['totalprice'] = zu.totalPrice
        lis.append(data)
    # print(lis)
    page_index = request.GET.get('page')
    # 前台传来的一页显示多少条数据
    page_limit = request.GET.get('limit')
    # 分页器进行分配
    paginator = Paginator(lis, page_limit)
    # 前端传来页数的数据
    data = paginator.page(page_index)
    # 放在一个列表里：data列表
    zufang_info = [x for x in data]
    # students.count()总数据量，layui的table模块要接受的格式
    zufangs = {"code": 0, "msg": "", "count": zus.count(), "data": zufang_info}
    return JsonResponse(zufangs)


#############################
#map
def to_map(request):
    return render(request,"mapdemo.html")
