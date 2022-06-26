from django.contrib import admin

# Register your models here.
from .models import Sex
from .models import Position
from .models import UserType
from .models import RegionType
from .models import UsersInfo
from .models import PaperInfo
from .models import ExpertReview
from .models import Allocate
from .models import EditorReview


class SexAdmin(admin.ModelAdmin):
    list_display = ("pk", "type_name")


class PositionAdmin(admin.ModelAdmin):
    list_display = ("pk", "type_name")


class UserTypeAdmin(admin.ModelAdmin):
    list_display = ("pk", "type_name")


class RegionTypeAdmin(admin.ModelAdmin):
    list_display = ("pk", "type_name")


class PaperInfoAdmin(admin.ModelAdmin):
    list_display = ("pk",
                    "title",
                    "authorID",
                    "authorname_1",
                    "authorname_2",
                    "authorname_3",
                    "authorname_4",
                    "authorname_5",
                    "abstract",
                    "research",
                    "paperfile",
                    "state",)


class UsersInfoAdmin(admin.ModelAdmin):
    list_display = ("pk",
                    "username",
                    "password",
                    "name",
                    "sex",
                    "user_type",
                    "introduction",
                    "company",
                    "position",
                    "created_time",
                    "last_updated_time",
                    "region",
                    "research",
                    )


class ExpertReviewAdmin(admin.ModelAdmin):
    list_display = ("pk",
                    "paperID",
                    "expertID",
                    "state",
                    "opinion",
                    )


class EditorReviewAdmin(admin.ModelAdmin):
    list_display = ("pk",
                    "paperID",
                    "state",
                    "opinion",
                    )

'''
class AllocateAdmin(admin.ModelAdmin):
    list_display = ("pk",
                    "paperID",
                    "expert1_ID",
                    "expert2_ID",
                    "expert3_ID",
                    )
'''


admin.site.register(Sex, SexAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(UserType, UserTypeAdmin)
admin.site.register(RegionType, RegionTypeAdmin)
admin.site.register(UsersInfo, UsersInfoAdmin)
admin.site.register(PaperInfo, PaperInfoAdmin)
admin.site.register(ExpertReview, ExpertReviewAdmin)
admin.site.register(EditorReview, EditorReviewAdmin)
admin.site.register(Allocate)#, AllocateAdmin)
