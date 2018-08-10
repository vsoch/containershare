# Helpers

# Create.py

[create.py](create.py) is a helper script that can help you to create a container share on
a cluster. It basically uses your containershare endpoint library.json to pull containers to
a folder, and then name them based on the hash of the docker uri. This is how the 
[forward tool](https://www.github.com/vsoch/forward) would find them. You should first 
define these environment variables:

```bash
export CONTAINERSHARE=${SCRATCH}/share
export ENDPOINT=https://vsoch.github.io/containershare/library.json
export SINGULARITY_CACHEDIR=$SCRATCH/.singularity

mkdir -p $CONTAINERSHARE SINGULARITY_CACHEDIR

chmod g+x -R "${CONTAINERSHARE}"
cd ${CONTAINERSHARE}"
```

And then you will want to run a little script that accesses your container share, and for each container, pulls to
your cluster resource named by the hash of its string. Remember that we are currently on the cluster
resource, and going to pull containers and move them to the share. This is how that would look in python:

and then run the script.

```
python create.py
```
