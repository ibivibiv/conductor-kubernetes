#Download base image ubuntu 16.04
FROM ubuntu:16.04
 
# Update Software repository
RUN apt-get update

#get libraries
RUN apt-get install -y wget zip default-jdk

#get the conductor master branch
RUN wget https://github.com/ibivibiv/conductor/archive/2.0.zip -O conductor.zip

#unzip the master branch
RUN unzip conductor.zip

#build conductor server
RUN cd /conductor-2.0/server && ../gradlew build
RUN mkdir /conductor
RUN cp /conductor-2.0/server/build/libs/conductor*.jar /conductor
RUN rm -r /conductor-2.0
RUN rm conductor.zip

#set up the config 
RUN mkdir /conductor/config
RUN cd /conductor/config && wget <your configuration file for conductor>

# Configure Services and Port
COPY start.sh /start.sh
CMD ["./start.sh"]

EXPOSE 8080
