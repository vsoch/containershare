# Containershare

<img src="https://vsoch.github.io/lessons/assets/img/logo-book.png" width="100px">

This is an open source library of containers. You can come here for one of several use cases:

 1. You want to [use a container](#use-a-container) that is available from the [browsable library](https://vsoch.github.io/containershare) provided by the registry. You can use the container locally, or as a suggestion for a shared resource that requires a graphical forward, you can use the [forward](https://www.github.com/vsoch/forward) tool.
 2. You want to contribute or use a [containershare template](#containershare-templates). Contributing means that your code gets packaged in a reproducible way, deployed for sharing, and with exposure of metadata like packages and files.
 3. You want to deploy your own [open source containershare](#deploy-a-containershare) all with freely available, easy to use tools that you are already familiar with.

Read about the development and [use cases here](https://vsoch.github.io/2018/build-deploy-docs/), and please reference the software if it is useful to you:

[![DOI](http://joss.theoj.org/papers/10.21105/joss.00878/status.svg)](https://doi.org/10.21105/joss.00878)
[![DOI](https://zenodo.org/badge/142066803.svg)](https://zenodo.org/badge/latestdoi/142066803)

Continue reading for details on the above, or [ask a question](https://www.github.com/vsoch/containershare/issues) if you need help.
Or jump down to one of our [templates](#containershare-templates):

# Container Repository Templates
Here are some [helpful templates](#containershare-templates) to get you started! Detailed instructions and usage can be found in their respective repositories.

 - [repo2docker](#repo2docker): A vanilla starter jupyter notebook. With pokemon. Highly recommended.
 - [repo2docker-r](#repo2docker-r): A notebook with R, Rstudio, and a shiny example.
 - [repo2docker-conda](#repo2docker-conda): If you like snakes and notebooks, this Miniconda starter is for you!
 - [repo2docker-julia](#repo2docker-julia): a notebook with the julia programming language.
 - [General Docker](#general-docker): You can build just a Dockerfile too.

For all of the above, jump down to the links to try out examples! If you have a request for a new template, please [ask](https://www.github.com/vsoch/containershare/issues).


# Use Cases

## Run a Container

You can browse available containers [here](https://vsoch.github.io/containershare). You can use a container is several ways!

 1. Follow [instructions](https://www.github.com/vsoch/forward) to configure the forward tool. There are also good instructions available in tutorials linked from that repository.
 2. Find a container you like, and pull directly with Docker or [Singularity](https://singularityware.github.io) for a shared HPC resource.
 3. Use the `containershare` library (under development) that will allow you to search container metadata and inspected content.

## Containershare Templates

### Step 1. What kind of container?
To contribute a new container, first decide what kind of container you want to build. We have getting started guides and templates for multiple kinds, along with examples for you to quickly demo them. For all of the containers below, we name them `repo2docker` 
and use the same port (`8888`) so be sure to change this if you want to run multiple at the same time. Or just kill the running container and do a la carte.


### Repo2Docker
Do you have a jupyter (or similar) notebook and want to quickly build and deploy it? You will want to use the [repo2docker share](https://github.com/vsoch/repo2docker-share) template. This is based on the [continuous builder](https://github.com/vsoch/continuous-build).

```bash
docker run --rm -it -p 8888:8888 vanessa/repo2docker-share jupyter notebook --ip 0.0.0.0
```

### Repo2Docker R
If you use R, this container comes with R, RStudio, and an example of Shiny! The [repo2docker-r](https://github.com/vsoch/repo2docker-r) template will allow you to add a `runtime.txt` file, a notebook file, along with an `install.R` file to build the perfect container.

```bash
docker run --rm -it -p 8888:8888 vanessa/repo2docker-r jupyter notebook --ip 0.0.0.0
```

### Repo2Docker Conda
Want to deploy a container with your favorite conda installs? This template will make it easy to install miniconda, and then run your notebook with dependencies ready to go! Want to get started? Check out the [repo2docker-conda](https://github.com/vsoch/repo2docker-conda) template.

```bash
docker run --rm -it -p 8888:8888 vanessa/repo2docker-conda jupyter notebook --ip 0.0.0.0
```

### Repo2Docker Julia
This is a complete example of a Julia+Jupyter notebook, built with repo2docker for you to use! The [repo2docker-julia](https://github.com/vsoch/repo2docker-julia) template drives this with a simple `environment.yml` file for Python dependencies, and `REQUIRE` file for Julia.
Another template for jupyter (that doesn't use repo2docker) is the [julia-share](https://github.com/vsoch/julia-share)

```bash
docker run --rm -it -p 8888:8888 vanessa/repo2docker-julia jupyter notebook --ip 0.0.0.0
```

### General Docker
If you have a general Docker container that is built from a Dockerfile in your repository, check out the
[share-docker template](https://www.github.com/vsoch/share-docker).

```bash
docker run --rm -it -p 8888:8888 vanessa/repo2docker-share jupyter notebook --ip 0.0.0.0
```

Do you have another container template you'd like? [Let me know](https://www.github.com/vsoch/containershare/issues)! Another good way to start is to [browse the table](https://vsoch.github.io/containershare), find a container like yours, and then copy the circle configuration.

### Step 2. Submit Metadata

After doing the above, you will have a repository that is hooked up to continuous integration, and deploys to Docker Hub. The rest from here is easy! You just need to submit this repository. How do you do that?

 1. Fork this repository, pull your fork on your local machine, and create a new branch for your container.
 2. Once the container is deployed on Docker Hub (step 1) add a markdown file to the [_library](docs/_library) folder. 
 3. Open a pull request to the master branch to add your contribution!

When the pull request is merged, the container will be added to [the table](https://vsoch.github.io/containershare) and [library](https://vsoch.github.io/containershare/library.json) for others to use.


## Deploy a Containershare

If you want to deploy your own containershare, there are two components that you can do.

 1. Is the web interface here
 2. Is a folder of shared containers on your research cluster that corresponds to them.

### 1. Deploy the Container Share Interface
You may just be interested in having the online library of tested containers, and so you would want to start here! For the interface, it's just a matter of forking this repository, and turning on Github pages to deploy from the docs folder, and then connecting the repository to circleci. Once this is done, third parties (others) should be able to equivalently submit pull requests to your registry that are tested, and upon merge, the container contribution added to the table, and the container available for discovery via the API exposed by the registry.

### 2. Deploy a containershare on your cluster
If you use the [forward tool](https://www.github.com/vsoch/forward) there is a script that will allow users to easily access a shared folder of containers that you provide. That's right... the container share! See the script [create.py](scripts) 
and the associated README to pull the containers. Then check out the forward tool's `sherlock/containershare-jupyter.sbatch`
(and similar) scripts for your users to use your containers!

**Note** that the create.py will be replaced with a better solution, this was a quick script that @vsoch threw together!

### Local Tests
The testing step of the registry that occurs on CircleCI is optimized to only test newly added files (so previous additions do not need to be tested and take, however the testing can be run locally (and manually) if desired. The general steps would be to do the following:

 - build the site locally with jekyll
 - inspect the image manifest
 - for each new container represented as a markdown file in the library, check that it serves metadata

#### Step 1. Build the Jekyll Site
You can [install jekyll](https://jekyllrb.com/docs/installation/) for your platform of interest], and build the site after
cloning the repository:

```bash
git clone https://www.github.com/vsoch/containershare
cd containershare/docs
jekyll build
```

This will generate static content for the site (including the library.json API file) in the `_site` folder.
Check it out!

```bash
cat _site/library.json
```

#### Step 2. Install Containershare
Containershare has a small [python library](https://pypi.org/project/containershare/) that is used to run the tests,
and this is done to ensure versioning of the testing itself. You can install this library (check the `.circleci/config.yml`
for the updated version, at the time of this writing the current version is 0.0.14) and then use it to run tests on the static
generated content.

```bash
pip install pyaml containershare==0.0.14
```

It's assumed that you have some flavor of python installed, along with the package manager pip. To
use the exact version that the CircleCI is using, these are the steps to install:

```bash
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
/bin/bash Miniconda3-latest-Linux-x86_64.sh -b 
$HOME/miniconda3/bin/python -m pip install pyaml containershare==0.0.14
```

#### Step 3. Test the library
The final command will run the tests! If you are in the "docs" folder, go up one level back
to the base of the repository ("tests" should be in the present working directory). Note that in the CircleCI
continuous integration, the tests are run like this:

```bash
python -m unittest tests.test_library
```

The above command will run through the library, and for each entry, clone the Github repository
Github pages and master branches, and check for all metadata files (tags.json, inspections and image manifests) along with "human friendly" metadata like a LICENSE and README. Finally, the tests ensure
that the Github Pages (or other preview link) is deployed based on a 200 status return, and that
the name does not include any invalid characters (outside of numbers, letters, `-` `_` and `/`).
