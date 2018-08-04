---
title: 'Containershare: Open Source Registry to build, test, deploy with CircleCI'
tags:
  - containers
  - continuous integration
  - circleci
  - docker
  - api
  - reproducibility
authors:
 - name: Vanessa Sochat
   orcid: 0000-0002-4387-3819
   affiliation: 1
affiliations:
 - name: Stanford University Research Computing
   index: 1
date: 04 August 2018
bibliography: paper.bib
---

# Summary

Containershare is an open source library of containers, both providing itself as a [template](https://www.github.com/vsoch/containershare), a [library](https://vsoch.github.io/containershare), and production [application programming interface](https://vsoch.github.io/containershare/library.json) (API) for interested users. Specifically, it is a complete metadata registry that can be freely deployed directly from a Github repository to validate and serve tested, tagged, and version controlled containers, each maintained from independent Github repositories. The registry uses several open source and free to use solutions to accomplish this, and brings them together programatically with steps that are easy for the user to set up. Specifically, the user must connect the repository to the continuous integration service CircleCI [@noauthor_undated-nt] and then turn on Github Pages [@noauthor_undated-vt] from the repository web interface. After these steps, adding text files to describe other container repositories via pull requests will test the submissions, and programatically add them to all components of the library.

![https://vsoch.github.io/assets/images/posts/containershare/table.png](https://vsoch.github.io/assets/images/posts/containershare/table.png)

## Container Repository Templates

The individual container repository is responsible for serving its own metadata that the containershare can discover, validate, and provide for the user. It is also driven by a simple definition of a general CircleCI workflow, including building of a container, extraction of metadata, and then deployment of the container to Docker Hub and metadata files and user interface back to Github Pages. The workflow definitions to accomplish this are provided by containershare, and include:

 - A table of version controlled containers, where each commit is associated with a tagged container for the user to interact with

![https://vsoch.github.io/assets/images/posts/containershare/share.png](https://vsoch.github.io/assets/images/posts/containershare/share.png)

 - A complete list of tags for a program to discover and consistently query for the associated container metadata
 - The traditional image manifests that are provided by Docker Hub
 - An "inspection" of the container that includes package manager packages and versions, along with a listing of files and sizes inside of the container, extracted during the build step using the open source Container Diff [@noauthor_undated-hl] tool provided by Google Open Source.

 ![https://vsoch.github.io/assets/images/posts/containershare/inspect.png](https://vsoch.github.io/assets/images/posts/containershare/inspect.png)

Containershare serves as a general skeleton that can be extended to several use cases and themes, including sharing of containers for behavioral paradigms, open source publications, or components to scientific workflows. The use of open source tools like Github and CircleCI means that the implementation is completely transparent and customizable for an individual or institutional needs. For a research scientist, submission of a container repository to a containershare gives confidence that the container can be discovered. For a service provider, deployment of a container share (and subsequent provision of containers using it) gives confidence that the service users have a central location to discover containers, and API to discover them programmatically. Containershare and links to container repository templates are provided for use from [the containershare repository](https://www.github.com/vsoch/containershare), contributions in the way of code or issues are encouraged, and for interested readers, a more descriptive writeup [is available](https://vsoch.github.io/2018/build-deploy-docs/).

# References
