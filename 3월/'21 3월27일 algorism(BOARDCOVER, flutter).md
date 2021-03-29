# 알고리즘
먼저 python 에서는 2차원 배열을 만들때 조심해야 한다.
*로 배열을 만들면 소프트한 복사이기 때문에 나머지 것으로 만들어야 한다.

예를 들어
```python
arr = [['0'] * 10] * 10
```
로 하면, '0'이 10개 들어간 배열이 10개 생기는데 모두 한개의 배열로 포인터가 가있는다.
하드한 복사를 할려면
```python
arr = [['0'] * 10 for _ in range(10)]
```
로 해야 제대로된 복사가 된다.

일단 풀려고 했으나, 왠지 모를 이유로 해결이 안된다.
다시 접근을 해야겠다.

# Flutter
Todo앱을 만들려고 한다.
DB로 firebase를 쓸 것이다.

이하는 flutter 디자인이다. 
```
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('남은 할 일'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Column(
          children: <Widget>[
            Row(
              children: <Widget>[
                Expanded(
                  child: TextField(
                    controller: _todoController,
                  ),
                ),
                RaisedButton(
                  child: Text('추가'),
                  onPressed: () {},
                ),
              ],
            ),
            Expanded(
              child: ListView(
                children: {},
              ),
            ),
          ],
        ),
      ),
    );
  }
```