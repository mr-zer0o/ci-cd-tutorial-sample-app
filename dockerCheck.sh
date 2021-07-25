result=$(docker ps -f name=myapp -q -a)
if [[ -n "$result" ]]; then
  docker ps -f name=myapp -q -a | xargs --no-run-if-empty docker container stop | xargs docker container rm
else
  echo "No such container"
fi
