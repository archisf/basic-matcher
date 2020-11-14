FROM mhart/alpine-node:latest

WORKDIR /app/frontend

COPY package.json /app/frontend
COPY package-lock.json /app/frontend

RUN npm ci

EXPOSE 3000

CMD ["npm", "start"]
