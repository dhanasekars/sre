#!/usr/bin/env bash
# wait-for-it.sh script

host=$1
shift
port=$1
shift
cmd="$@"

until nc -z "$host" "$port"; do
  echo "Waiting for $host:$port..."
  sleep 2
done

echo "$host:$port is up - executing command"
exec $cmd
