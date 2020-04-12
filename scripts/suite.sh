#!/bin/sh


export ret=0

wait_for_url () {
    echo "Testing url $1 availability."

    if [ $# -ge 3 ]
    then
      echo "authentication is enabled."
      auth="-u $2:$3"
    fi

    i=0
    until $(curl $auth --connect-timeout 180 --output /dev/null --silent --head --fail $1); do
        i=$((i+1))
        if [ $i -gt 10 ]; then
            printf "X\n"
            ret=1
            return
        fi
        printf '.'
        sleep 15
    done

    printf "OK\n"
}



# For Dynamic hosting.
wait_for_url http://localhost:5000/automation/api/v1.0/prediction/admin/is-alive
#wait_for_url http://localhost:4000/

exit $ret
