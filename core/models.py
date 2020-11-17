from django.db import models
from django.contrib.auth import get_user_model

#User model 
User = get_user_model()

#tranfert methods 
TRANSFERT_METHODS = (
    ('F', 'FLOOZ to FLOOZ'),
    ('T', 'TMONEY to TMONEY'),
    ('FT', 'FLOOZ to TMONEY'),
    ('TF', 'TMONEY to FLOOZ')
)
class Method(models.Model):
    name = models.CharField(choices=TRANSFERT_METHODS, max_length=2)
    description = models.TextField()


class Transfert(models.Model):
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='sender_transaction')
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='receiver_transaction')
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    amount = models.IntegerField()
    transferred = models.BooleanField(default=True)




class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
