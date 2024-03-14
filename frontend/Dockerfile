# Use the official Node.js image as the base image
FROM node:16

# Set the working directory within the container
WORKDIR /app

# Copy package.json and package-lock.json into the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code into the container
COPY . .

# Build the React application
RUN npm run build

# Set the command to start the application
CMD ["npx", "serve", "-s", "build", "-l", "3000"]