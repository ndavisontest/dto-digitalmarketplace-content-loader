#!/bin/sh

set -ex

pep8 .
py.test tests/
