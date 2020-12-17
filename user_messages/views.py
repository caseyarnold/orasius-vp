from django.shortcuts import render, redirect
from .models import UserMessage
from .forms import CreateUserMessageForm
from django.contrib.auth.models import User

# Create your views here.
def list_messages(req):

    messages = UserMessage.objects.all()

    return render(req, 'user_messages/list_messages.html',
                  {'messages': messages})

def view_message(req, id):
    return 0

def create_message(req):

    form = 0

    if req.method == 'POST':
        # if UserMessage.user_can_send(req.user) == False and req.user.has_perm('UserMessage.no_wait') == False:
        #     messages.info(req, "You can only send mail once every minute!")
        #     return redirect("/messages")


        form = CreateUserMessageForm(req.POST)

        if form.is_valid():

            to_user = form.cleaned_data['to_user']
            to_user = User.objects.get(username=to_user);

            message = UserMessage(to_user=to_user, body=form.cleaned_data['body'],
                    title=form.cleaned_data['title'], from_user=req.user)

            message.save()


            return redirect(user_messages_view_message, message.pk, 1)

        else:
            form = CreateUserMessageForm(req.POST)

    else:
        form = CreateUserMessageForm()

    return render(req, 'user_messages/create_message.html',
                {'form': form})
    form = 0

    if req.method == 'POST':
        # if UserMessage.user_can_send(req.user) == False and req.user.has_perm('UserMessage.no_wait') == False:
        #     messages.info(req, "You can only send mail once every minute!")
        #     return redirect("/messages")


        form = CreateUserMessageForm(req.POST)

        if form.is_valid():

            to_user = form.cleaned_data['to_user']
            to_user = User.objects.get(username=to_user);

            message = UserMessage(to_user=to_user, body=form.cleaned_data['body'],
                    title=form.cleaned_data['title'], from_user=req.user)

            message.save()


            return redirect(user_messages_view_message, message.pk, 1)

        else:
            form = CreateUserMessageForm(req.POST)

    else:
        form = CreateUserMessageForm()

    return render(req, 'user_messages/create_message.html',
                {'form': form})