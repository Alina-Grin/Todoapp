from django.core.management import BaseCommand
from django.utils import timezone
from datetime import datetime
from tasks.models import TodoItem
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = u"Analize user-activity and their tasks from db"

    #def add_arguments(self, parser):
        #parser.add_argument('--file', dest='input_file', type=str)

    def handle(self, *args, **options):
    	count=0
    	for u in User.objects.all():
            for t in u.tasks.all():
            	if t.is_completed==True:
            		count+=1
    	#print(count)
    	count_task_dict={}
    	count_task_not_comlpete_dict={}
    	for u in User.objects.all():
    		count_task=0
    		count_not_complete=0
    		for t in u.tasks.filter(owner=u):
    			count_task+=1
    			count_task_dict[u]=count_task
    			if t.is_completed==False:
    				count_not_complete+=1
    				count_task_not_comlpete_dict[u]=count_not_complete
    	sorted_by_value = sorted(count_task_dict.items(), key=lambda kv: kv[1], reverse=True)
    	d = {k: v for k, v in count_task_not_comlpete_dict.items() if v < 20}
    	sorted_not_comlpete_dict=sorted(count_task_not_comlpete_dict.items(), key=lambda kv: kv[1], reverse=True)
    	print(sorted_not_comlpete_dict, len(d))