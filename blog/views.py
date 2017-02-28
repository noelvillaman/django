from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment
from account.models import Profile
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from taggit.models import Tag


class PostListView(ListView):
	queryset = Post.published.all()
	context_object_name = 'posts'
	paginate_by = 3
	template_name = 'blog/list.html'

def post_list(request):
	object_list = Post.published.all()
	tag = None 

	if tag_slug:
		tag = get_object_or_404(Tag, slug=tag_slug)
		object_list = object_list.filter(tags_in=[tag])

	paginator = Paginator(object_list, 3) # 3 posts in each page
	page = request.GET.get('page')

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render(request, 'blog/list.html', {'page':page, 'posts' : posts,
		'tag': tag })


def post_detail(request, post):
	# post = get_object_or_404(Post, slug=post,
	# 						status='published',
	# 						publish__year=year,
	# 						publish__month=month,
	# 						publish__day=day)

	current_site = get_current_site(request)
	namesite = current_site.name
	domain = current_site.domain

	post = Post.published.get(slug=post)

	profile = Profile.objects.get(id='1')

	#list of active comments for this post
	comments = post.comments.filter(active=True)

	#list of active subcomments for this post comments
	#reply = 

	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			parent_obj = None
			#create Comment object but do not say to database just yet
			new_comment = comment_form.save(commit=False)
			#Assigng the current post to the comment
			new_comment.post = post
			try:
				parent_id = int(comment_form.POST.get("parent_id"))
			except:
				parent_id = None

			# if parent_id:
			# 	parent_qs = Comment.objects.filter(id=parent_id)
			# 	if parent_id.exists() and parent_qs.count() == 1:
			# 		parent_obj = parent_id.first()



			#save the comment to the database
			new_comment.save()
			comment_form = CommentForm()
	else:
		comment_form = CommentForm()

	return render(request, 'blog/detail.html',
					{'post': post, 'comments': comments, 
					 'comment_form': comment_form, 'namesite': namesite, 'domain': domain, 'profile': profile })

def post_share(request, post_id):
	post = get_object_or_404(Post, id=post_id, status='published')

	sent = False

	if request.method == 'POST':
		form = EmailPostForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			#.. send email
			post_url = request.build_absolute_uri(post.get_absolute_url())
			subject = '{} ({}) recommends you reading "{}"'.format(cd['name'],
				cd['email'], post.title)
			message = 'Read "{}" at {}\n\n{}\'s comments:{}'.format(post.title,
				post_url, cd['name'], cd['comments'])
			send_mail(subject, message, 'noel@namalliv.com', [cd['to']])
			sent = True
	else:
		form = EmailPostForm()
	return render(request, 'blog/share.html',  {'post': post, 'form': form, 'sent': sent })