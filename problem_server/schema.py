import graphene

from core.schema import Query as CoreQuery

class Query(CoreQuery):
	hello_world = graphene.String(default_value='Hello, World!')


schema = graphene.Schema(query=Query)
