from django.contrib.auth.models import User, Group
from rest_framework import serializers
from my_app.models import Testtable, Organization, ProjectMember, Project, ProjectMemberRole, ProjectSupplement
from customField import Base64Field


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TestSerializer(serializers.HyperlinkedModelSerializer):
    image = Base64Field()
    class Meta:
        model = Testtable
        fields = ('username', 'image')


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organization
        fields = ('org_id', 'org_name')


class ProjectMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectMember
        fields = ('project_member_name', 'project_member_email', 'project_member_phone', 'project_member_address',
                  'project_member_org')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('project_id', 'project_org', 'project_title', 'project_client_ref')


class ProjectMemberRoleSerializer(serializers.HyperlinkedModelSerializer):
    #project_id = serializers.SlugRelatedField(slug_field=Project.project_id, queryset=User.objects.all(), required=False)
    class Meta:
        model = ProjectMemberRole
        fields = ('project_id', 'member_id', 'roles')


class ProjectSupplementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectSupplement
        fields = ('project_supplement_project', 'project_supplement_rush', 'project_supplement_material_info',
                  'project_supplement_objectives','')