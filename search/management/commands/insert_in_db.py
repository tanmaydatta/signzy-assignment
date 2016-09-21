from django.core.management import BaseCommand
from search.models import *

    #The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
# Show this when the user types help
    help = "Inserting data to mysql"

    # A command must define handle()
    def handle(self, *args, **options):
		self.stdout.write("Getting data from files and making combinations .....")
		count = 0
		x = set([])
		f = open("search/firstnames.out")
		firstnames = f.readlines()
		f.close()
		f = open("search/lastnames.out")
		lastnames = f.readlines()
		f.close()
		for fn in firstnames:
			bulk_insert = []
			print "Inserting with first name as ", str(fn)
			for ln in lastnames:
				new_obj = Names()
				new_obj.firstname = fn
				new_obj.lastname = ln
				bulk_insert.append(new_obj)
			try:
				Names.objects.bulk_create(bulk_insert)
			except:
				pass
		self.stdout.write("Done !!!")
