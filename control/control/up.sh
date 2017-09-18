for i in {1..5}; do
    ssh n$i /jepsen/run.sh;
done

ssh master /jepsen/run.sh
