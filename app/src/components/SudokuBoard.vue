<template>
    <div align="center">
      <nav class="navbar navbar-expand-lg navbar-light bg-light" style="width: 60%; height: 50px; margin-bottom: 20px;">
            <button @click="randomizeBoard" class="btn btn-light">New puzzle</button>
            <button @click="validateBoard" class="btn btn-light">Validate puzzle</button>
            <button @click="solveBoard" class="btn btn-light">Solve puzzle</button>
            <button @click="lockCells" class="btn btn-light">Lock current cells</button>
      </nav>

      <div>
        <table>
          <tbody>
          <tr v-for="(row, idx) in grid" :key="idx">
            <td
              v-for="(cell, idy) in row" :key="idy"
              @click="setSelected(idx, idy)"
              :style="[locked.includes(makeKey(idx, idy)) ? {'background-color':'#cccccc'} : {}]"
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
            <button type="button" class="btn btn-outline-primary" style="margin-left:10px;" @click="cleanBoard" >Clear</button>
          </div>
      </div>

      <div style="width: 600px;margin-top: 50px;">
        <Transition>
        <div class="alert alert-dismissible alert-danger" v-if="error">{{ error }}</div>
        <div class="alert alert-dismissible alert-success" v-else-if="success">{{ success }}</div>
        </Transition>
      </div>
    </div>
</template>

<script>
import axios from 'axios';

const initial_grid = [
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

function resertAlert(){
  return {
    error: null,
    success: null
  }
}

export default {
    name: 'SudokuBoard',
    data() {
      return {
        grid: JSON.parse(JSON.stringify(initial_grid)),
        saved_grid: initial_grid,
        locked: [],
        error: null,
        success: null,
        chosen_number: 0
      }
    },
    methods : {
        fadeAlert(data){
          Object.assign(this.$data, data)
          setTimeout(() => {
            Object.assign(this.$data, resertAlert())
          }, 1500)
        },
        solveBoard(){
          axios.post('http://localhost:5000/solve', {data: this.grid})
          .then ((res) => {
            const result = res.data.solution
            Object.assign(this.$data, resertAlert())

            if(result.length == 0){
              this.fadeAlert({error: 'Solution does not exist!'})
            } else {
              this.fadeAlert({
                grid: result,
                success: 'Solution found!'
              })
            }
          })
          .catch((err) => {
            console.error(err);
          })
        },
        randomizeBoard(){
          axios.get('http://localhost:5000/randomize')
          .then ((res) => {
            const result = res.data
            Object.assign(this.$data, resertAlert())
            Object.assign(this.$data, {grid: result.puzzle})
          })
          .catch((err) => {
            console.error(err);
          })
        },
        validateBoard(){
          axios.post('http://localhost:5000/validate', {data: this.grid})
          .then ((res) => {
            const result = res.data
            Object.assign(this.$data, resertAlert())
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
          let grid_copy = JSON.parse(JSON.stringify(this.grid))
          
          // Do not overwrite locked cells
          if (this.locked.includes(this.makeKey(x, y))){
            return
          }

          // Make it possible to revert input by clicking
          if (grid_copy[x][y] == this.chosen_number) {
            grid_copy[x][y] = 0
          } else {
            grid_copy[x][y] = this.chosen_number
          }

          Object.assign(this.$data, {grid: grid_copy})
        },
        setNumber(number) {
          this.chosen_number = number
        },
        greaterThanZero(cell){
          return cell > 0 ? cell.toString() : ""
        },
        loadBoard(){
          Object.assign(this.$data, resertAlert())
          Object.assign(this.$data, {grid: this.saved_grid})
        },
        cleanBoard(){
          Object.assign(this.$data, resertAlert())
          Object.assign(this.$data, {grid: initial_grid})
        },
        saveBoardState() {
          Object.assign(this.$data, resertAlert())
          this.fadeAlert({
            saved_grid: this.grid,
            success: 'Board is saved!'
          })
        },
        makeKey(x, y){
          return x.toString() + ',' + y.toString()
        },
        lockCells() {
          if (this.locked.length == 0) {
            for (var x = 0; x < this.grid.length; x++) {
              for (var y = 0; y < this.grid.length; y++) {
                  if (this.grid[x][y] > 0){
                    this.locked.push(this.makeKey(x, y))
                  }
              }
            }
          } else {
            this.locked = []
          }

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

.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from, .v-leave-to {
  opacity: 0;
}

</style>
