from django.shortcuts import render, get_object_or_404
import os
import datetime

from Demo.settings import BASE_DIR
# Create your views here.
from .models import PaperInfo, Allocate, UsersInfo, UserType, EditorReview, ExpertReview
from . import models
from django.http import HttpResponse
from django.conf import settings
import os
import logging
logger = logging.getLogger(__name__)
GlobalUsername = ""
GlobalPaperID = []

def login_index(request):
    path = os.path.join(settings.BASE_DIR, 'templates', 'login.html')
    html = ''
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    return HttpResponse(html)

def register_index(request):
    path = os.path.join(settings.BASE_DIR, 'templates', 'register.html')
    html = ''
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    return HttpResponse(html)

def change_index(request):
    path = os.path.join(settings.BASE_DIR, 'templates', 'changepassword.html')
    html = ''
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    return HttpResponse(html)

def user_welcome(request):
    global GlobalUsername
    if request.method == 'POST':
        # username = request.GET.get('username')
        # 查询用户名密码
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        user_info1 = UsersInfo.objects.filter(username=Username)
        if len(user_info1) == 0:
            return HttpResponse("账号不存在，请先注册！")
        else:
            context = {}
            context['paper'] = PaperInfo.objects.all()
            user_info2 = UsersInfo.objects.filter(username=Username).first()
            if user_info2.password == Password:
                GlobalUsername = Username
                print(user_info2.user_type)
                if user_info2.user_type == '1':#普通用户
                    return render(request, 'post_par.html')
                elif user_info2.user_type == '2':#审稿人
                #---kkx---#
                    paperID = []
                    expert = UsersInfo.objects.filter(username=Username)
                    allocateall = Allocate.objects.all()
                    for allocate in allocateall:
                        logger.error('尝试一次')
                        if expert.filter(pk=allocate.ExpertID_1).exists():
                            logger.error('文章ID搜索:' + allocate.PaperID)
                            dic = {"test_index": allocate.PaperID, "expertid": allocate.ExpertID_1}
                            paperID.append(dic)
                        elif expert.filter(pk=allocate.ExpertID_2).exists():
                            logger.error('文章ID搜索:' + allocate.PaperID)
                            dic = {"test_index": allocate.PaperID, "expertid": allocate.ExpertID_2}
                            paperID.append(dic)
                        elif expert.filter(pk=allocate.ExpertID_2).exists():
                            logger.error('文章ID搜索:' + allocate.PaperID)
                            dic = {"test_index": allocate.PaperID, "expertid": allocate.ExpertID_3}
                            paperID.append(dic)
                    logger.error(len(paperID))
                    context['test1'] = paperID
                    context['alloc'] = allocateall
                    return render(request, 'paper_list_expert.html', context)
                elif user_info2.user_type == '3':#主编
                    return render(request, 'paper_list_editor.html',context)
                else:
                    return HttpResponse("用户类型错误！")
            else:
                return HttpResponse("密码错误！")
    else:
        return HttpResponse("error")

def user_register(request):
    if request.method == 'POST':
        print(111)
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        Confirmpassword = request.POST.get('confirmpassword')
        user_info = UsersInfo.objects.filter(username=Username)
        if len(user_info) != 0:
            return HttpResponse("该用户名已被注册，请更换其他用户名！")
        elif Password != Confirmpassword:
            return HttpResponse("两次输入密码不一致，请重新输入！")
        else:
            Name = request.POST.get('name')
            Sex = request.POST.get('sex')
            if(Sex == "男"):
                Sex = "1"
            else:
                Sex = "2"
            User_type = "1"
            Introduction = request.POST.get('introduction')
            Company = request.POST.get('company')
            Position = request.POST.get('position')
            Region = request.POST.get('region')
            Research = request.POST.get('research')

            UsersInfo.objects.create(username=Username, name=Name, password=Password, sex=Sex, user_type=User_type,
                                 introduction=Introduction, company=Company, position=Position, region=Region, research=Research)
            return render(request, 'registerresult.html',)
    elif request.method == 'GET':
        print(222)
        Username = request.GET.get('username')
        Originalpassword = request.GET.get('originalpassword')
        Newpassword = request.GET.get('newpassword')
        Confirmpassword = request.GET.get('confirmpassword')
        user_info1 = UsersInfo.objects.filter(username=Username)
        if len(user_info1) == 0:
            return HttpResponse("用户不存在，请先注册！")
        user_info2 = UsersInfo.objects.filter(username=Username).first()
        if user_info2.password != Originalpassword:
            return HttpResponse("原密码不正确，请重试！")
        elif Newpassword != Confirmpassword:
            return HttpResponse("两次输入密码不一致，请重新输入！")
        else:
            user_info = UsersInfo.objects.get(username=Username)
            user_info.password = Newpassword
            user_info.save()
            return render(request, 'registerresult.html',)


    else:
        return HttpResponse("error")

