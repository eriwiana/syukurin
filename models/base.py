from enum import Enum
from tortoise import fields
from tortoise import models
from tortoise.validators import MinLengthValidator


class BaseModel(models.Model):
    id = fields.UUIDField(pk=True)
    created_on = fields.DatetimeField(auto_now_add=True)
    modified_on = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseInvitationModel(BaseModel):
    start_datetime = fields.DatetimeField()
    end_datetime = fields.DatetimeField()
    venue_name = fields.CharField(max_length=64)
    venue_maps = fields.CharField(max_length=40)
    audio_link = fields.CharField(max_length=255, null=True)
    video_link = fields.CharField(max_length=255, null=True)
    active_until = fields.DatetimeField()
    template = fields.CharField(max_length=10)
    gallery_url = fields.CharField(max_length=255, null=True)
    donation = fields.CharField(
        max_length=255, null=True, description="Link/Account to donate."
    )

    class Meta:
        abstract = True


class Message(BaseModel):
    """Message model"""

    class Respond(str, Enum):
        YES = "Yes"
        MAYBE = "Maybe"
        NO = "No"

    guest_name = fields.CharField(max_length=64, index=True)
    content = fields.TextField(validators=[MinLengthValidator(16)])
    respond = fields.CharEnumField(Respond, default=Respond.MAYBE, index=True)
