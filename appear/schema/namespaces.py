from rdflib.namespace import DC, RDF, RDFS, OWL, ClosedNamespace, URIRef
from rdflib import Graph, Literal


def generate_schema(version, date):
    """Example namespace building"""

    versions = version.split('.')
    HOST_URL = "http://appear-schema.org/{}/{}/{}/".format(versions[0],
                                                           versions[1],
                                                           versions[2])
    APPEAR = ClosedNamespace(URIRef("{}namespaces#".format(HOST_URL)),
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

    g = Graph()
    g.bind("rdf", RDF)
    g.bind("rdfs", RDFS)
    g.bind("owl", OWL)
    g.bind("dc", DC)
    g.bind("appear", APPEAR)

    g.add((APPEAR.namespace, RDF.type, OWL.Ontology))
    g.add((APPEAR.namespace, DC.title, Literal("Appear schemas")))
    g.add((APPEAR.namespace, DC.date, Literal(date)))
    g.add((APPEAR.namespace, DC.description, Literal(
        "This namespace includes all Appear schemas")))
    g.add((APPEAR.application, RDF.type, RDFS.Class))
    g.add((APPEAR.application, RDFS.isDefinedBy, URIRef("{}application#".format(HOST_URL))))
    g.add((APPEAR.application, RDFS.label, Literal('Application')))
    return g.serialize(format='turtle').encode('utf-8')