def paper_list(request):
    context = {}
    context['papers'] = PaperInfo.objects.all()
    return render(request, 'paper_list_editor.html', context)


def allocate_list(request):
    context = {}
    context['papers'] = PaperInfo.objects.all()
    return render(request, 'allocate_list_editor.html', context)


def allocate_detail(request):
    context = {}
    context['papers'] = PaperInfo.objects.all()
    context['allocates'] = Allocate.objects.all()
    context['users'] = UsersInfo.objects.all()
    return render(request, 'allocate_detail_editor.html', context)


def review_list(request):
    context = {}
    context['papers'] = PaperInfo.objects.all()
    return render(request, 'review_list_editor.html', context)


def paper_review(request, pk):
    context = {}
    context['papers'] = PaperInfo.objects.all()
    return render(request, 'review_editor.html', context)


def post(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'post_par.html', context)

def check_user(request):
    global GlobalUsername
    tmp=models.UsersInfo.objects.get(username=GlobalUsername)
    paper_lists=models.PaperInfo.objects.filter(authorID=tmp)
    return render(request, 'check_user.html', {'paper_lists':paper_lists})

def check_admin(request):
    paper_lists=models.PaperInfo.objects.all();
    return render(request, 'check_admin.html', {'paper_lists':paper_lists})

def check_reviewer(request):
    global GlobalUsername
    tmp=models.UsersInfo.objects.get(username=GlobalUsername)
    paper_lists=models.ExpertReview.objects.filter(expertID=tmp)
    return render(request, 'check_reviewer.html', {'paper_lists':paper_lists})

def postsubmit(request):
    global GlobalUsername
    tmp=models.UsersInfo.objects.filter(username=GlobalUsername).first()
    if not tmp:
        return HttpResponse(GlobalUsername)
    tmp.save();
    result = models.PaperInfo()
    result.title = request.POST.get('name')
    result.paperfile=request.FILES.get('paper').name
    result.authorname_1 = request.POST.get('author_name1')
    result.authorname_2 = request.POST.get('author_name2')
    result.authorname_3 = request.POST.get('author_name3')
    result.authorname_4 = request.POST.get('author_name4')
    result.authorname_5 = request.POST.get('author_name5')
    result.abstarct = request.POST.get('abstarct')
    result.research = request.POST.get('direction')
    result.authorID=tmp;
    if request.method=='POST':   #判断是否为POST请求
        myFile=request.FILES.get('paper',None)
        
        if not myFile:
            return HttpResponse('no file for index')
        savepath=BASE_DIR/'upload'
        f=open(os.path.join(savepath,myFile.name),'wb+')
        print(f)
        for chunk in myFile.chunks():  #分块写入文件
            print(chunk)
            f.write(chunk)
        f.close()
        print(myFile.name)
    result.save();
    return render(request, 'post_complete.html')

def download(request):
    paper=request.GET.get('name')
    savepath=BASE_DIR/'upload'
    print(savepath)
    f=open(os.path.join(savepath,paper),'rb')
    response = HttpResponse(f)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition']='attachment;filename='+paper
    return response


def logout(request):
    global GlobalUsername
    GlobalUsername=""
    GlobalPaperID.clear()
    return render(request,'login.html')

