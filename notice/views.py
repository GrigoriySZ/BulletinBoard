from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Notice
from .forms import NoticeCreateForm

def notice_list(request):
    notices = Notice.objects.all().order_by('-created_at')
    context = {
        'notices': notices, 
        'page_title': 'Все объявления'
    }
    return render(request, 'notice/notice_list.html', context)

def notice_detail(request, notice_id): 
    notice = get_object_or_404(Notice, pk=notice_id)
    context = {
        'notice': notice,
        'page_title': notice.title
    }
    return render(request, 'notice/notice_detail.html', context)

def notice_create(request):
    if request.method == 'POST':
        form = NoticeCreateForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.save()
            messages.success(request, 'Объявление создано')
            return redirect('notice:notice_detail', notice_id=notice.id)
        else:
            messages.error(request, 'Ошибка в форме ввода')
    else:
        form = NoticeCreateForm()
    context = {
        'form': form,
        'page_title': 'Создание нового объявления'
    }
    return render(request, 'notice/notice_create.html', context)