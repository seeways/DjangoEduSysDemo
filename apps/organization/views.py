from pure_pagination import Paginator, PageNotAnInteger
from django.shortcuts import render
from django.views.generic.base import View
from .models import CourseOrg, CityDict, Teacher
from django.http import HttpResponse
from .forms import UserAskForm


# Create your views here.


class OrgView(View):
    """课程机构"""

    def get(self, request):
        # 所有机构
        all_orgs = CourseOrg.objects.all()

        # 所有城市
        all_citys = CityDict.objects.all()

        # 城市id过滤
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 类别过滤
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)

        # 热门课程机构排名
        hot_orgs = all_orgs.order_by('-click_nums')[:3]

        # 学习人数和课程数筛选
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_orgs = all_orgs.order_by("-students")
            elif sort == "courses":
                all_orgs = all_orgs.order_by("-course_nums")

        # 机构总数
        org_nums = all_orgs.count()

        # 机构分页
        try:
            page = request.GET.get("page", 1)
        except PageNotAnInteger:
            page = 1
        # 默认每页显示5个
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)

        return render(request, "org-list.html", {
            "all_orgs": orgs,
            "all_citys": all_citys,
            "org_nums": org_nums,
            'city_id': city_id,
            "category": category,
            "hot_orgs": hot_orgs,
            "sort": sort,
        })


class AddUserAskView(View):
    """
    用户咨询
    """

    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            # 如果保存成功,返回json字符串,后面content type是告诉浏览器返回的数据类型
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            # 如果保存失败，返回json字符串,并将form的报错信息通过msg传递到前端
            return HttpResponse('{"status":"fail", "msg":"您提交的信息有误！"}', content_type='application/json')
