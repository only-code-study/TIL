# Nestjs

## Controllers

## Getting up and running 

위 컨트롤러가 정의된 상태에서 Nest는 여전히 CatsController가 존재앟낟는 것을 알지 못해 이 클래스의 인스턴스를 만들지 못했다.

컨트롤러는 항상 모듈에 속하므로 `@Module()`데코레이터 내에 컨트롤러 배열을 포함시킨다. 루트 AppModule을 제외한 다른 모듈은 아직 정의하지 않았으므로 이를 사용하여 `CatsController`를 소개한다.
```js
@@filename(app.module)
import { Module } from '@nestjs/common';
import { CatsController } from './cats/cats.controller';

@Module({
    controllers: [CatsController],
})
export class AppModule {}
```

`@Module()`데코레이터를 사용하여 메타 데이터를 모듈 클래스에 첨부했으며 Nest는 이제 컨트롤러를 마운트 해야하는지 쉽게 반응 할 수 있다.

### Appendix: Library-specific approach

이전까지는 Nest의 표준 응답객체를 만들었다. 이제 두번째 방법으로 라이브러리 별 응답 객체를 만든다. 특정 응답 객체를 주입하려면 `@Res()`데코레이터를 사용해야 한다. 차이점을 보여주기 위해 CatsController를 다시 작성하겠다.

```js
import { Controller, Get, Post, Res, HttpStatus } from '@nestjs/common';
import { Response } from 'express';

@Controller('cats')
export class CatsController {
    @Post()
    create(@Res() res: Response) {
        res.status(HttpStatus.CREATE).SEND();
    }

    @Get()
    findAll(@Res() res: Response) {
        res.status(HttpStatus.Ok).json([]);
    }
}
```

위 방법은 효과가 있으며, 응답 객체를 완벽하게 제어하여 유연성을 허용한다. 이 접근 방식은 덜 명확하며 `@HttpCode()`데코레이터 같은 Nest표준 응답 처리에 의존하는 Nest기능과의 호환성이 손실이 된다.

즉 가능한 경우 Nest 표준접근 방식을 쓰는 것이 좀 더 좋다.

## Providers

### Providers

Provider은 Nest의 기본 개념이다. 기본 Nest클래스는 서비스, 저장소, 팩토리, 헬퍼 등 공급자로 취급될 수 있다. Provider의 주요 아이디어는 의존성을 **주입**할 수 있다는 것이다. 즉, 객체가 서로 다양한 관계를 만들 수 있으며 개체의 "배선"기능을 Nest런타임 시스템에 크게 위임 할 수 있다. 공급자는 `@Injectable()`데코레이터로 주석이 달리 클래스이다.

