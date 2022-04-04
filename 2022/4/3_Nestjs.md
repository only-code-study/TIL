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