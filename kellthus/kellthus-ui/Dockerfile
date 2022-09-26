FROM node:16-slim as build-stage

ENV apt-get -qq -y update \ && apt-get -qq -y install python build-essential

RUN mkdir /app
WORKDIR /app

COPY package.json /app

RUN npm install

COPY ./ /app

RUN npm run build

CMD npm run start


#FROM nginx:1.15
#COPY nginx.conf /etc/nginx.nginx.conf

# COPY --from=build-stage /app/build/ /usr/share/nginx/html
# COPY --from=build-stage /nginx.conf /etc/nginx/conf.d/default.conf


