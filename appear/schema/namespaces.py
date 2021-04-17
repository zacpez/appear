from rdflib.namespace import DC, RDF, RDFS, OWL, ClosedNamespace, URIRef
from rdflib import Graph, Literal
from .. import __version__, __date__


APPEAR = ClosedNamespace(URIRef("http://appear-schema.org/1/0/0/namespaces#"),
                         terms=[
    "namespace",
    "application",
    "asset",
    "backend",
    "frontend",
    "container",
    "build",
    "schema"
])


def generate_schema():
    g = Graph()
    g.bind("rdf", RDF)
    g.bind("rdfs", RDFS)
    g.bind("owl", OWL)
    g.bind("dc", DC)
    g.bind("appear", APPEAR)

    g.add((APPEAR.namespace, RDF.type, OWL.Ontology))
    g.add((APPEAR.namespace, DC.title, Literal("Appear schemas")))
    g.add((APPEAR.namespace, DC.date, Literal(__date__)))
    g.add((APPEAR.namespace, DC.description, Literal(
        "This namespace includes all Appear schemas")))
    g.add((APPEAR.application, RDF.type, RDFS.Class))
    g.add((APPEAR.application, RDFS.isDefinedBy, URIRef(
        "http://appear-schema.org/1/0/0/application")))
    g.add((APPEAR.application, RDFS.label, Literal('Application')))

    print(__version__)
    return g.serialize(format='turtle').decode('utf-8')
