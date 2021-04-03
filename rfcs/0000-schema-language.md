# 0000-schema-language

- Start Date: 2021-04-03
- Target Major Version: (1.x)
- Reference Issues:
- Implementation PR:

# Summary

The schema language under discussion here is the description language that
Appear will use to generate code. The overarching design pattern follows
Resource Description Framework(RDF), under which has multiple data formats
or serializations. See the options in alternatives.

This proposal suggests the use of RDF as the source of the application code
schema. The serialized format of choice is [JSON-LD](https://w3c.github.io/json-ld-syntax/).

# Basic example

Example using inline context definition. But to note, definitions can be
separated or hosted externally too.

```json
{
  "@context": {
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "appear": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    ...
  },
  "@type": "appear:stack",
  "appear:title": "Users",
  "appear:class": {
    "@type": "rdfs:Class",
    "db:primaryKey": "user:user_id",
    "db:database": "<url>",
    "db:table": "user"
  },
  "appear:properties": [
    "user:user_id": {
      "@type": "rdf:Property",
      "db:col": "<url>",
      "db:colType": "int"
    },
    "user:name": {
      "@type": "rdf:Property",
      "db:col": "<url>",
      "db:colType": "string"
    },
    "user:verified": {
      "@type": "rdf:Property",
      "db:col": "<url>",
      "db:colType": "boolean"
    }
  ],
  "appear:build": {
    "@list": ["appear:frontend", "appear:backend", "appear:database"]
  },
  ...
}
```

# Motivation

`Why are we doing this?`

Using data to define initial application code to reduce the semantic
ambiguity, increase development speed, improved maintainability of an
application. The scope here is to choose a language that represents
definitions of resources as if writing an application from scratch.
The language must be generic enough to cover future applications'
representations.

`What use cases does it support?`

Creating applications from data definitions, not considering updates to
existing applications. From a business perspective, the purpose is to getting
to customized workflows with clients quickly.

`What is the expected outcome?`

Scope of work, deliverables:

```
1. A schema language choosen
2. Application schema namespaces hosted for use
3. Application code to read and validate developer schemas
4. Application summary
```

From a users perspective this supports:

```
Input schema files or command line arguments generate application files as output. Subsets of the application can be built as required by the developer.
```

# Detailed design

## Installation steps

Desired installation steps
```
pip install appear
```

## CLI Toolkit

Desired start of an application in a project folder

```bash
> appear init # Creates a `.appear` directory in your project.
> ls
  .
  .. 
  .appear/
  README.md
```

Desired build of an application in a project folder

```bash
> appear build # Creates project files in your project.
> ls
  .
  .. 
  .appear/
  frontend/
  backend/
  database/
  docker-compose.yml
  README.md
```

Desired summary of an application

```bash
> appear build --summary # returns metat data on .appear configs
Components: frontend, backend, database
Number of user Schemas: 12
Number of Template files: 144
...
```

## Hosting
Using a basic host provider to serve a schema for Appear.
http://appear-schema.org

Deliverables:

```
* Homepage
* Documentation deployment
* Activity Index of deployed schemas
```

### Semantic versioning
Use semantic versioning to versions the schema(eg. http://appear-schema.org/1/0/0/application-ns#)

## Resource definitions

There are likely more considerations to make for parent and child classifications. However, here is an initial list of namespaces.

### `appear:namespaces`

This is an index of all available namepsaces to use in Appear code generation.

MUST have URI http://appear-schema.org/1/0/0/namespaces#

### `appear:application`

Defines the general meta data of the application.

MUST have URI http://appear-schema.org/1/0/0/application-ns#

### `appear:asset`

Defines assets for the application, backend, frontend, database, or container.

MUST have URI http://appear-schema.org/1/0/0/asset-ns#

### `appear:backend`

Defines a backend framework, and its meta data.

MUST have URI http://appear-schema.org/1/0/0/backend-ns#

### `appear:build`

Defines application subsets and ordering for the build steps.

MUST have URI http://appear-schema.org/1/0/0/build-ns#

### `appear:container`

Defines generic containers, say docker for example.

MUST have URI http://appear-schema.org/1/0/0/container-ns#

### `appear:database`

Defines a datastore, such as postgres or mongoDB.

MUST have URI http://appear-schema.org/1/0/0/database-ns#

### `appear:frontend`

Defines a frontend framework.

MUST have URI http://appear-schema.org/1/0/0/frontend-ns#

### `appear:schema`

Defines an application object such as a user, page, form submission, etc.

MUST have URI http://appear-schema.org/1/0/0/schema-ns#

## Common recipes

Using flags to pull known common patterns, community support would be lovely.
```bash
> appear init --frontend=vue --backend=flask --database=postgres --container=nginx-proxy
```

# Drawbacks

`Why should we *not* do this?`

Defining a generic application structure for a universe of applications hard to future proof.

* Can you really support PaaS, SaaS, IaaS, and other services as they evolve?
* Can you really support all language options out there? 

Self-imposed limitations and considerations upfront:

* Web applications only
* No updating of existing applications
* Common recipes limited to Vue, Flask, Postgres, Docker
* No infrastructure orchestration(future terraform)
* Using more/less basic templates to facilitate builds, rather than a compiler
* Use existing open-source code generators where possible


# Alternatives

RDF has many serialization types.

* Turtle
* N-Triples
* N-Quads
* JSON-LD
* N3 or Notation3
* RDF/XML
* RDF/JSON

# Adoption strategy

Supply a GETTING_STATED.md

Supply multiple example applications or use cases.

# Unresolved questions

