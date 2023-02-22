FROM python:3.7-alpine

WORKDIR /src/app/

COPY ./requirements.txt .

RUN ["pip", "install", "-r", "./requirements.txt"]

COPY . .

RUN addgroup -S projects && adduser -S -H projects -G projects
RUN chown -R projects:projects /src/app
USER projects

FROM node:16-alpine

WORKDIR /src/app/

ENV PATH /src/app/node_modules/.bin:$PATH

COPY package.json ./

RUN npm install
RUN npm install react-router-dom
RUN npm install -D tailwindcss@npm:@tailwindcss/postcss7-compat postcss@^7 autoprefixer@^9
RUN npm install @craco/craco
RUN npx tailwindcss-cli@latest init

COPY ./ ./

CMD ["npm", "start"]