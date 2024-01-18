# hr_tool/serializers.py
from rest_framework import serializers
from .models import Location, Resume,Projects

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['city', 'country']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'project_name', 'others']




class ResumeSerializer(serializers.ModelSerializer):
    workplace_location = LocationSerializer()
    work_experience = ProjectSerializer(many=True)

    class Meta:
        model = Resume
        fields = ['id', 'name', 'experience', 'tech_skills', 'workplace_location', 'work_experience']

    def validate_experience(self, value):
        if value < 0:
            raise serializers.ValidationError("Experience must be a non-negative integer.")
        return value

    def create(self, validated_data):
        location_data = validated_data.pop('workplace_location')
        projects_data = validated_data.pop('work_experience', [])

        location = Location.objects.create(**location_data)

        # Create projects associated with the resume
        projects = []
        for project_data in projects_data:
            project = Projects.objects.create(project_name=project_data['project_name'], others=project_data.get('others', {}))
            projects.append(project)

        # Create the resume with the associated location
        resume = Resume.objects.create(workplace_location=location, **validated_data)

        # Associate the created projects with the resume
        resume.work_experience.set(projects)
        # resume.work_experience = projects

        print(" resume",resume)

        return resume