![Providers](https://docs.nestjs.com/assets/Components_1.png)

이전 장에서 `CatsController`을 만들었는다. 컨트롤러는 HTTP요청을 처리하고 더 복잡한 작업을 **공급자**에게 위임해야 한다. 공급자는 클래스 선언 앞에 `@Injectable()`데코레이터가 있는 일반 JavaScript클래스이다.

> **힌트** Nest를 사용하면 좀 더 다양한 방법으로 종속성을 디자인하고 구성 할 수 있으므로 [SOLID](https://en.wikipedia.org/wiki/SOLID)원칙을 따르는 것이 좋다.

### Services

간단한 `CatsService`를 만들어 보자. 데이터 저장 및 검색을 담당하며 `CatsController`에서 사용하도록 설계되어있으므로 공금자를 정의하는 것이 좋다. 따라서 클래스를 `@Injectable()`으로 장식하면 된다.

```js
@@filename(cats.service)
import { Injectable } from '@nestjs/common';
import { Cat } from './interfaces/cat.interface';

@Injectable()
export class CatsService {
    private readyonly cats: Cat[] = [];

    create(cat: Cat) {
        this.cats.push(cat);
    }

    findAll(): Cat[] {
        return this.cats;
    }
}
```

> **힌트** CLI를 사용하여 서비스를 만드려면 간단히 `$nest g service cats`명령을 실행하면 된다.

`CatsService`는 하나의 속성과 두개의 메소드를 가진 기본 클래스이다. 유일한 새로운 기능은 `@Injectable()`데코레이터를 사용한다는 것이다. `@Injectable()`데코레이터는 메타 데이터를 첨부하여 이 클래스가 Nest공급자라는 것을 Nest에게 알려준다.

```js
export interface Cat {
    name: string;
    age: number;
    breed: string;
}
```

Cat를 검색하는 서비스 클래스가 생겼으니 `CatsController`안에서 사용하자:

```js
@@filename(cats.controller)
import { Controller, Get, Post, Body } from '@nestjs/common';
import { CreateCatDto } from './dto/create-cat.dto';
import { CatsService } from './cats.service';
import { Cat } from './interfaces/cat.interface';

@Controller('cats')
export class CatsController {
    constructor(private readonly catsService: CatsService) {}

    @Post()
    async create(@Body() createCatDto: CreateCatDto) {
        this.catsService.create(createCatDto);
    }

    @Get()
    async findAll(): Promise<Cat[]> {
        return this.catsSerive.findAll();
    }
}
```

### Dependency injection

Nest는 일반적으로 **종속 주입**으로 알려진 강력한 디자인 패턴을 중심으로 구축되어 잇다. 

Nest의 TypeScript기능 덕분에 종속성은 유형별로 해결되기 때문에 종속성을 관리하기가 매우 쉽다. 아래 예제에서 Nest는 `CatsService`의 인스턴스를 생성하고 반환함으로써(또는 일반으로 싱글 톤일 경우 기존 인스턴스를 반환하여) `catsService`를 해결한다. 이 종속성은 해결되어 컨트롤러의 생성자에게 전달되거나 표시된 속성에 할당된다.

```js
constructor(private readonly catsService: CatsService) {}
```

### Scopes

Provider은 일반적으로 응용 프로그램 수명 주기와 동시화된 수명을 갖는다. 응용 프로그램이 부트 스트랩 될 때 모든 종속성을 해결해야 하므로 모든 공급자를 인스턴스화 해야 한다. 마찬가지로 응용 프로그램이 종료되면 각 공급자가 삭제가 된다. 그러나 공급자의 수명을 요청 범위로 만드는 방법도 있다. 이러한 기술은 [여기](https://docs.nestjs.com/fundamentals/injection-scope)를 참고하면 된다.


### Custom providers

Nest에는 공급자간 관계를 해결하는 기본 제어 역전("IoC")컨테이너가 있다. 이 기능은 위에서 설명한 종속성 주입 기능의 기초가 되지만 실제로 지금 설명한 것보다 훨신 강력하다. `@Injectable()` 데코레이터는 빙산의 일각일 뿐이며 공급자를 정의하는 유일한 방법은 아니다. 실제고 일반 값, 클래스 및 비동기 또는 동기 팩토리를 사용할 수 있다. [여기](https://docs.nestjs.com/fundamentals/custom-providers)에서 더 예시를 볼 수 있습니다.

### Optional providers

때때로 반드시 해결 될 필요가 없는 종속성이 있을 수 있다. 예를 들어 클래스는 **구성 객체**에 의존할 수 있지만 전달되지 않은 경우 기본값을 사용해야 한다. 이러한 경우 구성 공급자가 없으면 오류가 발생하지 않으므로 종속성이 선택사항이 된다.

공급자가 선택적임을 나타내려면 `constructor`서명에 `@optional()`데코레이터를 사용하면 된다.

```js
import { Injecatble, Optional, Inject } from '@nestjs/common';

@Injectable()
export class HttpService<T> {
    constructor (
        @Optional() @Inject('HTTP_OPTIONS') private readonly httpClient: T) {}
    )
}
```

위의 예에서 커스템 제공자를 사용하고 있는데 `HTTP_OPTIONS`커스텀 **토큰**을 포함하는 이유이다. 이전 예제는 생성자에서 클래스를 통한 종속성을 나타내는 생성자 기반 주입을 보여준다. 사용자 지정 공급자 및 관련 토큰에 대한 자세한 내용은 [여기](https://docs.nestjs.com/fundamentals/custom-providers)에서 하면 된다.

### Property-based injection

우리가 지금까지 사용한 기술은 생성자 메서드를 통해 공급자가 주입이 되어 constructor 기반 주입이라고 한다. 매우 특정한 경우에는 **속성 기반 주입**이 유용할 수 있다. 예를 들어 최상위 클래스가 하나 이상의 공급자에 의존하는 경우 생성자의 하위 클래스에서 `super()`를 호출하여 모든 공급자를 전달하는 것은 매우 지루할 수 있다. 이를 피하기 위해 속성 레벨에서 `@Ineject()`데코레이터를 사용할 수 있다.

```js
import { Injectable, Inject } from '@nestjs/common';

@Injectable()
export class HttpService<T> {
    @Inject('HTTP_OPTIONS')
    private readonly httpClient: T;
}
```

> **경고** 클래스가 다른 제공자를 확장하지 않은 경우 항상 **생성자 기반** 주입을 사용하는 것이 좋다.

### Provider registration

우리는 공급자(CatService)를 정의했고, 그 서비스의 소비자(CatsController)를 가지고 있으므로, 주입을 수행할 수 있도록 Nest에 서비스를 등록해야 한다. 모듈파일(`app.moule.ts`)을 편집하고 서비스를 `@Module()`데코레이터의 `providers`배열에 추가하면 된다.

```js
@@filename(app.module)
import { Module } from '@nestjs/common';
import { CatsController } from './cats/cats.controller';
import { Cats Service } from './cats.service';

@Module({
    controllers: [CatsController],
    providers: [CatsService],
})
export class AppModule {}
```

Nest는 이제 `CatsContoller`클레스의 의존성을 해결할 수 있다.