#选择待分配的文章
def allocate_paper_jump(request):
    global GlobalPaperID
    global GlobalUsername
    index = []
    if request.method == 'GET':
        # username = request.GET.get('username')
        # 查询用户名密码
        papers = PaperInfo.objects.all()
        print(GlobalPaperID)
        for paper in papers:
            # logger.error(str(paper.title))
            temp = paper.title
            paperid = request.GET.get(temp)
            logger.error('test:' + str(paperid))
            if str(paperid) == str(paper.pk):
                index.append(int(paper.pk))
                logger.error('For test:')
                logger.error(logger.error(index[0]))

        paper_info = PaperInfo.objects.filter(pk=index[0])

        if len(GlobalPaperID) != 0:
            user_info = UsersInfo.objects.get(username=GlobalUsername)
            paper_info = PaperInfo.objects.filter(pk=GlobalPaperID[0])
            expert_info = UsersInfo.objects.all()
            context = {}
            context['user'] = user_info
            context['papers'] = paper_info
            context['expert'] = expert_info
            return render(request, 'allocate_detail_editor.html', context)
        elif paper_info.exists():
            for paper in paper_info:
                if paper.pk == index[0]:
                    GlobalPaperID.append(index[0])
                    expert_info = UsersInfo.objects.all()
                    context = {}
                    context['user'] = UsersInfo.objects.filter(username=GlobalUsername)
                    context['papers'] = paper_info
                    context['expert'] = expert_info
                    return render(request, 'allocate_detail_editor.html', context)
                else:
                    return HttpResponse("error")
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error")

#分配表
def allocate_list(request):
    global GlobalUsername
    global GlobalPaperID
    paperID = []
    context={}
    expert = UsersInfo.objects.filter(username=GlobalUsername)
    allocateall = Allocate.objects.all()
    for allocate in allocateall:
        logger.error('尝试一次')
        if expert.filter(pk=allocate.ExpertID_1).exists():
            logger.error('文章ID搜索:' + allocate.PaperID)
            dic = {"test_index": allocate.PaperID, "expertid": allocate.ExpertID_1}
            paperID.append(dic)
        elif expert.filter(pk=allocate.ExpertID_2).exists():
            logger.error('文章ID搜索:' + allocate.PaperID)
            dic = {"test_index": allocate.PaperID, "expertid": allocate.ExpertID_2}
            paperID.append(dic)
        elif expert.filter(pk=allocate.ExpertID_2).exists():
            logger.error('文章ID搜索:' + allocate.PaperID)
            dic = {"test_index": allocate.PaperID, "expertid": allocate.ExpertID_3}
            paperID.append(dic)
    logger.error(len(paperID))
    context['test1'] = paperID
    context['papers'] = PaperInfo.objects.all()
    return render(request, 'allocate_list_editor.html', context)

#分配后返回分配表
def allocate_detail(request):
    global GlobalPaperID
    global GlobalUsername
    index = 0
    result = Allocate()
    result.PaperID = GlobalPaperID[0]
    logger.error("寻找：" + str(request.GET.get('expert1')))
    result.ExpertID_1 = request.GET.get('expert1')
    result.ExpertID_2 = request.GET.get('expert2')
    result.ExpertID_3 = request.GET.get('expert3')
    temp = PaperInfo.objects.filter(pk=GlobalPaperID[0])
    temp.update(state=request.GET.get('state'))
    result.save()
    GlobalPaperID.clear()
    context = {}
    context['users'] = UsersInfo.objects.filter(username=GlobalUsername)
    context['papers'] = PaperInfo.objects.all()
    return render(request, 'allocate_list_editor.html', context)

#专家审核表
def review_list(request):
    global GlobalPaperID
    global GlobalUsername
    context = {}
    paperID = []
    expert = UsersInfo.objects.filter(username=GlobalUsername)
    allocateall = Allocate.objects.all()
    for allocate in allocateall:
        logger.error('尝试一次')
        if expert.filter(pk=allocate.ExpertID_1).exists():
            logger.error('文章ID搜索:' + allocate.PaperID)
            dic = {"test_index": allocate.PaperID, "expertid": allocate.ExpertID_1}
            paperID.append(dic)
        elif expert.filter(pk=allocate.ExpertID_2).exists():
            logger.error('文章ID搜索:' + allocate.PaperID)
            dic = {"test_index": allocate.PaperID, "expertid": allocate.ExpertID_2}
            paperID.append(dic)
        elif expert.filter(pk=allocate.ExpertID_2).exists():
            logger.error('文章ID搜索:' + allocate.PaperID)
            dic = {"test_index": allocate.PaperID, "expertid": allocate.ExpertID_3}
            paperID.append(dic)
    logger.error(len(paperID))
    context['test1'] = paperID
    context['users'] = UsersInfo.objects.filter(username=GlobalUsername)
    context['papers'] = PaperInfo.objects.all()
    return render(request, 'review_list_expert.html', context)


