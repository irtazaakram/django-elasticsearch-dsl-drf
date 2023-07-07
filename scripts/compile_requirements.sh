#!/usr/bin/env bash
cd examples/requirements/
pip-compile base.in "$@"
pip-compile code_style.in "$@"
pip-compile common.in "$@"
pip-compile coreapi_coreschema.in "$@"
pip-compile debug.in "$@"
pip-compile deployment.in "$@"
pip-compile dev.in "$@"
pip-compile django_3_2.in "$@"
pip-compile django_4_0.in "$@"
pip-compile django_4_1.in "$@"
pip-compile django_4_2.in "$@"
pip-compile docs.in "$@"
pip-compile documentation.in "$@"
pip-compile elastic.in "$@"
pip-compile elastic_6x.in "$@"
pip-compile elastic_7x.in "$@"
pip-compile elastic_docker.in "$@"
pip-compile schema.in "$@"
pip-compile test.in "$@"
pip-compile testing.in "$@"
