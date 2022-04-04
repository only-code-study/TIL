# Nestjs

## Controllers

### Request object

Nest는 요청 객체에 대해 액세스를 제공한다. 기본적으로 Express를 사용하며, @Req()데코레이터를 추가하여 접근 할 수 있다.

```js
@@filename(cats.controller)
import { Controller, Get, Req } from '@nestjs/common';
import { Request } from 'express';

@Controller('cats')
export class CatsController {
    @Get()
    findAll(@Req() request: Request): string {
        return 'This action returns all cats';
    }
}
```

> **힌트** express타이핑을 이용하려면(위의 `request: Request` 파라미터 같이) @types/express 패키지를 설치하면 된다.

요청 개체는 HTTP요청을 나타내며 요청 쿼리 문자열, 매개 변수, HTTP헤더 및 본문에 대한 속성을 가진다. 대부분 수동으로 가져오지 않아도 된다. `@Body()` 또는 `@query()`와 같은 전용 데코레이터를 대신 사용 할 수 있다.

|데코레이터|가지고 오는 내용|
|------|---|
|`@Request()`|`req`|
|`@Response()`|`res*`|
|`@Next()`|`next`|
|`@Session()`|`req.session`|
|`@Param(key?: string)`|`req.parmas`/`req.parqams[key]`|
|`@Body(key?: string)`|`req.body`/`req.body[key]`|
|`@Query(key?: string)`|`req.query`/`req.query[key]`|
|`@Headers(name?: string)`|`req.headers`/`req.headers[name]|

*위 라이브러리별 섹션에서 Response 객체에는 2가지 종류가 있다. 보통 `Request()`로 접근을 하지만 기존의 `Response`(express의 req 같은)를 객체를 쓰고 싶으면 `Req()`를 쓰면 된다.

> **힌트** 나만의 커스텀 데코레이터를 만드는 방법을 배우려면 [여기](https://docs.nestjs.com/custom-decorators)를 방분하면 된다.

### Resources

이전엔 Cats를 가지고 오는데 Get으로 엔드 포인트를 정의했다. 새 래코드를 작성하는 엔드 포인트를 제공해보자.

```js
@@filename(cats.controller)
import { Controller, Get, Post } from '@nestjs/common';

@Controller('cats')
export class CatsController {
    @Post()
    create(): string {
        return 'This acttion adds a new cat';
    }

