# Building a Node.js API with Express.js in a Docker Container 🐳

This repository aims to illustrate how you can run a simple API in Node.js, using Express.js, and build a Docker image. You can then use this Docker image to run your app inside a Docker container and access your Node.js API from there.

To build your own API you'll need to create a node app, build the api with express.js and create a dockerfile:

## Steps:

1. Install [Docker Desktop](https://docs.docker.com/get-docker/)
2. Create a folder for your app and initialize your node.js app by running this command:

```console
> npm init
```

3. Install express.js and build your api using a public port like 8080 e.g. like the index.js file in the src folder in this repo.
4. Test your api by running the **node** command making sure you get the desired response:

```console
> node ./src/index.js
```

5. Create your docker file with the following set of instructions. Instructions are like steps/layers which make it possible for Docker to cahce some of the steps if nothing has changed. Thats why the step to install the node_modules comes early on so that Docker doesn't have to reinstall them everytime something changes in your app's source code ⏱️

```docker
FROM node:12

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

ENV PORT=8080

EXPOSE 8080

CMD [ "npm", "start" ]
```

6. Make sure you have a script in your package.json that handles the last step **npm start**. See the package.json file "scripts" section in the repo.
7. Run the Docker build command like below:

```console
> docker build -t node-api-docker:1.0 .
```

8. If successful you should see a line that looks like this with the id you need for the last step

```console
Successfully built 9d1h36e6a333
```

9. Execute the Docker run command using the id from the last step and making sure you map your enviroment port from your express.js api (e.g. 8080) to another port like 5001.

```console
docker run -p 5001:8080 9d1h36e6a333
```

10. If all goes well you should be able to visit localhost:5001 and see the response from your api now running in a Docker container 🐳

## Documentation

- [Node npm](https://docs.npmjs.com/cli/v6/commands/npm-init)
- [Express.js](https://expressjs.com/en/guide/routing.html)
- [Docker File](https://docs.docker.com/engine/reference/builder/)
