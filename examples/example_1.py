#!/use/bin/env python3

from torment import Store,Literal,URI
from uuid import uuid4

store = Store('https://example.org/')
foaf = store.register('foaf', 'http://xmlns.com/foaf/0.1/')

@store.id('/agent/', uuid4)
@store.type('/vocab/Person')
class Person(store.rdfs.Resource):
    name = Literal('name', property=foaf.name, required=True)
    email = Literal('email', property=foaf.email)

print(store.context)

# {
#   "@context": {
#     "name": "http://xmlns.com/foaf/0.1/name",
#     "email": "http://xmlns.com/foaf/0.1/email"
#   }
# }

person = Person(name="XYZ")
person.email = "xyz@example.org"
store.add(person)

print(store.all())

# [
#   {
#     "@context": { ... },
#     "@id": "https://example.org/agent/633be6da-8eef-4988-b3ac-a3f760e61847",
#     "@type": "https://example.org/vocab/Person",
#     "name": "XYZ",
#     "email": "xyz@example.org"
#   }
# ]


