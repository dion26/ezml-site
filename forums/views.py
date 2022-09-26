from wsgiref.util import request_uri
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse, reverse_lazy

from .models import FavoriteThread, Thread, Subforum, Comment, LikeThread, DisLikeThread
from .forms import ThreadForm

# rest framework
from api.mixins import StaffEditorPermissionMixin
from rest_framework import generics, permissions
from .serializers import ThreadSerializer

### Django REST VIEW

class ThreadListCreateAPIView(
    permissions.AllowAny, # StaffEditorPermissionMixin , 
    generics.ListCreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

    def perform_create(self, serializer):

        serializer.save(host=self.request.user)
        # serializer.save()

class ThreadDetailAPIView(permissions.AllowAny,
                        generics.RetrieveAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    lookup_field = 'slug'

class ThreadListAPIView(generics.RetrieveAPIView):
    '''
    Not Used
    '''
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

class ThreadUpdateAPIView(generics.UpdateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

class ThreadDeleteAPIView(generics.DestroyAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy()





# class UpdateLikeMixin:
#     def update_status(self, thread, action):
#         try:
#             If child DisLike model doesnot exit then create
#             thread.dis_likes
#         except Thread.dis_likes.RelatedObjectDoesNotExist as identifier:
#             DisLikeThread.objects.create(thread = thread)

#         try:
#             If child Like model doesnot exit then create
#             thread.likes
#         except Thread.likes.RelatedObjectDoesNotExist as identifier:
#             LikeThread.objects.create(thread = thread)

#         try:
#             thread.fav_thread
#         except Thread.fav_thread.RelatedObjectDoesNotExist as identifier:
#             FavoriteThread.objects.create(thread = thread)

#         print(action)
#         if action.lower() == 'upvote':
#             if self.request.user in thread.likes.users.all():
#                 pass
#             else:
#                 thread.likes.users.add(self.request.user)
#                 thread.dis_likes.users.remove(self.request.user)
#         elif action.lower() == 'unupvote':
#             thread.likes.users.remove(self.request.user)
#         elif action.lower() == 'downvote':
#             if self.request.user in thread.dis_likes.users.all():
#                 pass
#             else:    
#                 thread.dis_likes.users.add(self.request.user)
#                 thread.likes.users.remove(self.request.user)
#         elif action.lower() == 'undownvote':
#             thread.dis_likes.users.remove(self.request.user)
#         elif action.lower() == 'star':
#             if self.request.user not in thread.fav_thread.users.all():
#                 thread.fav_thread.users.add(self.request.user)
#         elif action.lower() == 'unstar':
#             thread.fav_thread.users.remove(self.request.user)
#         else:
#             return HttpResponseRedirect(reverse('forum'))
#         return HttpResponseRedirect(reverse('forum'))

# class ThreadListView(UpdateLikeMixin, ListView):
#     model = Thread
#     paginate_by = 5
#     template_name = 'forums/forum_class.html'
#     context_object_name = 'threads'
#     thread_comments = Comment.objects.all()[:10]

#     extra_context = {'topics': Subforum.objects.all(), 'thread_comments': thread_comments}

#     def get_queryset(self):
#         qs = Thread.objects.all()
#         qs = sorted(qs, key=lambda x: x.get_hot_score(), reverse=True)
#         return qs

#     def post(self, request, *args, **kwargs): 
#         context = self.get_context_data(**kwargs)
#         like_id = self.request.POST.get('id') # context['id']
#         action = self.request.POST.get('action') #context['action']
#         new_state = self.request.POST.get('newState') #context['newState']
#         user = self.request.user
#         thread = get_object_or_404(Thread, id=like_id)

#         return self.update_status(thread, action)

# class OrderedThreadListView(ListView):
#     model = Thread
#     paginate_by = 5
#     template_name = 'forums/forum_class.html'
#     context_object_name = 'threads'
#     thread_comments = Comment.objects.all()[:10]
#     extra_context = {'topics': Subforum.objects.all(), 'thread_comments': thread_comments}

#     def get_ordering_method(self, qs, ord):
#         if ord == 'new':
#             qs = qs.order_by('-created')
#         elif ord == 'top':
#             qs = sorted(qs, key=lambda x: x.get_top_score(), reverse=True)
#         else:
#             qs = sorted(qs, key=lambda x: x.get_hot_score(), reverse=True)
#         return qs

#     def get_queryset(self):
#         cat = self.kwargs.get('cat').lower()
#         order_list = ['new', 'top', 'hot']
#         if cat in order_list:
#             qs = Thread.objects.all()
#             ord = cat
#         else:
#             ord = self.kwargs.get('ord').lower()
#             qs = Thread.objects.filter(Q(subforum__name__icontains=cat))
#         qs = self.get_ordering_method(qs, ord)
#         return qs
    
#     def get_thread_count(self):
#         return self.get_queryset.count()

# '''
# def forums(request):
#     q = request.GET.get('q') if request.GET.get('q') != None else ''
#     threads = Thread.objects.filter(
#         Q(subforum__name__icontains=q) |
#         Q(name__icontains=q) |
#         Q(description__icontains=q)
#     )
#     subforum = Subforum.objects.all()[0:5]
#     thread_count = threads.count()
#     thread_comments = Comment.objects.filter(Q(thread__subforum__name__icontains=q))

#     context = {'threads': threads, 'topics': subforum, 
#                 'thread_count': thread_count, 'thread_comments': thread_comments}
#     return render(request, 'forums/forum.html', context)
# '''

# def thread(request, pk):
#     thread = Thread.objects.get(id=pk)
#     comments = thread.comment_set.all()
#     threads = Thread.objects.all()

#     if request.method == 'POST':
#         comment = Comment.objects.create(
#             user=request.user,
#             thread=thread,
#             body=request.POST.get('body')
#         )
#         return redirect('thread', pk=thread.id)

#     context = {'thread': thread, 'comments': comments, 'threads': threads}
#     return render(request, 'forums/thread.html', context)

# class CreateThreadView(LoginRequiredMixin, CreateView):
#     model = Thread
#     form_class = ThreadForm
#     template_name = 'forums/thread_form.html'
#     success_url = reverse_lazy('forum')

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.host = self.request.user
#         self.object.save()
#         return super(CreateThreadView, self).form_valid(form)

# '''
# @login_required(login_url='account_login')
# def createThread(request):
#     form = ThreadForm()

#     if request.method == 'POST':
#         form = ThreadForm(request.POST)
#         if form.is_valid():
#             thread = form.save(commit=False)
#             thread.host = request.user
#             thread.save()
#             return redirect('forum')

#     context = {'form': form}
#     return render(request, 'forums/thread_form.html', context)
#     '''

# class UpdateThreadView(LoginRequiredMixin, UpdateView):
#     model = Thread
#     form_class = ThreadForm
#     template_name = 'forums/thread_form.html'
#     success_url = reverse_lazy('forum')

# '''
# @login_required(login_url='login')
# def updateThread(request, pk):
#     thread = Thread.objects.get(id=pk)
#     form = ThreadForm(instance=thread)

#     if request.user != thread.host:
#         return HttpResponse('You are not allowed to edit this post')
    
#     if request.method == 'POST':
#         form = ThreadForm(request.POST, instance=thread)
#         if form.is_valid():
#             form.save()
#             return redirect('forum')

#     context = {'form': form}
#     return render(request, 'forums/thread_form.html', context)
# '''

# @login_required(login_url='login')
# def deleteThread(request, pk):
#     thread = Thread.objects.get(id=pk)

#     if request.user != thread.host:
#         return HttpResponse('You are not allowed to delete this post')

#     if request.method == 'POST':
#         thread.delete()
#         return redirect('forum')
#     return render(request, 'base/delete.html', {'obj': thread})

# @login_required(login_url='login')
# def deleteComment(request, pk):
#     comment = Comment.objects.get(id=pk)

#     if request.user != comment.user:
#         return HttpResponse('You are not allowed to delete this post')

#     if request.method == 'POST':
#         comment.delete()
#         return redirect('forum')
#     return render(request, 'base/delete.html', {'obj': comment})

# def topicsPage(request):
#     q = request.GET.get('q') if request.GET.get('q') != None else ''
#     topics = Subforum.objects.filter(name__icontains=q)
#     return render(request, 'forums/topics.html', {'topics': topics})

# def activityPage(request):
#     thread_comments = Comment.objects.all()
#     return render(request, 'forums/activity.html', {'thread_comments':thread_comments})