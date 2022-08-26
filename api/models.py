from django.db import models
 
class UserModel(models.Model):
    
    user_id = models.IntegerField(primary_key = True)
    cumulative_score = models.IntegerField()

    def __str__(self):
        return str(self.user_id)

