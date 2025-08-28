# # 1. Collection-level (no ID required, like /students/search/)
# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     @action(detail=False, methods=["get"])
#     def search(self, request):
#         q = request.query_params.get("q", "")
#         students = Student.objects.filter(name__icontains=q)
#         serializer = self.get_serializer(students, many=True)
#         return Response(serializer.data)


# # ➡️ Now you can hit:
# # GET /students/search/?q=alice
# # and it will return filtered students.

# # 2. Object-level (requires ID, like /students/{id}/promote/)
#     @action(detail=True, methods=["post"])
#     def promote(self, request, pk=None):
#         student = self.get_object()
#         # example: add " (Promoted)" to their name
#         student.name = student.name + " (Promoted)"
#         student.save()
#         serializer = self.get_serializer(student)
#         return Response(serializer.data)


# # ➡️ Now you can hit:
# # POST /students/5/promote/
# and it will apply your custom logic for student 5.