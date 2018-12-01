from kubernetes import client, config
import os
import time
import logging
import sys




def main():


    PODNAME = 'POD_NAME'

    NAMESPACE = "default"

    STARTUPSLEEP = 120


    #time for some logging that will help make the console logs visible in pod logs for debug
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)



    # this is so cheating but lets let conductor at least start up first
    logging.info("sleeping")
    time.sleep(STARTUPSLEEP)

    try:

        #get the client
        config.load_incluster_config()

        v1 = client.CoreV1Api()

        logging.info("built client")

        #get the pod name

        pod_name = os.environ.get(PODNAME)


        logging.info("set to running")

        #tell the service selector we are up and running, maybe put a check here as well?

        v1.patch_namespaced_pod(name=pod_name, namespace=NAMESPACE, body=[{
            "op": "add", "path": "/metadata/labels/status", "value": "running"
        }])

        logging.info("set the pod data is running")

    except Exception, e:
        logging.info(str(e))
        exit(1)

exit(0)

if __name__ == '__main__':
    main()
