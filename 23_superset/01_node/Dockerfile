# if BUILDPLATFORM is null, set it to 'amd64' (or leave as is otherwise).

ARG BUILDPLATFORM=${BUILDPLATFORM:-amd64}
FROM --platform=${BUILDPLATFORM} node:18-bullseye-slim   

LABEL description="superset node 镜像, 基于 node:18-bullseye-slim"


ARG NPM_BUILD_CMD="build"

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        python3

ENV BUILD_CMD=${NPM_BUILD_CMD} \
    PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true
# NPM ci first, as to NOT invalidate previous steps except for when package.json changes
WORKDIR /app/superset-frontend

RUN --mount=type=bind,target=/frontend-mem-nag.sh,src=./docker/frontend-mem-nag.sh \
    /frontend-mem-nag.sh

RUN --mount=type=bind,target=./package.json,src=./superset-frontend/package.json \
    --mount=type=bind,target=./package-lock.json,src=./superset-frontend/package-lock.json \
    npm ci

COPY ./superset-frontend ./
# This seems to be the most expensive step
RUN npm run ${BUILD_CMD}
