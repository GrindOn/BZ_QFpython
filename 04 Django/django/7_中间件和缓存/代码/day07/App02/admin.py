from django.contrib import admin

# Register your models here.
from App02.models import User,Detail

# 用户管理
class UserAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ['pk','username','password','sex']
    # 搜做字段
    search_fields = ['username']

    # 分页
    list_per_page = 1

    # 过滤
    list_filter = ['username']

    # 信息分组
    fieldsets = [
        ("基本信息", {"fields": ['username']}),
        ("其它信息", {'fields': ['password','sex']}),
    ]





admin.site.register(User,UserAdmin)
admin.site.register(Detail)