FROM mhart/alpine-node:latest

WORKDIR /app/frontend

COPY . .

# Install dependencies
RUN npm ci --prod

EXPOSE 3000
