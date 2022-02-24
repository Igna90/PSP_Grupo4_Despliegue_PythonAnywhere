from rest_framework import serializers
from nucleo.models import Participate, Project, User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','username','password','role_user']
        
class ParticipateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Participate
        fields = ['id','idCliente','idProject','registrationDate','rol']
        
class ProjectsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','title','description','level','startDate','endDate','endReport','idEmployee','idCategory']