from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from lbforum.models import LBForumUserProfile

User = get_user_model()


class Command(BaseCommand):
    help = "Init LBForumUserProfile"

    def handle(self, **options):
        users = User.objects.all()
        for o in users:
            try:
                o.lbforum_profile
            except LBForumUserProfile.DoesNotExist:
                LBForumUserProfile.objects.create(user=o)
