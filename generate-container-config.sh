#!/bin/bash

AZURE_CONTAINER_INSTANCE_GROUP=$1
EMAIL_ERROR_RECIEVER=$2
EMAIL_ERROR_SUBJECT=$3
EMAIL_SUBJECT=$4
EMAIL_RECIEVER=$5
EMAIL_SENDER=$6
EMAIL_BCC=$7

cat << EOF > container-config.yaml
location: canadacentral
name: "$AZURE_CONTAINER_INSTANCE_GROUP"
properties:
  containers:
  - name: ford-web-scrapper
    properties:
      resources:
        requests:
          cpu: 1.0
          memoryInGb: 1.5
      environmentVariables:
      - name: EMAIL_ERROR_RECIEVER
        value: "$EMAIL_ERROR_RECIEVER"
      - name: EMAIL_ERROR_SUBJECT
        value: "$EMAIL_ERROR_SUBJECT"
      - name: EMAIL_SUBJECT
        value: "$EMAIL_SUBJECT"
      - name: EMAIL_RECIEVER
        value: "$EMAIL_RECIEVER"
      - name: EMAIL_SENDER
        value: "$EMAIL_SENDER"
      - name: EMAIL_BCC
        value: "$EMAIL_BCC"
      - name: GITHUB_TOKEN
        secureValue: "$FIREFOX_GITHUB_TOKEN"
      - name: EMAIL_PASSWORD
        secureValue: "$EMAIL_PASSWORD"
  osType: Linux
  restartPolicy: Never
EOF
cat container-config.yaml