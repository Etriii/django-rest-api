
from django.db import models
from api.core.BaseModel import BaseModel

class UserSystem(BaseModel): 
    user = models.ForeignKey( 
        "User", on_delete=models.CASCADE, related_name="user_systems"
    )
    system = models.ForeignKey(
        "System", on_delete=models.CASCADE, related_name="system_users"
    )
    
    class Meta:
        db_table = "user_systems"

    def __str__(self):
        return f"User: {self.user.username}, System: {self.system.name}"
