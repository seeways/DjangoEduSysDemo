from django.shortcuts import render

# Create your views here.

from django.views.generic import View
from pure_pagination import Paginator, PageNotAnInteger
from operation.models import UserFavorite

from .models import Course


class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by("-add_time")
        # 热门课程推荐
        hot_courses = Course.objects.all().order_by('-click_nums')[:3]
        # 排序
        # 默认按时间排序，最新
        sort = request.GET.get('sort', "")
        if sort:
            # 按学习人数排序
            if sort == "students":
                all_courses = all_courses.order_by("-students")
            # 按热门程度排序(点击)
            elif sort == "hot":
                all_courses = all_courses.order_by("-click_nums")
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, 2, request=request)
        courses = p.page(page)
        return render(request, "course-list.html", {
            # 课程分页
            "all_courses": courses,
            # 排序
            "sort": sort,
            # 热门课程
            "hot_courses": hot_courses,

        })


class CourseDetailView(View):
    """课程详情"""

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        # 课程的点击数加1
        course.click_nums += 1
        course.save()
        # 课程标签
        # 通过当前标签，查找数据库中的课程
        has_fav_course = False
        has_fav_org = False

        # 必须是用户已登录我们才需要判断。
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True
        tag = course.tag
        if tag:
            # 需要从1开始不然会推荐自己
            relate_courses = Course.objects.filter(tag=tag)[:2]
        else:
            relate_courses = []
        return render(request, "course-detail.html", {
            'course': course,
            "relate_courses": relate_courses,
            "has_fav_course": has_fav_course,
            "has_fav_org": has_fav_org,

        })
