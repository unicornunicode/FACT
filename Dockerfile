ARG python_tag=3.9-slim-bullseye


FROM docker.io/library/python:${python_tag} AS poetry

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN python -m pip install poetry
RUN poetry export --format requirements.txt \
		--extras sqlite \
		--extras postgres \
		--extras mysql \
		> requirements.txt


FROM docker.io/library/python:${python_tag} AS dependencies

RUN apt-get update \
	&& apt-get install --yes openssh-client \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY --from=poetry /app/requirements.txt ./
RUN python -m pip install --requirement requirements.txt \
	&& rm -rf ~/.cache


FROM poetry AS build

COPY fact/ ./fact/
RUN poetry build --format wheel


FROM dependencies AS production

COPY --from=build /app/dist/ ./dist/
RUN python -m pip install ./dist/* \
	&& rm -rf ~/.cache ./dist


FROM production AS worker

ENTRYPOINT ["python", "-m", "fact.worker"]
CMD ["--controller-addr", "controller:5123"]


FROM production AS controller

ENTRYPOINT ["python", "-m", "fact.controller"]
CMD ["--listen-addr", "0.0.0.0:5123"]
