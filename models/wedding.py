from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

from .base import BaseModel


class Wedding(BaseModel):
    """
    The Wedding model
    """

    bride_name = fields.CharField(max_length=64)
    bride_parent_name = fields.CharField(max_length=64)
    groom_name = fields.CharField(max_length=64)
    groom_parent_name = fields.CharField(max_length=64)
    akad_datetime = fields.DatetimeField()
    reception_datetime = fields.DatetimeField()
    venue_name = fields.CharField(max_length=64)
    venue_maps = fields.CharField(max_length=40)
    active_until = fields.DatetimeField()
    audio_link = fields.TextField(null=True)
    video_link = fields.TextField(null=True)


WeddingDetailPydantic = pydantic_model_creator(Wedding, name="WeddingDetail")
WeddingCreatePydantic = pydantic_model_creator(
    Wedding, name="WeddingCreate", exclude_readonly=True
)
