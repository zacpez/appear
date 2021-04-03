# Appear
Appear is a CLI toolkit to generate application code.

* Swiftly write application code by leaving the repeatable tasks for a generator.
* Improve maintainability by making the application files consistent.
* Reduce copy-paste errors or dangling unused code by design.

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
