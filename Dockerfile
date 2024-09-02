# Use an official Node.js runtime as a parent image
FROM node:14-alpine AS build

WORKDIR /app


# Copy package.json and package-lock.json to the working directory
COPY angular.json ./
COPY package*.json ./
COPY tsconfig*.json ./
COPY src/ ./src/

# Install app dependencies
RUN npm install
# Build AngularJS application
RUN npm run build -- --output-path=dist/superAdminPortal

# Stage 2: Serve the Angular application with Nginx
FROM nginx:alpine

# Copy the built Angular application from the previous stage
COPY --from=build /app/dist/superAdminPortal /usr/share/nginx/html

# Expose port 80 to the outside world
EXPOSE 80

# Start Nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]

#groups $USER
#sudo usermod -aG docker $USER
#ls -l /var/run/docker.sock
#sudo chown root:docker /var/run/docker.sock
#sudo chmod 660 /var/run/docker.sock
#sudo reboot
