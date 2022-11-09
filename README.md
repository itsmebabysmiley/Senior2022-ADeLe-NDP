# Senior2022-ADeLe-NDP

MUICT Senior project 2022 | APPLICATION OF DEEP LEARNING ON CLASSIFICATION OF NUTRIENT DEFICIENCIES AND PESTS FOR HANG KRA ROG THAI CANNABIS

**Advisor:** Dr. Jidapa Kraisangka
**Co-advisor:** Dr. Wudhichart Sawangphol
### Group members

1. Krittitee Nildam(Boat)
2. Nopparat Pengsuk(Baby)
3. Pranungfun Prapaenee(Pin)
## Pre-required

1. Docker.

## Getting started

I recommend you run on Docker.

## How to run

1. Change directory to root directory.
2. Run following command.

```sh
docker compose -f docker-compose.yml up -d
# When it finished, you should see something similar to this.
# Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
# [+] Running 3/3
#  ⠿ Network senior2022-adele-ndp_default    Created                                                               0.1s
#  ⠿ Container senior2022-adele-ndp-redis-1  Started                                                               0.8s
#  ⠿ Container senior2022-adele-ndp-web-1    Started                                                               0.8s
```

3. Check if container is running by run the following command.

```sh
docker ps
# CONTAINER ID   IMAGE                      COMMAND                  CREATED          STATUS          PORTS                    NAMES
# 7e4a8424f258   redis:alpine               "docker-entrypoint.s…"   10 minutes ago   Up 10 minutes   6379/tcp                 senior2022-adele-ndp-redis-1
# c2bb7bcbd12d   senior2022-adele-ndp_web   "flask run"              10 minutes ago   Up 10 minutes   0.0.0.0:8000->5000/tcp   senior2022-adele-ndp-web-1
```

4. Enter [http://localhost:8000/](http://localhost:8000/) in a browser to see the application running.