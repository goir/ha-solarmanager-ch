#!/bin/bash

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i https://cloud.solar-manager.ch/swagger.json \
    -g python-pydantic-v1 \
    -o /local/out/python
