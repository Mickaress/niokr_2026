# Сборка статики Vite (переменные VITE_* зашиваются на этапе build)
FROM node:20-alpine AS build

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .

ARG VITE_BASE_URL=/
ARG VITE_API_URL=http://localhost:8000/api/
ARG VITE_FILE_URL=http://localhost:8000

ENV VITE_BASE_URL=$VITE_BASE_URL \
    VITE_API_URL=$VITE_API_URL \
    VITE_FILE_URL=$VITE_FILE_URL

RUN npm run build-only

FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
