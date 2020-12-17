from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import ForumReply, ForumCategory, ForumTopic
from django.contrib import messages
from django.http import HttpResponseNotFound
from .forms import CreateTopicForm, CreateReplyForm

def index(req):
    categories = ForumCategory.objects.all()

    return render(req, "forum/category_listing.html",
                  {'categories': categories})

def create_topic(req, cat_id):
    form = 0

    if req.method == 'POST':
        if ForumTopic.user_can_post(req.user) == False and req.user.has_perm('ForumTopic.no_wait') == False:
            messages.info(req, "You can only post a topic once every ten minutes!")
            return redirect("/forum")


        form = CreateTopicForm(req.POST)

        if form.is_valid():

            # ensure user can post to category
            # TODO
            topic = ForumTopic(title=form.cleaned_data['title'], body=form.cleaned_data['body'],
                               category=form.cleaned_data['category'], user=req.user)

            topic.save()

            return redirect(view_topic, topic.pk, 1)

        else:
            form = CreateTopicForm(req.POST)

    else:
        form = CreateTopicForm(initial = {'category': ForumCategory.objects.filter(pk=cat_id).first()})

    return render(req, "forum/create_topic.html",
           {'form': form, 'cat_id': cat_id})

def view_topic(req, id, page):
    try:
        topic = ForumTopic.objects.filter(pk=id).get()
    except ForumTopic.DoesNotExist:
        return HttpResponseNotFound("Topic does not exist");

    reply_list = ForumReply.objects.filter(topic=topic).order_by('created_at').all()

    if page == 1:
        per_page = 9
    else:
        per_page = 10

    paginator = Paginator(reply_list, 10)

    try:
        replies = paginator.page(page)
    except PageNotAnInteger:
        replies = paginator.page(1)
    except EmptyPage:
        return redirect(view_topic, id, paginator.num_pages)

    # wait until below to ensure the topic exists before
    # doing logic

    if req.method == 'POST':
        if ForumReply.user_can_post(req.user) == False and req.user.has_perm('ForumTopic.no_wait') == False:
            messages.info(req, "You can only post a reply once every 30 seconds!")
            return redirect(req.path)

        form = CreateReplyForm(req.POST)

        if form.is_valid():

            # ensure user can post to topic
            # TODO
            reply = ForumReply(body=form.cleaned_data['body'],
                               topic=topic, user=req.user)

            reply.save()

            return redirect(view_topic, id, page)

        else:
            form = CreateReplyForm(req.POST)

    else:
        form = CreateReplyForm()

    return render(req, 'forum/view_topic.html',
                  {'topic': topic, 'replies': replies, 'id': id, 'form': form})

def list_topics(req, id, page):
    topics_list = ForumTopic.objects.filter(category_id=id).order_by('-created_at').all()
    paginator = Paginator(topics_list, 25) # 25 listings per page
    category_name = 0

    # oh no, there are no topics!
    if topics_list.exists() == False:
        messages.info(req, "There aren't any topics in this category yet, you should create one below!")
        return redirect('forum_create_topic', id)

    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        topics = paginator.page(1)
    except EmptyPage:
        return redirect('forum_list_topics', id, paginator.num_pages)

    category_name = topics_list.first().category.title

    return render(req, 'forum/list_topics.html',
                  {'topics': topics, 'id': id, 'category_name': category_name})
