import os
import datetime
from datetime import timedelta

Date = datetime.datetime.now()
def populate():
	
	f=open("issue_names.txt")
	for line in f:
		cname=line.replace("\n","")
		cat_added=add_category(cname)
	f.close()

def add_category(cname):
    cat = Issue.objects.get_or_create(name=cname,date_created=Date,date_modified=Date)[0]#for now description is same as category_names
    print "category " +str(cname)+" added at "+str(Date)
    return cat

# Start execution here!
if __name__ == '__main__':
    print "Starting population script for adding category..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'forums.settings')
    from website.models import *
    populate()
