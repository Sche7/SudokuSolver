<template>
    <div align="center">
        <nav class="navbar navbar-expand-lg navbar-light bg-light" style="width: 50%; margin-bottom: 20px;">
          <ul class="navbar-nav ml-auto text-center">
            <li>
              <button @click="randomizeBoard" class="btn btn-light">New puzzle</button>
            </li>
            <li>
              <button @click="validateBoard" class="btn btn-light">Validate puzzle</button>
            </li>
            <li>
              <button @click="solveBoard" class="btn btn-light">Solve puzzle</button>
            </li>
            <li>
              <button @click="lockCells" class="btn btn-light" v-if="locked.length==0">Lock cells</button>
              <button @click="unlockCells" class="btn btn-light" v-else>Unlock cells</button>
            </li>
          </ul>
            <ul class="navbar-nav ml-auto">
              <li>
                <LoadingSpinner :computing="computing"/>
              </li>
            </ul>
        </nav>

      <div>
        <table>
          <tbody>
          <tr v-for="(row, idx) in grid" :key="idx">
            <td
              v-for="(cell, idy) in row" :key="idy"
              @click="setSelected(idx, idy)"
              :style="[locked.includes(generateKey(idx, idy)) ? {'background-color':'#cccccc'} : {}]"
            >
              {{ greaterThanZero(grid[idx][idy]) }}
            </td>
          </tr>
          </tbody>
        </table>
      </div>

      <div style="margin-top: 20px;">
          <div class="btn-group" role="group">
            <button type="button" class="btn btn-secondary" @click="setNumber(0)">Erase</button>
            <button type="button" class="btn btn-secondary" v-for="number in 9" :key="number" @click="setNumber(number)">
              {{number}}
            </button>
          </div>
          <div style="margin-left:25px;display: inline;">
            <button type="button" class="btn btn-outline-primary" @click="saveBoardState">Save</button>
            <button type="button" class="btn btn-outline-primary" style="margin-left:10px;" @click="loadBoard">Load</button>
            <button type="button" class="btn btn-outline-primary" style="margin-left:10px;" @click="clearBoard" >Clear</button>
          </div>
      </div>

      <AlertBox :error="error" :success="success"/>
    </div>
</template>

<script>
import axios from 'axios';
import LoadingSpinner from './LoadingSpinner.vue';
import AlertBox from './AlertBox.vue';

const initialGrid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
];

function resetAlert(){
  return {
    error: null,
    success: null,
    computing: false,
  }
}

function createGridCopy(grid){
  return JSON.parse(JSON.stringify(grid))
}

export default {
    name: 'SudokuBoard',
    components: {
      LoadingSpinner,
      AlertBox
    },
    data() {
      return {
        grid: createGridCopy(initialGrid),
        savedState: {grid: initialGrid, locked: []},
        locked: [],
        error: null,
        success: null,
        computing: false,
        chosenNumber: 0,
        idleSpinnerColor: '#2ca444',
        activeSpinnerColer: '#ff1d5e',
      }
    },
    methods : {
        fadeAlert(data){
          Object.assign(this.$data, data)
          setTimeout(() => {
            Object.assign(this.$data, resetAlert())
          }, 1500)
        },
        solveBoard(){
          this.computing = true
          axios.post('http://localhost:5000/solve', {data: this.grid})
          .then ((res) => {
            const result = res.data.solution
            Object.assign(this.$data, resetAlert())

            if(result.length == 0){
              this.fadeAlert({error: 'Solution does not exist!'})
            } else {
              this.fadeAlert({
                grid: result,
                success: 'Solution found!',
              })
            }
          })
          .catch((err) => {
            console.error(err);
          })
        },
        randomizeBoard(){
          this.computing = true
          axios.get('http://localhost:5000/randomize')
          .then ((res) => {
            const result = res.data
            Object.assign(this.$data, resetAlert())
            Object.assign(this.$data, {grid: result.puzzle, locked: []})
            this.lockCells()
          })
          .catch((err) => {
            console.error(err);
          })
        },
        validateBoard(){
          this.computing = true
          axios.post('http://localhost:5000/validate', {data: this.grid})
          .then ((res) => {
            const result = res.data
            Object.assign(this.$data, resetAlert())
            if(!result.valid){
              this.fadeAlert({error: 'Board is invalid!'})
            } else {
              this.fadeAlert({success: 'Board is valid!'})
            }
          })
          .catch((err) => {
            console.error(err)
          })
        },
        setSelected(x, y) {
          let gridCopy = createGridCopy(this.grid)
          
          // Do not overwrite locked cells
          if (this.locked.includes(this.generateKey(x, y))){
            return
          }

          // Make it possible to revert input by clicking
          if (gridCopy[x][y] == this.chosenNumber) {
            gridCopy[x][y] = 0
          } else {
            gridCopy[x][y] = this.chosenNumber
          }

          Object.assign(this.$data, {grid: gridCopy})
        },
        setNumber(number) {
          this.chosenNumber = number
        },
        greaterThanZero(cell){
          return cell > 0 ? cell.toString() : ""
        },
        loadBoard(){
          Object.assign(this.$data, resetAlert())
          Object.assign(this.$data, {
            grid: this.savedState.grid,
            locked: this.savedState.locked
            }
          )
        },
        cleanUnlockedCells(grid){
          let gridCopy = createGridCopy(grid)
          for (var x = 0; x < this.grid.length; x++) {
            for (var y = 0; y < this.grid.length; y++) {
              if (!this.locked.includes(this.generateKey(x, y))){
                gridCopy[x][y] = 0
              }
            }
          }
          return gridCopy
        },
        clearBoard(){
          Object.assign(this.$data, resetAlert())

          // Only clean cells that are not locked
          if (this.locked.length == 0){
            Object.assign(this.$data, {grid: initialGrid})
          } else {
            Object.assign(this.$data, {grid: this.cleanUnlockedCells(this.grid)})
          }
        },
        saveBoardState() {
          Object.assign(this.$data, resetAlert())
          this.fadeAlert({
            savedState: {
              grid: this.grid,
              locked: this.locked
            },
            success: 'Board is saved!'
          })
        },
        generateKey(x, y){
          return x.toString() + ',' + y.toString()
        },
        lockCells() {
          let newLocked = []
          for (var x = 0; x < this.grid.length; x++) {
            for (var y = 0; y < this.grid.length; y++) {
                if (this.grid[x][y] > 0){
                  newLocked.push(this.generateKey(x, y))
                }
            }
          }
          Object.assign(this.$data, {locked: newLocked})
        },
        unlockCells(){
          Object.assign(this.$data, {locked: []})
        }
    }
}
</script>

<style>
table {
  border-collapse: collapse;
  border: 3px solid;
}

td {
  border: 0.5px solid;
  text-align: center;
  height: 40px;
  width: 40px;
}

table tbody tr td:nth-child(3), table tbody tr td:nth-child(6) {
  border-right: 3px solid;
}

table tbody tr:nth-child(3), table tbody tr:nth-child(6) {
  border-bottom: 3px solid;
}

td {
  cursor: pointer;
}

</style>
