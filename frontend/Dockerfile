# Use the official Node.js base image
FROM node:14

# Set the working directory
WORKDIR /app

COPY package*.json ./

# Install the dependencies and build the project
RUN npm install

# Copy the frontend source code
COPY . .

# RUN npm run build
EXPOSE 8080
CMD ["npm", "run", "serve"]
