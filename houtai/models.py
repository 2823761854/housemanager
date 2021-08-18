from django.db import models

# python manage.py makemigrations
# python manage.py migrate
# Create your models here.

class ershoufang(models.Model):#10
    title = models.CharField(max_length=50)  # 小区楼盘名称
    img = models.CharField(max_length=100)  # img
    position1 = models.CharField(max_length=50)  # 地理位置1jinngzhun
    position2 = models.CharField(max_length=50)  # 地理位置2xioqu
    position3 = models.CharField(max_length=50)  # 地理位置3daqu
    houseInfo1 = models.CharField(max_length=50)  # 房屋信息1:huxing
    houseInfo2 = models.CharField(max_length=50)  # 房屋信息2:mianji
    houseInfo3 = models.CharField(max_length=50)  # 房屋信息3:chaoxiang
    totalPrice = models.IntegerField()  # 总价 floatfield
    unitPrice = models.CharField(max_length=50)  # 单价

class newfang(models.Model):#7
    name = models.CharField(max_length=50) #楼盘名称
    #img = models.CharField(max_length=100)  # img
    position1 = models.CharField(max_length=50)  # 地理位置1
    position2 = models.CharField(max_length=50)  # 地理位置2
    position3 = models.CharField(max_length=50)  # 地理位置3
    houseinfo = models.CharField(max_length=50)  # 房屋信息
    unitPrice = models.CharField(max_length=50)  # 单价
    totalPrice = models.CharField(max_length=50) # 总价


class zufang(models.Model):#8
    title = models.CharField(max_length=50)  # 小区楼盘名称
    position1 = models.CharField(max_length=50)  # 地理位置1
    position2 = models.CharField(max_length=50)  # 地理位置2
    position3 = models.CharField(max_length=50)  # 地理位置3
    totalPrice = models.IntegerField()  # zujin
    size_room = models.CharField(max_length=50)  # 大小
    area_room = models.CharField(max_length=50)  # 方位
    num_room = models.CharField(max_length=50)  # 房间数量


# 记录用户信息
class User(models.Model):
    username = models.CharField(max_length=20)# id
    name = models.CharField(max_length=20)# 用户名
    password = models.CharField(max_length=20)# 密码
    gender = models.CharField(max_length=20)# 性别
    minzu = models.CharField(max_length=20)# 民族
    age = models.CharField(max_length=20)# 民族
    phone = models.CharField(max_length=20)# 联系方式
    address = models.CharField(max_length=30)# 家庭住址
    picture = models.CharField(max_length=20)# 照片

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{}".format(self.username,self.name, self.password,self.gender,self.minzu,self.age, self.phone, self.address, self.picture)


# 记录登录者信息
class Denglu(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return "{},{},{}".format(self.id, self.username, self.password)


# 租赁管理
class zulin(models.Model):
    title = models.CharField(max_length=50)  # 发布者id
    type = models.CharField(max_length=50)  # 联系方式
    position1 = models.CharField(max_length=50)  # 地理位置
    # position2 = models.CharField(max_length=50)  # 地理位置
    # position3 = models.CharField(max_length=50)  # 地理位置
    totalPrice = models.CharField(max_length=50)  # 租金
    size_room = models.CharField(max_length=50)  # 占地面积需求
    area_room = models.CharField(max_length=50)  # 其他需求
    num_room = models.CharField(max_length=50)  # 房间规模需求

    def __str__(self):
        return "{},{},{},{},{},{},{}".format(self.title,
        self.type, self.position1, self.totalPrice, self.size_room,self.area_room,self.num_room)


# 求购管理
class shoumai(models.Model):
    title = models.CharField(max_length=50)  # 发布者id
    type = models.CharField(max_length=50)  # 联系方式
    position1 = models.CharField(max_length=50)  # 地理位置
    # position2 = models.CharField(max_length=50)  # 地理位置
    # position3 = models.CharField(max_length=50)  # 地理位置
    totalPrice = models.CharField(max_length=50)  # 租金
    size_room = models.CharField(max_length=50)  # 占地面积需求
    area_room = models.CharField(max_length=50)  # 其他需求
    num_room = models.CharField(max_length=50)  # 房间规模需求

    def __str__(self):
        return "{},{},{},{},{},{},{}".format(self.title, self.type,
        self.position1, self.totalPrice, self.size_room,self.area_room,self.num_room)