#专家审核表
def paper_review_detail(request):
    global GlobalPaperID
    global GlobalUsername
    index = []
    if request.method == 'GET':
        review = ExpertReview.objects.filter(expertID=GlobalUsername)
        papers = PaperInfo.objects.all()
        print(GlobalPaperID)
        for paper in papers:
            # logger.error(str(paper.title))
            temp = paper.title
            paperid = request.GET.get(temp)
            logger.error('test:' + str(paperid))
            if str(paperid) == str(paper.pk):
                index.append(int(paper.pk))
                logger.error('For test:')
                logger.error(logger.error(index[0]))

        paper_info = PaperInfo.objects.filter(pk=index[0])

        if len(GlobalPaperID) != 0:
            user_info = UsersInfo.objects.get(username=GlobalUsername)
            paper_info = PaperInfo.objects.filter(pk=GlobalPaperID[0])
            expert_info = UsersInfo.objects.all()
            context = {}
            context['user'] = user_info
            context['papers'] = paper_info
            context['expert'] = expert_info
            if review.exists():
                logger.error('你存在吗？')
            return render(request, 'review_detail_expert.html', context)
        elif paper_info.exists():
            for paper in paper_info:
                if paper.pk == index[0]:
                    GlobalPaperID.append(index[0])
                    expert_info = UsersInfo.objects.all()
                    context = {}
                    context['user'] = UsersInfo.objects.filter(username=GlobalUsername)
                    context['papers'] = paper_info
                    context['expert'] = expert_info
                    return render(request, 'review_detail_expert.html', context)
                else:
                    return HttpResponse("error")
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error")

#返回审核表用
def paper_review_list_jump(request):
    global GlobalPaperID
    global GlobalUsername
    context = {}
    paperID = []
    expert = UsersInfo.objects.filter(username=GlobalUsername)
    allocateall = Allocate.objects.all()
    for allocate in allocateall:
        logger.error('尝试一次')
        if expert.filter(pk=allocate.ExpertID_1).exists():
            logger.error('文章ID搜索:' + allocate.PaperID)
            dic = {"test_index": allocate.PaperID, "expertid": allocate.ExpertID_1}
            paperID.append(dic)
        elif expert.filter(pk=allocate.ExpertID_2).exists():
            logger.error('文章ID搜索:' + allocate.PaperID)
            dic = {"test_index": allocate.PaperID, "expertid": allocate.ExpertID_2}
            paperID.append(dic)
        elif expert.filter(pk=allocate.ExpertID_2).exists():
            logger.error('文章ID搜索:' + allocate.PaperID)
            dic = {"test_index": allocate.PaperID, "expertid": allocate.ExpertID_3}
            paperID.append(dic)
    logger.error(len(paperID))
    context['test1'] = paperID
    context['users'] = UsersInfo.objects.filter(username=GlobalUsername)
    context['papers'] = PaperInfo.objects.all()
    return render(request, 'paper_list_expert.html', context)

#专家审核提交
def review_jump_reviewer(request):
    global GlobalPaperID
    global GlobalUsername
    index = 0
    result = ExpertReview()
    result.paperID = request.GET.get('标题')
    logger.error("求求了:"+ str(request.GET.get('标题')))
    #logger.error("寻找：" + str(request.GET.get('expert1')))
    user = ExpertReview.objects.filter(expertID=GlobalUsername)
    paper = ExpertReview.objects.filter(paperID=str(request.GET.get('标题')))
    logger.error("求求了:" + str(paper.exists()))
    logger.error("user??:" + str(GlobalUsername))
    if user.exists() and paper.exists():
        temp = ExpertReview.objects.filter(paperID=GlobalPaperID[0])
        temp.update(opinion=request.GET.get('advise'))
        temp.update(state=request.GET.get('review_state'))
    else:
        result.expertID = GlobalUsername
        result.opinion = request.GET.get('advise')
        result.state = request.GET.get('review_state')
        result.save()

    GlobalPaperID.clear()
    context = {}
    context['users'] = UsersInfo.objects.filter(username=GlobalUsername)
    context['papers'] = PaperInfo.objects.all()
    return render(request, 'review_list_expert.html', context)

