from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from ..models import School
from .serializers import SchoolCreateSerializer,SchoolReadSerializer,SchoolUpdateSerializer,SchoolDeleteSerializer,SchoolSummarySerializer
from .permissions import CanCreateSchool, CanUpdateSchool, CanDeleteSchool
from .throttles import CreateSchoolThrottle, UpdateSchoolThrottle
from .utils import CustomPagination


"""

| Action name (`self.action`) | HTTP Method(s) | URL pattern (assuming router prefix = `schools`) | What it does                        |
| --------------------------- | -------------- | ------------------------------------------------ | ----------------------------------- |
| **`list`**                  | GET            | `/schools/`                                      | Get a paginated list of all objects |
| **`retrieve`**              | GET            | `/schools/{pk}/`                                 | Get a single object by ID           |
| **`create`**                | POST           | `/schools/`                                      | Create a new object                 |
| **`update`**                | PUT            | `/schools/{pk}/`                                 | Replace an object (all fields)      |
| **`partial_update`**        | PATCH          | `/schools/{pk}/`                                 | Update only some fields             |
| **`destroy`**               | DELETE         | `/schools/{pk}/`                                 | Delete an object                    |


Extra actions
- Any time you add @action yourself, DRF will treat that as a new custom action.

The built-ins are only list, retrieve, create, update, partial_update, and destroy. Everything else you add with @action.

"""

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    pagination_class = CustomPagination # list actions use this
    
    def get_serializer_class(self):
        if self.action == "create":
            return SchoolCreateSerializer
        elif self.action == "retrieve":
            return SchoolReadSerializer
        elif self.action in ["update", "partial_update"]:
            return SchoolUpdateSerializer
        elif self.action == "destroy":
            return SchoolDeleteSerializer
        elif self.action == "summary":
            return SchoolSummarySerializer
        return SchoolReadSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [CanCreateSchool]
        elif self.action in ["update", "partial_update"]:
            permission_classes = [CanUpdateSchool]
        elif self.action == "destroy":
            permission_classes = [CanDeleteSchool]
        elif self.action == "summary":
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]  # default
        return [p() for p in permission_classes]

    def get_throttles(self):
        # pero enoiugh naman pud noon tung sa global nga throttle :>
        if self.action == "create":
            return [CreateSchoolThrottle()]
        elif self.action in ["update", "partial_update"]:
            return [UpdateSchoolThrottle()]
        return super().get_throttles()

    # 🔹 Custom action
    # @action(detail=False, methods=["get"], permission_classes=[AllowAny]) # default kasi is is IsAuthenticaed :>
    # or 
    @action(detail=True, methods=["get"])
    def summary(self, request, pk=None):
        school = self.get_object()
        serializer = self.get_serializer(school)
        return Response(serializer.data)


    # Overriding the create method
    def create(self, request, *args, **kwargs):
        data = request.data
        
        # Manually checking if the user has permission (Optional if naa kay gusto nga custom validation before nimo ipa proceed :>)
        permission = IsAuthenticated()
        if not permission.has_permission(request, self):
            return Response({"error": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)
        
        if 'name' not in data:
            return Response({"error": "Name field is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # If everything is fine, proceed with the normal create
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)