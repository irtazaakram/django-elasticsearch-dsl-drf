Installing Elasticsearch
========================
For development and testing purposes, it's often handy to be able to
quickly switch between different Elasticsearch versions. Since this packages
supports 7.x and 8.x branches, you could make use of
the following boxes/containers for development and testing.

.. note::

    As of ``django-elasticsearch-dsl-drf`` 0.19, support for Elasticsearch
    versions prior 6.x has been dropped.

For all containers/boxes mentioned below, no authentication is required (for
Elasticsearch).

Docker
------
Using ``docker-compose`` (persistent):

.. code-block:: sh

    docker-compose up elasticsearch

7.x
~~~
**7.3.0**

.. code-block:: sh

    docker pull docker.elastic.co/elasticsearch/elasticsearch:7.3.0
    docker run -p 9200:9200 -e "discovery.type=single-node" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:7.3.0

8.x
~~~
**8.10.2**

.. code-block:: sh

    docker pull docker.elastic.co/elasticsearch/elasticsearch:8.10.2
    docker run -p 9200:9200 -e "discovery.type=single-node" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:8.10.2
