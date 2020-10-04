from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Userorders

def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'userprofiles/userprofile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def profile_order_history(request, orderid):
    order = get_object_or_404(Userorders, orderid=orderid)

    messages.info(request, (
        f'This is a past confirmation for order number {orderid}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/confirmcheckout.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)