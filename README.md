## **Instructions**
The goal of the game is to get rid of all the blocks while making sure the ball does not fall below the orange block you control.
The green blocks are regular blocks which require one hit to remove while the red blocks require two. The yellow block if hit
adds an extra ball into the game.
[![gameplay.png](https://i.postimg.cc/Tw0H3m6n/gameplay.png)](https://postimg.cc/ygJTfDWN)

The user controls the orange block by moving the mouse in the window.
### **How to run the program**
Once the folder is open in terminal:
```
python3 game.py
```

## **How to modify the game**
The user can change the number and location of the blocks, as well as the ball's velocity and starting position.
#### **Changing the ball's atributes**
The ball's starting position can be changed in line 17. By modifying the current value of (225,300) which represent (x,y) coordinates.
```python
this.balls.append(this.makeBall (225, 300))
```
The ball's velocity can be changed in line 55. By modifying the current value of (1,2) which represents the (x,y) velocities.
```python
this.ballv.append([1, 2])
```
#### **Changing the blocks' atributes**
The blocks' positions can be changed in lines 20-50. By modifying the current values of (x,y) which represent the position of each block.
```python
this.makeBlock(250, 125)
```
Adding and removing blocks can be done by adding makeBlock, makeStrongBlock, or makeExtraBlock into lines 20-50.

