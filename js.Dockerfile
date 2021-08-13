FROM node:14-buster

#RUN npm install --build-from-source zeromq@6.0.0-beta.5 
RUN npm install express

WORKDIR /app
COPY . .

CMD node app/server.js