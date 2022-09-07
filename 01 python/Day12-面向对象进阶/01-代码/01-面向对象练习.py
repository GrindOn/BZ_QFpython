# 房子(House) 有 户型、总面积 、剩余面积(等于总面积的60%) 和 家具名称列表 属性
# 新房子没有任何的家具
# 将 家具的名称 追加到 家具名称列表 中
# 判断 家具的面积 是否 超过剩余面积，如果超过，提示不能添加这件家具

# 家具(Furniture) 有 名字 和 占地面积属性，其中
# 席梦思(bed) 占地 4 平米
# 衣柜(chest) 占地 2 平米
# 餐桌(table) 占地 1.5 平米
# 将以上三件 家具 添加 到 房子 中
# 打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表


class House(object):
    # 缺省参数
    def __init__(self, house_type, total_area, fru_list=None):
        if fru_list is None:  # 如果这个值是None
            fru_list = []  # 将fru_list设置为空列表
        self.house_type = house_type
        self.total_area = total_area
        self.free_area = total_area * 0.6
        self.fru_list = fru_list

    def add_fru(self, x):  # x = bed
        if self.free_area < x.area:
            print('剩余面积不足，放不进去了')
        else:
            self.fru_list.append(x.name)
            self.free_area -= x.area

    # def __repr__(self):
    def __str__(self):
        return '户型={},总面积={},剩余面积={},家具列表={}'.format(self.house_type, self.total_area, self.free_area, self.fru_list)


class Furniture(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area


# 创建房间对象的时候，传入户型和总面积
house = House('一室一厅', 20)  # 12

sofa = Furniture('沙发', 10)
bed = Furniture('席梦思', 4)
chest = Furniture('衣柜', 2)
table = Furniture('餐桌', 1.5)

# 把家具添加到房间里(面向对象关注点:让谁做)
house.add_fru(sofa)
house.add_fru(bed)
house.add_fru(chest)
house.add_fru(table)

# print(house.__str__())
print(house)  # print打印一个对象的时候，会调用这个对象的__repr__或者__str__ 方法，获取它们的返回值
