from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
# Create your views here.
from .models import Post
from django.contrib import messages
from django.http import HttpResponseRedirect


def myPosts(request):
    context = {
        'posts': Post.objects.filter(author=request.user)
    }

    return render(request, 'Post/posts.html', context)


# class PostListView(ListView):
#     model = Post
#     template_name = 'Post/posts.html'
#     context_object_name = "posts"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image', 'image_name', 'image_caption']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Image successfully uploaded")
        return super().form_valid(form)


def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    is_liked = False

    how_many = post.likes.all().count()
    if post.likes.filter(id=request.user.id).exists():

        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)

        is_liked = True
    context = {
        'is_liked': is_liked,
        'likers': post.likes.all()
    }
    # return render(request, 'Post/post_detail.html', context)
    messages.success(request, "Post Liked")
    return redirect('insta_home')
    # return HttpResponseRedirect(post.get_absolute_url())


