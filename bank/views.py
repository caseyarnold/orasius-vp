from django.shortcuts import redirect, render
from .models import BankAccount
from .forms import BankForm

def index(req):
    try:
        account = BankAccount.objects.get(user=req.user)
    except BankAccount.DoesNotExist:
        account = BankAccount(user=req.user).save()
        redirect(req.path)

    form_class = BankForm
    type = 0
    success = "default"

    if (req.method == 'POST'):
        type = req.POST.get('type')

        try:
            amount = int(req.POST.get('cp'))
        except TypeError:
            amount = 0

        if amount == 0 or amount == '':
            redirect(req.path)
        elif type == 'withdraw':
            success = account.withdraw(req.user, amount)
        elif type == 'deposit':
            success = account.deposit(req.user, amount)

        redirect(req.path)


    return render(req, 'bank/index.html',
                  {'account': account, 'form': form_class, 'type': type, 'success': success})




