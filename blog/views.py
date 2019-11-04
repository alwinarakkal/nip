from django.shortcuts import render,redirect
from .models import Article,Comment
from django.views.generic import UpdateView,DeleteView
from .forms import CommentForm,AskForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# @login_required
def blog_index(request):
    posts = Article.objects.all().order_by('-created_on')
                                                        #pagination
    paginator=Paginator(posts,3)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts=paginator.page(paginator.num_pages)
                                                        #/pagination
    context = {
        "posts": posts,
    }
    
    return render(request, "wall.html", context)
    
@login_required
def blog_detail(request, pk):
    post = Article.objects.get(pk=pk)
    print(request.user.username)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print ("valid")
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
            return redirect('/h')

    comments = Comment.objects.filter(post=post)
    aut=request.user.username
    context = {
        "post": post,
        "comments": comments,
        "form": form,
        
        
    }

    return render(request, "b_detail.html", context)

@login_required
def Ask_Form(request):
    aut=request.user.username
    if request.method == "POST":
        form = AskForm(request.POST,initial={'aut':aut})
        if form.is_valid():



            form.save()
            return redirect('b_index')
        

    else:
        form = AskForm(initial={'aut':aut})
    context = {
        'form':form
    }
    return render(request, 'ask.html', context)




class post_update(UpdateView):

    model = Article
    form_class = AskForm
    template_name = 'ask.html'
    success_url = '/h'


class post_delete(DeleteView):
    model = Article
    template_name = 'board_element_confirm_delete.html'
    success_url = '/h'


