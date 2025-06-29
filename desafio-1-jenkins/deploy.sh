#!/bin/bash

APP_NAME="aplicacao-desafio"

case $1 in
  build)
    echo "Simulando build da aplicação..."
    ;;
  current)
    echo "blue"
    ;;
  deploy)
    COLOR=$2
    echo "Fazendo deploy na instância $COLOR..."
    ;;
  switch)
    COLOR=$2
    echo "Mudando proxy reverso para $COLOR..."
    ;;
  test)
    echo "Rodando testes pós-deploy..."
    ;;
  *)
    echo "Uso: $0 {build|current|deploy COLOR|switch COLOR|test}"
    ;;
esac
