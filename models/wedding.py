from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

from .base import BaseInvitationModel, Message


class Wedding(BaseInvitationModel):
    """
    The Wedding model
    """

    bride_name = fields.CharField(max_length=64)
    bride_parent_name = fields.CharField(max_length=64)
    groom_name = fields.CharField(max_length=64)
    groom_parent_name = fields.CharField(max_length=64)
    akad_start_datetime = fields.DatetimeField()
    akad_end_datetime = fields.DatetimeField(null=True)

    messages: fields.ManyToManyRelation["Message"] = fields.ManyToManyField(
        "models.Message", related_name="messages", through="wedding_message"
    )


WeddingDetailPydantic = pydantic_model_creator(Wedding, name="WeddingDetail")
WeddingCreatePydantic = pydantic_model_creator(
    Wedding, name="WeddingCreate", exclude_readonly=True
)
