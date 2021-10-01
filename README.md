<p align="center">
<a href="https://github.com/sauljabin/kaskade"><img alt="kaskade" src="https://raw.githubusercontent.com/sauljabin/kaskade/main/screenshots/kaskade.png"></a>
</p>
<p align="center">
<a href="https://github.com"><img alt="GitHub" src="https://img.shields.io/badge/-github-orange?logo=github&logoColor=white"></a>
<a href="https://github.com/sauljabin/kaskade"><img alt="GitHub" src="https://img.shields.io/badge/status-active-success"></a>
<a href="https://github.com/sauljabin/kaskade"><img alt="GitHub" src="https://badges.pufler.dev/updated/sauljabin/kaskade?label=updated"></a>
<a href="https://github.com/sauljabin/kaskade/blob/main/LICENSE"><img alt="MIT License" src="https://img.shields.io/github/license/sauljabin/kaskade"></a>
<a href="https://github.com/sauljabin/kaskade/actions"><img alt="GitHub Actions" src="https://img.shields.io/github/checks-status/sauljabin/kaskade/main?label=tests"></a>
<a href="https://app.codecov.io/gh/sauljabin/kaskade"><img alt="Codecov" src="https://img.shields.io/codecov/c/github/sauljabin/kaskade"></a>
<br>
<a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/-python-success?logo=python&logoColor=white"></a>
<a href="https://pypi.org/project/kaskade"><img alt="Version" src="https://img.shields.io/pypi/v/kaskade?label=kaskade"></a>
<a href="https://pypi.org/project/kaskade"><img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/kaskade"></a>
<a href="https://libraries.io/pypi/kaskade"><img alt="Dependencies" src="https://img.shields.io/librariesio/release/pypi/kaskade"></a>
<a href="https://pypi.org/project/kaskade"><img alt="Platform" src="https://img.shields.io/badge/platform-linux%20%7C%20osx-0da5e0"></a>
<br>
<a href="https://www.docker.com/"><img alt="Docker" src="https://img.shields.io/badge/-docker-blue?logo=docker&logoColor=white"></a>
<a href="https://hub.docker.com/r/sauljabin/kaskade"><img alt="Docker Image Version (latest by date)" src="https://img.shields.io/docker/v/sauljabin/kaskade?label=tag"></a>
<a href="https://hub.docker.com/r/sauljabin/kaskade"><img alt="Docker Image Size (latest by date)" src="https://img.shields.io/docker/image-size/sauljabin/kaskade"></a>
<br>
<a href="https://kafka.apache.org/"><img alt="Kafka" src="https://img.shields.io/badge/-kafka-grey?logo=apache-kafka&logoColor=white"></a>
<a href="https://kafka.apache.org/"><img alt="Kafka" src="https://img.shields.io/badge/kafka-2.8%20%7C%203.0-blue"/></a>
<a href="https://pypi.org/project/confluent-kafka/"><img alt="Kafka Client" src="https://img.shields.io/pypi/v/confluent-kafka?label=kafka%20client"></a>
</p>

`kaskade` is a tui (terminal user interface) for [kafka](https://kafka.apache.org/).

# Installation and Usage

Install with pip:
```sh
pip install kaskade
```

Upgrade with pip:
```sh
pip install --upgrade kaskade
```

Help:
```sh
kaskade --help
```

Version:
```sh
kaskade --version
```

Run without config file (it'll take any of `kaskade.yml`, `kaskade.yaml`, `config.yml`, `config.yaml`):
```sh
kaskade
```

Run with config file:
```sh
kaskade my-file.yml
```

# Running with Docker

Using docker (add a `network` and `volume`):
```sh
docker run --rm -it --network kafka-sandbox_network -v $(pwd)/config.yml:/kaskade/config.yml sauljabin/kaskade:latest
```

# Configuration

A default [yaml](https://yaml.org/spec/1.2/spec.html) configuration file name can be either `kaskade.yml`, `kaskade.yaml`, `config.yml` of `config.yaml`. It supports all the configuration on [kafka consumer configuration](https://kafka.apache.org/documentation/#consumerconfigs) page.

Simple example:

```yml
kafka:
    bootstrap.servers: kafka1:9092,kafka2:9092,kafka3:9092
```

SSL auth example:

```yml
kafka:
    bootstrap.servers: kafka:9092
    security.protocol: SSL
    ssl.truststore.location: {{path}}/truststore.jks
    ssl.truststore.password: {{password}}
    ssl.keystore.type: PKCS12
    ssl.keystore.location: {{path}}/keystore.p12
    ssl.keystore.password: {{password}}
    ssl.key.password: {{password}}
```

# Alternatives

- cli [kcat](https://github.com/edenhill/kcat)
- cli [zoe](https://github.com/adevinta/zoe)
- cli [kaf](https://github.com/birdayz/kaf)
- ui [akhq](https://github.com/tchiotludo/akhq)

# To Do

- Paginated table + key events for moving forward and backward
- Consumed messages table
- Consumer groups table
- Shortcuts at header

# Development

Installing poetry:
```sh
pip install poetry
```

Installing development dependencies:
```sh
poetry install
```

Build (it'll create the `dist` folder):
```sh
poetry build
```

### Scripts

Running unit tests:
```sh
poetry run python -m scripts.tests
```

Running multi version tests (`3.7`, `3.8`, `3.9`):

> Make sure you have `python3.7`, `python3.8`, `python3.9` aliases installed

```sh
poetry run python -m scripts.multi-version-tests
```

Applying code styles:
```sh
poetry run python -m scripts.styles
```

Running code analysis:
```sh
poetry run python -m scripts.analyze
```

Running code coverage:
```sh
poetry run python -m scripts.tests-coverage
```

Generate readme banner:
```sh
poetry run python -m scripts.banner
```

Running kaskade using `poetry`:
```sh
poetry run kaskade
```

### Docker

Build docker:
```sh
poetry build
docker build -t sauljabin/kaskade:latest -f ./docker/Dockerfile .
```

Run with docker:
```sh
docker run --rm -it --network kafka-sandbox_network -v $(pwd)/config.yml:/kaskade/config.yml sauljabin/kaskade:latest
```