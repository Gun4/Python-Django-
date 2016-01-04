from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from my_app.serializers import UserSerializer, GroupSerializer, TestSerializer, OrganizationSerializer,\
    ProjectMemberSerializer, ProjectSerializer, ProjectMemberRoleSerializer, ProjectSupplementSerializer
from my_app.models import Testtable, Organization,ProjectMember, Project, ProjectMemberRole, ProjectSupplement


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Testtable.objects.all()
    serializer_class = TestSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class ProjectMemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectMemberRoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ProjectMemberRole.objects.all()
    serializer_class = ProjectMemberRoleSerializer


class ProjectSupplementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ProjectSupplement.objects.all()
    serializer_class = ProjectSupplementSerializer