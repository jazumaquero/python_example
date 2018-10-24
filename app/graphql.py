from graphql.type.definition import *
from graphql.type.scalars import *
from graphql.type.schema import GraphQLSchema

from calendars.services import latest_business_day

QueryRootType = GraphQLObjectType(
    name='calendars',
    fields={
        'latest_business_day': GraphQLField(
            type=GraphQLString,
            args={
                'country': GraphQLArgument(GraphQLNonNull(GraphQLString)),
                'current_date': GraphQLArgument(GraphQLString),
                'shifted_days': GraphQLArgument(GraphQLString)
            },
            resolver=latest_business_day
        )
    }
)

schema = GraphQLSchema(QueryRootType, None)
