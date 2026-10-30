#!/bin/sh

if [ -z "$1" ]; then
  echo "Введите название вакансии"
  exit 1
fi

curl -s "https://api.hh.ru/vacancies?text=$(echo "$1" | sed 's/ /%20/g')&per_page=20" | jq '.' > hh.json
