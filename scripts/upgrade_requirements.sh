#!/usr/bin/env bash
cd /Users/irtazaakram/bom/django-elasticsearch-dsl-drf/examples/requirements/
pip-compile base.in "$@" --upgrade
pip-compile code_style.in "$@" --upgrade
pip-compile common.in "$@" --upgrade
pip-compile coreapi_coreschema.in "$@" --upgrade
pip-compile debug.in "$@" --upgrade
pip-compile deployment.in "$@" --upgrade
pip-compile dev.in "$@" --upgrade
pip-compile django_3_2.in "$@" --upgrade
pip-compile django_4_0.in "$@" --upgrade
pip-compile django_4_1.in "$@" --upgrade
pip-compile django_4_2.in "$@" --upgrade
pip-compile docs.in "$@" --upgrade
pip-compile documentation.in "$@" --upgrade
pip-compile elastic.in "$@" --upgrade
pip-compile elastic_6x.in "$@" --upgrade
pip-compile elastic_7x.in "$@" --upgrade
pip-compile elastic_docker.in "$@" --upgrade
pip-compile schema.in "$@" --upgrade
pip-compile test.in "$@" --upgrade
pip-compile testing.in "$@" --upgrade
