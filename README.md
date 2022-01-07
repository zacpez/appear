# Appear

[![Project Status: Concept – Minimal or no implementation has been done yet, or the repository is only intended to be a limited example, demo, or proof-of-concept.](https://www.repostatus.org/badges/latest/concept.svg)](https://www.repostatus.org/#concept)

Appear is a CLI toolkit to generate application code.

* Swiftly write application code by leaving the repeatable tasks for a generator.
* Improve maintainability by making the application files consistent.
* Reduce copy-paste errors or dangling unused code by design.

## Installation steps

Appear can be installed with Python package manager.
``` bash
$ pip install appear
```

OR

Clone and install the latest version of Appear directly
```bash
$ pip install git+https://github.com/zacpez/appear@main
```

## Getting started

Initialize an Appear configuration in a project folder. Initialization
without setting flags will create a skeleton configuration folder, and
the develop must fill out their own schema and templates.

```bash
$ pwd 
  /my/projects/new_project
$ appear init # Creates a `.appear` directory in your project.
$ ls
  .appear/
  README.md
```

Create a configuration with preferred starting templates. Using flags such as
the example below, will create schemas and templates that match the stack
described. The application will be bare bones, but the app can stand up easily.

```bash
$ appear init --frontend=vue --backend=flask --database=postgres --container=nginx-proxy
$ tree .appear
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

After setting up the application configuration run a build the project folder.

```bash
$ appear build # Creates project files in your project.
$ ls
  .appear/
  frontend/
  backend/
  database/
  docker-compose.yml
  README.md
```

Check some basic statistics of the application configuration. This can be handy
to validate the build.

```bash
$ appear build --summary # returns meta data on .appear configs
Components: frontend, backend, database
Number of user Schemas: 12
Number of Template files: 144
...
```

## RFC Process
In this project we will follow an [RFC process that vuejs follows](https://github.com/vuejs/rfcs). It is a github-based workflow that is manageable for a project like this. Below is a reiteration of the above link, please read both.

### Scope

The intention is that RFCs capture the larger ideas that require significant forethought, design, and planning. Smaller issues can be submitted through a usual Pull Request(PR) such as bugs, hardening, and feature extensions.

### Definition & Lifecycle

To submit an RFC, create a PR with RFC labelm, and a title starting with `"RFC:"`, for example `RFC: First application code languages and frameworks`. The content of the RFC will reside in the ``/rfcs/`` directory RFCs will formatted as a Markdown file with incrementing file number and a unique feature name.
Please follow the [template](https://github.com/vuejs/rfcs/blob/master/0000-template.md) for a RFC, this will ensure fewer edits before implementation.
```
/rfcs/
  + 0000-project-name.md
```

An RFC has an associated status

1. **Pending**: Submitted and under public review as an open PR
2. **Active**: RFC clarifications complete, and implementations underway
3. **Landed**: Implementation complete and released
4. **Rejected**: Rejected during public review, a closed PR

## Contribution

In addition to RFC contribution we also follow an [implementation contribution guide](CONTRIBUTION.md). Thanks goes to [PurpleBooth](https://gist.github.com/PurpleBooth) for supplying a [template contribution file](https://gist.github.com/PurpleBooth/b24679402957c63ec426).
