# Nestjs

## 개요

이번 프로젝트는 Nestjs로 진행 할 예정이다.

공식 문서를 번역을 한 [이곳](https://jakekwak.gitbook.io/nestjs/introduction/introduction)에서 보고 작성할 것이다.

기본적으로 JS를 알고 있으므로 좋을 것 같다.

## Introduction

### Introduction

Nest는 효율적으로 개발하기 위해서 만들어진 framework이다. Typescript로 개발 가능하며 OOP, FP, FRP요소를 포함하여 개발할 수 있게 했다.

### Philosophy

아키텍쳐가 지원하지 못해, 효율적으로 해결하지 못하였다. Nest는 즉시 사용가능한 아키텍쳐를 제공하며, 느슨하게 결합이 되어있어 유지가 쉬운 애플리케이션을 작성 할 수 있다.

### Installation

nestjs는 시작할 때 NestCLI로 시작하면 좋다.

```sh
$ npm i -g @nestjs/cli
$ nest new project-name
```

## First steps
기본 CRUD 애플리케이션을 만들어 보자.

### Language
이 프레임워크는 Typescript로 작성하는 것이 좋다.

### Prerequisites
이 프레임워크는 8.9.0 이상이어야 한다.

### Setup
새로운 프로젝트를 실행하면 src/아래 여러 core 파일이 생성이 된다. 핵심파일와 기능은 다음과 같습니다.

`scr/app.controller.ts`: 단일 경로의 기본 컨트롤러 샘플.

`src/app.module.ts`: 응용 프로그램의 루트 모듈

`src/main.ts`: 애플리케이션 엔트리 파일

main.ts안에는 다음과 같이 작성되어 있다.

```js
@@filename(main)

import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  await app.listen(3000);
}
bootstrap();
```

create()메소드는 INestApplication인터페이스를 충족하는 애플리케이션을 반환한다.
main.ts예제에서 HTTP리스너를 시작하면 HTTP요청을 기다리게 할 수 있다.

Nest는 각 모듈을 전용 디렉토리에 보관하는 규칙을 따르도록 권장한다.

### Platform

Nest는 플렛폼에 구애받지 않게 한다. express와 fastify 2개로 쓸 수 있는데, 필요에 맞추어 쓸 수 있다. 기본 플렛폼 API에 액세스 하지 않은 이상 지정할 필요가 없다.

### Running the application

```sh
$ npm run start:dev
```
위와 같이 실행하고, `http://localhost:3000/`으로 이동하면 `Hello world!`같은 메세지가 나타날 것이다.

## Controllers

컨트롤러는 requests를 처리하고 responses을 클라이언트에 반환하는 역활을 한다.

![controllers](https://docs.nestjs.com/assets/Controllers_1.png)

컨트롤러의 목적은 응용 프로그램에 대한 특정 요청을 받는 것이다. rounting 메커니즘은 컨트롤러가 어떤 요청을 받는지 제어한다. 각 컨트롤러는 한개 이상의 경로가 있다.

기본적으로 컨트롤러는 클래스와 Decorators를 사용한다.

### Routing

`@controller()`데코레이터를 사용해서 만들어야 한다. 경로 접두사를 사용하면 관련된 경로 세트를 쉽게 그룹화 시키고 반복 코드를 최소할 수 있다.

```js
@@filename(cats. controller)
import { Controller, Get } from '@nestjs/common';

@Controller('cats')
export class CatsController {
    @Get()
    findAll(): string {
        return 'This action returns all cats';
    }
}
```

> **힌트** `$ nest g controller cats`을 하면 생성이 된다. 

`findAll()`메소드 앞에 있는 `@Get()`은 HTTP요청 메소드 데코레이터 이며 Nest에게 HTTP요청에 대한 특정 **엔드 포인트**에 대한 핸들러를 작성하도록 지시한다.(Get뿐 아니라 Post 등 많다) 위에서 `@Controller('cats')`로 라우팅이 되어 있어서 `findAll()`은 `GET/cats`요청에 대해서 매핑 되어 있다. 다른 예시를 들자면 `@Controller('profile')`과 `@Get('customers')`으로 매핑 되어 있다면 `GET/profile/customers`에 들어오는 요청들을 매핑한다.

Nest가 응답을 하기 위해서 2가지 옵션이 있다.

1. 표준: 자동으로 JSON으로 직렬화 해서 문자를 보낸다. POST를 제외하고 200응답을 보낸다. `@HttpCode(...)`데코레이터를 추가하면 된다([Status code](#Statuscodes)에서 더 자세하게 볼 수 있다.)

2. 라이브러리 옵션: express 같은 경우에는 응답 객체를 사용 할 수 있다. 메소드에 `@Res()`같은 데코레이터를 사용하여 삽입할 수 있다(e.g., `findAll(@Res() response`)). 이렇게 하면 기본 응답처리 방식을 사용 할 수 있다.(e.g., `response.status(200).send()`)

> **경고** 두 가지 방법을 동시에 사용할 수 없다.