#审核表-主编
def review_list_editor(request):
    global GlobalUsername
    global GlobalPaperID
    paperID = []
    context={}
    expert = UsersInfo.objects.filter(username=GlobalUsername)
    allocateall = Allocate.objects.all()
    for allocate in allocateall:
        logger.error('尝试一次')
        if expert.filter(pk=allocate.ExpertID_1).exists():
            logger.error('文章ID搜索:' + allocate.PaperID)
            dic = {"test_index": allocate.PaperID, "expertid": allocate.ExpertID_1}
            paperID.append(dic)
        elif expert.filter(pk=allocate.ExpertID_2).exists():
            logger.error('文章ID搜索:' + allocate.PaperID)
            dic = {"test_index": allocate.PaperID, "expertid": allocate.ExpertID_2}
            paperID.append(dic)
        elif expert.filter(pk=allocate.ExpertID_2).exists():
            logger.error('文章ID搜索:' + allocate.PaperID)
            dic = {"test_index": allocate.PaperID, "expertid": allocate.ExpertID_3}
            paperID.append(dic)
    logger.error(len(paperID))
    context['test1'] = paperID
    context['papers'] = PaperInfo.objects.all()
    return render(request, 'review_list_editor.html', context)

def review_paper_jump_editor(request):
    global GlobalPaperID
    global GlobalUsername
    index = []
    EXPID = []
    if request.method == 'GET':
        # username = request.GET.get('username')
        # 查询用户名密码
        papers = PaperInfo.objects.all()
        print(GlobalPaperID)
        for paper in papers:
            # logger.error(str(paper.title))
            temp = paper.title
            paperid = request.GET.get(temp)
            logger.error('test:' + str(paperid))
            if str(paperid) == str(paper.pk):
                index.append(int(paper.pk))
                logger.error('For test:')
                logger.error(logger.error(index[0]))

        paper_info = PaperInfo.objects.filter(pk=index[0])

        if len(GlobalPaperID) != 0:
            user_info = UsersInfo.objects.get(username=GlobalUsername)
            paper_info = PaperInfo.objects.filter(pk=GlobalPaperID[0])
            expert_info = UsersInfo.objects.all()

            context = {}
            context['user'] = user_info
            context['papers'] = paper_info
            context['expert'] = expert_info
            #expert = UsersInfo.objects.filter(username=GlobalUsername)
            allocateall = Allocate.objects.filter(PaperID=GlobalPaperID[0])
            for all in allocateall:
                review = ExpertReview.objects.filter(paperID=all.PaperID)
            context['review'] = review
            return render(request, 'review_detail_editor.html', context)
        elif paper_info.exists():
            for paper in paper_info:
                if paper.pk == index[0]:
                    GlobalPaperID.append(index[0])
                    expert_info = UsersInfo.objects.all()
                    context = {}
                    context['user'] = UsersInfo.objects.filter(username=GlobalUsername)
                    context['papers'] = paper_info
                    context['expert'] = expert_info
                    allocateall = Allocate.objects.filter(PaperID=GlobalPaperID[0])
                    for all in allocateall:
                        review = ExpertReview.objects.filter(paperID=all.PaperID)
                    context['review'] = review
                    return render(request, 'review_detail_editor.html', context)
                else:
                    return HttpResponse("error")
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error")

def review_jump_editor(request):
    global GlobalPaperID
    global GlobalUsername
    index = 0
    result = EditorReview()
    result.PaperID = GlobalPaperID[0]
    result.opinion = request.GET.get('advise')
    result.opinion = request.GET.get('review_state')
    temp = PaperInfo.objects.filter(pk=GlobalPaperID[0])
    temp.update(state=request.GET.get('review_state'))
    result.save()
    GlobalPaperID.clear()
    context = {}
    context['users'] = UsersInfo.objects.filter(username=GlobalUsername)
    context['papers'] = PaperInfo.objects.all()
    return render(request, 'review_list_editor.html', context)