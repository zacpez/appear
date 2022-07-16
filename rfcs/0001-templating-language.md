# 0000-template-language

- Start Date: 2021-04-04
- Target Major Version: (1.x)
- Reference Issues:
- Implementation PR:

## Summary

The template language under discussion here is the string formatting language
that Appear will use to generate code. The overarching design pattern follows
file-based templates, under which a search and replace method renders many new
files with data inserted.
See the options in alternatives.

This proposal suggests the use of [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/)
as the source of the application code templates.

## Basic example

Example using inline context definition. But to note, definitions can be
separated or hosted externally too.

```jinja
{# Example vue component #}
<template>
{% block component.template %}{% endblock %}
</template>

<style>
{% block component.style %}{% endblock %}
</style>

<script>
export default {
  props: {
  {% for prop in component.properties %}
    type: {{ prop.type }},
    default: {{ prop.default }},
    required: {{ prop.required }},
  {% endfor %}
  },
  ...
};
</script>
```

```jinja
{# Example REST API #}
from flask import Flask, jsonify
app = Flask(__name__)

{% for endpoint in application.endpoints %}
from .models.{{ endpoint.subject_domain }} import {{ endpoint.subject_class }}
{% endfor %}

{% for endpoint in application.endpoints %}
@app.route('{{ endpoint.uri }}/<id>', methods=["GET"])
def {{ endpoint.name }}():
    result = {{ endpoint.subject_class }}.find_by_id(id)
    return jsonify({ 'item': result })

@app.route('{{ endpoint.uri }}/list/', methods=["GET"])
def {{ endpoint.name }}():
    result = {{ endpoint.subject_class }}.query.all()
    return jsonify({ 'list': result })
{% endfor %}
```

## Motivation

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

```text
1. A template language chosen
2. Application common recipe templates available for use
3. Application code writable to project folders
```

## Detailed design

The scope of the design encompasses a number of example jinja files with
an application to render them. The application is easy to acquire and run.
In the initial version there will be a singular technology stack chosen to
be rendered as output: Vue, Flask, SQLAlchemy, Pytest, Postgres, nginx proxy.

## Installation steps

Desired installation steps

```bash
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
> appear build --summary # returns meta data on .appear configs
Components: frontend, backend, database
Number of user Schemas: 12
Number of Template files: 144
...
```

Create a config with preferred starting templates

```bash
> appear init --frontend=vue --backend=flask --database=postgres --container=nginx-proxy
> tree .appear
.
├── templates
│   ├── frontend
│   │   ├── component.vue.jinja
│   │   ├── page.vue.jinja
│   │   ├── app.vue.jinja
│   │   └── app.docker.jinja
│   ├── proxy
│   │   └── nginx.docker.jinja
│   ├── backend
│   │   ├── model.sqlalchemy.jinja
│   │   ├── app.flask.jinja
│   │   ├── test.pytest.jinja
│   │   └── app.docker.jinja
│   └── database
│       ├── fixture.postgres.jinja
│       └── app.docker.jinja
└── schema
    ├── user
    │   ├── user.assignment.json
    │   ├── user.history.json
    │   └── user.roles.json
    ├── page
    │   ├── page.content.json
    │   └── page.plugin.json
    └── form
        ├── form.fields.json
        └── form.submission.json
```

## Drawbacks

`Why should we *not* do this?`

Defining a templates for many application structure will be time consuming.

- Can you really support PaaS, SaaS, IaaS, and other services as they evolve?
- Can you really support all language options out there?

Self-imposed limitations and considerations upfront:

- Web applications only
- No updating of existing applications
- Common recipes limited to Vue, Flask, Postgres, Docker
- No infrastructure orchestration(future terraform)
- Using more/less basic templates to facilitate builds, rather than a compiler
- Use existing open-source code generators where possible

## Alternatives

There are many ways to write files, with a search and replace pattern.

- [Inline Perl](https://www.perl.com/pub/2001/08/21/templating.html/)
- [PHP Twig](https://twig.symfony.com/)

## Adoption strategy

Supply a GETTING_STATED.md

Supply multiple example applications or use cases.

## Unresolved questions
