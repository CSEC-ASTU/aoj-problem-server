import graphene

from graphene_django import DjangoObjectType
from core.models import Contest, Problem, SampleInput, SampleOutput, Sponsor
from graphene_django.filter import DjangoFilterConnectionField

class SampleInputNode(DjangoObjectType):
	class Meta:
		model = SampleInput
		filter_fields = '__all__'
		interfaces = (graphene.relay.Node,)

class SampleOutputNode(DjangoObjectType):
	class Meta:
		model = SampleOutput
		filter_fields = '__all__'
		interfaces = (graphene.relay.Node,)

class ProblemNode(DjangoObjectType):
	sample_input = DjangoFilterConnectionField(SampleInputNode)
	sample_output = DjangoFilterConnectionField(SampleOutputNode)

	class Meta:
		model = Problem
		filter_fields = '__all__'
		interfaces = (graphene.relay.Node,)

class SponsorNode(DjangoObjectType):
	class Meta:
		model = Sponsor
		filter_fields = '__all__'
		interfaces = (graphene.relay.Node,)

class ContestNode(DjangoObjectType):
	problems = DjangoFilterConnectionField(ProblemNode)
	sponsors = DjangoFilterConnectionField(SponsorNode)

	class Meta:
		model = Contest
		filter_fields = '__all__'
		interfaces = (graphene.relay.Node,)

	def resolve_length(root, info):
		return root.length.total_seconds()

	def resolve_problems(root, info):
		return root.problems.all()

	def resolve_sponsors(root, info):
		return root.sponsors.all()

class Query(graphene.ObjectType):
	contest = graphene.relay.Node.Field(ContestNode)
	contests = DjangoFilterConnectionField(ContestNode)
	problem = graphene.relay.Node.Field(ProblemNode)
	problems = DjangoFilterConnectionField(ProblemNode)

schema = graphene.Schema(query=Query)