#!/bin/bash

podman build -t hex3api -f Dockerfile .

podman run -d -p  8501:8501 --name geoglue hex3api