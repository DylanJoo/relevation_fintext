import json
from django.conf import settings
from django.db import models

# Create your models here.
class Document(models.Model):
	docId = models.CharField(max_length=100)
	text = models.TextField()

	def __str__(self):
		return self.docId

	def get_content(self):
		content = ""
		try:
			with open(settings.DATA_DIR+"/"+self.docId) as f:
			    read = f.read()
			    try:
			        metadata = json.loads(read)['metadata']
			        self.text = "{} {} {} -- #{}".format(
			                metadata['company_name'],
			                metadata['form'],
			                metadata['filing_date'],
			                metadata['order'],
			        )
			        data = json.loads(read)
			        # for c in data['contents']:
			        #     print(c)
			        content = json.loads(read)['contents']
			    except:
			        content += read
		except Exception:
			content = "Could not read file %s" % settings.DATA_DIR+"/"+self.docId
		return content


category2label = {
        0: "type_0",
        1: "type_1",
        2: "type_2",
        3: "type_3",
        4: "type_4",
}
def default_query_categories():
    return {str(i): 0 for i in range(4)}

class Query(models.Model):
	# qId = models.IntegerField()
	qId = models.CharField(max_length=100)
	text = models.CharField(max_length=250)
	category = models.JSONField(default=default_query_categories)
	comment = models.TextField(default="", null=True)

	instructions = models.TextField(blank=True, null=True)
	criteria = models.TextField(blank=True, null=True)
	example = models.TextField(blank=True, null=True)

	def __str__(self):
		# categories = " ".join(self.category.values())
		data_dict = {
                "id": self.qId,
                "text": self.text,
                "highlight": self.comment,
                "categories": self.category,
		}
		to_return = json.dumps(data_dict)
		# return '{%s: %s}'% (self.qId, self.text)
		return to_return + '\n'

	def num_unjudged_docs(self):
		unjugded = [judgement for judgement in self.judgements() if judgement.relevance < 0]
		return len(unjugded)

	def num_judgements(self):
		return len(self.judgements())

	def judgements(self):
		return Judgement.objects.filter(query=self.id)

class Judgement(models.Model):

	labels = {-1: 'Unjudged', 0: 'Not relvant', 1: 'Somewhat relevant', 2:'Highly relevant'}

	query = models.ForeignKey(Query, on_delete=models.CASCADE)
	document = models.ForeignKey(Document, on_delete=models.CASCADE)
	comment = models.TextField(default="", null=True)
	relevance = models.IntegerField()

	def __str__(self):
		return '%s Q0 %s %s\n' % (self.query.qId, self.document.docId, self.relevance)

	def label(self):
		return self.labels[self.relevance]
