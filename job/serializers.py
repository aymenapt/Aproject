from rest_framework import serializers
from.models import *
from challenges.serializers import ChallengesSreilalizer

class JobOfferSerializer(serializers.ModelSerializer):
    challenge = ChallengesSreilalizer(many=True, read_only=True)
    class Meta:
        model = JobOffer
        fields = ('id', 'name', 'descreption', 'skillsrequirment', 'jobbenifits', 'employment_nedded', 'image', 'challenge')
