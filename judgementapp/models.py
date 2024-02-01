import json
from django.conf import settings
from django.db import models

# Create your models here.
class Document(models.Model):
	docId = models.CharField(max_length=100)
	text = models.TextField()
	# add document

	def get_topic(self):
	    if '_item1_' in self.docId: # business --> 1
	        return 1
	    if '_item2_' in self.docId: # risk --> 2
	        return 3
	    if '_item3_' in self.docId: # legal --> 3
	        return 4
	    if '_item8_' in self.docId: # financial status --> 8
	        return 5
	    if '_item7_' in self.docId: # operation --> 7
	        return 5
	    return 0

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
			        content = json.loads(read)['contents']
			    except:
			        content += read
		except Exception:
			content = "Could not read file %s" % settings.DATA_DIR+"/"+self.docId
		return content

# label2topic = {
#         1: "Business",
#         2: "Risk",
#         3: "Legal",
#         4: "Financial Status",
#         5: "Strategic Plan",
#         6: "Operataionl",
# }

label2topic = {
        1: "Overview",
        2: "Industry",
        3: "Risk",
        4: "Legal",
        5: "Financial Status",
        6: "Strategy",
        7: "Operation",
        0: "Others",
}

label2subtopic = {
        '3-1': "Government",
        '7-1': "Capital",
        '7-2': "Accounting",
}

label2type = {
        0: "trivial",
        1: "company-specific",
        2: "change/action",
        3: "reason",
        4: "redirect",
}

def default_query_categories():
    return {str(i): 0 for i in label2type}

def default_query_topics():
    return {str(i): 0 for i in label2topic}

class Query(models.Model):
	# qId = models.IntegerField()
	qId = models.CharField(max_length=100)
	text = models.CharField(max_length=250, default="NA")
	type = models.JSONField(default=default_query_categories)
	comment = models.TextField(default="", null=True)
	topic = models.JSONField(default=default_query_topics)
	metadata = models.TextField()

	def get_topic(self):
	    to_return = []
	    for topic, value in self.topic.items():
	        if value == 1:
	            to_return.append(label2topic[int(topic)])
	        if value > 1:
	            value = f"{topic}-{value}"
	            to_return.append(label2topic[int(topic)])
	    return to_return

	def __str__(self):
		data_dict = {
                "id": self.qId,
                "text": self.text,
                "highlight": self.comment,
                "type": self.type,
                "topic": self.topic,
		}
		to_return = json.dumps(data_dict)
		# return '{%s: %s}'% (self.qId, self.text)
		return to_return + '\n'

	def unclassified(self):
		return sum([int(v) for v in self.type.values()]) == 0

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
