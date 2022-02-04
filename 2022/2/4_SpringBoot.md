# SpringBoot
## SpringData JPA
### 페이징
페에징 처리하는 기능이다. 예전에 JDBC를 다룰 때, 페이징을 직접 작성하였지만, 여기서는 직접 지원이 된다.

```java
@Test
public void testPage() {
    Pageable pageable = PageRequest.of(0, 10);
    Page<TestEntity> result = testRepository.findAll(pageable);
}
```
위처럼 처리하면 페이징을 할 수 있다.

안에 내부적으로 여러가지로 쓸 수 있는데 그 기능들은 다음과 같다.
* result.getTotalPages(): 총 페이지의 개수
* result.getTotalElements(): 전체개수
* result.getNumber(): 현재 페이지 수
* result.getSize(): 페이지당 데이터 개수
* result.hasNext(): 다음 페이지의 유무
* result.isFirst(): 시작 페이지의 여부
* result.getContent(): 안에 들어온 값들

값들은 List<엔티티 타입>, Stream<엔티티 타입>을 반환하는 get()을 이용할 수 있다.

이외에도 페이징이라서 그런지 정렬 기능도 있다.
```java
@Test
public void testSort() {
    Sort sort1 = Sort.by("t_id").descending();
    Sort sort2 = Sort.by("text").ascending();
    Sort sortAll = sort1.and(sort2);

    Pageable pageable = PageRequest.of(0, 10, sortAll);
    //...
}
```
위처러 사용하면 여러개의 Sort도 사용 가능하다.


### Query메서드
#### 쿼리 메서드()
쿼리메소드의 리턴타입은 자유롭다.
* select를 하는 작업이면 List타입이나 배열 사용 가능
* 파라미터에 Pageable타입을 넣는 경우 `Page<E>`타입을 써야함.
```java
    List<TestEntity> findByT_idBetweenOrderByT_idDesc(Long from, Long to);

    Page<TestEntity> findByTestEntityBetween(Long form, Long to, Pageable pageable);

    void deleteTestByT_idLessThan(Long num);
```
delete는 `@Commit`과 `@Transactional`을 써야한다.