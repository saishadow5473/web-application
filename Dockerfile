# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory to /usr/src/app
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install app dependencies
RUN npm install

# Bundle app source
COPY . .

# Build AngularJS application
RUN npm run build

# Expose the port the app runs on
EXPOSE 80

# Command to run your AngularJS application
CMD [ "npm", "start" ]
