from yafig_api.celery import app
import logging
from .models import Timeline, Post
from user.models import User, Relationship

logger = logging.getLogger(__name__)

@app.task
def generate_thumbnail():
    logger.info("Generating thumbnail")

@app.task
def publish_post_to_timelines(posted_by, post_id):
    logger.info("Publishing post to owner")

    user = User.objects.get(pk=posted_by)
    post = Post.objects.get(pk=post_id)
    Timeline.objects.create(user=user, post=post)

    # Find all users that follow the user that post the picture
    # user2 is the target user
    logger.info("Publishing post to followers")
    for relationship in Relationship.objects.filter(user2=user, type=Relationship.FRIEND):
        Timeline.objects.create(user=relationship.user1, post=post)
