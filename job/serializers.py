from rest_framework import serializers
from.models import *
from challenges.serializers import ChallengesSreilalizer

class JobOfferSerializer(serializers.ModelSerializer):
    challenge = ChallengesSreilalizer(many=True, read_only=True)
    image_url = serializers.SerializerMethodField()
    def get_image_url(self, obj):
          if obj.image:
            return f"http://127.0.0.1:8000{obj.image.url}"
          return None
    class Meta:
        model = JobOffer
        fields = ('id', 'name', 'descreption', 'skillsrequirment', 'jobbenifits', 'employment_nedded', 'image','image_url', 'challenge')
