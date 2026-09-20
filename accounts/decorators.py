from django.contrib.auth.decorators import login_required, user_passes_test


def owner_required(view):
    return login_required(user_passes_test(
        lambda u: u.is_superuser or u.groups.filter(name='Owner').exists())(view))