# Containershare

<img src="https://vsoch.github.io/lessons/assets/img/logo-book.png" width="100px">

This is an open source library of containers. You can come here for one of several use cases:

 1. You want to [browse available containers](https://vsoch.github.io/containershare) provided for use locally or on the Sherlock cluster via the [forward](https://www.github.com/vsoch/forward) tool.
 2. You want to [contribute a container](#contribute-a-container) to this registry, meaning that your code gets packaged in a reproducible way, deployed for sharing, and with exposure of metadata like packages and files.
 3. You want to deploy your own [open source registry](#deploy-a-registry) all with freely available, easy to use tools that you are already familiar with.

Continue reading for details on the above, or [ask a question](https://www.github.com/vsoch/containershare/issues) if you need help.

# Use Cases

## Run a Container

You can browse available containers [here](https://vsoch.github.io/containershare). The basic usage to use a container from the list:

 1. Follow [instructions](https://www.github.com/vsoch/forward) to configure the forward tool. There are also good instructions available in the tutorials above (one time only!)
 2. Using the forward tool, the basic command would be as follows:

```bash
start.sh singularity
```

## Contribute a Container

### Step 1. What kind of container?
To contribute a new container, first decide what kind of container you want to build.

### Repo2Docker
Do you have a jupyter (or similar) notebook and want to quickly build and deploy it? You will want to use the [repo2docker template](https://github.com/vsoch/share-repo2docker) that uses the [continuous builder](https://github.com/vsoch/continuous-build) to generate a container from a jupyter notebook and requirements.txt file.

### General Docker
If you have a general Docker container that is built from a Dockerfile in your repository, check out the
[share-docker template](https://github.com/vsoch/share-docker).

### Step 2. Submit Metadata

After doing the above, you will have a repository that is hooked up to continuous integration, and deploys to Docker Hub. The rest from here is easy! You just need to submit this repository. How do you do that?

 1. Fork this repository, pull your fork on your local machine, and create a new branch for your container.
 2. Once the container is deployed on Docker Hub (step 1) add a markdown file to the [_containers](_containers) folder. 
 3. Open a pull request to the master branch to add your contribution!

When the pull request is merged, the container will be added to the table for others to use.


## Deploy a Registry
If you want to deploy your own containershare, it's just a matter of forking this repository, and turning on Github pages to deploy from the docs folder, and then connecting the repository to circleci. Once this is done, third parties (others) should be able to equivalently submit pull requests to your registry that are tested, and upon merge, the container contribution added to the table, and the container available for discovery via the API exposed by the registry.

# Forward Tutorials
Example tutorials are provided for:

  - [Singularity on Sherlock](https://vsoch.github.io/lessons/sherlock-singularity/)
  - [Tensorflow on Sherlock](https://vsoch.github.io/lessons/jupyter-tensorflow/)
