# Repo2Docker Container Library

<img src="https://vsoch.github.io/lessons/assets/img/logo-book.png" width="100px">

[![CircleCI](https://circleci.com/gh/vsoch/repo2docker-containers.svg?style=svg)](https://circleci.com/gh/vsoch/repo2docker-containers)

This is the library of repo2docker experiment containers provided for use on the Sherlock cluster via the [forward](https://www.github.com/vsoch/forward) tool. See the README at the link for usage instructions for forward.

## Tutorials
Example tutorials are provided for:

  - https://vsoch.github.io/lessons/sherlock-singularity/
  - https://vsoch.github.io/lessons/jupyter-tensorflow/

# Usage

## Run a Container

You can browse available containers [here](https://vsoch.github.io/repo2docker-containers). The basic usage to use a container from the list:

 1. Follow [instructions](https://www.github.com/vsoch/forward) to configure the forward tool. There are also good instructions available in the tutorials above (one time only!)
 2. Using the forward tool, the basic command would be as follows:

```bash
start.sh singularity
```

## Contribute a Container

To contribute a new container:

 1. Use the repo2docker [continuous builder](https://github.com/vsoch/continuous-build) to generate a container from a jupyter notebook and requirements.txt file.
 2. Fork this repository, pull your fork on your local machine, and create a new branch for your container.
 3. Once the container is deployed on Docker Hub (step 1) add a markdown file to the [_containers](_containers) folder. 
 4. Open a pull request to the master branch to add your contribution!

When the pull request is merged, the container will be added to the table for others to use.
