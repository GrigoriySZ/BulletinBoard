from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Notice
from .forms import NoticeCreateForm

def notice_list(request):
    notices = Notice.objects.all().order_by('-created_at')

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.warning(request, 'Авторизируйтесь, чтобы оставить объявление')
            return redirect('login')
        form = NoticeCreateForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.author = request.user
            notice.save()
            messages.success(request, 'Объявление создано')
            return redirect('notice:notice_list')
        else:
            messages.error(request, 'Ошибка в форме ввода')
    else:
        form = NoticeCreateForm()

    context = {
        'notices': notices,
        'form': form, 
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

@login_required
def edit_notice(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id, author=request.user)
    if request.method == 'POST':
        form = NoticeCreateForm(request.POST, instance=notice)
        if form.is_valid():
            form.save()
            messages.success(request, 'Объявление обновлено')
            return redirect('notice:notice_detail', notice_id=notice.id)
        else:
            messages.error(request, 'Ошибка в форме')
    else:
        form = NoticeCreateForm(instance=notice)
    context = {
        'form': form,
        'notice': notice,
        'page_title': f'Редактирование {notice.title}'
    }
    return render(request, 'notice/notice_edit.html', context)

@login_required
def delete_notice(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id, author=request.user)
    if request.method == 'POST':
        if 'confirm_deletion' in request.POST:
            notice.delete()
            messages.success(request, 'Объявление удалено')
            return redirect('notice:notice_list')
        else:
            return redirect('notice:notice_detail', notice_id=notice.id)
        
    context = {
        'notice': notice,
        'confirm_deletion': True,
        'page_title': f'Удаление {notice.title}'
    }
    return render(request, 'notice/notice_detail.html', context)