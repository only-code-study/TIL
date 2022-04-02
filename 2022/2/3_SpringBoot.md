# SpringBoot

당분간은 Rust공부를 포기하기로 함.
## SpringData JPA
### Entity
JPA를 통해서 관리하기 위해서는 Entity객체를 생성해야한다. 이것으로 Repository를 통하여 처리하게 한다.

```java
//entity/TestEntity.java
import lombok.*;
import javax.persistence.*;

@Entity // 1
@Table(name="test_table") // 2
@ToString
@Getter
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class TestEntity {
    @Id // 3
    @GeneratedValue(strategy = GenerationType.IDENTITY) //4
    private Long t_id;

    @Colum(length = 200, nullable = false)//5
    private String text;
}
```
1. Entity라는 어노테이션을 추가해야 JPA에서 관리가 되며, 클래스가 자동으로 추가된다.
2. Table이며 없으며 생성을 한다. 이름뿐 아니라 인덱스를 생성하기도 한다.
3. PK를 쓰겠다는 뜻이다.
4. 자동 생성할때 다른 번호를 가지도록 처리하는 것이다. 자세한 것은 밑에 더 서술 하겠다.
5. Column라는 어노테이션은 추가적인 필드가 필요할때 만드는 것이다. columnDefinition을 사용하기도 한다.

자동생성할때 strategy는 4가지가 있다.
* AUTO(default): JPA구현체가 생성방식 결정
* IDENTITY: 데이터베이스가 생성을 결정
* SEQUENCE: 데이터베이스의 sequence를 이용해서 키를 생성, `@SequenceGenerator`와 같이 사용
* TABLE: 키 생성 전용 테이블을 생성해서 키 생성, `@TableGenerator`와 함께 사용

나머지를 말로 설명하자면, `@Getter`은 말그대로 Getter이고, `@Builder`은 객체를 생성할 수 있게 한다. 
만약 `@Builder`을 사용하고자 하면, `@AllArgsConstructer`와 `@NoArgsConstructor`을 써야한다.

### JpaRepository
JpaReposity는 다음과 같이 상속한다.

![JpaRepository상속 계층](https://github.com/only-code-study/TIL-oripk/blob/main/2022/2/JpaRepository1.png?raw=true)

그래서 일반적인 기능을 사용할 때는 CrudRepository를 사용하고, JPA의 모든 기능을 사용하고 싶다면, JpaRepository를 이용한다.

Repository는 다음을 통해서 생성이 가능하다.
```java
import org.springframework.data.jpa.repository.JpaRepository;
import org.zerock.ex2.entity.TestEntity;

public interface TestRepository extends JpaRepository<TestEntity, Long>{}
```
위 코드는 독득한데 잘 보면, TestReository는 인터페이스 그 자체이며 JpaRepository를 상속함으로써 끝이난다.(잘 모르겠는데, 스프링이 알아서 bean으로 등록이 된다고 한다.)

CRUD를 한번 해보자면,

#### 1. INSERT
```java
@Autowired
TestRepository testRepository;

public void testInsertDummie() {
    TestEntity t = TestEntity.builder().text("asdf").build();
    testRepository.save(t);
}
```

#### 2. SELECT
```java
Long t_id = 1L;
Optional<TestEntity> result = testRepository.findById(t_id);

if(result.isPresent()) {
    TestEntity t = result.get();
    System.out.println(t);
}
```
좀 독특하게 옵셔널을 써서 검색이 안될때를 방지 하였다.

#### 3. UPDATE
```java
public void testUpdate() {
    TestEntity t = TestEntity.builder().t_id(1L).text("Update").build();
    System.out.println(testRepository.save(t));
}
```
만약에 없으면 INSERT를 한다.

#### 4. DELETE
```java
public void testDelete() {
    Long t_id = 1L;
    testRepository.deleteById(t_id);
}
```
삭제할 것이 없으면 `org.springframework.dao.EmptyResultDataAccessException`예외를 발생한다.