# BOARDCOVER

내가 푼거... 속도가 느리다.
```python
N = int(input())
board = [['#']* 20 for _ in range(20)]
result = 0

def getResult (board, x, y):
    global result
    if y == 18 and x == 18:
        if isFinish(board):
            result = result + 1
            return
        else:
            return
    if board[x][y] == board[x + 1][y] == board[x][y + 1] == '.':
        putPiece(board, x, y, 3)
    if board[x][y] == board[x + 1][y] == board[x + 1][y + 1] == '.':
        putPiece(board, x, y, 2)
    if board[x][y] == board[x][y + 1] == board[x + 1][y + 1] == '.':
        putPiece(board, x, y, 1)
    if board[x + 1][y] == board[x][y + 1] == board[x + 1][y + 1] == '.':
        putPiece(board, x, y, 0)
    if x == 18:
        getResult(board, 0, y + 1)
    else:
        getResult(board, x + 1, y)
        
def isFinish(board):
    for i in range(20):
        for j in range(20):
            if(board[i][j] == '.'):
                return False
    return True

def putPiece(board, x, y, index):
    for i in range(2):
        for j in range(2):
            board[x+j][y+i] = '#'
    if x == 18:
        getResult(board, 0, y + 1)
    else:
        getResult(board, x + 1, y)
    for i in range(2):
        for j in range(2):
            board[x+j][y+i] = '.'

def init():
    global board, result
    board = [['#']* 20 for _ in range(20)]
    result = 0
    temp = input()
    H = int(temp[0])
    W = int(temp[1])
    for i in range(H):
        temp = input()
        for j in range(W):
            board[i][j] = temp[j]
    getResult()
    print(result)
    
for i in range(N):
    init()
```
이런식으로 전체다 접근하면 풀수 있긴 하다.
하지만 자원을 너무 많이 먹기 때문에 다른 방식을 추천하기도 한다.
이는 내일 또 하겠다.

# Flutter

Flutter에서는 DB에 직접 접근하는 것이 어렵다.
실제로 앱에서 DB에 직접 접근하는 것은 보안에서 위험한 것이라고 한다.
그래서 DB와 연결을 해줄 중간자 역활로 nodejs에서 mongoose와 express를 활용하기로 했다.

## Todo Schema 구조
mongoose에서는 NoSQL이지만 관계형데이터베이스처럼 스키마의 구조를 구현할 수 있다.
아래는 Todo를 만들기 위한 Schema구조이다.
```javascript
const mongoose = require('mongoose');
const todoSchema = new mongoose.Schema({
    title: {
      type: String,
      required: true,
    },
    content: {
      type: String,
      required: true,
    },
    completed: {
      type: String, default: false,
    },    
  });
module.exports = mongoose.model('Todo', todoSchema);
```
## Todo 삽입 및 조회
위의 스키마구조를 토대로 mongoose는 새로운데이터를 삽입하거나, 수정, 조회 및 삭제가 가능하다.
CRUD의 구조를 그대로 이용 할 수 있다는 이야기이다.

일단 밑에 있는 코드는 삽입, 조회만 가능한 코드이다.
추후에 수정이나 삭제가 필요할 경우 더 삽입할 것이다.

```javascript
module.exports = function(app, Todo){
    app.post('/', (req, res, next) => {
        let title = req.query.title;
        let content = req.query.content;
        
        const newTodo = new Todo({
            title: title,
            content: content,
        });

        newTodo.save()
            .then(() => {
                console.log(newTodo);
            })
            .catch((err) => {
                console.log('Error: ' + err);
                res.status(500).send(err);
            });
        res.send('success');
    });
    app.post('/getAllTodo', (req, res, next) => {
        Todo.find()
            .then((todos) => {
                if(!todos.length) return res.status(404).send({err: 'Todo not found' });
                res.send(todos);
            })
            .catch(err => res.status(500).send(err));
    });
    app.post('/getOneTodo', (req, res, next) => {
        let id = req.query.todoId;
        Todo.findOne({_id: id})
            .then((Todo) => {
                if(!Todo) return res.status(404).send({err: 'Todo not found'});
                res.send(Todo);
            })
            .catch(err => res.status(500).send(err));
    });
}
```