    @Get()
    findAll: string {
        return 'This action returns all cats';
    }
}
```

간단하게 엔드포인트를 작성할 수 있다. `@Put()`, `@Delete()`, `@Patch()`, `@Options()`, `@Head()`및 `@All()` 각각은 해당 HTTP요청 방법을 나타낸다.

### Route wildcards

패턴 기반 경로도 지원이 된다.
```js
@Get("ab*cd")
findAll() {
    return 'This route uses a wildcard';
}
```

`'ab*cd'`라우트 경로는 `abcd`, `ab_cd`, `abecd`등과 일치합니다. `?`, `+`, `*`및 `()`문자는 라우트 경로에 사용될 수 있으며 정규 표현식의 하위 집합이다.

### Status code

Status Code라는 응답은 201인 POST요청을 제외하고 기본적으로 항상 200이다. `@HttpCode(...)`데코레이터를 추가하여 동작을 쉽게 바꿀 수 있다.

```js
@Post()
@HttpCode(204)
create() {
    return 'This action adds a new cat';
}
```
라이브러리의 특정 Response을 사용할 수 있다.

### Headers

`res.header()`를 직접 호출 할 수 있다.

```js
@Post()
@Header('Cache-Control', 'none')
create() {
    return 'This action adds a new cat';
}
```

### Route parameters

동적 데이터를 수락해야 하는 경운 작동하지 않는다. (e.g., `GET /cats/1`) 매개변수로 경로를 정의하기 위해 라우트 경로에 경로 매개 변수 **토큰**을 추가하여 요청 URL의 해당 위치에서 동적 값을 캡처 할 수 있습니다. 아래의 `@Get()`데코레이터 예제에서 경로 매개 변수 토큰은 이 사용법을 보여줍니다.
```js
@@filename()
@Get(':id')
findOne(@Param() params): string {
    console.log(params.id);
    return `This action returns a #${params.id} cat`;
}
```

`@Param()`은 메소드 매개 변수를 장식하는데 사용되며 route매개 변수를 매소드 본문 내에서 장식 된 메소드 매개 변수의 특성으로 사용 가능하게 한다. 다음가 같이 직접 경로 매개 변수를 참조 할수도 있다.

```js
@@filename()
@Get(':id')
findone(@Param('id') id): string {
    return `This action returns a #${id} cat';
}
```

### Routes order

경로 등록 순서도 중요하다. 만약에 `cat/:id`로 Cat을 반환하는 경로가 있다고 하면 그 밑에 있는 다른 cat하위의 도메인은 접근하지 못한다.

```js
@Controller('cats')
export class CatsController {
    @Get(':id')
    findOne(@Param('id') id: string) {
        return 'This action retuns a #${id} cat';
    }

    @Get()
    findAll() {
        // 아무것도 못함.
    }
}
```

### Scopes

Nest 데이터베이스에 대한 연결 풀, 전역 상태를 가진 싱글 톤 서비스 등을 가지고 있다. Node.js는 모든 요청이 별도의 스레드에 의해 처리되는 요청/응답 다중 스레드 상애 비 저장 모델을 따르지 않는다. 따라서 싱글 톤 인스턴스를 사용하는 것은 애플리케이션에 안전하다.

그러나 컨트롤의 요청 기반 수명이 원하는 동작, 예를 들어 GraphQL 애플리케이션의 요청 별 캐싱, 요청 추적 또는 다중 테넌시가 될 수 있는 경우가 있다. 

### Asynchronicity

모든 비동기 함수는 `Promise`를 반환해야 한다.

```js
@@filename(cats.controller)
@Get()
async findAll(): PromiseM<any[]> {
    return [];
}
```

Nest경로 처리는 RxJS 관측 가능한 스트림을 반환할 수 있어 훨씬 강력하게 사용 할 수 있다. 자동으로 구독하고 방출된 값을 취한다.

```js
@@filename(cats.controller)
@Get()
findAll(): Observable<any[]> {
    return of([]);
}
```

### Request payloads

`@Body()` 데코레이터를 추가하여 이 문제를 해결하면 된다.

그러나 DTO(데이터 전송 개체)스키마를 결정해야 한다. DTO는 네트워크를 통해 데이터가 전송되는 방식을 정의하는 개체이다. 여기서는 class를 사용하여 entity를 유지시키면 좋다. 파이프와 같은 기능은 런타임에 변수 메타 타입에 액세스 할 때 추가 가능성을 가능하게 하기 때문에 중요하다.

`CreateCatDto` 클래스를 만들어 봅시다:

```js
@@filename(create-cat.dto)
export class createCatDto {
    readonly name: string;
    readonly age: number;
    readonly bread: string;
}
```

세 가지 기본 속성만 있습니다. 그 후에 우리는 `CatsController`안에서 새로 생성된 DTO을 사용할 수 있습니다.

```js
@@filename(cats.controller)
@Post()
async create(@Body() createCatDto: createCatDto) {
    return 'This action adds a new cat';
}
```

### Handling errors

오류 처리(예: 예외 작업) [여기](https://docs.nestjs.kr/exception-filters)에 대한 별도의 장이 있다.

### Full resource sample 

아래는 사용 가능한 여러 데코레이터를 사용하여 기본 컨트롤러를 만드는 예이다. 이 컨트롤러는 내부 데이터에 액세스하고 조작하는 몇 가지 방법을 제공한다.

```js
@@filename(cats.controller)
import { Controller, Get, Query, Post, Body, Put, Param, Delete } from '@nestjs/common';
import { CreateCatDto, UpdateCatDto, ListAllEntities } from './dto';

@Controller('cats')
export class CatsController {
    @Post()
    create(@Body() createCatDto: CreateCatDto) {
        return 'This action adds a new cat';
    }

    @Get()
    findAll(@Query() query: ListAllEntities) {
        return `This action returns all cats(limit: ${query.limit} items)`;
    }

    @Get(':id')
    findOne(@Param('id') id: string) {
        return `This action returns a #${id} cat`;
    }

    @Put(':id')
    update(@Param('id') id: string, @Body() updateCatDto: UpdateCatDto) {
        return `This action updates a #${id} cat`;
    }

    @Delete(':id')
    remove(@Param('id') id: string) {
        return `This action removes a #${id} cat`;
    }
}

