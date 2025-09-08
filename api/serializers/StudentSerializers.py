from rest_framework import serializers
from api.models import Student
from api.serializers import ProgramSerializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ["id"]

class StudentReadSerializer(serializers.ModelSerializer):
    program = ProgramSerializers.ProgramSlimReadSerializer()

    class Meta:
        model = Student
        fields = "__all__"


class StudentReadSlimSerializer(serializers.ModelSerializer):
    # program_id = serializers.CharField(source="program.name", read_only=True)
    # program = serializers.CharField(source="program.name", read_only=True)
    # institute_id = serializers.CharField(source="program.institute.id", read_only=True)
    # institute = serializers.CharField(source="program.institute.institute_name", read_only=True)
    # school_id = serializers.CharField(source="program.institute.school.id", read_only=True)
    # school = serializers.CharField(source="program.institute.school", read_only=True)
    program = ProgramSerializers.ProgramSlimReadSerializer()            

    class Meta:
        model = Student
        exclude = ["created_at", "updated_at"]
