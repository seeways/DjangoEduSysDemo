from pure_pagination import Paginator, PageNotAnInteger
from django.shortcuts import render
from django.views.generic.base import View
from .models import CourseOrg, CityDict, Teacher


# Create your views here.


class OrgView(View):
    """课程机构"""

    def get(self, request):
        # 所有机构
        all_orgs = CourseOrg.objects.all()
        # 机构总数
        org_nums = all_orgs.count()
        # 所有城市
        all_citys = CityDict.objects.all()
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
        })
