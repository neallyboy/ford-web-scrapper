#!/bin/bash

EMAIL_ERROR_RECIEVER=$1
EMAIL_ERROR_SUBJECT=$2
EMAIL_SUBJECT=$3
EMAIL_RECIEVER=$4
EMAIL_SENDER=$5
EMAIL_BCC=$6

cat << EOF > container-config.yaml
location: canadacentral
name: ford-web-scrapper
properties:
  containers:
  - name: ford-web-scrapper
    properties:
      image: neallyboy/ford-web-scrapper
      resources:
        requests:
          cpu: 1.0
          memoryInGb: 1.5
      environmentVariables:
      - name: EMAIL_ERROR_RECIEVER
        value: $EMAIL_ERROR_RECIEVER
      - name: EMAIL_ERROR_SUBJECT
        value: $EMAIL_ERROR_SUBJECT
      - name: EMAIL_SUBJECT
        value: $EMAIL_SUBJECT
      - name: EMAIL_RECIEVER
        value: $EMAIL_RECIEVER
      - name: EMAIL_SENDER
        value: $EMAIL_SENDER
      - name: EMAIL_BCC
        value: $EMAIL_BCC
      - name: GITHUB_TOKEN
        secureValue: $FIREFOX_GITHUB_TOKEN
      - name: EMAIL_PASSWORD
        secureValue: "$EMAIL_PASSWORD"
  osType: Linux
  restartPolicy: Never
EOF
cat container-config.yaml