from yafig_api.celery import app
import logging

logger = logging.getLogger(__name__)

@app.task
def generate_thumbnail():
    logger.info("Generating thumbnail")

@app.task
def publish_post_to_timelines():
    logger.info("Publishing post to timelines")
